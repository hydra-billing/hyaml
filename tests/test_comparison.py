#!/usr/bin/env python

from unittest import main
from tests import TranslationCase as TestCase


class TestComparison(TestCase):
    def test_gt(self):
        self.assertTranslated("1 > 2", "1 > 2")

    def test_gte(self):
        self.assertTranslated("1 >= 2", "1 >= 2")

    def test_lt(self):
        self.assertTranslated("1 < 2", "1 < 2")

    def test_lte(self):
        self.assertTranslated("1 <= 2", "1 <= 2")

    def test_eq(self):
        self.assertTranslated("1 == 2", "1 == 2")
