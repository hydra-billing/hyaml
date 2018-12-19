#!/usr/bin/env python

from unittest import main
from tests import CompilerCase as TestCase
from datetime import datetime

from hydra.hyaml.methods import prelude


class TestString(TestCase):
    bindings = ("variables",)
    method_table = prelude.string

    def test_length(self):
        self.assertMethodCall("$x.length()", 0, x="")
        self.assertMethodCall("$x.length()", 3, x="foo")

    def test_substring(self):
        self.assertMethodCall("$x.substring(0)", "foo", x="foo")
        self.assertMethodCall("$x.substring(1)", "oo", x="foo")
        self.assertMethodCall("$x.substring(10)", "", x="foo")
        self.assertMethodCall("$x.substring(10)", "", x="")
        self.assertMethodCall("$x.substring(0, 1)", "f", x="f")
        self.assertMethodCall("$x.substring(0, 10)", "foo", x="foo")

    def test_converting_to_integer(self):
        self.assertMethodCall("$x.to_i()", 10, x="10")
        self.assertMethodCall("$x.to_i(8)", 8, x="10")
        self.assertMethodCall("$x.to_i(16)", 255, x="ff")
        self.assertMethodCall("$x.to_i(2)", 15, x="1111")

    def test_unhex(self):
        self.assertMethodCall("$x.unhex()", "-", x="0x2d")
        self.assertMethodCall("$x.unhex()", "-", x="2d")

    def test_replace(self):
        self.assertMethodCall("$x.replace($y)", "ac", x="abcb", y="b")
        self.assertMethodCall("$x.replace($y, 'd')", "adcd", x="abcb", y="b")

    def test_reverse(self):
        self.assertMethodCall("$x.reverse()", "cba", x="abc")
        self.assertMethodCall("$x.reverse()", "", x="")

    def test_padding(self):
        self.assertMethodCall("$x.pad_right($y, $z)", "abczzz", x="abc", y=6, z="z")
        self.assertMethodCall("$x.pad_right($y, $z)", "abc", x="abc", y=2, z="z")
        self.assertMethodCall("$x.pad_right($y, $z)", "abc", x="abc", y=0, z="z")
        self.assertMethodCall("$x.pad_left($y, $z)", "zzzabc", x="abc", y=6, z="z")
        self.assertMethodCall("$x.pad_left($y, $z)", "abc", x="abc", y=2, z="z")
        self.assertMethodCall("$x.pad_left($y, $z)", "abc", x="abc", y=0, z="z")

    def test_regexp_replace(self):
        self.assertMethodCall("$x.regexp_replace('\\s+')", "abc", x="  a  b\n\rc")
        self.assertMethodCall("$x.regexp_replace('^\\d', 'd')", "d23", x="123")

    def test_string_start_end(self):
        self.assertMethodCall("$x.starts_with?($y)", True, x="abc", y="ab")
        self.assertMethodCall("$x.starts_with?($y)", False, x="abc", y="ba")
        self.assertMethodCall("$x.ends_with?($y)", True, x="abc", y="bc")
        self.assertMethodCall("$x.ends_with?($y)", False, x="abc", y="cb")

    def test_matching(self):
        self.assertMethodCall("$x.like?('^foo')", True, x="foobar")
        self.assertMethodCall("$x.like?('^foo')", False, x="barfoo")

    def test_split(self):
        self.assertMethodCall("$x.split()", ["123", "456"], x="123 456")
        self.assertMethodCall("$x.split('.')", ["1", "2", "3"], x="1.2.3")
        self.assertMethodCall("$x.split('.')", ["123"], x="123")
        self.assertMethodCall("$x.split('.', 1)", ["1", "2.3"], x="1.2.3")

    def test_strip(self):
        self.assertMethodCall("$x.strip()", "foo", x=" \n\r\t   foo   \n\t\r ")

    def test_upper_lower(self):
        self.assertMethodCall("$x.upper()", "FOO", x="foo")
        self.assertMethodCall("$x.lower()", "foo", x="FOO")

    def test_date_conversion(self):
        self.assertMethodCall(
            "$x.to_date($fmt)", datetime(2018, 12, 19), x="2018-12-19", fmt="%Y-%m-%d"
        )


class TestNumber(TestCase):
    bindings = ("variables",)
    method_table = prelude.number

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


