---
description: The Groth16 shielded pool, an internal contract in the native space. Superseded by the shielded space.
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

# Legacy pool (Groth16)

{% hint style="warning" %}
**Superseded.** This pool is replaced by the [shielded space](README.md). It remains in the code base and in these docs for reference and for existing test setups.
{% endhint %}

The legacy pool is an internal contract in the native space. It verifies Groth16 proofs over BLS12-381 and keeps a Poseidon Merkle tree of commitments, depth 32, with the last 64 roots usable as anchors.

## Why it was replaced

| | Legacy pool | Shielded space |
| --- | --- | --- |
| Proofs | Groth16, BLS12-381 | STARK (PS-1), Plonky3 over KoalaBear |
| Trusted setup | **Yes**, a single-party setup | None |
| Post-quantum | No: pairings break under a quantum attack | Yes: hash-based |
| Commitments | Computationally hiding | Statistically hiding |
| Where it runs | Internal contract, native transactions | Its own space and block section |
| Transaction shape | Up to 8 nullifiers, 8 commitments, 8 outputs | Always 2 in, 2 out, constant fee |
| Recovery | Decrypt logged ciphertexts | Seed-derived self-notes and recovery slots |

The security audit rated the single trusted setup **Critical** (finding P-1): anyone holding the setup trapdoor could mint inside the pool without detection. The shielded space removes the trusted setup instead of patching it.

## Pages

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Pool contract</strong></td><td>Functions, limits and storage layout.</td><td><a href="shielded-pool.md">shielded-pool.md</a></td></tr><tr><td><strong>Pool transactions</strong></td><td>How unsigned shielded native transactions are validated and packed.</td><td><a href="transactions.md">transactions.md</a></td></tr><tr><td><strong>Keys and tooling</strong></td><td>The verifying key and the helper binaries.</td><td><a href="keys-and-tooling.md">keys-and-tooling.md</a></td></tr></tbody></table>

## CLI flow

The pool needs a non-zero verifying key hash on chain. On a dev chain, re-genesis with shielded keys:

```bash
./run/regenesis-shielded.sh --dev
./run/mazze-cli.sh vkhash
```

Then:

```bash
# Deposit into the pool
./run/mazze-cli.sh wallet shield-deposit --name alice --amount 10

# Private transfer
./run/mazze-cli.sh wallet transfer --name alice --dest <shielded-address> --amount 5 --shielded

# Unshield to a public base32 address
./run/mazze-cli.sh wallet unshield --name alice --dest <base32-address> --amount 2

# Private balance: scans shielded logs and spent nullifiers
./run/mazze-cli.sh wallet balance --name alice --private
```

Legacy shielded addresses are base32 encodings of a 64-byte secp256k1 public key:

```bash
target/debug/shielded_note address --secret <secret-hex> --network-id 1990
```

## Reading the pool over RPC

The pool lives at `MAZZE:TYPE.BUILTIN:AAEJUAAAAAAAAAAAAAAAAAAAAAAAAAAABAJ1SJV3W2`.

| Function | Selector |
| --- | --- |
| `root()` | `0xebf0c717` |
| `verifyingKeyHash()` | `0x69b5d6d1` |
| `isNullifierSpent(bytes32)` | `0xd5a4e325` |

```bash
curl -sS -X POST -H 'Content-Type: application/json' \
  --data '{"jsonrpc":"2.0","id":1,"method":"mazze_call","params":[{"to":"MAZZE:TYPE.BUILTIN:AAEJUAAAAAAAAAAAAAAAAAAAAAAAAAAABAJ1SJV3W2","data":"0xebf0c717"},"latest_state"]}' \
  http://127.0.0.1:12539
```
