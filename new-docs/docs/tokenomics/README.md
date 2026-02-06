# Tokenomics

This folder documents wrapped MAZZE on Ethereum, bridge liquidity policy, and
native MAZZE issuance on Mazze.

## Current model (as of February 6, 2026)
- Wrapped MAZZE currently on Ethereum: 4,900,000,000 MAZZE.
- Native genesis issuance: 3,900,000,000 MAZZE.
- Bridge bootstrap reserve: 1,000,000,000 MAZZE.
- The 1,000,000,000 bridge reserve is sourced partially from Ecosystem
  Development and Team Growth allocations.
- Native mining emission logic is unchanged (same halving schedule and mining
  target of 2,500,000,000 MAZZE).
- Theoretical native upper bound in the far future: 6,400,000,000 MAZZE.
  This upper bound is theoretical because realized supply is reduced by burn.

## Important bridge constraint
Bridge liquidity is directional. If one bridge direction runs out of funds,
that direction is paused until enough liquidity returns from the opposite flow.

## Pages
- [Wrapped ERC20](wrapped-erc20.md)
- [Allocations](allocations.md)
- [Bridge liquidity](bridge-liquidity.md)
- [Shielded pool genesis fund](shielded-pool-genesis-fund.md)
- [Issuance](issuance.md)
