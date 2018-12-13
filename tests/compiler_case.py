from unittest import TestCase
from hydra.hyaml.compiler import Compiler


class CompilerCase(TestCase):
    bindings = ()
    method_table = {}

    def assertEvaluatedTo(self, expr, *args):
        *values, expectation = args
        self.assertEqual(self.compile(expr)(*values), expectation)

    @property
    def compile(self):
        return Compiler(bindings=self.bindings, method_table=self.method_table)
