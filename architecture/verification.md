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
- Proof of Work validity, skipped only in catch-up mode. A block whose RandomX
  seed hash cannot be resolved is rejected; it is no longer accepted without a
  PoW check.
- Referee count bound and duplicate parent/referee hashes.
- Basic timestamp validity (when enabled).

## Block integrity
- Transactions root is re-computed via MPT and compared to the header.
- Block size is checked against `max_block_size_in_bytes`.

## Shielded section (stage A)
`verify_sync_graph_block_basic` checks a block's shielded section before the
block enters the sync graph:

1. The block is at a slot height, and the section is within the per-block count.
2. Every body pays exactly the constant fee.
3. Nullifiers are distinct across the section.
4. Every proof verifies against its body (`verify_body`): pool version, proof
   system, proof length cap, `proof_hash`, canonical decoding, then the STARK.

A proof that does not match its body's `proof_hash` is the peer's fault and the
block is requested again. Any other failure makes the block invalid. Blocks
re-read from the node's own database skip the proofs. A block that charges
shielded gas is invalid.

## Sync-graph bounds
Outside catch-up mode, the sync graph holds at most 200,000 blocks
(`SYNC_GRAPH_ARENA_HARD_CAP`). Blocks beyond the cap are rejected and counted.

## Transaction validation
- Signature and encoding checks.
- Intrinsic gas: a native transaction whose gas limit is below its intrinsic
  gas is dropped before execution (`NotEnoughGasLimit`).
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
- `crates/shielded_pq/src/verify.rs`
- `crates/primitives/src/block_header.rs`
- `crates/dbs/storage/src/impls/merkle_patricia_trie/trie_proof.rs`
