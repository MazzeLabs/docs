---
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

# ZK Proofs Types

<table data-header-hidden><thead><tr><th width="212"></th><th width="138"></th><th width="191"></th><th></th></tr></thead><tbody><tr><td></td><td><mark style="color:orange;"><strong>ZK-SNARKs</strong></mark></td><td><mark style="color:orange;"><strong>ZK-STARKs</strong></mark></td><td><mark style="color:orange;"><strong>Bulletproofs</strong></mark></td></tr><tr><td><mark style="color:orange;"><strong>Setup Requirement</strong></mark></td><td>Trusted Setup</td><td>No Trusted Setup</td><td>No Trusted Setup</td></tr><tr><td><mark style="color:orange;"><strong>Proof Size</strong></mark></td><td>Very Small</td><td>Larger than SNARKs</td><td>Smaller than STARKs, larger than SNARKs</td></tr><tr><td><mark style="color:orange;"><strong>Computation Time</strong></mark></td><td>Very Fast</td><td>Fast</td><td>Slower than SNARKs and STARKs</td></tr><tr><td><mark style="color:orange;"><strong>Quantum Resistance</strong></mark></td><td>No</td><td>Yes</td><td>No</td></tr><tr><td><mark style="color:orange;"><strong>Trust Assumptions</strong></mark></td><td>High</td><td>Low</td><td>Low</td></tr><tr><td><p><mark style="color:orange;"><strong>Scalability</strong></mark></p><p> </p></td><td><p>Moderate</p><p> </p></td><td><p>High</p><p> </p></td><td><p>Moderate</p><p> </p></td></tr><tr><td><mark style="color:orange;"><strong>Use Cases</strong></mark></td><td>Private transactions, Blockchain scalability</td><td>Private transactions, Quantum-resistant applications</td><td>Confidential transactions, Range proofs</td></tr></tbody></table>

### <mark style="color:orange;">ZK-SNARKs | Efficiency Meets Blockchain</mark>

**Zero-Knowledge Succinct Non-Interactive Argument of Knowledge (ZK-SNARKs)** is a breakthrough in the realm of privacy-focused computations. Renowned for its efficiency and compact proof sizes, ZK-SNARKs have become a cornerstone in blockchain applications, such as Zcash. The key feature? They require a trusted setup, which while facilitating their efficiency, introduces a unique consideration in their deployment. This makes ZK-SNARKs a go-to choice for scenarios prioritizing swift and space-efficient cryptographic proofs.

### <mark style="color:orange;">ZK-STARKs | The Future-Proof Solution</mark>

Enter **Zero-Knowledge Scalable Transparent Argument of Knowledge (ZK-STARKs)**. Building upon the foundations laid by SNARKs, STARKs eliminate the need for a trusted setup. This not only enhances their transparency but also arms them against quantum attacks, offering a quantum-resistant shield. The lack of a trusted setup, coupled with their scalability, positions ZK-STARKs as a robust option for applications that demand enhanced security measures in the face of evolving technological landscapes.

### <mark style="color:orange;">Bulletproofs | Versatility in Batching</mark>

Bulletproofs are a distinct variant in the zero-knowledge proof arena. Their most notable feature? The ability to efficiently handle multiple proofs in a single batch. This makes them exceptionally potent in scenarios where batching is prevalent. While they forgo the need for a trusted setup, akin to ZK-STARKs, they do come with a trade-off: larger proof sizes and longer verification times compared to ZK-SNARKs. However, their versatility makes them a suitable choice for a range of applications that balance proof size and verification speed with the convenience of not requiring a trusted setup.

Each of these ZK-proof types embodies a unique approach to achieving zero-knowledge, striking different balances in computational efficiency, proof size, and security assumptions. This diversity makes them apt for a wide array of applications in digital privacy and secure communication, ensuring that every need finds its match in the world of ZK-proofs. Explore more about these technologies in the Mazze Docs.
