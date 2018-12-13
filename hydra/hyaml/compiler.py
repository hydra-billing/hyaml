from hydra.hyaml.translator import translate
from textwrap import dedent


def _safe_get(obj, attr):
    if obj is not None and attr in obj:
        return obj[attr]
    else:
        return None


def _safe_call(obj, f, *args):
    if obj is None:
        return None
    else:
        return f(obj, *args)


class Compiler:
    prelude = {"safe_get": _safe_get, "safe_call": _safe_call}

    def __init__(self, bindings=(), method_table={}):
        self._bindings = bindings
        self.arg_names = ", ".join(self._bindings)
        self._method_table = {**self.prelude, **method_table}

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
