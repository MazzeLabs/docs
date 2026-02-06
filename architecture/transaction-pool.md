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
supports two "spaces" (native and EVM).

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

## Space-aware packing
Mazze uses `SpaceMap` for dual spaces:
- Native space is always packable.
- EVM space is packable only after the configured transition height.

The pool tracks gas usage per space and enforces per-space limits during block
validation.

## Key source files
- `crates/mazzecore/core/src/transaction_pool/mod.rs`
- `crates/mazzecore/core/src/transaction_pool/transaction_pool_inner.rs`
- `crates/mazzecore/packing-pool/src/pool.rs`
- `crates/mazzecore/packing-pool/src/packing_batch.rs`
