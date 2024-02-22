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

# Smart contracts

### <mark style="color:orange;">What is a Smart Contract?</mark>

A "smart contract" is a program operating on the Mazze blockchain, an EVM-compatible platform. It consists of both code (its functions) and data (its state), housed at a unique address on the Mazze blockchain.

Smart contracts function as a type of Mazze blockchain account, possessing a balance and capable of receiving transactions. Unlike user-controlled accounts, smart contracts are automatically executed by the network once deployed. Users can interact with these contracts through transactions that trigger specific functions within the contract. Smart contracts establish and autonomously enforce rules, akin to traditional contracts, but through their code. Once deployed, smart contracts are typically immutable and interactions with them are permanent.

### <mark style="color:orange;">Permissionless Deployment</mark>

On the Mazze blockchain, anyone can create and deploy a smart contract, provided they have the necessary coding skills in a smart contract language and sufficient native blockchain tokens (similar to ETH) for deployment. Deploying a smart contract, a form of transaction, requires payment of network fees ("gas"), with contract deployment generally incurring higher gas costs than standard transactions.

The Mazze blockchain supports user-friendly programming languages for smart contract development, such as Solidity. These contracts must be compiled for the Mazze blockchain's virtual machine to interpret and store them.

### <mark style="color:orange;">Limitations</mark>

Smart contracts inherently lack the ability to access real-world information directly, as they cannot pull data from external sources. This is intentional, as external data reliance could compromise the network's consensus, crucial for its security and decentralization.

To integrate real-world data, blockchain applications use oracles, tools that provide external data to smart contracts.

Another constraint is the maximum contract size. On the Mazze blockchain, a smart contract can be up to 24KB; exceeding this limit results in gas exhaustion. Developers can circumvent this limitation by employing methods like [<mark style="color:orange;">The Diamond Pattern</mark>](https://eips.ethereum.org/EIPS/eip-2535).

### <mark style="color:orange;">Multisig Contracts</mark>

Multisig (multiple-signature) contracts on the Mazze blockchain require several authentic signatures for transaction execution. They offer a safeguard against single failure points, especially for contracts managing significant token amounts. Multisig contracts distribute contract management and key holding responsibilities, preventing catastrophic losses from a single key compromise. They are also useful for simple DAO governance structures. A multisig contract might require, for example, 3 out of 5 or 4 out of 7 valid signatures (N ≤ M, M > 1) for execution. In a 4/7 multisig setup, four out of seven possible valid signatures are needed, ensuring fund retrievability even if three signatures are lost and mandating majority agreement for contract execution.
