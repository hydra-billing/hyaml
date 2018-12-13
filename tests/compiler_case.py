from unittest import TestCase
from hydra.hyaml.compiler import Compiler


class CompilerCase(TestCase):
    bindings = ()

    def assertEvaluatedTo(self, expr, expectation):
        self.assertEqual(self.compile(expr)(), expectation)

    @property
    def compile(self):
        return Compiler(self.bindings)