class TestPolymorphic(TestCase):
    bindings = ("variables",)
    method_table = prelude.polymorphic

    def test_to_hex(self):
        self.assertMethodCall("$x.to_hex()", "0xa", x=10)
        self.assertMethodCall("$x.to_hex()", "3130", x="10")

    def test_null(self):
        self.assertMethodCall("$x.null?()", True, x=None)
        self.assertMethodCall("$x.null?()", False, x=1)

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

    def test_to_s(self):
        self.assertMethodCall("$x.to_s()", "5", x=5)
        self.assertMethodCall("$x.to_s()", "5", x="5")
        self.assertMethodCall("$x.to_s()", "", x=None)
        self.assertMethodCall("$x.to_s()", "5.0", x=5.0)

    def test_try(self):
        self.assertMethodCall("$x.try('Foo')", 5, x={"Foo": 5})
        self.assertMethodCall("$x.try('Bar')", None, x={"Foo": 5})
        self.assertMethodCall("$x.try('Bar').try('Buzz')", None, x={"Foo": 5})
        self.assertMethodCall("$x.try('Bar', 6)", 6, x={"Foo": 5})
        self.assertMethodCall("$x.try(1)", 2, x=[1, 2, 3])
        self.assertMethodCall("$x.try(1, 6)", 2, x=[1, 2, 3])
        self.assertMethodCall("$x.try(10, 6)", 6, x=[1, 2, 3])
        self.assertMethodCall("$x.try(-1)", 3, x=[1, 2, 3])
        self.assertMethodCall("$x.try(-3)", 1, x=[1, 2, 3])
        self.assertMethodCall("$x.try(-10)", None, x=[1, 2, 3])
        self.assertMethodCall("$x.try(2)", 4, x=range(2, 10))
        self.assertMethodCall("$x.try(20)", None, x=range(2, 10))

    def test_coalesce(self):
        self.assertMethodCall("$x.coalesce()", None, x=None)
        self.assertMethodCall("$x.coalesce()", 0, x=0)
        self.assertMethodCall("$x.coalesce(1)", 1, x=None)
        self.assertMethodCall("$x.coalesce($y, 1)", 1, x=None, y=None)
        self.assertMethodCall("$x.coalesce($y, 1)", 2, x=None, y=2)
        self.assertMethodCall("$x.coalesce(1, $y)", 1, x=None, y=None)
        self.assertMethodCall("$x.coalesce($y)", None, x=None, y=None)


class TestDictionary(TestCase):
    bindings = ("variables",)
    method_table = prelude.dictionary

    def test_merge(self):
        self.assertMethodCall("$x.merge('b', 10)", {"a": 5, "b": 10}, x={"a": 5})
        self.assertMethodCall("$x.merge({b: 10})", {"a": 5, "b": 10}, x={"a": 5})
        self.assertMethodCall("$x.merge(['b', 10])", {"a": 5, "b": 10}, x={"a": 5})
        self.assertMethodCall(
            "$x.merge([['b', 10], ['c', 20]])", {"a": 5, "b": 10, "c": 20}, x={"a": 5}
        )

    def test_pairs(self):
        self.assertMethodCall("$x.pairs()", [("a", 1), ("b", 2)], x={"b": 2, "a": 1})

    def test_except(self):
        self.assertMethodCall(
            "$x.except('b', 'c')", {"a": 1}, x={"a": 1, "b": 2, "c": 3}
        )


class TestArray(TestCase):
    bindings = ("variables",)
    method_table = prelude.array

    def test_map_join(self):
        self.assertMethodCall(
            "$x.map_join()", ["1,2,3", "a,b,c"], x=[["1", "2", "3"], ["a", "b", "c"]]
        )
        self.assertMethodCall(
            "$x.map_join('-')", ["1-2-3", "a-b-c"], x=[["1", "2", "3"], ["a", "b", "c"]]
        )
        self.assertMethodCall(
            "$x.map_join('')", ["123", "abc"], x=[["1", "2", "3"], ["a", "b", "c"]]
        )

    def test_join(self):
        self.assertMethodCall("$x.join()", "", x=[])
        self.assertMethodCall("$x.join()", "123", x=[1, 2, 3])
        self.assertMethodCall("$x.join()", "123", x=[1, None, 2, None, 3])

