#!/usr/bin/env python

from unittest import main
from tests import CompilerCase as TestCase

from hydra.hyaml.methods import units


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
