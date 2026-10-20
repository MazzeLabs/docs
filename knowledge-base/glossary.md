---
description: The terms used across these docs.
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

# Glossary

## Chain

<table data-header-hidden><thead><tr><th width="240"></th><th></th></tr></thead><tbody><tr><td><strong>BPS</strong></td><td>Blocks per second. The operational target is <strong>4 BPS</strong>; dev mode can run at other intervals.</td></tr><tr><td><strong>Checkpoint</strong></td><td>A point where consensus declares an era final. Every <code>era_epoch_count</code> epochs (20,000 by default).</td></tr><tr><td><strong>DAG</strong></td><td>Directed acyclic graph. Mazze blocks reference a parent and any number of referees, forming a DAG.</td></tr><tr><td><strong>Deferred roots</strong></td><td>State, receipt and log roots of an executed epoch, committed in a later block header.</td></tr><tr><td><strong>DETS</strong></td><td>DAG-Embedded Tree Structure. The tree consensus uses to pick the pivot chain and order blocks.</td></tr><tr><td><strong>Epoch</strong></td><td>A pivot block and the blocks it newly brings into the order. The unit of execution.</td></tr><tr><td><strong>Era</strong></td><td>The span between two checkpoints.</td></tr><tr><td><strong>Pivot chain</strong></td><td>The chain through the DAG that consensus selects. Each pivot block defines an epoch.</td></tr><tr><td><strong>PoW</strong></td><td>Proof of Work. Mazze's security model.</td></tr><tr><td><strong>RandomX</strong></td><td>The CPU-oriented PoW hash function Mazze uses. Its seed rotates by RandomX epoch.</td></tr><tr><td><strong>Referee</strong></td><td>A block referenced in addition to the parent, so every block a miner has seen joins the graph.</td></tr><tr><td><strong>Snapshot</strong></td><td>A copy of the state at an epoch, ready to send to a new node. About every 2,000 epochs.</td></tr><tr><td><strong>Stratum</strong></td><td>Mining mode in which external miners connect to the node's Stratum endpoint.</td></tr></tbody></table>

## Spaces and execution

<table data-header-hidden><thead><tr><th width="240"></th><th></th></tr></thead><tbody><tr><td><strong>Space</strong></td><td>A separate account model inside the chain, with its own addresses, VM and RPC. Mazze has three.</td></tr><tr><td><strong>Native space</strong></td><td>Mazze's own space: base32 addresses, sponsorship, storage collateral, internal contracts.</td></tr><tr><td><strong>eSpace</strong></td><td>The Ethereum-compatible space, executed by revm.</td></tr><tr><td><strong>Shielded space</strong></td><td>The private space, where value is held as notes and spent with STARK proofs.</td></tr><tr><td><strong>Cross-space bridge</strong></td><td>The internal contract that moves value and calls between the native space and eSpace.</td></tr><tr><td><strong>Mapped address</strong></td><td>The eSpace address deterministically derived from a native address.</td></tr><tr><td><strong>Internal contract</strong></td><td>A built-in contract at a fixed address, implemented in the node rather than in bytecode.</td></tr><tr><td><strong>revm</strong></td><td>A Rust EVM implementation. eSpace runs on revm 40.0.0 with the Prague spec.</td></tr><tr><td><strong>mazzy</strong></td><td>The smallest unit. 1 MAZZE = 10¹⁸ mazzy.</td></tr></tbody></table>

## Shielded space

