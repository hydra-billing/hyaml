#!/usr/bin/env python

from unittest import main
from tests import ExpressionCompilerCase as TestCase
from datetime import timedelta

from hyaml.methods import units


class TestUnits(TestCase):
    bindings = ("variables",)
    method_table = units

    def test_bytes(self):
        self.assertMethodCall("$x.bytes()", 10, x=10)
        self.assertMethodCall("$x.bytes()", 10, x=10.0)
        self.assertMethodCall("$x.kilobytes()", 10240, x=10)
        self.assertMethodCall("$x.megabytes()", 10485760, x=10)
        self.assertMethodCall("$x.gigabytes()", 10737418240, x=10)
        self.assertMethodCall("$x.terabytes()", 10995116277760, x=10)

    def test_time_intervals(self):
        self.assertMethodCall("$x.seconds()", timedelta(seconds=5), x=5)
        self.assertMethodCall("$x.minutes()", timedelta(minutes=5), x=5)
        self.assertMethodCall("$x.hours()", timedelta(hours=5), x=5)
        self.assertMethodCall("$x.days()", timedelta(days=5), x=5)
        self.assertMethodCall("$x.weeks()", timedelta(weeks=5), x=5)
        self.assertMethodCall("$x.months()", timedelta(days=150), x=5)
        self.assertMethodCall("$x.years()", timedelta(days=5 * 365), x=5)
