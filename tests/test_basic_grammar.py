#!/usr/bin/env python

from unittest import TestCase, main
from hydra.hyaml.translator import translate


class TestBasicGrammar(TestCase):
    def assertTranslated(self, expr, expectation):
        self.assertEqual(translate(expr + "\n"), expectation)

    def test_variable(self):
        self.assertTranslated("$foo", "variables.get('foo')")

    def test_integer(self):
        self.assertTranslated("50", "50")
        self.assertTranslated("-50", "-50")

    def test_float(self):
        self.assertTranslated("50.01", "50.01")
        self.assertTranslated("-50.01", "-50.01")

    def test_string(self):
        self.assertTranslated("'foo'", "'foo'")
        self.assertTranslated('"foo"', '"foo"')

    def test_empty_hash(self):
        self.assertTranslated("{}", "{}")

    def test_boolean(self):
        self.assertTranslated("true", "True")
        self.assertTranslated("false", "False")

