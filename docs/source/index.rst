Create C project skeleton
--------------------------

**gen_rpc** is tool for creating C project skeleton.

Developed in `python <https://www.python.org/>`_ code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|gen_rpc python checker| |gen_rpc python package| |github issues| |documentation status| |github contributors|

.. |gen_rpc python checker| image:: https://github.com/vroncevic/gen_rpc/actions/workflows/gen_rpc_python_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_rpc/actions/workflows/gen_rpc_python_checker.yml

.. |gen_rpc python package| image:: https://github.com/vroncevic/gen_rpc/actions/workflows/gen_rpc_package_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_rpc/actions/workflows/gen_rpc_package.yml

.. |github issues| image:: https://img.shields.io/github/issues/vroncevic/gen_rpc.svg
   :target: https://github.com/vroncevic/gen_rpc/issues

.. |github contributors| image:: https://img.shields.io/github/contributors/vroncevic/gen_rpc.svg
   :target: https://github.com/vroncevic/gen_rpc/graphs/contributors

.. |documentation status| image:: https://readthedocs.org/projects/gen-rpc/badge/?version=latest
   :target: https://gen-rpc.readthedocs.io/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents

   self
   modules

Installation
-------------

|gen_rpc python3 build|

.. |gen_rpc python3 build| image:: https://github.com/vroncevic/gen_rpc/actions/workflows/gen_rpc_python3_build.yml/badge.svg
   :target: https://github.com/vroncevic/gen_rpc/actions/workflows/gen_rpc_python3_build.yml

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_rpc/releases

To install this set of modules type the following

.. code-block:: bash

    tar xvzf gen_rpc-x.y.z.tar.gz
    cd gen_rpc-x.y.z
    #python3
    pip3 install -r requirements.txt
    python3 setup.py install_lib
    python3 setup.py install_egg_info
    python3 setup.py install_data

You can use Docker to create image/container, or You can use pip to install

.. code-block:: bash

    #python3
    pip3 install gen_rpc

Dependencies
-------------

**gen_rpc** requires next modules and libraries

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

Tool structure
------------------

**gen_rpc** is based on OOP

Code structure

.. code-block:: bash

    gen_rpc/
        ├── conf/
        │   ├── gen_rpc.cfg
        │   ├── gen_rpc.logo
        │   ├── gen_rpc_util.cfg
        │   ├── project.yaml
        │   └── template/
        │       ├── rpc_client.template
        │       ├── rpc_server.template
        │       └── rpc_square.template
        ├── __init__.py
        ├── log/
        │   └── gen_rpc.log
        ├── pro/
        │   ├── __init__.py
        │   ├── read_template.py
        │   └── write_template.py
        └── run/
            └── gen_rpc_run.py
    
    6 directories, 14 files

Copyright and licence
----------------------

|license: gpl v3| |license: apache 2.0|

.. |license: gpl v3| image:: https://img.shields.io/badge/license-gplv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |license: apache 2.0| image:: https://img.shields.io/badge/license-apache%202.0-blue.svg
   :target: https://opensource.org/licenses/apache-2.0

Copyright (C) 2020 - 2024 by `vroncevic.github.io/gen_rpc <https://vroncevic.github.io/gen_rpc>`_

**gen_rpc** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|python software foundation|

.. |python software foundation| image:: https://raw.githubusercontent.com/vroncevic/gen_rpc/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|donate|

.. |donate| image:: https://www.paypalobjects.com/en_us/i/btn/btn_donatecc_lg.gif
   :target: https://www.python.org/psf/donations/

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
