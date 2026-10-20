---
description: Where to start building on Mazze, depending on the space you target.
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

# Overview

Mazze has three spaces, and each suits a different kind of work. Most applications target **eSpace**, which is Ethereum-compatible.

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><mark style="color:purple;"><strong>● ESPACE</strong></mark></td><td><strong>Smart contracts and dApps</strong></td><td>Solidity, MetaMask, Foundry, Hardhat, ethers and viem, unchanged. revm 40, Prague.</td><td><a href="evm-compatibility.md">evm-compatibility.md</a></td></tr><tr><td><mark style="color:orange;"><strong>● NATIVE</strong></mark></td><td><strong>Node and chain tooling</strong></td><td>The <code>mazze_*</code> RPC, base32 addresses, sponsorship and the cross-space bridge.</td><td><a href="../architecture/rpc-and-apis.md">rpc-and-apis.md</a></td></tr><tr><td><strong>● SHIELDED</strong></td><td><strong>Private payments</strong></td><td>Build wallets on the <code>shielded_*</code> RPC and the <code>mazze-shielded-pq</code> crate.</td><td><a href="../privacy/rpc.md">rpc.md</a></td></tr></tbody></table>

## Get set up

{% stepper %}
{% step %}
### Get an RPC endpoint

Run your own node with the [setup guide](../testnet/setup-guide.md), or use a public endpoint. A local node serves eSpace on port `58545` (HTTP) and `58546` (WebSocket), and the native RPC on `12539` (local HTTP).
{% endstep %}

{% step %}
### Connect your wallet

Add the network to MetaMask: see [Wallet connection](../testnet/how-to-add-the-mazze-testnet-to-metamask.md).
{% endstep %}

{% step %}
### Deploy a contract

Follow [Developing smart contracts](developing-smart-contracts.md) and [Deploying on testnet](../testnet/deploying-smart-contracts-on-mazze-testnet.md).
{% endstep %}

{% step %}
### Watch it on the explorer

Look up transactions, blocks and contracts on [mazzescan.io](https://mazzescan.io).
{% endstep %}
{% endstepper %}

## Source code

The node, the miner, the key tool and the shielded wallet are open source in [MazzeLabs/mazze-rust-release](https://github.com/MazzeLabs/mazze-rust-release). See [Project GitHub](project-github.md).

| Binary | Use |
| --- | --- |
| `mazze` | The node, plus `mazze rpc …` subcommands |
| `mazze-miner` | The RandomX miner, connecting over Stratum |
| `mazze_key` | Key generation and inspection |
| `mazze_store` | Keystore management |
| `mazze-shielded-wallet` | Shielded-space wallet (`shielded-space` branch) |
