#!/usr/bin/env python

from unittest import TestCase, main
from hydra.hyaml.translator import translate


class TestBasicGrammar(TestCase):
    def assertTranslated(self, expr, expectation):
        self.assertEqual(translate(expr + "\n"), expectation)

    def test_sample(self):
        self.assertTranslated("", "")

    def test_variable(self):
        print("fooooo")
        self.assertTranslated("$foo", "variables.get('foo')")
