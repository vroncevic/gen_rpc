# -*- coding: UTF-8 -*-

'''
Module
    opt_validator_test.py
Info
    Unit tests for GenRPCBundleOptionsValidator class.
'''

from __future__ import annotations

import unittest

from gen_rpc.setup.opt_validator import GenRPCBundleOptionsValidator


class TestGenRPCBundleOptionsValidator(unittest.TestCase):

    def test_validate_success(self) -> None:
        options = {'info_file': 'some_path'}
        GenRPCBundleOptionsValidator.validate(options)

    def test_validate_none(self) -> None:
        with self.assertRaises(Exception):
            GenRPCBundleOptionsValidator.validate(None)

    def test_validate_invalid_type(self) -> None:
        with self.assertRaises(Exception):
            GenRPCBundleOptionsValidator.validate("not_a_mapping")

    def test_validate_invalid_option_type(self) -> None:
        with self.assertRaises(Exception):
            options = {'info_file': 123}
            GenRPCBundleOptionsValidator.validate(options)

    def test_is_valid_success(self) -> None:
        options = {'info_file': 'some_path'}
        self.assertTrue(GenRPCBundleOptionsValidator.is_valid(options))

    def test_is_valid_failure(self) -> None:
        self.assertFalse(GenRPCBundleOptionsValidator.is_valid(None))
        self.assertFalse(GenRPCBundleOptionsValidator.is_valid("not_a_mapping"))
        self.assertFalse(GenRPCBundleOptionsValidator.is_valid({'info_file': 123}))
