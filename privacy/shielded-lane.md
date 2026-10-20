---
description: How shielded transactions travel in blocks, how they are verified and executed, and what they cost.
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

# The shielded lane

Shielded transactions have no sender, nonce, signature or gas, so they do not fit in the account transaction list. They have their own lane: in the transaction pool, in the block, on the wire and in execution.

## Parameters

| Parameter | Default | Config option |
| --- | --- | --- |
| Activation height | inactive (`u64::MAX`) | `shielded_activation_height` |
| Slot length | 20 epochs | `shielded_slot_epochs` |
| Transactions per block section | 8 | `shielded_max_txs_per_block` |
| Anchor window | 100,000 epochs | — |
| Fee per transaction | 197,049 × 100 Gmazzy ≈ **0.0197 MAZZE** | — |
| Shielded chain ID | the chain's ID | `shielded_chain_id` |

The fee is constant. Every transaction has the same weight: a 441-byte body plus the largest proof (192 KiB), 197,049 units in total, priced at 100 times the native minimum base price. The fee is **burned in full**.

## The block section

A block is encoded as `[header, transactions]`, or `[header, transactions, shielded]` when it carries shielded bodies. An empty section has one valid form, absent, so blocks without shielded transactions keep their old encoding and hash.

* **No new header field.** When the section is non-empty, `transactions_root` becomes `keccak(domain ‖ account_root ‖ shielded_root)`.
* **Slot heights only.** A block may carry a section only at a height `h ≥ activation_height` with `h % slot_epochs == 0`.
* **Shielded gas is zero.** Shielded transactions are not charged in gas, and a block that charges shielded gas is invalid.

### The witness sidecar

Proofs are not part of the bodies. They travel as a witness, one proof per body, in the network encoding only: `[header, transactions, shielded, witness]`, compact blocks included.

* The block database never stores the proofs inside blocks. A separate MDBX column, `ShieldedWitness`, keyed by `height ‖ hash`, keeps them, and every node prunes them an era behind the stable checkpoint.
* A node does not serve a block whose witness it has lost.
* Packet size limits count the proofs.

## The pool lane

The transaction pool keeps shielded transactions apart from account transactions, keyed by body hash, with an index of the nullifiers they spend. Admission checks:

| Refusal | Meaning |
| --- | --- |
| `Inactive` | The lane is not active yet |
| `Duplicate` | Already in the pool |
| `Conflict` | A pooled transaction already spends one of its nullifiers |
| `WrongFee` | The fee is not the constant fee |
| `InvalidProof` | The proof does not verify against the body |
| `Spent` | A nullifier is already spent on chain |
| `UnknownAnchor` | The anchor is not a recorded root inside the window |
| `Full` | The lane is full |

At slot heights the block generator packs shielded transactions in random order.

## Relay: Dandelion++

Shielded transactions are relayed with Dandelion++, in the `ShieldedTransactions` message (`0x25`), sent only while the lane is active.

* **Stem.** A transaction travels one peer at a time. Each hop forwards it to its current stem successor, kept for 10 minutes.
* **Fluff.** At each hop, with probability 0.1, the transaction switches to an ordinary broadcast.
* **Embargo.** A node that relays a stem transaction sets a timer of 30 to 60 seconds. If it has not seen the transaction broadcast by then, because a peer swallowed it, it broadcasts the transaction itself.

The node a transaction came from is then not the first to broadcast it, which defeats "first spy" origin detection. It does not hide the transaction from someone watching that node's own uplink.

## Stage A: verification at block acceptance

`verify_sync_graph_block_basic` runs these checks before a block enters the sync graph:

1. the slot rule and the number of shielded transactions;
2. the exact constant fee;
3. distinct nullifiers across the section;
4. every proof, through `verify_body`: pool version, proof system, proof length cap, `proof_hash`, canonical decoding, then the STARK against public values built from the body.

A proof that does not match its body's `proof_hash` is the sending peer's fault, and the block is requested again. Any other failure makes the block invalid. Blocks re-read from the node's own database skip proof verification. No verification result is cached.

## Stage B: execution

The shielded engine runs on the pivot block of each slot epoch, after the account transactions. For each body, it checks every rule before it writes anything, so a transaction applies entirely or not at all:

1. a shield-in has a deposit credit for its body hash, exactly equal to its `v_public_in`;
2. the anchor is a recorded root inside the window;
3. neither nullifier is spent;
4. the backing covers the shield-out and the fee;
5. the tree has room for two more leaves.

Then it marks the nullifiers spent, appends the two commitments, records the new root, consumes the deposit credit or pays the shield-out, and burns the fee from the backing. Burned shielded fees count in the same total as burned base fees (`mazze_getFeeBurnt`). Stage B never needs the proof.

A transaction that fails a rule is **skipped**, with no state change. The outcome of each transaction (applied with its two tree positions, or skipped with a reason) is kept per block for wallets.

| Skip reason | Meaning |
| --- | --- |
| `NoDeposit` | A shield-in without a matching deposit credit |
| `UnknownAnchor` | The anchor is unknown or outside the window |
| `Spent` | A nullifier was already spent |
| `Backing` | The backing does not cover the shield-out and fee. Never expected. |
| `TreeFull` | The commitment tree is full |

## The shield-in bridge

A shielded body has no signature, so it cannot debit an account. A deposit therefore takes two transactions:

1. A signed native transaction calls `shieldIn(bytes32 bodyHash)` on the bridge at `0x0888…09`, with the amount as its value. The value joins the backing and a credit for `bodyHash` is recorded. The call fails before activation, for a zero value, or for a value of 2⁶⁴ or more.
2. The shielded transaction with that body hash consumes the credit when its slot executes.

`deposit(bytes32)` returns the credit recorded for a body hash. A shield-out needs no bridge call: the engine pays `v_public_out` from the backing to the destination, in the native space or in eSpace.
