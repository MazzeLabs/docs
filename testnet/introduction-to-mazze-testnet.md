---
description: Run a Mazze node and miner, and test wallets, RPC and mining against a live network.
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

# Run a node

This section is for node operators and testers: running a node and a miner, using the CLI and the RPC, and reading the logs.

{% hint style="info" %}
**Network cadence.** The operational target is **4 blocks per second**. Dev mode can run at other intervals (`dev_block_interval_ms`), so do not read dev-mode throughput as network throughput.
{% endhint %}

## Guides

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Setup guide</strong></td><td>A node and a miner with Docker Compose, or from source.</td><td><a href="setup-guide.md">setup-guide.md</a></td></tr><tr><td><strong>Mazze CLI</strong></td><td>Wallets, transfers and chain summaries from the command line.</td><td><a href="mazze-cli.md">mazze-cli.md</a></td></tr><tr><td><strong>Mining</strong></td><td>The <code>stratum</code>, <code>cpu</code> and <code>disable</code> modes, and the RandomX miner.</td><td><a href="mining.md">mining.md</a></td></tr><tr><td><strong>RPC guide</strong></td><td>Ports, examples, safe exposure and the full method list.</td><td><a href="rpc.md">rpc.md</a></td></tr><tr><td><strong>Viewing logs</strong></td><td>Where logs go and how to follow them.</td><td><a href="viewing-logs.md">viewing-logs.md</a></td></tr><tr><td><strong>Soak test</strong></td><td>Sustained high-BPS load, with metrics for tuning.</td><td><a href="soak-test.md">soak-test.md</a></td></tr></tbody></table>

## Before you upgrade

{% hint style="warning" %}
**Wipe local chain state** before you start a node built from the current code. The genesis block hash changed when the genesis transaction gained a message.
{% endhint %}

* The default state database is now MDBX. Set `state_db_type = "paritydb"` to keep using ParityDB.
* Logs go to the repository-root `logs/` directory.
* `public_rpc_apis` defaults to `"safe"`. Review `run/hydra.toml` before exposing RPC.

## What to test

* Running and validating node and miner infrastructure.
* Wallet and transfer workflows with the CLI.
* RPC integrations, native and eSpace.
* Mining modes: `stratum`, `cpu`, `disable`.
* Contract deployment on eSpace: see [Deploying smart contracts](deploying-smart-contracts-on-mazze-testnet.md).

Found a problem? See [Feedback and reporting issues](feedback-and-reporting-issues.md).
