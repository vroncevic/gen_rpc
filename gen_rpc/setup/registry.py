# -*- coding: UTF-8 -*-

'''
Module
    registry.py
Copyright
    Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    gen_rpc is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    gen_rpc is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Encapsulates core gen_rpc components for simplification of gen_rpc bundle.
'''

from __future__ import annotations

from ats_utilities.base.setup.bundle import BaseBundle

from gen_rpc.core.service.iservice import IService
from gen_rpc.core.service.isubprocessor import ISubProcessor
from gen_rpc.infrastructure.cli.icli import ICLI
from gen_rpc.setup.bundle import GenRPCBundle
from gen_rpc.setup.validator import GenRPCBundleValidator
from gen_rpc.setup.keys import GenRPCBundleKeys
from gen_rpc.setup.dependencies import GenRPCBundleDependencies
from gen_rpc.setup.dep_validator import GenRPCBundleDependenciesValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_rpc'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_rpc/blob/dev/LICENSE'
__version__ = '1.0.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenRPCBundleRegistry:
    '''
        Encapsulates core gen_rpc components for simplification of gen_rpc bundle.

        It defines:

            :methods:
                | create_bundle - Creates the gen_rpc bundle.
    '''

    @classmethod
    def create_bundle(cls, dependencies: GenRPCBundleDependencies) -> GenRPCBundle:
        '''
            Creates the gen_rpc bundle.

            :param dependencies: The gen_rpc bundle dependencies.
            :return: The gen_rpc bundle.
            :exceptions:
                | ATSValueError: The gen_rpc bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The gen_rpc bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_rpc bundle must be provided and have proper values.
                | ATSTypeError:  The gen_rpc bundle must be an instance of GenRPCBundle and
                |                its attributes must be instances of their respective types.
        '''
        GenRPCBundleDependenciesValidator.validate(dependencies)

        base: BaseBundle | None = dependencies.get(GenRPCBundleKeys.DEPENDENCY_BASE) if dependencies else None
        service: IService | None = dependencies.get(GenRPCBundleKeys.DEPENDENCY_SERVICE) if dependencies else None
        subprocessor: ISubProcessor | None = dependencies.get(GenRPCBundleKeys.DEPENDENCY_SUBPROCESSOR) if dependencies else None
        cli: ICLI | None = dependencies.get(GenRPCBundleKeys.DEPENDENCY_CLI) if dependencies else None

        bundle: GenRPCBundle = GenRPCBundle(base=base, service=service, subprocessor=subprocessor, cli=cli)

        GenRPCBundleValidator.validate(bundle)

        return bundle
