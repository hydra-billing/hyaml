from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker
from hydra.hyaml.grammar import HyamlListener, HyamlLexer, HyamlParser


class Listener(HyamlListener):
    def __init__(self):
        self._op = None
        self._args = []
        self._stack = []

    @property
    def output(self):
        return "".join(self._args)

    def enterExpr(self, ctx: HyamlParser.ExprContext):
        if ctx.MULT_DIV_OP():
            self._stack.append((self._op, self._args))
            self._op = ctx.MULT_DIV_OP().getText()
            self._args = []
        elif ctx.ADD_SUB_OP():
            self._stack.append((self._op, self._args))
            self._op = ctx.ADD_SUB_OP().getText()
            self._args = []
        elif ctx.NUMBER():
            number = ctx.NUMBER().getText()
            self._addArg(number)
        elif ctx.VAR():
            var_name = ctx.VAR().getText()[1:]
            expr = "variables.get('%s')" % var_name
            self._addArg(expr)
        elif ctx.STRING():
            string = ctx.getText()
            self._addArg(string)
        elif ctx.EMPTY_HASH():
            self._addArg("{}")
        elif ctx.boolLiteral():
            if ctx.boolLiteral().TRUE():
                self._addArg("True")
            else:
                self._addArg("False")

    def exitExpr(self, ctx):
        if ctx.MULT_DIV_OP() or ctx.ADD_SUB_OP():
            op, args = self._pop()
            left, right = args

            arg = "%s %s %s" % (left, op, right)

            if self._op not in ("+", "-", "*", "/"):
                self._addArg(arg)
            else:
                self._addArg("(%s)" % arg)

    def enterAttribute(self, ctx):
        target = self._removeArg()
        arg = "%s['%s']" % (target, ctx.ID())
        self._addArg(arg)

    def enterMethodCall(self, ctx):
        target = self._removeArg()
        self._push()
        if ctx.PRED():
            method_name = "is_%s" % ctx.ID()
        else:
            method_name = ctx.ID()

        self._op = method_name
        self._args = [target]

    def exitMethodCall(self, ctx):
        method, args = self._pop()
        self._addArg("%s(%s)" % (method, ", ".join(args)))

    def _push(self):
        self._stack.append((self._op, self._args))

    def _pop(self):
        op, args = self._op, self._args
        self._op, self._args = self._stack.pop()

        return (op, args)

    def _addArg(self, arg):
        self._args.append(arg)

    def _removeArg(self):
        return self._args.pop()


class Translator:
    def __call__(self, expr):
        input = InputStream(expr)
        lexer = HyamlLexer(input)
        stream = CommonTokenStream(lexer)
        parser = HyamlParser(stream)
        tree = parser.prog()
        # lisp_tree_str = tree.toStringTree(recog=parser)
        # print(lisp_tree_str)
        listener = Listener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        return listener.output


_translator = Translator()

translate = lambda text: _translator(text)
