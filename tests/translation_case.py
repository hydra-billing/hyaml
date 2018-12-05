from unittest import TestCase
from hydra.hyaml.translator import translate


class TranslationCase(TestCase):
    def assertTranslated(self, expr, expectation):
        self.assertEqual(translate(expr + "\n"), expectation)

