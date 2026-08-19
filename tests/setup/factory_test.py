# -*- coding: UTF-8 -*-

'''
Module
    factory_test.py
Info
    Unit tests for GenRPCBundleFactory class.
'''

from __future__ import annotations

import unittest

from gen_rpc.setup.bundle import GenRPCBundle
from gen_rpc.setup.factory import GenRPCBundleFactory


class TestGenRPCBundleFactory(unittest.TestCase):

    def test_create_bundle_default(self) -> None:
        bundle = GenRPCBundleFactory.create_bundle()
        self.assertIsInstance(bundle, GenRPCBundle)

    def test_create_bundle_with_options(self) -> None:
        options = {'info_file': 'gen_rpc/infrastructure/config/gen_rpc.cfg'}
        bundle = GenRPCBundleFactory.create_bundle(options)
        self.assertIsInstance(bundle, GenRPCBundle)

    def test_create_bundle_invalid_options(self) -> None:
        options = {'info_file': 123}
        with self.assertRaises(Exception):
            GenRPCBundleFactory.create_bundle(options)

    def test_get_version(self) -> None:
        self.assertEqual(GenRPCBundleFactory.get_version(), '1.0.5')
