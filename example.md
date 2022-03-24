# RPC Application Development

Consider an example:
A client/server lookup in a personal database on a remote machine.
Assuming that we cannot access the database from the local machine (via NFS).
We use UNIX to run a remote shell and execute the command this way.
There are some problems with this method:

```
  the command may be slow to execute.
  You require an login account on the remote machine.
```

The RPC alternative is to

```
  establish an server on the remote machine that can respond to queries.
  Retrieve information by calling a query which will be quicker than previous approach.
```

To develop an RPC application the following steps are needed:

```
  Specify the protocol for client server communication.
  Develop the client program.
  Develop the server program.
```

The programs will be compiled seperately. The communication protocol is
achieved by generated stubs and these stubs and rpc (and other libraries)
will need to be linked in.

### Defining the Protocol

The easiest way to define and generate the protocol is to use a protocol
complier such as rpcgen. For the protocol you must identify the name of the
service procedures, and data types of parameters and return arguments.

The protocol compiler reads a definition and automatically generates client
and server stubs.

rpcgen uses its own language (RPC language or RPCL) which looks very similar
to preprocessor directives.

rpcgen exists as a standalone executable compiler that reads special files
denoted by a .x prefix.

So to compile a RPCL file you simply do:

```
rpcgen rpcprog.x
```

This will generate possibly four files:

```
rpcprog_clnt.c -- the client stub
rpcprog_svc.c -- the server stub
rpcprog_xdr.c -- If necessary XDR (external data representation) filters
rpcprog.h -- the header file needed for any XDR filters.
```

The external data representation (XDR) is an data abstraction needed for
machine independent communication. The client and server need not be machines
of the same type.

### Defining Client and Server Application Code

We must now write the the client and application code. They must communicate
via procedures and data types specified in the Protocol.

The service side will have to register the procedures that may be called by
the client and receive and return any data required for processing.

The client application call the remote procedure pass any required data and
will receive the retruned data.

There are several levels of application interfaces that may be used to develop
RPC applications. We will briefly disuss these below before exapnading the
most common of these in later chapters.

### Compliling and running the application

Let us consider the full compilation model required to run a RPC application.
Makefiles are useful for easing the burden of compiling RPC applications but
it is necessary to understand the complete model before one can assemble a
convenient makefile.Assume the the client program is called rpcprog.c, the
service program is rpcsvc.c and that the protocol has been defined in
rpcprog.x and that rpcgen has been used to produce the stub and filter files:
rpcprog_clnt.c, rpcprog_svc.c, rpcprog_xdr.c, rpcprog.h.

The client and server program must include ( #include "rpcprog.h").

You must then:

- compile the client code:

```
cc -c rpcprog.c
```

- compile the client stub:

```
cc -c rpcprog_clnt.c

```

- compile the XDR filter:

```
cc -c rpcprog_xdr.c
```

- build the client executable:

```
cc -o rpcprog rpcprog.o rpcprog_clnt.o rpcprog_xdr.c
```

- compile the service procedures:

```
cc -c rpcsvc.c
```

- compile the server stub:

````
cc -c rpcprog_svc.c
```s

- build the server executable:

````

cc -o rpcsvc rpcsvc.o rpcprog_svc.o rpcprog_xdr.c

```

Now simply run the programs rpcprog and rpcsvc on the client and server
respectively. The server procedures must be registered before the client can
call them.
```
