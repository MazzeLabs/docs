---
layout:
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

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

## Shielded transactions and Dandelion++
Shielded transactions are relayed in their own message,
`ShieldedTransactions` (`0x25`), sent only while the shielded lane is active.
They are routed with Dandelion++:

- **Stem:** forwarded to one peer at a time, the node's current stem successor
  (redrawn every 10 minutes).
- **Fluff:** at each hop, with probability 0.1, switched to an ordinary
  broadcast.
- **Embargo:** a node that relays a stem transaction broadcasts it itself if it
  has not seen it broadcast within 30 to 60 seconds.

The node a transaction came from is then not the first to broadcast it. See
[The shielded lane](../privacy/shielded-lane.md#relay-dandelion).

## Handshake
The cryptographic handshake cannot be bypassed in release builds. The
`BYPASS_CRYPTOGRAPHY` switch exists only in test builds, and a release build
logs an error if anything tries to flip it.

## Key source files
- `crates/network/src/lib.rs`
- `crates/network/src/service.rs`
- `crates/network/src/discovery.rs`
- `crates/mazzecore/core/src/sync/message/status.rs`
- `crates/mazzecore/core/src/sync/dandelion.rs`
- `crates/mazzecore/core/src/sync/message/shielded_transactions.rs`
