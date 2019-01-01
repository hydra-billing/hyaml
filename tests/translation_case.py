from unittest import TestCase
from hyaml.translator import translate


class TranslationCase(TestCase):
    def assertTranslated(self, expr, expectation):
        self.assertEqual(translate(expr + "\n"), expectation)

