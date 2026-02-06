# Overview

Mazze privacy is implemented as a shielded pool that accepts deposits and
shielded spends. The pool is an internal contract that verifies Groth16 proofs
and maintains a Poseidon Merkle tree of commitments.

## High-level flow
1. Shield (deposit): A public transfer calls `shield(bytes32,bytes)` with a
   commitment and ciphertext. The pool appends the commitment to its Merkle
   tree, stores a new root, and emits a log with the commitment and ciphertext.
2. Spend (shielded bundle): A shielded transaction calls
   `applyShieldedBundle(...)` with an anchor (root), nullifiers, new
   commitments/ciphertexts, optional transparent outputs/values, and a fee.
   The pool verifies the Groth16 proof, marks nullifiers as spent, updates the
   Merkle tree, and transfers any transparent outputs and fees from the pool.

## Cryptography in the implementation
- Groth16 over BLS12-381 is used for proof verification in the pool contract.
- Poseidon is used for commitment hashing and Merkle tree construction.
- The Merkle tree depth is 32, and the pool keeps a history of 64 roots for
  anchor selection.

## What is public on chain
- Commitments and ciphertexts are logged as `ShieldedNote` events.
- Nullifiers are stored to prevent double spends.
- Merkle roots are stored and exposed via `root()`.
- Transparent outputs and their values are public inputs in the proof.


