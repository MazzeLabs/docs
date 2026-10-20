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

# PoW and mining

Mazze uses a Proof of Work scheme backed by RandomX hashing. Mining produces a
nonce that satisfies a difficulty boundary.

## Proof of Work primitives
- `ProofOfWorkProblem` bundles the block hash, difficulty, boundary, and seed.
- `ProofOfWorkSolution` carries the nonce.
- `PowComputer` computes the PoW hash with RandomX using a cached VM.

The boundary is derived from difficulty; a block is valid when
`pow_hash <= boundary`.

## RandomX cache and seed
`PowComputer` uses `RandomXCacheBuilder` to hold RandomX VMs and to swap context
when the seed hash changes. This makes per-block hashing fast while still
rotating the seed across epochs.

## Difficulty adjustment
`target_difficulty` computes the next target from recent blocks, the configured
block generation period, and the adjustment epoch period in
`ProofOfWorkConfig`.

## Mining modes
- `CPU` - local worker threads iterate nonces.
- `Stratum` - a job dispatcher hands work to external miners and validates
  submitted nonces.
- `Disable` - mining is turned off (used for read-only nodes or some dev modes).

The Stratum server runs on tokio 1. It keeps the wire protocol: newline-delimited
JSON-RPC 1.0 and 2.0 (responses mirror the request version), the same
subscribe and submit semantics, and `mining.notify` pushes.

A node normally refuses to mine with fewer than two peers. Dev mode is exempt,
since a dev node runs alone by design.

## Verification metrics
Every case where PoW verification is skipped is counted:
`pow.verification_verified`, `pow.verification_skipped_catch_up`,
`pow.verification_skipped_zero_seed_hash`,
`pow.verification_skipped_consortium`, `pow.verification_bench_mode_failure`
and `pow.catch_up_transitions_total`. A block whose seed hash cannot be
resolved is rejected.

## Key source files
- `crates/mazzecore/core/src/pow/mod.rs`
- `crates/mazzecore/core/src/pow/cache.rs`
- `crates/blockgen/src/lib.rs`
- `crates/blockgen/src/miner/stratum.rs`
- `crates/stratum/src/lib.rs`
