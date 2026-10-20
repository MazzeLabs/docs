---
description: The 2-in × 2-out spend statement and PS-1, the STARK that proves it.
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Proof system PS-1

## The spend statement

One circuit covers every shielded transaction: two inputs, two outputs. Its circuit ID is `mazze/shielded/spend-2x2/v1`.

For each **input**, the prover shows that it knows `nsk` and a note opening such that:

1. `ak` and `nk` derive from the same `nsk`, and the owner is `H_OWN(ak ‖ nk ‖ d)`;
2. the commitment opens to that owner, value and `ψ`;
3. the leaf sits at position `pos` under the public anchor (skipped for a zero-value dummy);
4. the public nullifier is `H_NF(H_MK(nk ‖ ψ) ‖ pos)`.

For each **output**, the public commitment opens to the hidden note.

Across the transaction:

* **Ranges.** Every 16-bit value limb, and the public `v_in`, `v_out` and fee, is range-checked bit by bit.
* **Balance.** `inputs + v_public_in = outputs + v_public_out + fee`, checked limb by limb with carries. Every term stays far below `p/2`, so the field equation implies the integer equation. Values cannot wrap around.
* **Sighash.** The body's sighash is a public input. It binds the proof to every field of the body.

The trace is 118 columns × 4,096 rows, about 123 Poseidon2 permutations, laid out one round per row.

## PS-1 parameters

| Parameter | Value |
| --- | --- |
| Library | Plonky3 `=0.8.0`, pinned because the verifier is consensus code |
| Base field | KoalaBear |
| Challenge field | degree-8 extension of KoalaBear (≈248 bits) |
| Commitments and Fiat–Shamir | Keccak-256 |
| Low-degree test | FRI, blowup 2⁶, arity up to 8 |
| Queries | 38, with 16 bits of grinding |
| Zero-knowledge | Hiding FRI with salted Merkle leaves and 8 random codewords |
| Soundness | **128 bits, proven** (not conjectured) |
| Proof size | 184.7–188.7 KB measured; **cap 192 KiB** |

Every parameter is a constant. The query count was chosen once with Plonky3's security estimator, and a test checks it again. The estimator never runs at run time, so updating it cannot change consensus.

The prover takes its randomness (Merkle salts and random codewords) only from the caller's CSPRNG and consumes it once. Reused or predictable randomness would break zero-knowledge. A proof that comes out longer than the cap is proven again with new randomness.

## Domain separation

The Fiat–Shamir transcript starts from:

```
"mazze/shielded/fiat-shamir/v1" ‖ proof_system_id ‖ chain_id ‖ len(air_id) ‖ air_id
```

A proof is therefore valid for one chain, one proof system and one circuit. The circuit ID is length-prefixed, so no ID is a prefix of another.

## Proof hash and wire format

* The proof is serialised in Mazze's own fixed-width canonical format. The decoder rejects trailing bytes and oversized lengths, so a proof has one encoding.
* The body commits to the proof with `proof_hash = SHAKE256-512("mazze/shielded/proof-hash/v1" ‖ proof)`, 512 bits in line with the design rule of digests of at least 372 bits.
* The transaction ID is the Keccak hash of the body. It covers `proof_hash`, so it commits to the proof too.

## Upgrading the proof system

Each body names its proof system (`proof_system_id`) and pool version. Notes do not depend on the proof system: notes created under PS-1 can be spent under a later PS-2, and PS-1 transactions can be refused once PS-1 is retired. Relabelling a proof's system is rejected.

## How it was chosen

Prototypes measured proof size and verification time before the circuit was fixed:

* **Plonky3** was chosen over **Stwo**.
* A KoalaBear⁴ challenge field (124 bits) cannot reach 128 bits of soundness; it plateaus at 105–108 bits. The degree-8 extension is used instead.
* Trace width is the main cost driver. Merkle multiproofs take most of a proof's bytes.
* In the prototypes, verification took about 4–6 ms per proof on a 16-core desktop.
