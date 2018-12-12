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
            self._args.append(number)
        elif ctx.VAR():
            var_name = ctx.VAR().getText()[1:]
            expr = "variables.get('%s')" % var_name
            self._args.append(expr)
        elif ctx.STRING():
            string = ctx.getText()
            self._args.append(string)
        elif ctx.EMPTY_HASH():
            self._args.append("{}")
        elif ctx.boolLiteral():
            if ctx.boolLiteral().TRUE():
                self._args.append("True")
            else:
                self._args.append("False")

    def exitExpr(self, ctx):
        if ctx.MULT_DIV_OP() or ctx.ADD_SUB_OP():
            current_op = self._op
            left_arg, right_arg = self._args
            self._op, self._args = self._stack.pop()
            arg = "%s %s %s" % (left_arg, current_op, right_arg)

            if self._op is None:
                self._args.append(arg)
            else:
                self._args.append("(%s)" % arg)


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
