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

# Synchronization

Synchronization brings the local node in sync with the network and feeds ready
blocks into consensus.

## Phases
Archive and full nodes follow a fixed phase pipeline:
1. CatchUpRecoverBlockHeaderFromDB
2. CatchUpSyncBlockHeader
3. CatchUpCheckpoint
4. CatchUpFillBlockBodyPhase
5. CatchUpSyncBlock
6. Normal

Each phase drives specific network requests and graph updates.

## SynchronizationGraph
The sync graph stores all received headers and blocks and tracks their status:
- Header-only, graph-ready, block-ready.
- Parent and referee connectivity.
- Frontiers for not-ready blocks and old-era blocks.

Only blocks that are graph-ready and have full bodies are delivered to
consensus.

## State sync
Snapshot-based state sync uses:
- Snapshot manifest requests.
- Chunk requests/responses.
- Candidate selection and restoration helpers.

## Key source files
- `crates/mazzecore/core/src/sync/synchronization_phases.rs`
- `crates/mazzecore/core/src/sync/synchronization_graph.rs`
- `crates/mazzecore/core/src/sync/message/mod.rs`
- `crates/mazzecore/core/src/sync/state/mod.rs`
