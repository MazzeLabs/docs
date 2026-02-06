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

# Verification

Verification rules ensure that incoming blocks and transactions are valid
before they enter consensus.

## Header validation
`verify_header_params` checks:
- Custom data length and custom prefix for fork markers.
- Presence of `base_price`.
- Proof of Work validity (unless in catch-up mode or seed unknown).
- Referee count bound and duplicate parent/referee hashes.
- Basic timestamp validity (when enabled).

## Block integrity
- Transactions root is re-computed via MPT and compared to the header.
- Block size is checked against `max_block_size_in_bytes`.

## Transaction validation
- Signature and encoding checks.
- Gas, storage, and epoch height bounds.
- Chain id and space-specific rules.

## Base fee and gas checks
`verify_sync_graph_ready_block` verifies that:
- Packed gas does not exceed per-space limits.
- Base price is correctly derived from parent and gas usage.

## Inclusion proofs
The verification module exposes helpers to compute and verify:
- Transaction inclusion proofs.
- Block receipt proofs.
- Epoch receipt proofs.

These are used by RPCs and light client workflows.

## Key source files
- `crates/mazzecore/core/src/verification.rs`
- `crates/primitives/src/block_header.rs`
- `crates/dbs/storage/src/impls/merkle_patricia_trie/trie_proof.rs`
