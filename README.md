# Generate RPC modules

<img align="right" src="https://raw.githubusercontent.com/vroncevic/gen_rpc/dev/docs/gen_rpc_logo.png" width="25%">

**gen_rpc** is tool for generation of RPC modules.

Developed in **[python](https://www.python.org/)** code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

[![gen_rpc python checker](https://github.com/vroncevic/gen_rpc/actions/workflows/gen_rpc_python_checker.yml/badge.svg)](https://github.com/vroncevic/gen_rpc/actions/workflows/gen_rpc_python_checker.yml) [![gen_rpc package checker](https://github.com/vroncevic/gen_rpc/actions/workflows/gen_rpc_package_checker.yml/badge.svg)](https://github.com/vroncevic/gen_rpc/actions/workflows/gen_rpc_package.yml) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_rpc.svg)](https://github.com/vroncevic/gen_rpc/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_rpc.svg)](https://github.com/vroncevic/gen_rpc/graphs/contributors)

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

![debian linux os](https://raw.githubusercontent.com/vroncevic/gen_rpc/dev/docs/debtux.png)

[![gen_rpc python3 build](https://github.com/vroncevic/gen_rpc/actions/workflows/gen_rpc_python3_build.yml/badge.svg)](https://github.com/vroncevic/gen_rpc/actions/workflows/gen_rpc_python3_build.yml)

Currently there are four ways to install framework
* Install process based on using pip mechanism
* Install process based on build mechanism
* Install process based on setup.py mechanism
* Install process based on docker mechanism

##### Install using pip

Python is located at **[pypi.org](https://pypi.org/project/gen_rpc/)**.

You can install by using pip

```bash
#python3
pip3 install gen_rpc
```

##### Install using build

Navigate to **[release page](https://github.com/vroncevic/gen_rpc/releases)** download and extract release archive.

To install **gen-rpc** run

```bash
tar xvzf gen-rpc-x.y.z.tar.gz
cd gen-rpc-x.y.z
# python3
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py 
python3 -m pip install --upgrade setuptools
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
pip3 install -r requirements.txt
python3 -m build -s --no-isolation --wheel
pip3 install dist/gen-rpc-x.y.z-py3-none-any.whl
rm -f get-pip.py
```

##### Install using py setup

Navigate to release **[page](https://github.com/vroncevic/gen_rpc/releases/)** download and extract release archive.

To install **gen_rpc** type the following

```bash
tar xvzf gen_rpc-x.y.z.tar.gz
cd gen_rpc-x.y.z/
# python3
pip3 install -r requirements.txt
python3 setup.py install_lib
python3 setup.py install_data
python3 setup.py install_egg_info
```

##### Install using docker

You can use Dockerfile to create image/container.

### Dependencies

**gen_rpc** requires next modules and libraries

* [ats-utilities - Python App/Tool/Script Utilities](https://vroncevic.github.io/gen_rpc)

### Generation flow of RPC modules

Base flow of generation process

![RPC generation flow](https://raw.githubusercontent.com/vroncevic/gen_rpc/dev/docs/gen_rpc_flow.png)

### RPC System
![RPC system](https://raw.githubusercontent.com/vroncevic/gen_rpc/dev/docs/rpc_system.png)

```bash
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

Generator structure

```bash
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
       ├── py.typed
       └── run/
           └── gen_rpc_run.py

    6 directories, 14 files
```

### Code coverage

| Name | Stmts | Miss | Cover |
|------|-------|------|-------|
| `gen_rpc/__init__.py` | 71 | 12 | 83% |
| `gen_rpc/pro/__init__.py` | 59 | 2 | 97% |
| `gen_rpc/pro/read_template.py` | 53 | 2 | 96% |
| `gen_rpc/pro/write_template.py` | 60 | 5 | 92% |
| **Total** | 243 | 21 | 91% |

### Docs

[![Documentation Status](https://readthedocs.org/projects/gen_rpc/badge/?version=latest)](https://gen-rpc.readthedocs.io/en/latest/?badge=latest)

More documentation and info at
* [gen_rpc.readthedocs.io](https://gen-rpc.readthedocs.io/en/latest/)
* [rpc mechanism](overview.md)
* [www.python.org](https://www.python.org/)

### Contributing

[Contributing to gen_rpc](CONTRIBUTING.md)

### Copyright and Licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2019 - 2024 by [vroncevic.github.io/gen_rpc](https://vroncevic.github.io/gen_rpc)

**gen_rpc** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/gen_rpc/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2)
