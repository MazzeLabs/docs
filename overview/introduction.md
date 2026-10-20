---
description: What Mazze is and how it fits together.
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

# Introduction

{% hint style="info" %}
These docs were last updated on **20 October 2026**. For technical questions, reach us on [Telegram](https://t.me/MazzeLabs) or [Discord](https://discord.mazze.io/).
{% endhint %}

Mazze is a layer 1 blockchain secured by Proof of Work. It aims to be **fast, secure and private**.

* **Fast.** Blocks form a DAG instead of a single chain. Miners can produce blocks in parallel, and consensus orders them all into epochs instead of discarding the losers. The operational target is 4 blocks per second.
* **Secure.** Proof of Work with RandomX, a hash function tuned for ordinary CPUs, keeps mining open to anyone with a computer. The node has been through a full security audit.
* **Private.** A shielded space keeps payments private with post-quantum zero-knowledge proofs, with no trusted setup.

## One chain, three spaces

Mazze runs three spaces on one chain, with one state root:

| Space | For |
| --- | --- |
| <mark style="color:orange;">**Native**</mark> | Mazze-specific features: base32 addresses, sponsored gas, storage collateral, internal contracts |
| <mark style="color:purple;">**eSpace**</mark> | Ethereum-compatible smart contracts and wallets, on revm 40 |
| **Shielded** | Private notes and payments, proven with STARKs |

Value moves between the spaces through built-in bridges. Read more in [Three spaces](three-spaces.md).

## How a block becomes final

1. Miners build blocks that reference a **parent** and any number of **referees**, so every block they have seen is included in the graph.
2. Consensus picks a **pivot chain** through the DAG. Each pivot block and the blocks it newly brings in form an **epoch**.
3. The node executes epochs in order. Results are committed in later headers as **deferred roots**.
4. Every 20,000 epochs, a **checkpoint** marks the era as final.

The [Architecture](../architecture/README.md) section follows this path through the node's code.

## Where to go next

* Building an app? Start with [Developers](../developers/overview.md).
* Running infrastructure? Start with [Run a node](../testnet/introduction-to-mazze-testnet.md).
* Curious about privacy? Start with [Shielded space](../privacy/README.md).
* Watching the chain? Open [mazzescan.io](https://mazzescan.io).
