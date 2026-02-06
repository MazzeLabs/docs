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

# Mazze Node Architecture

This folder breaks the node into focused pages. Each topic is scoped to code in
this repo and points to the main source files.

## Reading order
1. [Overview](overview.md) - end-to-end pipeline and crate map.
2. [Block structure](block-structure.md) - header/body fields and roots.
3. [Transaction pool](transaction-pool.md) - intake, validation, packing.
4. [Block generation](block-generation.md) - assembling blocks before mining.
5. [PoW and mining](pow-and-mining.md) - Proof of Work, RandomX, Stratum.
6. [DAG and DETS](dag-and-dets.md) - parent/referee graph model.
7. [Consensus](consensus.md) - ordering, timer chain, checkpoints.
8. [Execution and state](execution-and-state.md) - epoch execution and state roots.
9. [Verification](verification.md) - block and tx validation rules.
10. [Storage and snapshots](storage-and-snapshots.md) - state DB and snapshots.
11. [Synchronization](synchronization.md) - sync phases and catch-up.
12. [Networking](networking.md) - P2P, discovery, peer management.
13. [RPC and APIs](rpc-and-apis.md) - JSON-RPC surfaces.
14. [Genesis and params](genesis-and-params.md) - genesis build and config.
15. [Rewards and fees](rewards-and-fees.md) - base reward, fees, penalties.
16. [Node types and light protocol](node-types-and-light-protocol.md) - archive/full/light behavior.
