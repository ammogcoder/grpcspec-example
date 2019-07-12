# grpcspec-example

This repo contains examples of writing contracts for gRPC service and git-hook to auto generate codes.

## Prerequisites
- Git
- Docker

## Writing protobuf spec
Write the ```.proto``` files in the /proto directory.

## Including the code in to your project
To use the generated stub and client code:
- go
```
go get -u github.com/redcranetech/grpcspec-example

```
- python
```
pip install -e git+https://github.com/redcranetech/grpcspec-example.git#egg=pygrpcspec
```

## Initialize project (setup git hook)
```
make init
```
## Generate code (go, python)
```
make generate
```

## Examples

Go: [go to this repo](https://github.com/redcranetech/grpc-go-example)

Python: [go to this repo](https://github.com/redcranetech/grpc-python-example)