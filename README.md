# RPC skeleton generator.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

### INSTALLATION

To install this set of modules type the following:

```
cp -R ~/gen_rpc/bin/   /root/scripts/gen_rpc/ver.1.0/
cp -R ~/gen_rpc/conf/  /root/scripts/gen_rpc/ver.1.0/
cp -R ~/gen_rpc/log/   /root/scripts/gen_rpc/ver.1.0/
```

### DEPENDENCIES

This module requires these other modules and libraries:

* ats_utilities https://vroncevic.github.io/ats_utilities

### RPC System
![alt tag](https://raw.githubusercontent.com/vroncevic/gen_rpc/dev/python-tool-docs/rpc_system.png)

```
1. Client encodes data through XDR Filter
2. Client passes XDR encoded data across network to remote host
3. Server decodes data through XDR Filter
4. Server encodes functional call result through XDR Filter
5. Server pass XDR encoded data across network back to Client
6. Client decodes RPC result through XDR Filter and continues processing
```

### RPC Mapper
![alt tag](https://raw.githubusercontent.com/vroncevic/gen_rpc/dev/python-tool-docs/rpc_portmap.png)

### COPYRIGHT AND LICENCE

Copyright (C) 2019 by https://vroncevic.github.io/gen_rpc/

This tool is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.7/3.4 or,
at your option, any later version of Python 3 you may have available.

:sparkles:

