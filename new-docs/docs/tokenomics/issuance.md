# Native MAZZE issuance (Mazze chain)

## Supply summary
- Native genesis issuance: 3,900,000,000 MAZZE.
- Mining emission target (unchanged schedule): 2,500,000,000 MAZZE.
- Theoretical native upper bound: 6,400,000,000 MAZZE.
- This `6.4B` is a theoretical long-term upper bound, not present-day
  circulating supply.

## Explicit supply logic
At epoch `t`, native issued supply follows:

`native_total_issued(t) = genesis_issued + mined_to_date(t) - burnt_to_date(t)`

Where:
- `genesis_issued = 3,900,000,000`
- `mined_to_date(t)` follows the halving schedule and is bounded by the mining
  target in configuration.
- `burnt_to_date(t)` includes MIP-1559 burns and other protocol burn paths.

The theoretical upper bound is:

`genesis_issued + mining_target = 3.9B + 2.5B = 6.4B`

This bound is only reached if the full mining target is emitted and cumulative
burn impact is zero.

## Codebase constants
Native supply and emission parameters are defined in
`crates/mazzecore/parameters/src/lib.rs`:

- `GENESIS_TOKEN_COUNT_IN_MAZZE = 3,900,000,000`
- `MINING_SUPPLY_TARGET_IN_MAZZE = 2,500,000,000`
- `MAX_SUPPLY_TOKEN_COUNT_IN_MAZZE = 6,400,000,000`
- `INITIAL_BASE_MINING_REWARD_IN_UMAZZE = 4,000,000` (4 MAZZE)
- `HALVING_INTERVAL_IN_BLOCKS = 312,500,000`

## Genesis accounting behavior in code
Genesis issuance is applied in
`crates/mazzecore/core/src/genesis_block.rs` using two steps:

1. Credit explicit genesis accounts first (for example treasury-related
   balances).
2. Mint only the remainder needed to reach
   `GENESIS_TOKEN_COUNT_IN_MAZZE` (3.9B).

This prevents accidental double-counting during genesis initialization.

## Mining reward schedule
- Initial base mining reward: 4,000,000 uMAZZE (4 MAZZE) per block.
- Halving interval: 312,500,000 blocks.
- Reward is halved by integer division each interval until it reaches zero.

The schedule is derived by `CommonParams::get_block_rewards_config` in
`crates/mazzecore/executor/src/spec.rs`.

Because rewards are halved by integer division, the tail is truncated and total
mined supply is slightly below the idealized 2.5B target.

### Schedule table (uMAZZE)
| Height | Reward (uMAZZE) | Reward (MAZZE) | Blocks at this reward |
| --- | --- | --- | --- |
| 0 | 4,000,000 | 4 | 312,500,000 |
| 312,500,000 | 2,000,000 | 2 | 312,500,000 |
| 625,000,000 | 1,000,000 | 1 | 312,500,000 |
| 937,500,000 | 500,000 | 0.5 | 312,500,000 |
| 1,250,000,000 | 250,000 | 0.25 | 312,500,000 |
| 1,562,500,000 | 125,000 | 0.125 | 312,500,000 |
| 1,875,000,000 | 62,500 | 0.0625 | 312,500,000 |
| 2,187,500,000 | 31,250 | 0.03125 | 312,500,000 |
| 2,500,000,000 | 15,625 | 0.015625 | 312,500,000 |
| 2,812,500,000 | 7,812 | 0.007812 | 312,500,000 |
| 3,125,000,000 | 3,906 | 0.003906 | 312,500,000 |
| 3,437,500,000 | 1,953 | 0.001953 | 312,500,000 |
| 3,750,000,000 | 976 | 0.000976 | 312,500,000 |
| 4,062,500,000 | 488 | 0.000488 | 312,500,000 |
| 4,375,000,000 | 244 | 0.000244 | 312,500,000 |
| 4,687,500,000 | 122 | 0.000122 | 312,500,000 |
| 5,000,000,000 | 61 | 0.000061 | 312,500,000 |
| 5,312,500,000 | 30 | 0.00003 | 312,500,000 |
| 5,625,000,000 | 15 | 0.000015 | 312,500,000 |
| 5,937,500,000 | 7 | 0.000007 | 312,500,000 |
| 6,250,000,000 | 3 | 0.000003 | 312,500,000 |
| 6,562,500,000 | 1 | 0.000001 | 312,500,000 |
| 6,875,000,000 | 0 | 0 | from this height onward |

## Burn interaction and realized supply
Realized supply can stay below the theoretical curve because burn is active.
Important paths include:

- MIP-1559 burn updates in execution (`burn_by_mip1559`).
- Net epoch issuance adjustment in reward settlement.
- Contract/self-destruct and collateral-related burn paths.

So, even with a 6.4B theoretical ceiling, actual issued and circulating supply
can be lower depending on chain activity.

## Bridge relation
The bridge reserve and directional liquidity policy are described in
`docs/tokenomics/bridge-liquidity.md`.

Shielded pool bootstrap fund behavior is documented in
`docs/tokenomics/shielded-pool-genesis-fund.md`.
