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

# Issuance

### <mark style="color:orange;">Supply Summary</mark>

* Native genesis issuance: **3,900,000,000 MAZZE**
* Mining emission target (unchanged schedule): **2,500,000,000 MAZZE**
* Theoretical native upper bound: **6,400,000,000 MAZZE**
* `6.4B` is a theoretical long-term upper bound, not present-day circulating supply.

### <mark style="color:orange;">Explicit Supply Logic</mark>

At epoch `t`, native issued supply follows:

`native_total_issued(t) = genesis_issued + mined_to_date(t) - burnt_to_date(t)`

Where:

* `genesis_issued = 3,900,000,000`
* `mined_to_date(t)` follows the halving schedule and is bounded by the mining target in configuration.
* `burnt_to_date(t)` includes MIP-1559 burns and other protocol burn paths.

### <mark style="color:orange;">Codebase Constants</mark>

Native supply and emission parameters are defined in `crates/mazzecore/parameters/src/lib.rs`:

* `GENESIS_TOKEN_COUNT_IN_MAZZE = 3,900,000,000`
* `MINING_SUPPLY_TARGET_IN_MAZZE = 2,500,000,000`
* `MAX_SUPPLY_TOKEN_COUNT_IN_MAZZE = 6,400,000,000`
* `INITIAL_BASE_MINING_REWARD_IN_UMAZZE = 4,000,000` (4 MAZZE)
* `HALVING_INTERVAL_IN_BLOCKS = 312,500,000`

### <mark style="color:orange;">Mining Reward Schedule</mark>

* Initial base mining reward: `4,000,000 uMAZZE` (4 MAZZE) per block.
* Halving interval: `312,500,000` blocks.
* Reward is halved by integer division each interval until it reaches zero.

### <mark style="color:orange;">Burn Interaction</mark>

Realized supply can stay below the theoretical curve because burn is active:

* MIP-1559 burn updates in execution (`burn_by_mip1559`).
* Net epoch issuance adjustment in reward settlement.
* Additional burn paths during execution.

### <mark style="color:orange;">Related Pages</mark>

* [Inflation](inflation.md)
* [Bridge Liquidity](bridge-liquidity.md)
* [Shielded Pool Genesis Fund](shielded-pool-genesis-fund.md)
