# Shielded pool genesis fund

This page explains how `SHIELDED_POOL_GENESIS_FUND_MAZZE` is applied at
genesis.

## What it is
- `SHIELDED_POOL_GENESIS_FUND_MAZZE` defines how many native MAZZE are moved to
  the shielded pool contract at genesis.
- Code location:
  `crates/mazzecore/core/src/genesis_block.rs`.

## Units
- `SHIELDED_POOL_GENESIS_FUND_MAZZE` is in MAZZE units.
- It is converted to base units (`mazzy`) by multiplying with
  `ONE_MAZZE_IN_MAZZY`.

## Funding source (important)
The shielded pool genesis fund is sourced from the genesis treasury balance.
It is not minted on top of genesis supply.

Flow in code:
1. Treasury is funded from `GENESIS_TREASURY_BALANCE_MAZZY_STR`.
2. Seed amount is computed from `SHIELDED_POOL_GENESIS_FUND_MAZZE`.
3. If treasury exists and `treasury_balance >= seed`, the code executes
   `transfer_balance(treasury -> shielded_pool, seed)`.
4. If treasury is missing or insufficient, seeding is skipped and a warning is
   logged.

## Supply/accounting impact
- No extra issuance is created by this step.
- `total_issued` is not increased during shielded pool seeding.
- This is a balance reallocation inside existing genesis-issued funds.

## Current-value check pattern
If your configured seed is larger than treasury balance, the transfer will not
happen at genesis. In that case, increase treasury funding or lower
`SHIELDED_POOL_GENESIS_FUND_MAZZE`.

## Related docs
- `docs/tokenomics/issuance.md`
- `docs/privacy/shielded-pool.md`
- `docs/architecture/genesis-and-params.md`
