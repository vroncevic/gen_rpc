# -*- coding: UTF-8 -*-

'''
 Module
     __init__.py
 Copyright
     Copyright (C) 2021 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Defined class RPCService with attribute(s) and method(s).
     Generate module file generator_test.py by template and parameters.
'''

import sys

try:
    from pathlib import Path
    from gen_rpc.pro.config import ProConfig
    from gen_rpc.pro.config.pro_name import ProName
    from gen_rpc.pro.config.pro_type import ProType
    from gen_rpc.pro.read_template import ReadTemplate
    from gen_rpc.pro.write_template import WriteTemplate
    from ats_utilities.checker import ATSChecker
    from ats_utilities.config_io.base_check import FileChecking
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config_io.yaml.yaml2object import Yaml2Object
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2021, https://vroncevic.github.io/gen_rpc'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_rpc/blob/dev/LICENSE'
__version__ = '1.0.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class RPCService(FileChecking, ProConfig, ProName, ProType):
    '''
        Defined class RPCService with attribute(s) and method(s).
        Generate module file generator_test.py by template and parameters.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
                | PRO_STRUCTURE - project setup (template, module).
                | __reader - reader API.
                | __writer - writer API.
            :methods:
                | __init__ - initial constructor.
                | get_reader - getter for template reader.
                | get_writer - getter for template writer.
                | gen_setup - generate module file setup.py.
                | select_rcp_type - select RCP type.
                | __str__ - dunder method for RPCService.
    '''

    GEN_VERBOSE = 'GEN_RPC::PRO::GEN_SETUP'
    PRO_STRUCTURE = '/../conf/project.yaml'

    def __init__(self, project_name, verbose=False):
        '''
            Initial constructor.

            :param project_name: project tool/generator name.
            :type project_name: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('str:project_name', project_name)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        verbose_message(RPCService.GEN_VERBOSE, verbose, 'init generator')
        FileChecking.__init__(self, verbose=verbose)
        ProConfig.__init__(self, verbose=verbose)
        ProName.__init__(self, verbose=verbose)
        ProType.__init__(self, verbose=verbose)
        project_structure = '{0}{1}'.format(
            Path(__file__).parent, RPCService.PRO_STRUCTURE
        )
        self.check_path(file_path=project_structure, verbose=verbose)
        self.check_mode(file_mode='r', verbose=verbose)
        self.check_format(
            file_path=project_structure, file_format='yaml', verbose=verbose
        )
        self.__reader = ReadTemplate(verbose=verbose)
        self.__writer = WriteTemplate(verbose=verbose)
        if self.is_file_ok():
            yml2obj = Yaml2Object(project_structure)
            self.config = yml2obj.read_configuration()
            self.pro_name = project_name

    def get_reader(self):
        '''
            Getter for template reader.

            :return: template reader object.
            :rtype: <ReadTemplate>
            :exceptions: None
        '''
        return self.__reader

    def get_writer(self):
        '''
            Getter for template writer.

            :return: template writer object.
            :rtype: <WriteTemplate>
            :exceptions: None
        '''
        return self.__writer

    def gen_setup(self, verbose=False):
        '''
            Generate module generator_test.py.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: boolean status, True (success) | False.
            :rtype: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        status = False
        verbose_message(
            RPCService.GEN_VERBOSE, verbose, 'generating MQTT service'
        )
        if all([bool(self.pro_name), bool(self.config)]):
            rpc_type = self.select_rcp_type(verbose=verbose)
            if rpc_type == 'cancel':
                status = True
            else:
                setup_content = None
                setup_content = self.__reader.read(rpc_type, verbose=verbose)
                if setup_content:
                    status = self.__writer.write(
                        setup_content, self.pro_name, verbose=verbose
                    )
        return status

    def select_rcp_type(self, verbose=False):
        '''
            Select RCP type.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: project template selected | None.
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        template_selected = None
        if bool(self.config):
            types = self.config['types']
            pro_types_len = len(types)
            for index, pro_type in enumerate(types):
                print(
                    '{0} {1}'.format(index + 1, pro_type.capitalize())
                )
                verbose_message(
                    RPCService.GEN_VERBOSE, verbose,
                    'to be processed template', pro_type.capitalize()
                )
            while True:
                try:
                    try:
                        input_type = raw_input(' select RPC type: ')
                    except NameError:
                        input_type = input(' select RPC type: ')
                    options = xrange(1, pro_types_len + 1, 1)
                except NameError:
                    options = range(1, pro_types_len + 1, 1)
                try:
                    if int(input_type) in list(options):
                        template_selected = self.config['templates'][
                            int(input_type) - 1
                        ]
                        break
                    else:
                        raise ValueError
                except ValueError:
                    error_message(
                        RPCService.GEN_VERBOSE, 'not an appropriate choice'
                    )
            verbose_message(
                RPCService.GEN_VERBOSE, verbose, 'selected', template_selected
            )
        return template_selected

    def __str__(self):
        '''
            Dunder method for RPCService.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2}, {3}, {4}, {5}, {6})'.format(
            self.__class__.__name__, FileChecking.__str__(self),
            ProConfig.__str__(self), ProName.__str__(self),
            ProType.__str__(self), str(self.__reader), str(self.__writer)
        )
