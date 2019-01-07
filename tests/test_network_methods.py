#!/usr/bin/env python

from unittest import main
from tests import ExpressionCompilerCase as TestCase

from hyaml.methods import network


class TestString(TestCase):
    bindings = ("variables",)
    method_table = network

    def test_mac(self):
        self.assertMethodCall("$x.mac?()", False, x="foobar")
        self.assertMethodCall("$x.mac?()", True, x="00-14-22-01-23-45")
        self.assertMethodCall("$x.mac?()", True, x="00-14-AA-01-23-45")
        self.assertMethodCall("$x.mac?()", True, x="00:14:AA:01:23:45")
        self.assertMethodCall("$x.mac?()", True, x="00:14:bb:01:23:45")

    def test_ip4(self):
        self.assertMethodCall("$x.ip4?()", False, x="foobar")
        self.assertMethodCall("$x.ip4?()", True, x="13.125.61.74")

    def test_private_ip4(self):
        self.assertMethodCall("$x.private_ip4?()", False, x="foobar")
        self.assertMethodCall("$x.private_ip4?()", False, x="13.125.61.74")
        self.assertMethodCall("$x.private_ip4?()", True, x="10.125.61.74")
        self.assertMethodCall("$x.private_ip4?()", True, x="172.16.61.74")
        self.assertMethodCall("$x.private_ip4?()", True, x="192.168.61.74")

    def test_ip4_mask(self):
        self.assertMethodCall("$x.ip4_mask?()", False, x="foobar")
        self.assertMethodCall("$x.ip4_mask?()", False, x="0.0.0.1")
        self.assertMethodCall("$x.ip4_mask?()", True, x="255.0.0.0")
        self.assertMethodCall("$x.ip4_mask?()", True, x="255.255.255.255")

    def test_ip4_masking(self):
        self.assertMethodCall("$x.ip4_and($y)", "1.2.0.0", x="1.2.3.4", y="255.255.0.0")
        self.assertMethodCall(
            "$x.ip4_or($y)", "1.2.255.255", x="1.2.3.4", y="0.0.255.255"
        )

    def test_ip4_scan(self):
        self.assertMethodCall("$x.ip4_scan()", "172.16.0.1", x="0x172.16.0.1.15")
        self.assertMethodCall("$x.ip4_scan()", "", x="172.16.0")

    def test_format_mac(self):
        self.assertMethodCall(
            "$x.format_mac()", "00-BB-CC-DD-EE-FF", x="00*bb*cc*dd*ee*ff"
        )
        self.assertMethodCall(
            "$x.format_mac(':')", "00:BB:CC:DD:EE:FF", x="00bbccddeeff"
        )
        self.assertMethodCall(
            "$x.format_mac(':', 3)", "00BB:CCDD:EEFF", x="00bbccddeeff"
        )

    def test_normalize_mac(self):
        self.assertMethodCall(
            "$x.normalize_mac()", "00-BB-CC-DD-EE-FF", x="00*bb*cc*dd*ee*ff"
        )
        self.assertMethodCall(
            "$x.normalize_mac()", "00-BB-CC-DD-EE-FF", x="00bbccddeeff"
        )

    def test_maks_convertions(self):
        self.assertMethodCall("$x.to_subnet_mask()", "255.255.255.255", x=32)
        self.assertMethodCall("$x.to_subnet_mask()", "255.255.255.254", x=31)
        self.assertMethodCall("$x.to_subnet_mask()", "255.255.255.252", x=30)
        self.assertMethodCall("$x.to_subnet_mask()", "255.255.0.0", x=16)
        self.assertMethodCall("$x.to_subnet_mask()", "0.0.0.0", x=0)

        self.assertMethodCall("$x.to_subnet_suffix()", 32, x="255.255.255.255")
        self.assertMethodCall("$x.to_subnet_suffix()", 23, x="255.255.254.0")
        self.assertMethodCall("$x.to_subnet_suffix()", 0, x="0.0.0.0")
