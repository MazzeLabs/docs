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

# Keys and tooling

## Verifying key lifecycle
The shielded pool verifies Groth16 proofs using a verifying key stored on chain.

- `setVerifyingKey(bytes)` stores the verifying key in system storage and
  exposes its hash via `verifyingKeyHash()`.
- The key is cached as a prepared verifying key to speed up proof checks.

At genesis, the node can load a verifying key from disk and execute a
`setVerifyingKey` transaction. The loader looks for:
- `run/shielded_vk.hex`
- `shielded_vk.hex`

If a key is set at genesis, the shielded pool admin is cleared so the key can
no longer be changed.

## Genesis pool seeding
Genesis optionally seeds the shielded pool balance from the treasury using
`SHIELDED_POOL_GENESIS_FUND_MAZZE`.

## CLI utilities
The executor crate includes helper binaries for the shielded flow:
- `shielded_keygen` - generate proving/verifying keys.
- `shielded_vkhash` - compute a verifying key hash.
- `shielded_verify` - verify a proof payload against a verifying key.
- `shielded_note` - build/decrypt notes and derive Merkle paths.
- `shielded_bundle` - build shielded bundles and proofs.

## Operational docs
Step-by-step CLI and RPC usage should follow your local shielded-transactions
runbook.
