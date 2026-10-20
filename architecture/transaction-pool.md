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

# Transaction pool

The transaction pool buffers incoming transactions, verifies them, and produces
a packable set for block generation. It manages per-sender nonce order and
keeps the account transactions of the native space and eSpace apart from the
shielded lane.

## Main components
- `TransactionPool` - public API, ties to data manager and executed state.
- `TransactionPoolInner` - core data structures and packing logic.
- `DeferredPool` - per-sender nonce pools plus a packing pool.
- `PackingPool` - randomized packing algorithm with gas/price weighting.
- `AccountCache` - keeps nonce and balance hints for validation.

## Intake and validation flow
1. RPC/P2P submits a `SignedTransaction`.
2. `VerificationConfig` and `Machine` checks validate chain id, gas bounds,
   epoch bounds, and signature.
3. Transaction is inserted into the sender's `NoncePool`.
4. Ready contiguous nonces are mirrored into the `PackingPool`.

## Packing model
- Transactions are grouped per sender into `PackingBatch` objects to preserve
  nonce order.
- `PackingPool` is a treap-based structure that supports randomized sampling.
- Sampling considers block gas limits, block size limits, and minimum gas price.
- For EIP-1559 style pricing, the pool estimates the next base price using
  `compute_next_price` and adjusts the packing gas limit accordingly.

## Per-peer limits
Each peer may hold at most `max_trans_count_per_peer_normal` transactions in
the pool (default 500,000). Transactions beyond the cap are rejected and
counted.

## Space-aware packing
Mazze uses `SpaceMap`, with one slot per space:
- Native space is always packable.
- EVM space is packable only after the configured transition height.

The pool tracks gas usage per space and enforces per-space limits during block
validation.

## Shielded lane
Shielded transactions have no sender, nonce or gas, so they live in their own
lane, keyed by body hash, with an index of the nullifiers they spend.

- Admission checks the lane is active, the constant fee, the proof, the anchor,
  and that no nullifier is spent on chain or by another pooled transaction.
- The block generator packs them only at slot heights, in random order, up to
  `shielded_max_txs_per_block` per block.
- They are relayed with Dandelion++ (see [Networking](networking.md)).

Details are in [The shielded lane](../privacy/shielded-lane.md#the-pool-lane).

## Key source files
- `crates/mazzecore/core/src/transaction_pool/mod.rs`
- `crates/mazzecore/core/src/transaction_pool/transaction_pool_inner.rs`
- `crates/mazzecore/core/src/transaction_pool/shielded.rs`
- `crates/mazzecore/packing-pool/src/pool.rs`
- `crates/mazzecore/packing-pool/src/packing_batch.rs`
