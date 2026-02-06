# Genesis and chain parameters

Genesis bootstraps chain state, internal contracts, and initial balances.

## Genesis block creation
`genesis_block` performs:
- State initialization and internal contract setup.
- Funding of configured genesis accounts (including dev/test keys when used).
- Genesis treasury account creation and shielded pool seeding.
- Emission of genesis transactions (create2 factory, optional shielded key).
- Construction of the genesis header with initial difficulty and gas limit.

## Explicit genesis issuance logic
Current native genesis target is 3,900,000,000 MAZZE.

In code, genesis accounting is two-step:
1. Credit explicit genesis accounts first.
2. Mint only the remaining amount needed to reach the configured genesis total.

This avoids double-counting between explicit allocations and the special
genesis-account mint path.

Shielded pool bootstrap at genesis is a treasury transfer, not extra issuance.
See `docs/tokenomics/shielded-pool-genesis-fund.md`.

## Genesis inputs
- `genesis_accounts` and `genesis_secrets` can override the account set.
- `execute_genesis` controls whether genesis is executed or loaded from db.

## Chain parameters
Configuration exposes key consensus parameters:
- `initial_difficulty`
- `era_epoch_count`
- `referee_bound`
- `adaptive_weight_beta`, `heavy_block_difficulty_ratio`
- `timer_chain_block_difficulty_ratio`, `timer_chain_beta`
- `transaction_epoch_bound`

Hardfork transitions are also configured by height/epoch.

## Key source files
- `crates/mazzecore/core/src/genesis_block.rs`
- `crates/client/src/configuration.rs`
- `crates/mazzecore/internal_common/src/chain_id.rs`
- `crates/mazzecore/parameters/src/lib.rs`
