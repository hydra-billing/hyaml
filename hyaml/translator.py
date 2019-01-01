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
    def __init__(self):
        self._op = None
        self._args = []
        self._stack = []

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
            expr = "variables.get('%s')" % var_name
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

    def enterAttributeOrDispatch(self, ctx):
        target = self._removeArg()
        if ctx.args():
            if ctx.PRED():
                method_name = "is_%s" % ctx.ID().getText()
            else:
                method_name = ctx.ID().getText()

            self._push(_escape_keyword(method_name), [target])
        else:
            method = "safe_get" if ctx.SAFE_ACCESS() else "get"
            arg = "%s(%s, '%s')" % (method, target, ctx.ID().getText())
            self._addArg(arg)

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
        self._push()

    def exitSubscription(self, ctx):
        _, args = self._pop()
        target = self._removeArg()
        arg, *_ = args
        self._addArg("%s[%s]" % (target, arg))

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


class Translator:
    def __call__(self, expr):
        input = InputStream(expr)
        lexer = HyamlLexer(input)
        stream = CommonTokenStream(lexer)
        parser = Parser(stream)
        tree = parser.prog()
        # lisp_tree_str = tree.toStringTree(recog=parser)
        # print(lisp_tree_str)
        listener = Listener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        return listener.output


_translator = Translator()

translate = lambda text: _translator(text)
