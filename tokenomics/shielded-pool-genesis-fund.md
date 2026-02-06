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

# Shielded Pool Genesis Fund

This page explains how `SHIELDED_POOL_GENESIS_FUND_MAZZE` is applied at genesis.

### <mark style="color:orange;">What It Is</mark>

* `SHIELDED_POOL_GENESIS_FUND_MAZZE` defines how many native MAZZE are moved to the shielded pool contract at genesis.
* Code location: `crates/mazzecore/core/src/genesis_block.rs`.

### <mark style="color:orange;">Funding Source (Important)</mark>

The shielded pool genesis fund is sourced from the genesis treasury balance. It is **not minted** on top of genesis supply.

Flow in code:

1. Treasury is funded from `GENESIS_TREASURY_BALANCE_MAZZY_STR`.
2. Seed amount is computed from `SHIELDED_POOL_GENESIS_FUND_MAZZE`.
3. If `treasury_balance >= seed`, code executes `transfer_balance(treasury -> shielded_pool, seed)`.
4. If treasury is missing or insufficient, seeding is skipped and a warning is logged.

### <mark style="color:orange;">Supply/Accounting Impact</mark>

* No extra issuance is created by this step.
* `total_issued` is not increased during shielded pool seeding.
* This is a balance reallocation inside existing genesis-issued funds.

### <mark style="color:orange;">Related Pages</mark>

* [Issuance](issuance.md)
* [Bridge Liquidity](bridge-liquidity.md)
