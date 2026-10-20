---
description: eSpace runs on revm 40 with the Prague spec. What works as on Ethereum, and where Mazze differs.
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

# EVM compatibility

<mark style="color:purple;">**● ESPACE**</mark>

eSpace is Mazze's Ethereum-compatible space. It executes on **revm 40.0.0**, with the **Prague** spec, from genesis. There is no transition flag and no parallel path.

## How compatible

| Check | Result |
| --- | --- |
| `ethereum/tests` `GeneralStateTests` | **34,036 / 34,036** pass |
| Spec | Prague (`SpecId::PRAGUE`) |
| revm | Unmodified upstream |
| Tracing | geth-style traces through `alloy-rpc-types-trace` |

The excluded fixtures cover transaction acceptance rules (intrinsic gas, insufficient funds, EIP-1559 fee checks), which Mazze checks before execution rather than inside the VM.

Future Ethereum hard forks reach eSpace through a revm update and a spec bump.

## What works as on Ethereum

* Solidity and Vyper contracts, compiled with standard tools.
* MetaMask, ethers, viem, web3.js.
* Foundry and Hardhat for testing and deployment.
* `eth_*` JSON-RPC, filters, logs, `eth_getProof`, `eth_feeHistory`, and `eth_subscribe` over WebSocket.
* The standard precompiles, including KZG point evaluation (`0x0a`).

## Where Mazze differs

These behaviours are implemented outside revm.

| Area | On Mazze |
| --- | --- |
| **Block tags** | `finalized` maps to the latest checkpoint |
| **`BLOCKHASH`** | Answered by Mazze's block history, with a restricted range |
| **Storage gas** | Gas for storage-occupying operations is multiplied by `evm_gas_ratio` (2 by default) |
| **Sponsorship and collateral** | Native-space features, not part of eSpace execution |
| **Cross-space calls** | Native accounts call eSpace through the cross-space internal contract (`callEVM`, `createEVM`, `staticCallEVM`, `transferEVM`). It is dispatched before either VM runs. |
| **Mapped accounts** | Every native address has a mapped eSpace address. `withdrawFromMapped` moves value back to the native space. |
| **Ordering** | Blocks form a DAG and execute in epochs. A transaction's position is final once its epoch is confirmed. |

## Known issue

{% hint style="warning" %}
After a successful contract creation through the live cross-space bridge, the account is stored with the right `code_hash`, but `eth_getCode` can return empty because the code-by-hash entry is missing. Direct deployments in eSpace are not affected. This is tracked for a fix.
{% endhint %}

## Native space VM

The native space keeps Mazze's own interpreter, with Mazze's own rules (sponsorship, collateral, internal contracts). The KZG precompile is not available there; it was removed from the native space and exists only in eSpace.
