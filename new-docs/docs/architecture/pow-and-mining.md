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

## Key source files
- `crates/mazzecore/core/src/pow/mod.rs`
- `crates/mazzecore/core/src/pow/cache.rs`
- `crates/blockgen/src/lib.rs`
- `crates/blockgen/src/miner/stratum.rs`
