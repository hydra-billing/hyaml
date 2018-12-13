from hydra.hyaml.translator import translate
from hydra.hyaml import prelude
from textwrap import dedent


class Compiler:
    def __init__(self, bindings=(), method_table={}):
        self._bindings = bindings
        self.arg_names = ", ".join(self._bindings)
        self._method_table = {**prelude.__dict__, **method_table}

    def __call__(self, expr):
        py_expr = translate(expr)

        glbs = self._method_table
        lcls = {}

        code = dedent(
            """
            def __compiled(%s):
                return %s
        """
            % (self.arg_names, py_expr)
        )

        exec(code, glbs, lcls)

        func = lcls["__compiled"]
        func.source = expr
        func.compiled = py_expr

        return func


_compiler = Compiler()

compile = lambda expr: _compiler(expr)
