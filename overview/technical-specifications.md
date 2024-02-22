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

# Technical Specifications

| <mark style="color:orange;">**Metric**</mark> | <mark style="color:orange;">**Value**</mark> |
| --------------------------------------------- | -------------------------------------------- |
| Consensus Mechanism                           | Proof of Work (PoW) with DAG structure       |
| Block Generation Rate                         | 1 block per second                           |
| Daily Block Generation                        | 86,400 blocks per day                        |
| Transaction Throughput                        | \~40,000 transactions per second (TPS)       |
| Initial Base Block Reward                     | 14 MAZZE per block                           |
| Inflation Rate (First 4 Years)                | 8.83% annually                               |
| Block Reward Reduction                        | Quarterly by a factor of 0.958               |
| Storage Cost                                  | 0.5 MAZZE per 1 kB                           |
| Smart Contract Language                       | Solidity                                     |
| Token Name                                    | MAZZE                                        |
| Smallest Token Unit                           | Mazzy (1 MAZZE = 10^18 Mazzy)                |
| Initial Token Supply                          | 5 billion MAZZE                              |

### <mark style="color:orange;">Key Features</mark>

1. **Consensus Mechanism** | Utilizes a hybrid of Proof of Work (PoW) and a Directed Acyclic Graph (DAG) structure, enhancing scalability and transaction throughput with a "Weighted Graph Ledger (WGL)".
2. **Security Features** | Employs advanced cryptographic techniques and robust hashing algorithms. Special emphasis on preventing common threats like 51% and double-spending attacks.
3. **Smart Contract Capabilities** | Supports Solidity and is compatible with the Ethereum Virtual Machine (EVM), facilitating easy migration of dApps from Ethereum.
4. **Innovations** | Unique block weight system and DAG-based ledger structure for improved scalability and throughput.
5. **Privacy with Zero-Knowledge (ZK) Proofs** | Integration of ZK Proofs in Phase D enhances transaction privacy and confidentiality, allowing for validation without exposing transaction data​​.

### <mark style="color:orange;">Core Components</mark>

1. **Weighted Ledger Selection Rule (WLSR)** | Balances throughput and security with a dynamic block weighting mechanism.
2. **DAG-Embedded Tree Structure (DETS)** | Improves ledger security and throughput, enabling blocks to reference multiple predecessors.
3. **Consensus Process** | Efficient DAG structure and WLSR for rapid block production, ensuring consistent transaction ordering and double-spending prevention.
4. **EVM Integration**: Incorporates an Ethereum Virtual Machine (EVM) environment to facilitate the deployment and execution of smart contracts written in Solidity, ensuring compatibility and flexibility.
5. **ZK-STARKs for Enhanced Privacy** | The implementation of ZK-STARKs significantly enhances security and privacy within the blockchain.
