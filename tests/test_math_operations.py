#!/usr/bin/env python

from unittest import main
from tests import TranslationCase as TestCase


class TestMathOperations(TestCase):
    def test_addition(self):
        self.assertTranslated("4 + 5", "4 + 5")
        self.assertTranslated("4 + 5 + 9", "4 + 5 + 9")

    def test_subtraction(self):
        self.assertTranslated("4 - 5", "4 - 5")
        self.assertTranslated("4 - 5 - -9", "4 - 5 - -9")

    def test_multiplication(self):
        self.assertTranslated("4*5", "4 * 5")
        self.assertTranslated(" 4 * 5 *-9", "4 * 5 * -9")

    def test_division(self):
        self.assertTranslated("9.0  / 5.1", "9.0 / 5.1")

    def test_modulo(self):
        self.assertTranslated("5 % 2", "5 % 2")

    def test_lack_of_spaces(self):
        self.assertTranslated("3-5", "3 - 5")
        self.assertTranslated("-3--5", "-3 - -5")


class TestMathOpPrecedence(TestCase):
    def test_mult_with_addition(self):
        self.assertTranslated("4 + 5 * 3", "4 + 5 * 3")


class TestGrouping(TestCase):
    def test_associating_to_right(self):
        self.assertTranslated("4 - (3 - 2 - 1)", "4 - (3 - 2 - 1)")

    def test_associating_to_left(self):
        self.assertTranslated("(4 - 3) - 2", "(4 - 3) - 2")
