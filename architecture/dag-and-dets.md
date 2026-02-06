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

# DAG and DETS

Mazze blocks form a DAG, not a single chain. Each block has a parent edge and
zero or more referee edges. The consensus layer treats this as a
DAG-Embedded Tree Structure (DETS).

## Graph primitives
The `dag` crate defines core traits:
- `Graph` - nodes with an index.
- `DAG` - predecessor edges and topological order.
- `DETS` - tree parent plus referee edges.
- `RichDAG` / `RichDETS` - forward edges for traversals.

`DETS` is the key abstraction used by sync and consensus.

## Parent and referee edges
- Parent edge: ensures a tree backbone and supports chain-like operations.
- Referee edges: link side blocks to expand the past set and increase
  throughput while preserving ordering.

## DAG tips and future sets
- Tips are terminal blocks with no children.
- `get_future` and `topological_sort` help build ordered subsets of the DAG,
  especially when computing outlier sets or epoch block ordering.

## Where DETS is implemented
- `SynchronizationGraphInner` implements DETS for all received blocks.
- `ConsensusGraphInner` implements DETS for validated, ready blocks.

## Key source files
- `crates/util/dag/src/lib.rs`
- `crates/mazzecore/core/src/sync/synchronization_graph.rs`
- `crates/mazzecore/core/src/consensus/consensus_inner/mod.rs`
