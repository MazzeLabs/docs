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

# Shielded pool contract

The shielded pool is an internal contract (built-in) that holds shielded
balances and verifies proof-based spends.

## Address
- `SHIELDED_POOL_CONTRACT_ADDRESS` in
  `crates/mazzecore/parameters/src/internal_contract_addresses.rs`

## Public functions
- `shield(bytes32,bytes)`
  - Accepts a commitment and ciphertext with a non-zero value transfer.
  - Appends the commitment to the Poseidon Merkle tree.
  - Emits a `ShieldedNote(bytes32,bytes)` event.
- `applyShieldedBundle(...)`
  - Verifies a Groth16 proof against the anchor, nullifiers, commitments,
    outputs, values, and fee.
  - Marks nullifiers as spent.
  - Appends new commitments and emits `ShieldedNote` events.
  - Pays the fee and transparent outputs from the pool balance.
- `root()`
  - Returns the latest Merkle root.
- `isNullifierSpent(bytes32)`
  - Returns whether a nullifier has been spent.
- `setVerifyingKey(bytes)`
  - Sets the Groth16 verifying key once (admin only).
- `verifyingKeyHash()`
  - Returns the keccak hash of the verifying key.

## Limits and parameters
- Tree depth: 32 levels.
- Root history: 64 roots.
- Max nullifiers per bundle: 8.
- Max commitments per bundle: 8.
- Max transparent outputs per bundle: 8.
- Max ciphertext size: 512 bytes.
- Max proof size: 256 bytes.
- Max verifying key size: 8192 bytes.

## Storage layout (system storage)
The pool stores its state in system storage keyed by hashed prefixes:
- `shielded:vk_len`, `shielded:vk_word:*`, `shielded:vk_hash`
- `shielded:nullifier:*`
- `shielded:root_index`, `shielded:root:*`
- `shielded:leaf_index`, `shielded:frontier:*`

## Genesis behavior
If a verifying key is provided at genesis, a `setVerifyingKey` transaction is
executed and the shielded pool admin is cleared.

Genesis can also seed shielded pool balance using
`SHIELDED_POOL_GENESIS_FUND_MAZZE`. That seed is transferred from treasury
(not newly minted). See `../tokenomics/shielded-pool-genesis-fund.md`.
