# -*- coding: UTF-8 -*-

'''
Module
    test_engine.py
Info
    Unit tests for GenRPC engine.
'''

from __future__ import annotations

import unittest
from unittest.mock import Mock, patch

from ats_utilities.base.setup.factory import BaseBundleFactory
from ats_utilities.base.setup.options import BaseBundleOptions
from ats_utilities.context.factory import ContextBundleFactory
from ats_utilities.exceptions import ATSValueError

from gen_rpc.engine import GenRPC
from gen_rpc.setup.bundle import GenRPCBundle
from gen_rpc.setup.factory import GenRPCBundleFactory
from gen_rpc.core.service.iservice import IService
from gen_rpc.core.service.isubprocessor import ISubProcessor
from gen_rpc.infrastructure.cli.icli import ICLI


class DummyService(IService):
    def execute(self, *, params: object) -> object:
        return None
    def is_initialized(self) -> bool:
        return True
    def __str__(self) -> str:
        return 'DummyService'


class DummySubProcessor(ISubProcessor):
    def run(self, *, params: object) -> dict[str, object]:
        return {}
    def is_initialized(self) -> bool:
        return True
    def __str__(self) -> str:
        return 'DummySubProcessor'


class DummyCLI(ICLI):
    def __init__(self, return_code: int = 0, stderr: str = '') -> None:
        self.return_code = return_code
        self.stderr = stderr

    def run(self) -> dict[str, object]:
        return {'returncode': self.return_code, 'stderr': self.stderr}

    def is_initialized(self) -> bool:
        return True

    def __str__(self) -> str:
        return 'DummyCLI'


