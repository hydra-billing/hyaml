from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker
from hydra.hyaml.grammar import HyamlListener, HyamlLexer, HyamlParser


class Listener(HyamlListener):
    def __init__(self):
        self._buffer = []

    @property
    def output(self):
        return "".join(self._buffer)

    def enterExpr(self, ctx: HyamlParser.ExprContext):
        fst = ctx.start

        if fst.type == HyamlParser.VAR:
            var_name = ctx.VAR().symbol.text[1:]
            expr = "variables.get('%s')" % var_name
            self._buffer.append(expr)
        elif fst.type == HyamlParser.NUMBER:
            number = ctx.NUMBER().symbol.text
            self._buffer.append(number)
        elif fst.type == HyamlParser.STRING:
            string = ctx.STRING().symbol.text
            self._buffer.append(string)
        elif fst.type == HyamlParser.EMPTY_HASH:
            self._buffer.append("{}")
        elif fst.type == HyamlParser.TRUE:
            self._buffer.append("True")
        elif fst.type == HyamlParser.FALSE:
            self._buffer.append("False")


class Translator:
    def __call__(self, expr):
        input = InputStream(expr)
        lexer = HyamlLexer(input)
        stream = CommonTokenStream(lexer)
        parser = HyamlParser(stream)
        tree = parser.prog()
        listener = Listener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        # lisp_tree_str = tree.toStringTree(recog=parser)
        # print(lisp_tree_str)

        return listener.output


_translator = Translator()

translate = lambda text: _translator(text)
