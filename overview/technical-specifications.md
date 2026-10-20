---
description: The numbers behind Mazze, by layer.
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

# Technical specifications

{% tabs %}
{% tab title="Chain" %}
| Metric | Value |
| --- | --- |
| Security | Proof of Work, RandomX |
| Ledger | DAG of blocks, ordered by DETS into epochs |
| Operational block rate | 4 blocks per second |
| Execution | Deferred by a fixed number of epochs |
| Checkpoint cadence | `era_epoch_count`, 20,000 epochs |
| Snapshot cadence | `snapshot_epoch_count`, about 2,000 epochs |
| Spaces | Native, eSpace, Shielded |
{% endtab %}

{% tab title="Execution" %}
| Metric | Value |
| --- | --- |
| Native space VM | Mazze interpreter |
| eSpace VM | revm 40.0.0, Prague spec |
| Ethereum state tests | 34,036 / 34,036 pass |
| Storage gas multiplier (`evm_gas_ratio`) | 2 |
| Smallest unit | 1 MAZZE = 10¹⁸ mazzy |
{% endtab %}

{% tab title="Shielded space" %}
| Metric | Value |
| --- | --- |
| Status | Devnet; inactive on public networks until activation |
| Transaction shape | 2 inputs × 2 outputs, always |
| Proof system | PS-1: Plonky3 STARK over KoalaBear⁸, FRI, Keccak-256 |
| Soundness | 128 bits, proven |
| Trusted setup | None |
| Commitment hiding | Statistical, ≤ 2⁻³⁷² |
| Body size | 441 bytes |
| Proof size | ≈185–189 KB, cap 192 KiB |
| Tree depth | 32 |
| Anchor window | 100,000 epochs |
| Slot length | 20 epochs |
| Transactions per block section | 8 |
| Fee | Constant, ≈0.0197 MAZZE, burned |
| Largest note | < 2⁶⁴ mazzy (≈18.4 MAZZE) |
{% endtab %}

{% tab title="Node" %}
| Metric | Value |
| --- | --- |
| Language | Rust (toolchain 1.93 on `shielded-space`, 1.91 on `master`) |
| Hot storage | MDBX |
| Cold storage | ParityDB |
| RPC | jsonrpsee 0.26 over HTTP, WebSocket and TCP |
| Default public RPC set | `safe`: `mazze`, `pubsub`, `txpool`, `shielded` |
| Mining | `stratum`, `cpu` or `disable` |
{% endtab %}

{% tab title="Token" %}
| Metric | Value |
| --- | --- |
| Native genesis issuance | 3,900,000,000 MAZZE |
| Mining supply target | 2,500,000,000 MAZZE |
| Theoretical native upper bound | 6,400,000,000 MAZZE |
| Initial base mining reward | 4 MAZZE |
| Halving interval | 312,500,000 blocks |
| Wrapped MAZZE on Ethereum (current baseline) | 4,900,000,000 MAZZE |

See [Tokenomics](../tokenomics/overview.md).
{% endtab %}
{% endtabs %}

## Reference sections

* [Three spaces](three-spaces.md)
* [Architecture](../architecture/README.md)
* [Shielded space](../privacy/README.md)
* [Tokenomics](../tokenomics/overview.md)
