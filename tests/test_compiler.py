#!/usr/bin/env python

from unittest import main, TestCase
from hydra.hyaml.compiler import compile_to_lambda


class TestCompiler(TestCase):
    def test_simple_expression(self):
        f = compile_to_lambda("9 + 10")
        self.assertEqual(f({}), 19)
