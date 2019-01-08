from functools import lru_cache
from hyaml.translator import translate
from hyaml.methods.prelude import all as prelude
from hyaml.methods import assignment
from textwrap import dedent


class Compiler:
    def __init__(self, bindings=(), method_table={}):
        self._bindings = bindings
        self.arg_names = ", ".join(self._bindings)
        self._method_table = {**prelude, **method_table}

    def add_methods(self, **methods):
        if methods == {}:
            return self
        else:
            return self.__class__(
                bindings=self._bindings, method_table={**self._method_table, **methods}
            )


class ExpressionCompiler(Compiler):
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
def _expr_compiler(bindings=()):
    return ExpressionCompiler(bindings=bindings)


compile_expression = lambda expr, bindings=(): _expr_compiler(bindings=bindings)(expr)


class AssignmentCompiler(Compiler):
    def __init__(self, bindings=(), method_table={}):
        if len(bindings) == 0 or bindings[0] != "value":
            bs = ("value",) + bindings
        else:
            bs = bindings

        super().__init__(bindings=bs, method_table={**assignment, **method_table})

    def __call__(self, stmt):
        py_stmt = translate(stmt, assignment=True)

        glbs = self._method_table
        lcls = {}

        code = dedent(
            """
            def __compiled(%s):
                %s
        """
            % (self.arg_names, py_stmt)
        )

        exec(code, glbs, lcls)

        func = lcls["__compiled"]
        func.source = stmt
        func.compiled = py_stmt

        return func
