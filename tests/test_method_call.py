#!/usr/bin/env python

from unittest import main
from tests import TranslationCase as TestCase


class TestMethodCall(TestCase):
    def test_simple_call(self):
        self.assertTranslated("$var.to_i()", "to_i(variables.get('var'))")

    def test_call_with_arguments(self):
        self.assertTranslated("$var.to_i(16)", "to_i(variables.get('var'), 16)")
        self.assertTranslated("$var.map_join('')", "map_join(variables.get('var'), '')")

    def test_accessing_attribute(self):
        self.assertTranslated(
            "$cdr.Custom-Attr", "get(variables.get('cdr'), 'Custom-Attr')"
        )

    def test_multiple_attributes(self):
        self.assertTranslated(
            "$cdr.Attr:1.Attr:2", "get(get(variables.get('cdr'), 'Attr:1'), 'Attr:2')"
        )

    def test_calls_as_arguments(self):
        self.assertTranslated(
            "$cdr.to_i($sixteen.upper())",
            "to_i(variables.get('cdr'), upper(variables.get('sixteen')))",
        )

        self.assertTranslated(
            "$cdr.to_i($var.sixteen, $var2.upper())",
            "to_i(variables.get('cdr'), get(variables.get('var'), 'sixteen'), "
            + "upper(variables.get('var2')))",
        )

    def test_expressions_as_arguments(self):
        self.assertTranslated("$var.to_i(8 + 8)", "to_i(variables.get('var'), 8 + 8)")

    def test_mixed_calls(self):
        self.assertTranslated(
            "$cdr.to_i(16).to_string().size",
            "get(to_string(to_i(variables.get('cdr'), 16)), 'size')",
        )

    def test_predicates(self):
        self.assertTranslated("16.odd?()", "is_odd(16)")

    def test_safe_navigation(self):
        self.assertTranslated(
            "$var?.FOO?.Maybe",
            "safe_get(safe_get(variables.get('var'), 'FOO'), 'Maybe')",
        )

        self.assertTranslated(
            "$var?.something(123)", "safe_call(variables.get('var'), something, 123)"
        )

        self.assertTranslated(
            "$var?.like?(123)", "safe_call(variables.get('var'), is_like, 123)"
        )

        self.assertTranslated("123?.odd?()", "safe_call(123, is_odd)")

    def test_reserved_words(self):
        self.assertTranslated("1.as()", "as_(1)")
        self.assertTranslated("1.assert()", "assert_(1)")
        self.assertTranslated("1.break()", "break_(1)")
        self.assertTranslated("1.class()", "class_(1)")
        self.assertTranslated("1.continue()", "continue_(1)")
        self.assertTranslated("1.def()", "def_(1)")
        self.assertTranslated("1.del()", "del_(1)")
        self.assertTranslated("1.elif()", "elif_(1)")
        self.assertTranslated("1.else()", "else_(1)")
        self.assertTranslated("1.except()", "except_(1)")
        self.assertTranslated("1.finally()", "finally_(1)")
        self.assertTranslated("1.for()", "for_(1)")
        self.assertTranslated("1.from()", "from_(1)")
        self.assertTranslated("1.global()", "global_(1)")
        self.assertTranslated("1.if()", "if_(1)")
        self.assertTranslated("1.import()", "import_(1)")
        self.assertTranslated("1.in()", "in_(1)")
        self.assertTranslated("1.is()", "is_(1)")
        self.assertTranslated("1.lambda()", "lambda_(1)")
        self.assertTranslated("1.nonlocal()", "nonlocal_(1)")
        self.assertTranslated("1.pass()", "pass_(1)")
        self.assertTranslated("1.raise()", "raise_(1)")
        self.assertTranslated("1.return()", "return_(1)")
        self.assertTranslated("1.try()", "try_(1)")
        self.assertTranslated("1.while()", "while_(1)")
        self.assertTranslated("1.with()", "with_(1)")
        self.assertTranslated("1.yield()", "yield_(1)")

