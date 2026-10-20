---
description: Use mazze-shielded-wallet to shield in, pay, receive, claim, shield out and restore from a seed.
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

# Wallet guide

`mazze-shielded-wallet` is the reference wallet for the shielded space. It holds the seed and the note openings, rebuilds the commitment tree from the node's public data, and proves on your machine. The node only ever sees public data.

{% hint style="warning" %}
The shielded space runs on a **local devnet** for now. On public networks the lane is inactive until its activation height. To try it, start a dev node with `shielded_activation_height` set in its config.
{% endhint %}

## Build

The wallet is a binary in the `shielded-space` branch of `mazze-rust-release`. That branch needs Rust 1.93.

```bash
git clone https://github.com/MazzeLabs/mazze-rust-release
cd mazze-rust-release
git checkout shielded-space
cargo build --release --bin mazze-shielded-wallet
```

Use a release build: proving is CPU-heavy.

## Amounts and fees

* Amounts are in **mazzy**: 1 MAZZE = 10¹⁸ mazzy.
* Every shielded transaction pays the constant fee returned by `shielded_getStatus` as `txFee`, about 0.0197 MAZZE by default. Shield-ins and claims pay it too.
* One note holds less than 2⁶⁴ mazzy, about 18.4 MAZZE.

## Commands

| Command | What it does |
| --- | --- |
| `init --wallet W` | Creates a wallet file with a fresh 32-byte seed from OS randomness |
| `address --wallet W --rpc URL` | Prints your `mzs1…` address for the node's chain |
| `sync --wallet W --rpc URL` | Reads the executed sections, rebuilds the tree, finds your notes and marks spent ones |
| `balance --wallet W` | Prints spendable and pending value and the number of notes |
| `shield-in --wallet W --rpc URL --amount A --funder-key HEX` | Moves `A` from a native account into a new self-note |
| `send --wallet W --rpc URL --to mzs1… --amount A --opening-out FILE` | Pays `A` privately and writes the recipient's note opening to `FILE` |
| `receive --wallet W --opening FILE` | Imports a note opening someone sent you |
| `claim --wallet W --rpc URL` | Folds a received note and your largest self-note into one new self-note |
| `unshield --wallet W --rpc URL --to 0xADDR [--espace] --amount A` | Pays `A` out to a native address, or to an eSpace address with `--espace` |
| `restore --wallet W --rpc URL --seed HEX` | Rebuilds your self-notes from the seed and syncs |

## A full round trip

{% stepper %}
{% step %}
### Create two wallets

```bash
W=target/release/mazze-shielded-wallet
RPC=http://127.0.0.1:12539

$W init --wallet alice.json
$W init --wallet bob.json
$W address --wallet bob.json --rpc $RPC
```
{% endstep %}

{% step %}
### Shield in

Alice moves 5 MAZZE from a funded native account into the shielded space.

```bash
$W shield-in --wallet alice.json --rpc $RPC \
  --amount 5000000000000000000 --funder-key <native-secret-hex>
```

The wallet first sends a signed native call, `shieldIn(bodyHash)`, with the amount as its value. It then submits the shielded transaction that consumes the deposit. The new note is worth the amount minus the fee.
{% endstep %}

{% step %}
### Sync and check the balance

The note becomes spendable once its slot has executed.

```bash
$W sync --wallet alice.json --rpc $RPC
$W balance --wallet alice.json
```
{% endstep %}

{% step %}
### Pay Bob

```bash
$W send --wallet alice.json --rpc $RPC \
  --to mzs1… --amount 2000000000000000000 --opening-out to-bob.json
```

Payments are delivered **out of band**: the wallet writes Bob's note opening to `to-bob.json`. Send that file to Bob over any private channel. Alice's change becomes a new self-note.
{% endstep %}

{% step %}
### Bob receives and claims

```bash
$W receive --wallet bob.json --opening to-bob.json
$W sync --wallet bob.json --rpc $RPC
$W claim --wallet bob.json --rpc $RPC
```

The claim spends the received note together with Bob's largest self-note and creates one self-note. Only self-notes can be restored from the seed.
{% endstep %}

{% step %}
### Shield out

```bash
$W unshield --wallet bob.json --rpc $RPC --to 0x… --amount 1000000000000000000
```

Without `--espace`, the destination is a native-space address.
{% endstep %}
{% endstepper %}

## Back up and restore

The 32-byte seed is the only backup you need for self-notes: change, shield-ins and claims.

```bash
$W restore --wallet restored.json --rpc $RPC --seed <seed-hex>
```

The wallet derives the recovery tags from the seed, finds them on chain, opens the sealed recovery slots, rebuilds the notes and syncs. It stops after 20 consecutive tags it cannot find.

{% hint style="danger" %}
**Claim after every receipt.** A note you received is not derived from your seed. Until you claim it into a self-note, losing the wallet file loses that note.
{% endhint %}

## Privacy tips

* The wallet takes fresh OS randomness for every note, dummy and proof.
* Shield-in and shield-out amounts are public. Waiting between them, and using amounts that are not unique, makes them harder to link.
* Send note openings over an end-to-end encrypted channel. Anyone who reads an opening learns that note's value, but cannot spend it: spending also needs the recipient's `nsk`.
