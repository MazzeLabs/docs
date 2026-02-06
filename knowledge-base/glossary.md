---
description: Navigating Blockchain Terminology
layout:
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Glossary

## <mark style="color:orange;">Definitions</mark>

<table data-header-hidden><thead><tr><th width="230"></th><th></th></tr></thead><tbody><tr><td><strong>BPS (Blocks Per Second)</strong></td><td>Block production rate. Current operational target documented here is <strong>4 BPS</strong>, while dev mode can run with different intervals.</td></tr><tr><td><strong>DAG</strong></td><td>Directed Acyclic Graph used by Mazze for parent/referee block relationships.</td></tr><tr><td><strong>DETS</strong></td><td>DAG-Embedded Tree Structure used by consensus to order and process blocks.</td></tr><tr><td><strong>Epoch</strong></td><td>Ordered execution unit in Mazze. State/receipts commitments are handled with deferred epoch execution.</td></tr><tr><td><strong>PoW (Proof of Work)</strong></td><td>Consensus security model used by Mazze. Hashing is RandomX-based.</td></tr><tr><td><strong>RandomX</strong></td><td>PoW algorithm implementation used for nonce search and block validation.</td></tr><tr><td><strong>Stratum</strong></td><td>Mining mode where miners connect to a node's stratum endpoint and submit solutions.</td></tr><tr><td><strong>CPU Mining</strong></td><td>Mining mode where the node mines locally without external stratum workers.</td></tr><tr><td><strong>Shielded Pool</strong></td><td>Internal contract handling privacy-preserving deposits and spends with proof verification.</td></tr><tr><td><strong>Groth16</strong></td><td>Zero-knowledge proof system currently used in Mazze privacy implementation.</td></tr><tr><td><strong>Poseidon Merkle Tree</strong></td><td>Merkle structure used by the shielded pool for commitments and roots.</td></tr><tr><td><strong>Nullifier</strong></td><td>Unique value recorded in shielded spends to prevent double-spending of private notes.</td></tr><tr><td><strong>Bridge Liquidity (Directional)</strong></td><td>Bridge capacity is direction-dependent; one direction can pause if destination-side liquidity is insufficient.</td></tr><tr><td><strong>Native Issuance</strong></td><td>Supply accounting model: <code>genesis + mined - burnt</code>.</td></tr><tr><td><strong>Mazze CLI</strong></td><td>Command-line tool (`run/mazze-cli.sh`) for wallet, transfer, and shielded workflows via RPC.</td></tr><tr><td><strong>RPC</strong></td><td>JSON-RPC interfaces (Mazze native + EVM-compatible) exposed over HTTP/WS/TCP depending on config.</td></tr></tbody></table>

For canonical technical details, see [Architecture](../architecture/README.md),
[Privacy](../privacy/README.md), [Tokenomics](../tokenomics/overview.md), and
[Testnet Operations](../testnet/setup-guide.md).
