# SNI gRPC Code Generation

Snirk uses the gRPC interface provided by [SNI][sni]. SNI includes [proto files][proto files] which describe the
interfaces in [protobuf][protobuf] (currently protobuf v3).

These files are used to generate the SNI python library code in `snirk.sni`.

## gRPC code generation

The gRPC and protobuf interfaces to SNI in the `snirk/sni/` directory were initially created using the `protoc` tool
with [`grpc-tools` python package][grpc-tools] from a checkout of the SNI repo (`alttpo/sni`).

However, the generated files did not pass `flake8`/`mypy` analysis, and were modified to pass, and fix imports to
match the package structure.

Additionally, the git commit of `alttpo/sni` was found (via `git rev-parse HEAD`) and committed as
`snirk/sni/version.txt`.

A `tools/generate-sni-code.sh` script is included to checkout the `alttpo/sni` repo in a temporary directory at this
commit and generate the code in `snirk/sni/`. In the event of updated proto files, this can be re-run to generate
new gRPC code.

[grpc-tools]: https://pypi.org/project/grpc-tools
[protobuf]: https://github.com/protocolbuffers/protobuf
[proto files]: https://github.com/alttpo/sni/tree/main/protos/sni
[sni]: https://github.com/alttpo/sni

