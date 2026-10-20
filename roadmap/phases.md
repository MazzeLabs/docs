---
description: What is done and what comes next. Phases are ordered by dependency, not by date.
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

# Phases

| Phase | Focus | Status |
| --- | --- | --- |
| **A · Foundation** | Concept, whitepaper, brand, community | <mark style="color:green;">**Done**</mark> |
| **B · Core network and tooling** | PoW and DAG network, eSpace, storage, RPC, audit | <mark style="color:green;">**Done**</mark> |
| **C · Privacy and mainnet readiness** | Shielded space, launch hardening, operators | <mark style="color:orange;">**In progress**</mark> |
| **D · Expansion** | Ecosystem, interoperability, long-term growth | Planned |

## Phase A · Foundation

* [x] Concept development
* [x] Whitepaper
* [x] Initial technical documentation
* [x] Branding and online presence
* [x] Early community outreach

## Phase B · Core network and tooling

* [x] PoW (RandomX) with DAG/DETS ordering
* [x] Wrapped MAZZE ERC20 and the allocation framework
* [x] Node and miner setup with Docker and from source
* [x] Mazze CLI, JSON-RPC and mining modes (`stratum`, `cpu`, `disable`) documented
* [x] eSpace on revm 40 (Prague), passing all 34,036 Ethereum state tests
* [x] Two-tier storage: MDBX hot tier, ParityDB cold tier
* [x] Hardened checkpoints, snapshots and snapshot sync
* [x] RPC on jsonrpsee, with safe defaults and server limits
* [x] Full security audit; Critical and High node findings fixed
* [x] Crypto and dependency modernisation (RustCrypto, upstream secp256k1, RustSec fixes)
* [x] Explorer: [mazzescan.io](https://mazzescan.io)

## Phase C · Privacy and mainnet readiness

* [x] Shielded-space design: statistically hiding notes, per-note nullifiers, seed recovery
* [x] Proof system PS-1 (Plonky3 STARK, 128-bit proven) and the 2×2 spend circuit
* [x] Shielded block section, stage A verification and witness store
* [x] Shielded engine, pool lane and Dandelion++ relay
* [x] Shielded RPC, the shielded wallet and the shield-in bridge, working on devnet
* [ ] Shielded space review and activation on public networks
* [ ] Mainnet launch readiness and validation
* [ ] Node operator expansion
* [ ] Bridge operations hardening and monitoring
* [ ] Hackathon and grant programme

## Phase D · Expansion

* [ ] Ecosystem apps (DEX and related integrations)
* [ ] Cross-chain interoperability
* [ ] DeFi ecosystem growth
* [ ] High-BPS tuning from soak results
* [ ] Governance and operational compliance
* [ ] Long-term sustainability initiatives
* [ ] Strategic ecosystem partnerships
