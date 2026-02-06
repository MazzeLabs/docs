# Bridge liquidity model

This page describes the operational bridge-liquidity logic used alongside
Mazze tokenomics.

## Current baseline
- Wrapped MAZZE on Ethereum: 4,900,000,000 MAZZE.
- Native genesis issuance: 3,900,000,000 MAZZE.
- Bridge bootstrap reserve: 1,000,000,000 MAZZE.
- The bridge reserve is sourced partially from Ecosystem Development and Team
  Growth allocations.

## Why the 1B reserve exists
The reserve is intended to bootstrap bridge operations and provide initial
coverage for mining-era flows.

It is not intended as infinite one-way bridge liquidity.

## Directional liquidity rule (explicit)
Bridge capacity is directional:

- Direction A: Ethereum -> Mazze native
- Direction B: Mazze native -> Ethereum

A transfer in one direction consumes destination-side liquidity.

If destination-side liquidity for that direction is insufficient, that
direction is blocked until opposite-direction flow restores enough funds.

Equivalent rule:
- Ethereum -> Native transfer of `x` requires `native_bridge_liquidity >= x`.
- Native -> Ethereum transfer of `x` requires `erc20_bridge_liquidity >= x`.
- If the inequality is false, that transfer direction is paused.

Practical consequence:
- If flows remain strongly one-way, the bridge can pause in that direction.
- Rebalancing from the opposite direction is required to reopen it.
- Funds are therefore not assumed to move entirely in only one direction.

## Relation to the 6.4B theoretical native maximum
- Native theoretical maximum comes from `3.9B genesis + 2.5B mining target`.
- This is a long-term issuance bound, not a statement that all assets are
  freely bridgeable at all times.
- Bridge throughput is constrained by directional liquidity, so supply may
  exist on one side while transfers are temporarily paused in one direction.

## Scope note
Mazze core node code in this repository defines native issuance and burn logic.
Bridge contracts and bridge operation policy are external components and
operational rules.
