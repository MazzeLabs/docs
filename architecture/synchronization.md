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

## Snapshot sync
A new full node can start from a peer's state snapshot instead of replaying
from genesis:

1. **Pick a candidate.** The node walks its header chain in
   `snapshot_epoch_count` strides and proposes the newest snapshot-aligned
   epoch that peers support.
2. **Fetch the manifest.** Each manifest lists the chunks and a Keccak hash per
   chunk. Manifest pages whose chunk boundaries do not increase are rejected.
3. **Fetch and check chunks.** Every chunk is checked against its hash when it
   arrives. A bad chunk is dropped and requested from another peer. A chunk
   restored twice is counted once.
4. **Restore.** The restored state is stored with its true state roots below
   the snapshot.

If no peer offers a usable candidate, the node canvasses every peer once more.
If that also fails, or the manifest attempts run out, it falls back to ordinary
sync instead of crashing. Block bodies are filled from the local database
without recomputing header PoW.

Counters: `snapshot_sync.last_ditch_canvasses_total`,
`snapshot_sync.last_ditch_recoveries_total`,
`snapshot_sync.fallback_total.*`, `snapshot_sync.invalid_transitions`.

## Key source files
- `crates/mazzecore/core/src/sync/synchronization_phases.rs`
- `crates/mazzecore/core/src/sync/synchronization_graph.rs`
- `crates/mazzecore/core/src/sync/message/mod.rs`
- `crates/mazzecore/core/src/sync/state/mod.rs`
