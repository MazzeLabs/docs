# Networking

The `network` crate implements the P2P transport, discovery, and peer
management used by sync and block propagation.

## Core services
- `NetworkService` manages sessions and protocol handlers.
- Discovery maintains a node table and periodically refreshes peers.
- Handshake and session layers enforce protocol compatibility.

## Configuration highlights
`NetworkConfiguration` includes:
- Listen/public addresses and UDP port.
- Bootnodes and reserved nodes.
- Peer limits and handshake limits.
- NAT and discovery settings.
- Throttling and IP filter controls.

## Node typing and tagging
Peers advertise `node_type` tags (archive/full) to bias requests during sync,
and the sync layer can choose preferred node types for block retrieval.

## Key source files
- `crates/network/src/lib.rs`
- `crates/network/src/service.rs`
- `crates/network/src/discovery.rs`
- `crates/mazzecore/core/src/sync/message/status.rs`
