---
description: The note commitment, the spend keys, nullifiers, the commitment tree and the recovery slot.
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

# Notes, keys and nullifiers

## Building blocks

| Primitive | Used for |
| --- | --- |
| **KoalaBear** field, `p = 2^31 − 2^24 + 1` | Every in-circuit value |
| **Poseidon2**, width 24, as a sponge | Commitments, keys, nullifiers, the Merkle tree. The chain ID is a sponge parameter. |
| **SHAKE256** | Deriving keys and randomness from the seed, the public matrix `A`, `proof_hash` |
| **Keccak-256** | STARK commitments and Fiat–Shamir |
| **ChaCha20-Poly1305** | Sealing the recovery slot |

A digest is 12 field elements, encoded as 48 bytes (4 bytes each, little-endian). The decoder rejects any element at or above the prime, so every digest has one encoding.

## Spend keys

A wallet derives everything from a 32-byte seed.

```
nsk   = SHAKE("mazze/nsk", seed)          the only spend secret
ak    = H_AK(nsk)
nk    = H_NK(nsk)                         nullifier key
d_j   = SHAKE("mazze/div", seed ‖ j)      diversifier j
owner = H_OWN(ak ‖ nk ‖ d_j)
```

`ak` and `nk` both come from `nsk`, and `nk` is committed into every note's owner. A shielded address is `mzs1` followed by the hex of `d ‖ owner`. Diversifiers give one wallet many unlinkable addresses.

## The note commitment

A note is `(d, owner, value, ψ, y)`. Its commitment is a Halevi–Micali construction over KoalaBear:

```
x  = owner(12) ‖ value limbs(4) ‖ ψ(12)     the message, 28 elements
y  ← 64 uniform field elements              the randomness
d  = Poseidon2_HM(y)
b  = x − A·y                                A: a public 28 × 64 matrix
cm = Poseidon2_LEAF(d ‖ b)                  the leaf in the tree
```

* **Hiding is statistical.** `A·y` is a universal hash of `y`. By the leftover hash lemma, `b` is within **2⁻³⁷²** of uniform, whatever `x` is. No hash assumption is involved.
* **Binding is computational.** Opening a commitment two ways needs a Poseidon2 collision.
* **The caveat.** The bound is exactly statistical when `y` is fresh OS randomness, as for payments to others. Self-notes derive `y` from the seed, so their hiding rests on SHAKE256 as a pseudorandom function.

Values are 64-bit, held as four 16-bit limbs. The circuit range-checks every limb, so one note holds less than 2⁶⁴ mazzy (about 18.4 MAZZE).

## Nullifiers

When a note is spent, its nullifier is published:

```
mk = H_MK(nk ‖ ψ)               a per-note key
nf = H_NF(mk ‖ pos_lo16 ‖ pos_hi16)
```

* `nk` is committed in the owner, `ψ` in the commitment, and `pos` by the Merkle path, so **each leaf has exactly one nullifier**.
* The per-note key `mk` makes every nullifier independent. Even an attacker who could invert the hash could not link two spends of the same user.
* The position is split into two 16-bit limbs because a 32-bit position would wrap modulo `p`.

The node keeps the set of spent nullifiers. A transaction that reuses one is refused by the pool and skipped by the engine.

## Commitment tree and anchors

* The tree is an incremental Poseidon2 Merkle tree of **depth 32**. The node keeps only its frontier.
* Each time a transaction is applied, the new root is recorded, with the height it was seen at. The empty tree's root is recorded when the pool is first used, so the first transactions have an anchor. A transaction proves membership against an **anchor**, one of the recorded roots.
* An anchor stays valid for **100,000 epochs** (`anchor_window_epochs`).
* The node serves no Merkle paths. Wallets rebuild the tree from `shielded_getSections`, so the node never learns which leaf a wallet cares about.

## Dummy inputs

Every transaction has two inputs. A transaction that needs one note fills the other slot with a zero-value dummy. The circuit enforces membership only for non-zero inputs, and the zero flag is computed from the value, never chosen by the prover.

## Recovery slot

Every body carries a recovery slot: a 32-byte tag, a 64-byte sealed slot and a 16-byte MAC.

* Notes the wallet keeps for itself (change, shield-ins, claims) are **self-notes**. Everything but the value derives from the seed, through a recovery key and a per-index counter.
* The value is sealed in the slot with ChaCha20-Poly1305, under a single-use key for that index.
* The tag is single-use and cannot be linked to the wallet without the seed.
* An unused slot is random bytes, so a slot gives nothing away.

To restore, the wallet derives the tags from the seed, finds them on chain, opens the slots and rebuilds the notes. It stops after 20 consecutive missing tags.

{% hint style="info" %}
**Received notes are recoverable only after a claim.** A note someone sent you is not derived from your seed. Run `claim` after every receipt to fold it into a self-note, which `restore` can rebuild.
{% endhint %}
