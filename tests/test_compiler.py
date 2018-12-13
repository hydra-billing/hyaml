#!/usr/bin/env python

from unittest import main
from tests import CompilerCase as TestCase


class TestCompiler(TestCase):
    def test_simple_expression(self):
        self.assertEvaluatedTo("9 + 10", 19)

    def test_math_expressions(self):
        self.assertEvaluatedTo("9 + 10 - 1", 18)
        self.assertEvaluatedTo("-3--4", 1)
        self.assertEvaluatedTo("5 / 2 + 1", 3.5)

    def test_string_concatenation(self):
        self.assertEvaluatedTo("'abyr' + \"valg\"", "abyrvalg")

    def test_boolean_expressions(self):
        self.assertEvaluatedTo("10 > 9", True)
        self.assertEvaluatedTo("10 < 9", False)
        self.assertEvaluatedTo("10 <= 9", False)
        self.assertEvaluatedTo("9 <= 9", True)
        self.assertEvaluatedTo("9==8", False)
        self.assertEvaluatedTo("9 != -0.1", True)

