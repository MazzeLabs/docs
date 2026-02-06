# Block generation

Block generation is responsible for assembling a candidate block header/body,
using the current consensus best view and a packable transaction set.

## Core flow
1. `BlockGenerator` queries the txpool for best info and packed transactions.
2. It asks the consensus graph for the latest deferred state/blame info.
3. It chooses a parent and a referee set (bounded terminal hashes).
4. It fills a new header via `BlockHeaderBuilder`.
5. It hands the candidate to the mining loop or dev-mode auto generator.

## Parent and referees
- The parent is the best block hash from consensus.
- Referees are selected from terminal DAG tips and filtered to exclude the
  parent.
- `choose_correct_parent` may adjust the parent/referees to satisfy consensus
  rules.

## Header assembly details
- `transactions_root` is computed from the packed transactions.
- `deferred_state_root`, `deferred_receipts_root`, `deferred_logs_bloom_hash`,
  and `blame` are pulled from consensus.
- `gas_limit` is derived from target gas limit and elasticity multiplier.
- `base_price` is computed by the txpool for EIP-1559 style pricing.
- `custom` data is set using `Machine::params().custom_prefix()` for fork flags.

## Mining integration
- A `ProofOfWorkProblem` is generated from the header's problem hash.
- Depending on `MiningType`, the problem is sent to CPU workers or Stratum.
- On a solved nonce, `on_mined_block` hands the block to the sync service.

## Key source files
- `crates/blockgen/src/lib.rs`
- `crates/mazzecore/core/src/consensus/mod.rs`
- `crates/mazzecore/core/src/transaction_pool/mod.rs`
