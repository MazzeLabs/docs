---
description: The node's pipeline from end to end, its runtime loops, and the crate map.
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Overview

Mazze Node is a set of Rust crates wired together by the main binary in `bins/mazze`.

<figure><picture><source srcset="../.gitbook/assets/brand/diagram-node-pipeline-dark.svg" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/brand/diagram-node-pipeline.svg" alt="Node pipeline"></picture><figcaption></figcaption></figure>

## Pipeline

1. **Intake.** Transactions arrive over RPC or P2P and enter the transaction pool. Account transactions go to per-sender nonce pools; shielded transactions go to the shielded lane.
2. **Packing.** The block generator asks the pool for a packable set and assembles a candidate block. At slot heights it also packs shielded bodies and their proofs.
3. **Proof of Work.** The nonce is found locally or by Stratum workers.
4. **Sync graph.** Headers and bodies are checked and connected into the DAG. Shielded proofs are verified here (stage A).
5. **Consensus.** The consensus graph keeps the DAG-Embedded Tree Structure (DETS), picks the pivot chain and emits ordered epochs.
6. **Execution.** The executor runs each epoch: native transactions on Mazze's interpreter, eSpace transactions on revm, then the shielded section (stage B) on slot epochs. It produces deferred state, receipt and log roots.
7. **Persistence.** The block data manager and storage manager write blocks, receipts, witnesses and state to MDBX and ParityDB.
8. **Queries.** RPC answers from the consensus graph, the block data manager and the state database.

## Runtime loops

| Loop | Job |
| --- | --- |
| Sync | Drives the catch-up phases and fetches missing headers and bodies |
| Consensus | Activates ready blocks, updates the ordering, emits epochs |
| Execution | Runs in a worker thread and commits epoch results |
| Mining | Assembles blocks, pushes PoW problems, submits solutions |
| RPC | Serves HTTP, WebSocket and TCP on one shared tokio runtime |

## Crate map

| Crate | Role |
| --- | --- |
| `bins/mazze` | Node entry point, CLI and wiring |
| `bins/mazze-miner` | Mining client |
| `bins/mazze-shielded-wallet` | Shielded-space wallet |
| `crates/mazzecore/core` | Consensus, sync, transaction pool, verification, PoW, Dandelion++ |
| `crates/mazzecore/executor` | Execution, internal contracts, the shielded engine |
| `crates/mazzecore/eth-vm` | eSpace execution on revm 40 |
| `crates/mazzecore/vm-interpreter` | Native-space interpreter |
| `crates/shielded_pq` | Shielded-space cryptography: field, notes, keys, tree, AIR, PS-1 |
| `crates/blockgen` | Block assembly and mining orchestration |
| `crates/network` | P2P transport, discovery, peer management |
| `crates/dbs/storage` | State DB (MDBX, ParityDB), snapshots, Merkle Patricia Trie |
| `crates/primitives` | Blocks, headers, transactions, receipts, shielded bodies |
| `crates/client` | Configuration and JSON-RPC handlers |
| `crates/util/rpc-error` | The JSON-RPC error type |
| `crates/stratum` | Stratum server on tokio |
| `crates/transactiongen` | Optional transaction generator for dev and test |

## Key source files

- `crates/mazzecore/core/src/consensus/mod.rs`
- `crates/mazzecore/core/src/sync/synchronization_graph.rs`
- `crates/mazzecore/core/src/consensus/consensus_inner/consensus_executor/mod.rs`
- `crates/mazzecore/core/src/transaction_pool/mod.rs`
- `crates/mazzecore/executor/src/shielded_engine.rs`
- `crates/blockgen/src/lib.rs`
- `crates/dbs/storage/src/lib.rs`
- `crates/client/src/rpc/impls/mazze/mazze_handler.rs`