<table data-header-hidden><thead><tr><th width="240"></th><th></th></tr></thead><tbody><tr><td><strong>Anchor</strong></td><td>A recorded root of the commitment tree that a spend proves membership against. Valid for 100,000 epochs.</td></tr><tr><td><strong>Backing</strong></td><td>The native balance that holds all value inside the shielded space. Always equal to the sum of the notes.</td></tr><tr><td><strong>Claim</strong></td><td>Folding a received note into a self-note, so it can be restored from the seed.</td></tr><tr><td><strong>Commitment</strong></td><td>The public, statistically hiding fingerprint of a note. A leaf of the commitment tree.</td></tr><tr><td><strong>Dandelion++</strong></td><td>A relay scheme that passes a transaction peer to peer before broadcasting it, hiding where it came from.</td></tr><tr><td><strong>Diversifier</strong></td><td>A value that gives one wallet many unlinkable addresses.</td></tr><tr><td><strong>KoalaBear</strong></td><td>The 31-bit prime field <code>2^31 − 2^24 + 1</code> the shielded circuit works in.</td></tr><tr><td><strong>Note</strong></td><td>A unit of shielded value: an owner, a value and randomness.</td></tr><tr><td><strong>Note opening</strong></td><td>Everything needed to use a note. A sender delivers it to the recipient off chain.</td></tr><tr><td><strong>Nullifier</strong></td><td>The value published when a note is spent. Each note has exactly one, which prevents double spends.</td></tr><tr><td><strong>Plonky3</strong></td><td>The STARK library PS-1 is built on, pinned at version 0.8.0.</td></tr><tr><td><strong>Poseidon2</strong></td><td>The hash function used inside the circuit, for commitments, keys, nullifiers and the tree.</td></tr><tr><td><strong>PS-1</strong></td><td>Proof system 1: the STARK configuration that proves shielded spends, at 128 bits of proven soundness.</td></tr><tr><td><strong>Recovery slot</strong></td><td>A sealed field in every shielded body that lets the sender's wallet rebuild its self-notes from the seed.</td></tr><tr><td><strong>Self-note</strong></td><td>A note a wallet pays to itself (change, shield-in, claim), derived from its seed.</td></tr><tr><td><strong>Shield-in / shield-out</strong></td><td>Moving value from a public account into the shielded space, and back.</td></tr><tr><td><strong>Slot</strong></td><td>A block height where a shielded section is allowed. Every 20 epochs by default.</td></tr><tr><td><strong>STARK</strong></td><td>A transparent, hash-based zero-knowledge proof. No trusted setup, and believed secure against quantum computers.</td></tr><tr><td><strong>Stage A / stage B</strong></td><td>Proof verification when a block is accepted (A), and applying the shielded section to the state when its epoch executes (B).</td></tr><tr><td><strong>Witness sidecar</strong></td><td>The proofs of a block's shielded bodies, sent with the block but not stored inside it.</td></tr></tbody></table>

## Node and tooling

<table data-header-hidden><thead><tr><th width="240"></th><th></th></tr></thead><tbody><tr><td><strong>Mazze CLI</strong></td><td><code>run/mazze-cli.sh</code>: wallets, transfers and chain summaries over RPC.</td></tr><tr><td><strong>MDBX</strong></td><td>The memory-mapped database used as the hot storage tier.</td></tr><tr><td><strong>ParityDB</strong></td><td>The database used as the cold tier for history and snapshots.</td></tr><tr><td><strong>RPC</strong></td><td>JSON-RPC over HTTP, WebSocket and TCP: <code>mazze_*</code>, <code>eth_*</code>, <code>shielded_*</code> and more.</td></tr></tbody></table>

## Token

<table data-header-hidden><thead><tr><th width="240"></th><th></th></tr></thead><tbody><tr><td><strong>Bridge liquidity</strong></td><td>Bridge capacity is directional: one direction can pause if the destination side lacks liquidity.</td></tr><tr><td><strong>Native issuance</strong></td><td>Supply accounting: <code>genesis + mined − burnt</code>.</td></tr></tbody></table>

## Legacy

<table data-header-hidden><thead><tr><th width="240"></th><th></th></tr></thead><tbody><tr><td><strong>Groth16</strong></td><td>The pairing-based proof system of the legacy shielded pool. Needs a trusted setup.</td></tr><tr><td><strong>Legacy shielded pool</strong></td><td>The Groth16 internal contract that preceded the shielded space.</td></tr></tbody></table>
