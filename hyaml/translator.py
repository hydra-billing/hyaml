from keyword import kwlist
from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker, BailErrorStrategy
from hyaml.grammar import HyamlListener, HyamlLexer, HyamlParser


def _escape_keyword(string):
    if string in kwlist:
        return "%s_" % string
    else:
        return string


class Parser(HyamlParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._errHandler = BailErrorStrategy()


class Listener(HyamlListener):
    def __init__(self, assignment=False):
        self._op = None
        self._args = []
        self._stack = []
        self._assignment = assignment

    @property
    def output(self):
        return "".join(self._args)

    def exitParens(self, ctx):
        self._addArg("(%s)" % self._removeArg())

    def enterExpr(self, ctx: HyamlParser.ExprContext):
        if ctx.MULT_DIV_OP():
            self._push(ctx.MULT_DIV_OP().getText())
        elif ctx.SIGN() and not ctx.NUMBER():
            self._push(ctx.SIGN().getText())
        elif ctx.COMP_OP():
            self._push(ctx.COMP_OP().getText())
        elif ctx.NUMBER():
            number = ctx.NUMBER().getText()
            if ctx.SIGN():
                sign = ctx.SIGN().getText()
            else:
                sign = ""
            self._addArg(sign + number)
        elif ctx.VAR():
            var_name = ctx.VAR().getText()[1:]

            if self._isAssignmentTarget(ctx):
                expr = "assign(variables, '%s', value)" % var_name
            else:
                expr = "get(variables, '%s')" % var_name

            self._addArg(expr)

        elif ctx.STRING():
            string = ctx.getText()
            self._addArg(self._escape(string))
        elif ctx.TRUE():
            self._addArg("True")
        elif ctx.FALSE():
            self._addArg("False")
        elif ctx.AND():
            self._push("and")
        elif ctx.OR():
            self._push("or")
        elif ctx.NOT():
            self._push("not")

    def exitExpr(self, ctx):
        bin_opt = (
            ctx.MULT_DIV_OP()
            or ctx.SIGN()
            and not ctx.NUMBER()
            or ctx.AND()
            or ctx.OR()
            or ctx.COMP_OP()
        )
        if bin_opt:
            op, args = self._pop()
            left, right = args

            arg = "%s %s %s" % (left, op, right)

            self._addArg(arg)
        elif ctx.NOT():
            _, args = self._pop()
            arg, *_ = args
            self._addArg("not %s" % arg)

    def enterListLiteral(self, ctx):
        self._push()

    def exitListLiteral(self, ctx):
        _, elements = self._pop()
        self._addArg("[%s]" % ", ".join(elements))

    def enterDictLiteral(self, ctx):
        self._push()

    def exitDictLiteral(self, ctx):
        _, elements = self._pop()
        self._addArg("{%s}" % ", ".join(elements))

    def enterCallChain(self, ctx):
        if self._isAssignmentTarget(ctx):
            self._top_child_countdown = ctx.getChildCount()

    def enterAttributeOrDispatch(self, ctx):
        if self._isAssignmentTarget(ctx.parentCtx):
            self._top_child_countdown = self._top_child_countdown - 1

        target = self._removeArg()

        if ctx.args():
            if ctx.PRED():
                method_name = "is_%s" % ctx.ID().getText()
            else:
                method_name = ctx.ID().getText()

            self._push(_escape_keyword(method_name), [target])
        else:
            if self._isAssignmentTarget(ctx):
                expr = "assign(%s, '%s', value)" % (target, ctx.ID().getText())
            else:
                method = "safe_get" if ctx.SAFE_ACCESS() else "get"
                expr = "%s(%s, '%s')" % (method, target, ctx.ID().getText())

            self._addArg(expr)

    def exitAttributeOrDispatch(self, ctx):
        if ctx.args():
            method, args = self._pop()
            if ctx.SAFE_ACCESS():
                target, *args = args
                self._addArg("safe_call(%s)" % ", ".join([target, method, *args]))
            else:
                self._addArg("%s(%s)" % (method, ", ".join(args)))

    def enterKeyValuePair(self, ctx):
        key = ctx.ID().getText()
        self._addArg(key)

    def exitKeyValuePair(self, ctx):
        value = self._removeArg()
        key = self._removeArg()
        self._addArg('"%s": %s' % (key, value))

    def enterSubscription(self, ctx):
        if self._isAssignmentTarget(ctx.parentCtx):
            self._top_child_countdown = self._top_child_countdown - 1

        self._push()

    def exitSubscription(self, ctx):
        _, args = self._pop()
        target = self._removeArg()
        arg, *_ = args

        if self._isAssignmentTarget(ctx):
            expr = "assign(%s, %s, value)" % (target, arg)
        else:
            expr = "%s[%s]" % (target, arg)

        self._addArg(expr)

    def _push(self, op_name=None, args=None):
        self._stack.append((self._op, self._args))
        self._op = op_name
        self._args = args or []

    def _pop(self):
        op, args = self._op, self._args
        self._op, self._args = self._stack.pop()

        return (op, args)

    def _addArg(self, arg):
        self._args.append(arg)

    def _removeArg(self):
        return self._args.pop()

    def _escape(self, string):
        return string.replace("\\", "\\\\")

    def _isAssignmentTarget(self, ctx):
        if self._assignment and len(self._stack) == 0:
            if ctx.getRuleIndex() == HyamlParser.RULE_expr:
                return ctx.parentCtx.getChildCount() == 1
            elif ctx.getRuleIndex() == HyamlParser.RULE_callChain:
                return True
            elif ctx.getRuleIndex() in (
                HyamlParser.RULE_attributeOrDispatch,
                HyamlParser.RULE_subscription,
            ):
                return self._top_child_countdown == 0
            else:
                return False
        else:
            return False


class Translator:
    def __call__(self, expr, assignment=False):
        input = InputStream(expr)
        lexer = HyamlLexer(input)
        stream = CommonTokenStream(lexer)
        parser = Parser(stream)
        tree = parser.prog()
        # lisp_tree_str = tree.toStringTree(recog=parser)
        # print(lisp_tree_str)
        listener = Listener(assignment=assignment)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        return listener.output


_translator = Translator()

translate = lambda text, **kwargs: _translator(text, **kwargs)
