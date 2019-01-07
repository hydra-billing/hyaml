#!/usr/bin/env python

from unittest import main
from tests import ExpressionCompilerCase as TestCase


class TestCompiler(TestCase):
    def test_simple_expression(self):
        self.assertEvaluatedTo("9 + 10", 19)

    def test_math_expressions(self):
        self.assertEvaluatedTo("9 + 10 - 1", 18)
        self.assertEvaluatedTo("-3--4", 1)
        self.assertEvaluatedTo("5 / 2 + 1", 3.5)

    def test_string_concatenation(self):
        self.assertEvaluatedTo("'abyr' + \"valg\"", "abyrvalg")

    def test_boolean_expressions(self):
        self.assertEvaluatedTo("10 > 9", True)
        self.assertEvaluatedTo("10 < 9", False)
        self.assertEvaluatedTo("10 <= 9", False)
        self.assertEvaluatedTo("9 <= 9", True)
        self.assertEvaluatedTo("9==8", False)
        self.assertEvaluatedTo("9 != -0.1", True)

    def test_lists(self):
        self.assertEvaluatedTo("[]", [])
        self.assertEvaluatedTo("[1]", [1])
        self.assertEvaluatedTo("[1 + 3]", [4])
        self.assertEvaluatedTo("[1] + [2]", [1, 2])
        self.assertEvaluatedTo("['[]']", ["[]"])

    def test_dicts(self):
        self.assertEvaluatedTo("{}", {})
        self.assertEvaluatedTo("{abc: 123}", {"abc": 123})
        self.assertEvaluatedTo("{abc:1: 123}", {"abc:1": 123})

    def test_boolean_operators(self):
        self.assertEvaluatedTo("not true", False)
        self.assertEvaluatedTo("true or false", True)
        self.assertEvaluatedTo("true and not false", True)
        self.assertEvaluatedTo("true or false and not true", True)
        self.assertEvaluatedTo("true and not (false or true)", False)

    def test_subscription(self):
        self.assertEvaluatedTo("{abc: 123}['abc']", 123)

    def test_escaping(self):
        self.assertEvaluatedTo("'\\s\\d'", "\\s\\d")


class TestVariables(TestCase):
    bindings = ("variables",)

    def test_simple_access(self):
        self.assertEvaluatedTo("$var", {"var": 5}, 5)

    def test_using_variables_in_expressions(self):
        self.assertEvaluatedTo("$a + $b", {"a": 5, "b": 6}, 11)


class TestMethodCalls(TestCase):
    method_table = {
        "square": lambda x: x ** 2,
        "take": lambda xs, y: xs[:y],
        "is_odd": lambda n: n % 1 == 1,
        "is_like": lambda a, b: a.startswith(b),
    }

    def test_simple_call(self):
        self.assertEvaluatedTo("5.square()", 25)

    def test_chain_call(self):
        self.assertEvaluatedTo("5.square().square()", 625)

    def test_arguments(self):
        self.assertEvaluatedTo("[1, 2, 3, 4].take(2)", [1, 2])

    def test_predicates(self):
        self.assertEvaluatedTo("2.odd?()", False)
        self.assertEvaluatedTo("'foobar'.like?('foo')", True)


class TestAttributesAccess(TestCase):
    bindings = ("variables",)
    method_table = {"is_foo": lambda _: 1 / 0}

    def test_simple_access(self):
        self.assertEvaluatedTo(
            "$cdr.REQ.Attr:1", {"cdr": {"REQ": {"Attr:1": 123}}}, 123
        )

    def test_safe_navigation(self):
        self.assertEvaluatedTo("$cdr?.REQ?.Attr:1", {"cdr": None}, None)
        self.assertEvaluatedTo("$cdr?.REQ?.Attr:1", {"cdr": {}}, None)
        self.assertEvaluatedTo("$cdr?.REQ?.Attr:1", {"cdr": {"REQ": None}}, None)
        self.assertEvaluatedTo(
            "$cdr?.REQ?.Attr:1", {"cdr": {"REQ": {"Attr:1": 123}}}, 123
        )

    def test_safe_calls(self):
        self.assertEvaluatedTo("$var?.foo?()", {"var": None}, None)
        self.assertEvaluatedTo("$var?.foo?(123)", {"var": None}, None)
        with self.assertRaises(Exception):
            self.compile("$var?.bar?()")({"var": None})

