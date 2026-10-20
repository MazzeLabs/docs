---
description: What changed in the Mazze node, and in these docs, as of 20 October 2026.
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

# What's new

These docs follow the `mazze-rust-release` repository. This update covers `master` and the `shielded-space` development branch, as of 20 October 2026.

## Shielded space: post-quantum privacy

<mark style="color:orange;">`shielded-space` branch · running on devnet</mark>

A third space joins Native and eSpace. It replaces the Groth16 pool with a design that needs no trusted setup and rests only on hash-based assumptions.

* **Notes and proofs.** Every shielded transaction spends two notes and creates two. A STARK proof (PS-1: Plonky3 over KoalaBear, FRI, Keccak-256) shows that the spend is valid, with 128 bits of proven soundness.
* **Statistically hiding commitments.** No future mathematics, quantum computers included, can reveal what a note contains.
* **Its own block section.** Shielded bodies travel beside the account transactions. Proofs are checked when a block is accepted and are not stored in the block database.
* **A fixed public shape.** Shield-in, payment and claim transactions look the same on chain: same size, same constant fee. The fee is burned.
* **A wallet that keeps the keys.** `mazze-shielded-wallet` holds the seed, rebuilds the tree from public data, proves locally, and restores from the seed alone.
* **Dandelion++ routing** for shielded transactions, so the node that first broadcasts one is not where it came from.

Start at [Shielded space](privacy/README.md). The previous Groth16 pool is documented under [Legacy pool](privacy/legacy-pool.md).

## eSpace on revm 40

* The EVM space runs on **revm 40.0.0** with the **Prague** spec. Future Ethereum hard forks arrive with a revm update.
* **34,036 of 34,036** `GeneralStateTests` from `ethereum/tests` pass.
* Mazze-specific behaviour (the cross-space bridge, sponsorship, storage collateral, `evm_gas_ratio`, restricted `BLOCKHASH`) is handled outside revm. revm itself is unmodified.
* The eSpace RPC accepts the `finalized` block tag. It maps to the latest checkpoint.

See [EVM compatibility](developers/evm-compatibility.md).

## Storage: two tiers

* **MDBX** is the hot tier and the default state database (`state_db_type = "mdbx"`).
* **ParityDB** is the cold tier: blocks, receipts, traces, history and snapshots. It is also the fallback state database.
* The SQLite backend has been removed.
* Checkpoints and snapshots are hardened: snapshot chunks are hashed and checked on receipt, a failed snapshot sync falls back gracefully instead of crashing, and a node refuses to start with a broken snapshot chain.

See [Storage and snapshots](architecture/storage-and-snapshots.md).

## RPC: jsonrpsee and safe defaults

* The JSON-RPC layer moved to **jsonrpsee 0.26** on tokio 1. Method names, pub-sub and error codes are unchanged.
* Server limits are configurable, with bounded defaults: 1,000 requests per batch, 25 MiB responses, 1,000 HTTP and 100 WebSocket connections.
* `public_rpc_apis` defaults to `"safe"`, and CORS no longer defaults to `"all"`.
* `mazze_getStatus` adds grouped `progress`, `randomx`, `snapshots` and `era` objects.

See [RPC and APIs](architecture/rpc-and-apis.md) and the [RPC guide](testnet/rpc.md).

## Security and dependencies

* A full audit fixed the Critical and High findings in the node, including a silent PoW bypass on unknown seed hashes and a peer-triggered executor panic. One High item, a per-request RPC timeout, is only partly closed.
* The audit rated the Groth16 pool's single trusted setup **Critical**: a leaked setup trapdoor would allow silent, unlimited minting inside the pool. The shielded space removes the trusted setup altogether.
* `parity-crypto` and `parity-secp256k1` are replaced by maintained RustCrypto crates and upstream `secp256k1`, with byte-identical output.
* Dependencies flagged by RustSec advisories are updated or replaced.
* Toolchain: Rust **1.93** on `shielded-space` (needed by Plonky3), 1.91 on `master`.

## Operator notes

{% hint style="warning" %}
**The genesis block hash has changed.** The genesis transaction now carries a message. Wipe local chain state before you start a node on the new build. This is pre-mainnet; no launched chain is re-genesised.
{% endhint %}

* Logs now go to the repository-root `logs/` directory.
* Review `run/hydra.toml` before exposing RPC on a public address.
