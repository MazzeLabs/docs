---
description: >-
  Documentation for Mazze: a PoW layer 1 on a DAG, with three spaces on one
  chain — Native, eSpace (EVM) and a post-quantum Shielded space.
cover: .gitbook/assets/brand/cover-home.png
coverY: 0
layout:
  cover:
    visible: true
    size: full
  title:
    visible: false
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: false
  pagination:
    visible: true
---

# Mazze docs

**Mazze is a Proof-of-Work layer 1 that orders blocks as a DAG.** One chain, one state root, three spaces: a native space, an Ethereum-compatible eSpace, and a shielded space for private payments.

{% hint style="info" %}
**Updated 20 October 2026** to the current `mazze-rust-release` code, including the `shielded-space` branch. Start with [What's new](whats-new.md) if you have read these docs before.
{% endhint %}

## One chain, three spaces

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><mark style="color:orange;"><strong>● NATIVE</strong></mark></td><td><strong>Native space</strong></td><td>Base32 addresses, sponsorship and storage collateral, internal contracts. Served by <code>mazze_*</code> RPC.</td><td><a href="overview/three-spaces.md">three-spaces.md</a></td></tr><tr><td><mark style="color:purple;"><strong>● ESPACE</strong></mark></td><td><strong>eSpace (EVM)</strong></td><td>Ethereum-compatible, on revm 40 with the Prague spec. MetaMask, Foundry and Hardhat work as they do on Ethereum.</td><td><a href="developers/evm-compatibility.md">evm-compatibility.md</a></td></tr><tr><td><strong>● SHIELDED</strong></td><td><strong>Shielded space</strong></td><td>Private notes proven with post-quantum STARKs. Running on devnet; inactive on public networks until activation.</td><td><a href="privacy/README.md">README.md</a></td></tr></tbody></table>

## Explore the docs

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Overview</strong></td><td>What Mazze is, the three spaces, and the specifications.</td><td><a href=".gitbook/assets/brand/card-overview.png">card-overview.svg</a></td><td><a href="overview/introduction.md">introduction.md</a></td></tr><tr><td><strong>Architecture</strong></td><td>How the node works, from the transaction pool to storage.</td><td><a href=".gitbook/assets/brand/card-architecture.png">card-architecture.svg</a></td><td><a href="architecture/README.md">README.md</a></td></tr><tr><td><strong>Shielded space</strong></td><td>Notes, nullifiers, STARK proofs, the shielded lane and the wallet.</td><td><a href=".gitbook/assets/brand/card-privacy.png">card-privacy.svg</a></td><td><a href="privacy/README.md">README.md</a></td></tr><tr><td><strong>Developers</strong></td><td>Build on eSpace with Ethereum tools, or call the native RPC.</td><td><a href=".gitbook/assets/brand/card-developers.png">card-developers.svg</a></td><td><a href="developers/overview.md">overview.md</a></td></tr><tr><td><strong>Run a node</strong></td><td>Set up a node and a miner, use the CLI and the RPC, and read the logs.</td><td><a href=".gitbook/assets/brand/card-node.png">card-node.svg</a></td><td><a href="testnet/introduction-to-mazze-testnet.md">introduction-to-mazze-testnet.md</a></td></tr><tr><td><strong>Tokenomics</strong></td><td>Issuance, allocations, the wrapped token and bridge liquidity.</td><td><a href=".gitbook/assets/brand/card-tokenomics.png">card-tokenomics.svg</a></td><td><a href="tokenomics/overview.md">overview.md</a></td></tr><tr><td><strong>Knowledge base</strong></td><td>Answers to common questions and the terms used in these docs.</td><td><a href=".gitbook/assets/brand/card-knowledge.png">card-knowledge.svg</a></td><td><a href="knowledge-base/faq.md">faq.md</a></td></tr><tr><td><strong>Community</strong></td><td>Ambassadors, the hackathon, grants and campaigns.</td><td><a href=".gitbook/assets/brand/card-community.png">card-community.svg</a></td><td><a href="community/grant-program.md">grant-program.md</a></td></tr><tr><td><strong>Roadmap</strong></td><td>What is done and what comes next, phase by phase.</td><td><a href=".gitbook/assets/brand/card-roadmap.png">card-roadmap.svg</a></td><td><a href="roadmap/phases.md">phases.md</a></td></tr></tbody></table>

## Quick start

{% stepper %}
{% step %}
### Run a node

Start a node and a miner with Docker Compose, or build them from source. See the [setup guide](testnet/setup-guide.md).
{% endstep %}

{% step %}
### Check that it syncs

```bash
./run/mazze-cli.sh summary
```

The [CLI guide](testnet/mazze-cli.md) covers wallets and transfers.
{% endstep %}

{% step %}
### Connect a wallet or your tools

Point MetaMask, Foundry or Hardhat at the eSpace RPC. See [Wallet connection](testnet/how-to-add-the-mazze-testnet-to-metamask.md) and [Deploying smart contracts](testnet/deploying-smart-contracts-on-mazze-testnet.md).
{% endstep %}

{% step %}
### Explore the chain

Follow blocks, epochs and the live DAG on the explorer at [mazzescan.io](https://mazzescan.io).
{% endstep %}
{% endstepper %}

## At a glance

| | |
| --- | --- |
| Security | Proof of Work, RandomX |
| Ledger | DAG of blocks, ordered by DETS into epochs |
| Execution | Native interpreter · revm 40 (Prague) for eSpace |
| Privacy | 2-in × 2-out notes, PS-1 STARK, 128-bit proven soundness |
| Storage | MDBX hot tier · ParityDB cold tier |
| RPC | JSON-RPC over HTTP, WebSocket and TCP (jsonrpsee) |

The full list is in [Technical specifications](overview/technical-specifications.md).
