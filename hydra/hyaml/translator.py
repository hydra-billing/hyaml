from antlr4 import CommonTokenStream, InputStream
from hydra.hyaml.grammar import HyamlVisitor, HyamlLexer, HyamlParser


class Visitor(HyamlVisitor):
    def visitExpr(self, ctx: HyamlParser.ExprContext):
        token_type = ctx.start.type

        if token_type == HyamlParser.VAR:
            var_name = ctx.VAR().symbol.text[1:]
            expr = "variables.get('%s')" % var_name
            self._buffer.append(expr)

        return super().visitExpr(ctx)

    def __call__(self, tree):
        self._buffer = []
        self.visitProg(tree)

        return "".join(self._buffer)


class Translator:
    _visitor = Visitor()

    def __call__(self, expr):
        input = InputStream(expr)
        lexer = HyamlLexer(input)
        stream = CommonTokenStream(lexer)
        parser = HyamlParser(stream)
        tree = parser.prog()
        # lisp_tree_str = tree.toStringTree(recog=parser)
        # print(lisp_tree_str)

        return self._visitor(tree)


_translator = Translator()

translate = lambda text: _translator(text)
