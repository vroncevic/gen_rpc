# -*- coding: UTF-8 -*-

'''
 Module
     write_template.py
 Copyright
     Copyright (C) 2019 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Defined class WriteTemplate with attribute(s) and method(s).
     Created API for write operation of template content.
'''

import sys
from datetime import date
from os import getcwd, chmod
from string import Template

try:
    from ats_utilities.checker import ATSChecker
    from ats_utilities.config_io.base_check import FileChecking
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2019, https://vroncevic.github.io/gen_rpc'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_rpc/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class WriteTemplate(FileChecking):
    '''
        Defined class WriteTemplate with attribute(s) and method(s).
        Created API for write operation of template content.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
            :methods:
                | __init__ - initial constructor.
                | get_setup - getter for setup file object.
                | write - write a template content to a RPC files.
                | __str__ - dunder method for WriteTemplate.
    '''

    GEN_VERBOSE = 'GEN_RPC::PRO::WRITE_TEMPLATE'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        FileChecking.__init__(self, verbose=verbose)
        verbose_message(WriteTemplate.GEN_VERBOSE, verbose, 'init writer')

    def write(self, setup_content, pro_name, verbose=False):
        '''
            Write a template content to a RPC files.

            :param setup_content: template content.
            :type setup_content: <list>
            :param pro_name: parameter project name.
            :type pro_name: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: boolean status, True (success) | False.
            :rtype: <bool>
            :exception: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('list:setup_content', setup_content),
            ('str:pro_name', pro_name)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        status, template = False, None
        package = {
            'PRO': '{0}'.format(pro_name),
            'YEAR': '{0}'.format(date.today().year)
        }
        for setup in setup_content:
            for module, template_content in setup.items():
                template = Template(template_content)
                if template:
                    module_path = '{0}/{1}'.format(getcwd(), module)
                    with open(module_path, 'w') as setup_file:
                        setup_file.write(template.substitute(package))
                        verbose_message(
                            WriteTemplate.GEN_VERBOSE, verbose,
                            'write', module_path
                        )
                        chmod(module_path, 0o666)
                        self.check_path(module_path, verbose=verbose)
                        self.check_mode('w', verbose=verbose)
                        self.check_format(
                            module_path, module_path.split('.')[1],
                            verbose=verbose
                        )
                        if self.is_file_ok():
                            status = True
        return status

    def __str__(self):
        '''
            Dunder method for WriteTemplate.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, FileChecking.__str__(self),
            str(self.__setup)
        )
