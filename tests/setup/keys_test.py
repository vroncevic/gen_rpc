# -*- coding: UTF-8 -*-

'''
Module
    keys_test.py
Info
    Unit tests for GenRPCBundleKeys class.
'''

from __future__ import annotations

import unittest
from types import MappingProxyType

from gen_rpc.setup.keys import GenRPCBundleKeys


class TestGenRPCBundleKeys(unittest.TestCase):

    def test_get_dependency_to_type(self) -> None:
        deps = GenRPCBundleKeys.get_dependency_to_type()
        self.assertIsInstance(deps, MappingProxyType)
        self.assertIn(GenRPCBundleKeys.DEPENDENCY_BASE, deps)
        self.assertIn(GenRPCBundleKeys.DEPENDENCY_SERVICE, deps)
        self.assertIn(GenRPCBundleKeys.DEPENDENCY_SUBPROCESSOR, deps)
        self.assertIn(GenRPCBundleKeys.DEPENDENCY_CLI, deps)

    def test_get_option_to_type(self) -> None:
        opts = GenRPCBundleKeys.get_option_to_type()
        self.assertIsInstance(opts, MappingProxyType)
        self.assertIn(GenRPCBundleKeys.OPTION_INFO_FILE, opts)
