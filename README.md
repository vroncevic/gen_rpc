<img align="right" src="https://raw.githubusercontent.com/vroncevic/gen_rpc/dev/docs/gen_rpc_logo.png" width="25%">

# Generate RPC modules

**gen_rpc** is tool for generation of RPC modules.

Developed in **[python](https://www.python.org/)** code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

![Python package](https://github.com/vroncevic/gen_rpc/workflows/Python%20package%20gen_rpc/badge.svg?branch=master) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_rpc.svg)](https://github.com/vroncevic/gen_rpc/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_rpc.svg)](https://github.com/vroncevic/gen_rpc/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
    - [Install using pip](#install-using-pip)
    - [Install using setuptools](#install-using-setuptools)
    - [Install using docker](#install-using-docker)
- [Dependencies](#dependencies)
- [Generation flow of RPC modules](#generation-flow-of-rpc-modules)
- [RPC System](#rpc-system)
- [RPC Mapper](#rpc-mapper)
- [Tool structure](#tool-structure)
- [Docs](#docs)
- [Copyright and Licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

Used next development environment

![Development environment](https://raw.githubusercontent.com/vroncevic/gen_rpc/dev/docs/debtux.png)

![Install Python2 Package](https://github.com/vroncevic/gen_rpc/workflows/Install%20Python2%20Package%20gen_rpc/badge.svg?branch=master) ![Install Python3 Package](https://github.com/vroncevic/gen_rpc/workflows/Install%20Python3%20Package%20gen_rpc/badge.svg?branch=master)

Currently there are three ways to install tool:
* Install process based on pip
* Install process based on setup.py (setuptools)
* Install process based on docker mechanism

##### Install using pip

Python package is located at **[pypi.org](https://pypi.org/project/gen-rpc/)**.

You can install by using pip
```
# python2
pip install gen-rpc
# python3
pip3 install gen-rpc
```

##### Install using setuptools

Navigate to release **[page](https://github.com/vroncevic/gen_rpc/releases/)** download and extract release archive.

To install modules, locate and run setup.py with arguments
```
tar xvzf gen_rpc-x.y.z.tar.gz
cd gen_rpc-x.y.z/
# python2
pip install -r requirements.txt
python setup.py install_lib
python setup.py install_data
python setup.py install_egg_info
# python3
pip3 install -r requirements.txt
python3 setup.py install_lib
python3 setup.py install_data
python3 setup.py install_egg_info
```

##### Install using docker

You can use docker to create image/container.

[![gen_rpc docker checker](https://github.com/vroncevic/gen_rpc/workflows/gen_rpc%20docker%20checker/badge.svg)](https://github.com/vroncevic/gen_rpc/actions?query=workflow%3A%22gen_rpc+docker+checker%22)

### Dependencies

**gen_rpc** requires next modules and libraries:

* [ats-utilities - Python App/Tool/Script Utilities](https://vroncevic.github.io/ats_utilities)

### Generation flow of RPC modules

Base flow of generation process:

![RPC generation flow](https://raw.githubusercontent.com/vroncevic/gen_rpc/dev/docs/gen_rpc_flow.png)

### RPC System
![RPC system](https://raw.githubusercontent.com/vroncevic/gen_rpc/dev/docs/rpc_system.png)

```
1. Client encodes data through XDR Filter
2. Client passes XDR encoded data across network to remote host
3. Server decodes data through XDR Filter
4. Server encodes functional call result through XDR Filter
5. Server pass XDR encoded data across network back to Client
6. Client decodes RPC result through XDR Filter and continues processing
```

### RPC Mapper
![RPC portmap](https://raw.githubusercontent.com/vroncevic/gen_rpc/dev/docs/rpc_portmap.png)

### Tool structure

**gen_rpc** is based on OOP.

Generator structure:

```

```

### Docs

[![Documentation Status](https://readthedocs.org/projects/gen_rpc/badge/?version=latest)](https://gen_rpc.readthedocs.io/projects/gen_rpc/en/latest/?badge=latest)

More documentation and info at:
* [gen_rpc.readthedocs.io](https://gen_rpc.readthedocs.io/en/latest/)
* [rpc mechanism](overview.md)
* [www.python.org](https://www.python.org/)

### Copyright and Licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2019 by [vroncevic.github.io/gen_rpc](https://vroncevic.github.io/gen_rpc)

**gen_rpc** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/gen_rpc/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2)
