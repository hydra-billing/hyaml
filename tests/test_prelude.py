#!/usr/bin/env python

from unittest import main
from tests import CompilerCase as TestCase

from hydra.hyaml import prelude


class TestPredicates(TestCase):
    bindings = ("variables",)
    method_table = prelude.predicates

    def test_evenness(self):
        self.assertMethodCall("$x.odd?()", True, x=1)
        self.assertMethodCall("$x.odd?()", False, x=2)
        self.assertMethodCall("$x.odd?()", False, x=0)
        self.assertMethodCall("$x.odd?()", True, x=-1)
        self.assertMethodCall("$x.odd?()", False, x=-2)
        self.assertMethodCall("$x.even?()", False, x=1)
        self.assertMethodCall("$x.even?()", True, x=2)
        self.assertMethodCall("$x.even?()", True, x=0)
        self.assertMethodCall("$x.even?()", False, x=-1)
        self.assertMethodCall("$x.even?()", True, x=-2)

    def test_matching(self):
        self.assertMethodCall("$x.like?('^foo')", True, x="foobar")
        self.assertMethodCall("$x.like?('^foo')", False, x="barfoo")

    def test_emptiness(self):
        self.assertMethodCall("$x.empty?()", True, x=False)
        self.assertMethodCall("$x.empty?()", False, x=True)
        self.assertMethodCall("$x.empty?()", True, x=[])
        self.assertMethodCall("$x.empty?()", False, x=[1])
        self.assertMethodCall("$x.empty?()", True, x=0)
        self.assertMethodCall("$x.empty?()", False, x=1)
        self.assertMethodCall("$x.empty?()", True, x="")
        self.assertMethodCall("$x.empty?()", False, x="a")
        self.assertMethodCall("$x.empty?()", True, x={})
        self.assertMethodCall("$x.empty?()", False, x={"a": 1})

    def test_inclusion(self):
        self.assertMethodCall("$x.in?($y)", True, x=1, y=[1, 2, 3])
        self.assertMethodCall("$x.in?($y)", False, x=10, y=[1, 2, 3])
        self.assertMethodCall("$x.in?($y)", True, x="a", y={"a": 1})
        self.assertMethodCall("$x.in?($y)", False, x="b", y={"a": 1})
        self.assertMethodCall("$x.in?($y)", True, x="a", y="bac")
        self.assertMethodCall("$x.in?($y)", False, x="d", y="bac")

    def test_null(self):
        self.assertMethodCall("$x.null?()", True, x=None)
        self.assertMethodCall("$x.null?()", False, x=1)

    def test_string_start_end(self):
        self.assertMethodCall("$x.starts_with?($y)", True, x="abc", y="ab")
        self.assertMethodCall("$x.starts_with?($y)", False, x="abc", y="ba")
        self.assertMethodCall("$x.ends_with?($y)", True, x="abc", y="bc")
        self.assertMethodCall("$x.ends_with?($y)", False, x="abc", y="cb")
