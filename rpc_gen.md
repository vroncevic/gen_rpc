# RPC protocol compiler

rpcgen is a tool that generates C code to implement an RPC protocol. The input
to rpcgen is ONC RPC (Remote Procedure Call) Language, which is similar to C.

rpcgen is normally used as in the first synopsis where it takes an input
file and generates four output files. If the infile is named proto.x,
rpcgen will generate a header file in proto.h, XDR routines in proto_xdr.c,
server-side stubs in proto_svc.c, and client-side stubs in proto_clnt.c.

The second synopsis provides special features which allow for the creation
of more sophisticated RPC servers. These features include support for RPC
dispatch tables, and user provided #defines. The entries in the ONC RPC
dispatch table contain:
```
  pointers to the service routine corresponding to that procedure,
  a pointer to the input and output arguments,
  the size of these routines
```

A server can use the dispatch table to check authorization and then to
execute the service routine; a client library may use it to deal with the
details of storage management and XDR data conversion.

The other synopses are used when one wants to generate a particular output
file.

The C-preprocessor, cpp, is run on all input files before they are actually
interpreted by rpcgen, so all the cpp directives are legal within an rpcgen
input file. For each type of output file, rpcgen defines a special cpp symbol
for use by the rpcgen programmer:
```
  RPC_HDR   Defined when compiling into header files,
  RPC_XDR   Defined when compiling into XDR routines,
  RPC_SVC   Defined when compiling into server-side stubs,
  RPC_CLNT  Defined when compiling into client-side stubs,
  RPC_TBL   Defined when compiling into RPC dispatch tables
```

In addition, rpcgen does a little preprocessing of its own. Any line beginning
with `%' is passed directly into the output file, uninterpreted by rpcgen.

You can customize some of your XDR routines by leaving those data types
undefined. For every data type that is undefined, rpcgen will assume that
there exists a routine with the name xdr_ prepended to the name of the
undefined type.

