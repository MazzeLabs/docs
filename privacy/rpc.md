---
description: The shielded_* JSON-RPC methods. The node serves public data only.
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

# Shielded RPC

The node serves public data only. It never sees a key, a note opening or a Merkle path, and there is deliberately no `getTreePath`: wallets rebuild the tree from `shielded_getSections`.

| Method | Returns |
| --- | --- |
| `shielded_sendRawTransaction(body, proof)` | The body hash. Admits the transaction and sends it into a Dandelion++ stem. |
| `shielded_getStatus()` | The lane's parameters and the pool state |
| `shielded_isNullifierSpent(nf)` | Whether a 48-byte nullifier is spent in the latest executed state |
| `shielded_getSections(fromEpoch, count)` | The executed shielded sections of up to `count` epochs from `fromEpoch` |

## shielded_getStatus

```bash
curl -s http://127.0.0.1:12539 -H 'content-type: application/json' \
  --data '{"jsonrpc":"2.0","id":1,"method":"shielded_getStatus","params":[]}'
```

| Field | Meaning |
| --- | --- |
| `active` | Whether the lane is active |
| `activationHeight`, `slotEpochs`, `maxTxsPerBlock`, `anchorWindowEpochs` | Lane parameters |
| `txFee` | The constant fee, in mazzy |
| `chainId` | The shielded chain ID that proofs must use |
| `root`, `leaves` | The tree root after the latest executed epoch (48 bytes), and the number of leaves |
| `backing` | The native balance backing every note |
| `poolSize` | Shielded transactions waiting in the pool |
| `executedEpoch` | The latest executed epoch |

## shielded_getSections

```bash
curl -s http://127.0.0.1:12539 -H 'content-type: application/json' \
  --data '{"jsonrpc":"2.0","id":1,"method":"shielded_getSections","params":["0x0","0x64"]}'
```

Each section has `epoch`, `blockHash` and `transactions`. Each transaction has:

| Field | Meaning |
| --- | --- |
| `bodyHash` | The transaction ID |
| `anchor` | The root the spend was proven against |
| `nullifiers` | The two nullifiers |
| `outputCommitments` | The two new commitments |
| `recoveryTag`, `recoverySlot`, `recoveryMac` | The recovery slot. Public, but opened only by the wallet whose seed derives the tag. |
| `vPublicIn`, `vPublicOut`, `fee` | The public amounts |
| `applied` | Whether stage B applied it |
| `positions` | The tree positions of the two outputs, when applied |
| `skipReason` | Why it was skipped, when skipped |

## shielded_isNullifierSpent

```bash
curl -s http://127.0.0.1:12539 -H 'content-type: application/json' \
  --data '{"jsonrpc":"2.0","id":1,"method":"shielded_isNullifierSpent","params":["0x<96 hex characters>"]}'
```

{% hint style="info" %}
The `shielded` API is part of the default `safe` set, so `public_rpc_apis = "safe"` exposes it. You can also list it on its own (`"shielded"`). Light nodes do not serve it. Server limits apply as for every other namespace; see [RPC and APIs](../architecture/rpc-and-apis.md).
{% endhint %}
