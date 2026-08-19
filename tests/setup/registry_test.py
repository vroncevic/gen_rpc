# -*- coding: UTF-8 -*-

'''
Module
    registry_test.py
Info
    Unit tests for GenRPCBundleRegistry class.
'''

from __future__ import annotations

import unittest
from unittest.mock import Mock

from ats_utilities.base.setup.bundle import BaseBundle

from gen_rpc.core.service.iservice import IService
from gen_rpc.core.service.isubprocessor import ISubProcessor
from gen_rpc.infrastructure.cli.icli import ICLI
from gen_rpc.setup.bundle import GenRPCBundle
from gen_rpc.setup.registry import GenRPCBundleRegistry


class DummyService:

    def execute(self, *, params: object) -> object:
        return None

    def is_initialized(self) -> bool:
        return True


class DummySubProcessor:

    def run(self, *, params: object) -> dict[str, object]:
        return {}

    def is_initialized(self) -> bool:
        return True


class DummyCLI:

    def run(self) -> dict[str, object]:
        return {}

    def is_initialized(self) -> bool:
        return True


class TestGenRPCBundleRegistry(unittest.TestCase):

    def test_create_bundle_success(self) -> None:
        mock_base = Mock(spec=BaseBundle)
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI()

        dependencies = {
            'base': mock_base,
            'service': dummy_service,
            'subprocessor': dummy_subprocessor,
            'cli': dummy_cli
        }
        
        bundle = GenRPCBundleRegistry.create_bundle(dependencies)
        self.assertIsInstance(bundle, GenRPCBundle)
        self.assertEqual(bundle.base, mock_base)

    def test_create_bundle_invalid_dependencies(self) -> None:
        with self.assertRaises(Exception):
            GenRPCBundleRegistry.create_bundle(None)

    def test_get_version(self) -> None:
        self.assertEqual(GenRPCBundleRegistry.get_version(), '1.0.5')