class TestGenRPC(unittest.TestCase):
    def test_engine_init_success(self) -> None:
        bundle = GenRPCBundleFactory.create_bundle()
        engine = GenRPC(bundle)
        self.assertTrue(engine.is_initialized())

    def test_engine_init_fail_validation(self) -> None:
        engine = GenRPC(None)
        self.assertFalse(engine.is_initialized())

    def test_engine_process_success(self) -> None:
        context_bundle = ContextBundleFactory.create_bundle()
        mock_base = BaseBundleFactory.create_bundle(
            options=BaseBundleOptions(
                info_file='gen_rpc/infrastructure/config/gen_rpc.cfg',
                use_generator=True,
                context_bundle=context_bundle
            )
        )
        
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI(return_code=0)

        bundle = GenRPCBundle(
            base=mock_base,
            service=dummy_service,
            subprocessor=dummy_subprocessor,
            cli=dummy_cli
        )

        engine = GenRPC(bundle)
        self.assertTrue(engine.is_initialized())
        self.assertTrue(engine.process())

    def test_engine_process_cli_failure(self) -> None:
        context_bundle = ContextBundleFactory.create_bundle()
        mock_base = BaseBundleFactory.create_bundle(
            options=BaseBundleOptions(
                info_file='gen_rpc/infrastructure/config/gen_rpc.cfg',
                use_generator=True,
                context_bundle=context_bundle
            )
        )
        
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI(return_code=1, stderr='CLI error')

        bundle = GenRPCBundle(
            base=mock_base,
            service=dummy_service,
            subprocessor=dummy_subprocessor,
            cli=dummy_cli
        )

        engine = GenRPC(bundle)
        self.assertTrue(engine.is_initialized())
        self.assertFalse(engine.process())

    def test_engine_process_not_initialized(self) -> None:
        context_bundle = ContextBundleFactory.create_bundle()
        mock_base = BaseBundleFactory.create_bundle(
            options=BaseBundleOptions(
                info_file='gen_rpc/infrastructure/config/gen_rpc.cfg',
                use_generator=True,
                context_bundle=context_bundle
            )
        )
        
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI()

        # Force base option_manager initialization to return False
        mock_base.option_manager.is_initialized = Mock(return_value=False)

        bundle = GenRPCBundle(
            base=mock_base,
            service=dummy_service,
            subprocessor=dummy_subprocessor,
            cli=dummy_cli
        )

        engine = GenRPC(bundle)
        self.assertFalse(engine.is_initialized())
        self.assertFalse(engine.process())

    def test_engine_process_exception(self) -> None:
        context_bundle = ContextBundleFactory.create_bundle()
        mock_base = BaseBundleFactory.create_bundle(
            options=BaseBundleOptions(
                info_file='gen_rpc/infrastructure/config/gen_rpc.cfg',
                use_generator=True,
                context_bundle=context_bundle
            )
        )
        
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        
        dummy_cli = DummyCLI()
        dummy_cli.run = Mock(side_effect=Exception('Unexpected error'))

        bundle = GenRPCBundle(
            base=mock_base,
            service=dummy_service,
            subprocessor=dummy_subprocessor,
            cli=dummy_cli
        )

        engine = GenRPC(bundle)
        self.assertTrue(engine.is_initialized())
        self.assertFalse(engine.process())

    def test_engine_process_validation_exception(self) -> None:
        context_bundle = ContextBundleFactory.create_bundle()
        mock_base = BaseBundleFactory.create_bundle(
            options=BaseBundleOptions(
                info_file='gen_rpc/infrastructure/config/gen_rpc.cfg',
                use_generator=True,
                context_bundle=context_bundle
            )
        )
        
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI()
        dummy_cli.run = Mock(side_effect=ATSValueError('Validation error in run'))

        bundle = GenRPCBundle(
            base=mock_base,
            service=dummy_service,
            subprocessor=dummy_subprocessor,
            cli=dummy_cli
        )

        engine = GenRPC(bundle)
        self.assertTrue(engine.is_initialized())
        self.assertFalse(engine.process())

    @patch('gen_rpc.setup.validator.GenRPCBundleValidator.validate')
    def test_engine_init_generic_exception(self, mock_validate: Mock) -> None:
        mock_validate.side_effect = Exception('Unexpected generic validation error')
        
        context_bundle = ContextBundleFactory.create_bundle()
        mock_base = BaseBundleFactory.create_bundle(
            options=BaseBundleOptions(
                info_file='gen_rpc/infrastructure/config/gen_rpc.cfg',
                use_generator=True,
                context_bundle=context_bundle
            )
        )
        
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI()

        bundle = GenRPCBundle(
            base=mock_base,
            service=dummy_service,
            subprocessor=dummy_subprocessor,
            cli=dummy_cli
        )

        engine = GenRPC(bundle)
        self.assertFalse(engine.is_initialized())

    def test_cli_bundle_factory(self) -> None:
        from gen_rpc.infrastructure.cli.setup.factory import CLIBundleFactory
        from gen_rpc.infrastructure.cli.setup.options import CLIBundleOptions
        from ats_utilities.option.imanager import IOptionManager
        from unittest.mock import MagicMock
        opts = CLIBundleOptions(
            service=DummyService(),
            parser=MagicMock(spec=IOptionManager)
        )
        bundle = CLIBundleFactory.create_bundle(opts)
        self.assertIsNotNone(bundle)

    def test_cli_bundle_factory_validation_error(self) -> None:
        from gen_rpc.infrastructure.cli.setup.factory import CLIBundleFactory
        from ats_utilities.exceptions import ATSValueError
        with self.assertRaises(ATSValueError):
            CLIBundleFactory.create_bundle(None)

    def test_cli_bundle_factory_type_error(self) -> None:
        from gen_rpc.infrastructure.cli.setup.factory import CLIBundleFactory
        from gen_rpc.infrastructure.cli.setup.options import CLIBundleOptions
        from ats_utilities.exceptions import ATSTypeError
        from unittest.mock import MagicMock
        opts = CLIBundleOptions(
            service="not a service",
            parser=MagicMock()
        )
        with self.assertRaises(ATSTypeError):
            CLIBundleFactory.create_bundle(opts)

