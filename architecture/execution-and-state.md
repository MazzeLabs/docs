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

# Execution and state

Mazze executes transactions in epochs. Execution is deferred by a fixed number
of epochs to limit reorg churn and to align with the DAG ordering.

## ConsensusExecutor
`ConsensusExecutor` owns a worker thread that processes `EpochExecutionTask`
items. Each task includes:
- The epoch hash and ordered block list.
- The start block number for VM `Env`.
- Optional reward execution info.
- A flag indicating whether the epoch is on the local main chain.

## Execution pipeline
1. Prefetch accounts and storage for the epoch.
2. Initialize epoch context and set base/burnt gas prices.
3. For each block:
   - Build the VM `Env` (chain id, block number, gas limit, base price).
   - Execute each transaction with `ExecutiveContext::transact`.
   - Record receipts, logs, and traces.
4. Produce `EpochExecutionCommitment` containing:
   - `StateRootWithAuxInfo` (snapshot and intermediate epoch ids).
   - Receipts root and logs bloom root.

If the epoch is on the local main chain, transactions that were packed but not
executed are recycled back into the txpool.

## Two VMs
`vm_factory.rs` routes each transaction by space:

| Space | VM |
| --- | --- |
| Native | Mazze's interpreter (`crates/mazzecore/vm-interpreter`) |
| eSpace | revm 40.0.0 with the Prague spec (`crates/mazzecore/eth-vm`) |

Mazze's own rules (the cross-space bridge, sponsorship, storage collateral,
`evm_gas_ratio`, restricted `BLOCKHASH`) are applied outside revm, which is
unmodified. The cross-space internal contract is dispatched before the VM
factory, so neither VM sees cross-space calls.

## Shielded engine (stage B)
On the pivot block of each slot epoch, after the account transactions, the
shielded engine applies the shielded section. It checks every rule before it
writes anything: deposit credit for a shield-in, anchor inside the window,
unspent nullifiers, enough backing, room in the tree. Then it marks nullifiers
spent, appends the commitments, records the new root, pays any shield-out and
burns the fee. A transaction that fails a rule is skipped with no state change.
Proofs are not needed here; they were verified in stage A. See
[The shielded lane](../privacy/shielded-lane.md#stage-b-execution).

## Deferred roots and blame
The execution output is stored in the block data manager and reflected into
later headers as deferred roots. The `blame` field allows light clients to
decide which deferred roots are trustworthy.

## State availability boundary
`StateAvailabilityBoundary` tracks the height range where state is available.
Archive nodes keep full history; full nodes may limit availability based on
snapshots and checkpoints.

## Key source files
- `crates/mazzecore/core/src/consensus/consensus_inner/consensus_executor/mod.rs`
- `crates/mazzecore/core/src/consensus/consensus_inner/consensus_executor/epoch_execution.rs`
- `crates/mazzecore/executor/src/machine/vm_factory.rs`
- `crates/mazzecore/eth-vm/src/lib.rs`
- `crates/mazzecore/executor/src/shielded_engine.rs`
- `crates/mazzecore/internal_common/src/state_root_with_aux_info.rs`
- `crates/mazzecore/internal_common/src/state_availability_boundary.rs`
