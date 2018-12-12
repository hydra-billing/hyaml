#!/usr/bin/env python

from unittest import main
from tests import TranslationCase as TestCase


class TestMethodCall(TestCase):
    def test_simple_call(self):
        self.assertTranslated("$var.to_i()", "to_i(variables.get('var'))")

    def test_call_with_arguments(self):
        self.assertTranslated("$var.to_i(16)", "to_i(variables.get('var'), 16)")

    def test_accessing_attribute(self):
        self.assertTranslated("$cdr.Custom-Attr", "variables.get('cdr')['Custom-Attr']")

    def test_multiple_attributes(self):
        self.assertTranslated(
            "$cdr.Attr:1.Attr:2", "variables.get('cdr')['Attr:1']['Attr:2']"
        )

    def test_calls_as_arguments(self):
        self.assertTranslated(
            "$cdr.to_i($sixteen.upper())",
            "to_i(variables.get('cdr'), upper(variables.get('sixteen')))",
        )

        self.assertTranslated(
            "$cdr.to_i($var.sixteen, $var2.upper())",
            "to_i(variables.get('cdr'), variables.get('var')['sixteen'], "
            + "upper(variables.get('var2')))",
        )

    def test_expressions_as_arguments(self):
        self.assertTranslated("$var.to_i(8 + 8)", "to_i(variables.get('var'), 8 + 8)")
