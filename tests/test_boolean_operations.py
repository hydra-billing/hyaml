#!/usr/bin/env python

from unittest import main
from tests import TranslationCase as TestCase


class TestBooleanOperations(TestCase):
    def test_conjuction(self):
        self.assertTranslated("true and false", "True and False")

    def test_disjunction(self):
        self.assertTranslated("true or false", "True or False")

    def test_negation(self):
        self.assertTranslated("not true", "not True")

    def test_complex_expression(self):
        self.assertTranslated(
            "true or false and not true", "True or False and not True"
        )

    def test_parens(self):
        self.assertTranslated(
            "(true and false) or (false and true)",
            "(True and False) or (False and True)",
        )
        self.assertTranslated(
            "true and not (false or true)", "True and not (False or True)"
        )

