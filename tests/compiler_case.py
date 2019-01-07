from unittest import TestCase
from hyaml.compiler import ExpressionCompiler, AssignmentCompiler


class ExpressionCompilerCase(TestCase):
    bindings = ()
    method_table = {}

    def assertEvaluatedTo(self, expr, *args):
        *values, expectation = args
        self.assertEqual(self.compile(expr)(*values), expectation)

    def assertMethodCall(self, expr, expectation, **kwargs):
        self.assertEqual(self.compile(expr)(kwargs), expectation)

    @property
    def compile(self):
        return ExpressionCompiler(
            bindings=self.bindings, method_table=self.method_table
        )


class AssignmentCompilerCase(TestCase):
    bindings = ("variables",)

    def assign(self, expr, value, **kwargs):
        self.compile(expr)(value, kwargs)
        return kwargs

    @property
    def compile(self):
        return AssignmentCompiler(bindings=self.bindings)

