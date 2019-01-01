from functools import lru_cache
from hyaml.translator import translate
from hyaml.methods.prelude import all as prelude
from textwrap import dedent


class Compiler:
    def __init__(self, bindings=(), method_table={}):
        self._bindings = bindings
        self.arg_names = ", ".join(self._bindings)
        self._method_table = {**prelude, **method_table}

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


@lru_cache(maxsize=128)
def _compiler(bindings=()):
    return Compiler(bindings=bindings)


compile = lambda expr, bindings=(): _compiler(bindings=bindings)(expr)

