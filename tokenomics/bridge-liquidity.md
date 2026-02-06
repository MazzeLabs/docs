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

# Bridge Liquidity Model

This page describes the operational bridge-liquidity logic used alongside Mazze tokenomics.

### <mark style="color:orange;">Current Baseline</mark>

* Wrapped MAZZE on Ethereum: **4,900,000,000 MAZZE**
* Native genesis issuance: **3,900,000,000 MAZZE**
* Bridge bootstrap reserve: **1,000,000,000 MAZZE**
* The bridge reserve is sourced partially from **Ecosystem Development** and **Team Growth** allocations.

### <mark style="color:orange;">Why the 1B Reserve Exists</mark>

The reserve is intended to bootstrap bridge operations and provide initial coverage for mining-era flows. It is not intended as infinite one-way bridge liquidity.

### <mark style="color:orange;">Directional Liquidity Rule</mark>

Bridge capacity is directional:

* Direction A: **Ethereum -> Mazze native**
* Direction B: **Mazze native -> Ethereum**

A transfer in one direction consumes destination-side liquidity.

If destination-side liquidity for that direction is insufficient, that direction is blocked until opposite-direction flow restores enough funds.

Equivalent rule:

* Ethereum -> Native transfer of `x` requires `native_bridge_liquidity >= x`.
* Native -> Ethereum transfer of `x` requires `erc20_bridge_liquidity >= x`.
* If the inequality is false, that transfer direction is paused.

### <mark style="color:orange;">Relation to 6.4B Native Theoretical Maximum</mark>

* Native theoretical maximum comes from `3.9B genesis + 2.5B mining target`.
* This is a long-term issuance bound, not a statement that all assets are freely bridgeable at all times.
* Bridge throughput is constrained by directional liquidity, so supply may exist on one side while transfers are temporarily paused in one direction.
