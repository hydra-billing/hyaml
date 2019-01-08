#!/usr/bin/env python

from unittest import main
from tests import TranslationCase as TestCase


class TestBasicGrammar(TestCase):
    def test_variable(self):
        self.assertTranslated("$foo", "variables.get('foo')")
        self.assertTranslated("$foo_1", "variables.get('foo_1')")

    def test_integer(self):
        self.assertTranslated("50", "50")
        self.assertTranslated("-50", "-50")

    def test_float(self):
        self.assertTranslated("50.01", "50.01")
        self.assertTranslated("-50.01", "-50.01")
        self.assertTranslated("0.01", "0.01")
        self.assertTranslated("-0.01", "-0.01")

    def test_string(self):
        self.assertTranslated("'foo'", "'foo'")
        self.assertTranslated('"foo"', '"foo"')

    def test_empty_hash(self):
        self.assertTranslated("{}", "{}")

    def test_boolean(self):
        self.assertTranslated("true", "True")
        self.assertTranslated("false", "False")

