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

# Storage and snapshots

State persistence is provided by the `mazze-storage` crate. It combines a
Merkle Patricia Trie (MPT) with snapshotting and delta layers to balance
performance and history retention.

## Storage layers
- Delta MPTs: append-only changes between snapshots.
- Snapshot MPTs: compact state snapshots at selected epochs.
- State DB backend: MDBX by default, configurable via `MdbxConfig`.

## StorageManager and state access
`StorageManager` and `StateManager` provide:
- Read/write access to the current state.
- Snapshot creation and pruning.
- Proof generation and state sync support.

## Snapshot policy
`StorageConfiguration` controls:
- `snapshot_epoch_count` and `era_epoch_count`.
- Extra snapshots for sync (`ProvideExtraSnapshotSyncConfig`).
- Cache sizes and open snapshot limits.
- Directory layout under `storage_db/`.

## Interaction with consensus
`BlockDataManager` keeps a `StateAvailabilityBoundary` describing which epoch
states can be read. This allows full nodes to prune old state while still
serving recent queries.

## Key source files
- `crates/dbs/storage/src/lib.rs`
- `crates/dbs/storage/src/state_manager.rs`
- `crates/dbs/storage/src/impls/storage_manager/snapshot_manager.rs`
- `crates/dbs/storage/src/impls/merkle_patricia_trie/mod.rs`
- `crates/mazzecore/core/src/block_data_manager/mod.rs`
