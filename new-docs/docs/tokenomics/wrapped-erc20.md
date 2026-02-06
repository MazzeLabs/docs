# Wrapped MAZZE (ERC20 on Ethereum)

## Token details
- Contract name: Mazze
- Symbol: MAZZE
- Chain: Ethereum
- Standard: ERC20
- Decimals: 18
- Contract address: `0x4A029F7bCf33AcB03547D8fA7be840347973e24e`

## Supply state
- Current wrapped MAZZE on Ethereum: 4,900,000,000 MAZZE.
- Legacy ITS reference in earlier materials: 5,000,000,000 MAZZE.
- The documentation baseline for current operations is the live 4.9B amount.

## Bridge bootstrap and mining coverage
- 1,000,000,000 MAZZE is planned to be locked for bridge bootstrap and initial
  mining-side coverage.
- This 1,000,000,000 MAZZE is sourced partially from Ecosystem Development and
  Team Growth allocations.
- This lock is intended to make both bridge users and miners covered during
  early bridge operation.

## Directional bridge liquidity rule
The bridge is not modeled as infinite one-way liquidity.

- If users bridge heavily in one direction, liquidity is consumed on the
  destination side.
- If destination-side liquidity becomes insufficient, that direction is
  blocked.
- The blocked direction reopens only after opposite-direction flow restores
  enough liquidity.

## Wrapped MAZZE utility
- Facilitates immediate liquidity.
- Supports DEX and CEX access before full native migration.
- Supports development funding and market continuity.
- Enables Ethereum-native holder onboarding before and during bridge rollout.
