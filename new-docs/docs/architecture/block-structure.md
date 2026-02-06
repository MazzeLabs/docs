# Block structure

Mazze blocks are encoded as a header plus a list of signed transactions. The
header carries both DAG topology information (parent + referees) and execution
outputs (deferred roots).

## Header fields (BlockHeader)
- `parent_hash` - parent edge in the tree portion of DETS.
- `height` - block height on the main chain (epoch height).
- `timestamp` - unix time used for ordering and PoW checks.
- `author` - miner/producer address.
- `transactions_root` - MPT root of transaction hashes.
- `deferred_state_root` - state root after deferred epoch execution.
- `deferred_receipts_root` - receipts root for the executed epoch.
- `deferred_logs_bloom_hash` - bloom for logs in the executed epoch.
- `blame` - count of ancestors whose deferred roots are incorrect, used for
  light verification and reward logic.
- `difficulty` - PoW difficulty for the block.
- `adaptive` - WLSR adaptive flag used by consensus weighting.
- `gas_limit` - block gas limit used by packing and verification.
- `referee_hashes` - extra DAG edges referencing other blocks.
- `custom` - custom bytes used for fork markers and protocol transitions.
- `nonce` - PoW nonce.
- `base_price` - per-space base fee (native and EVM).

## Deferred roots and epochs
Execution is deferred by a fixed number of epochs to reduce reorg churn. The
header of block N carries roots computed from earlier epoch execution, which is
why these fields are labeled "deferred".

## Block body
The body is a vector of `SignedTransaction`. The canonical `Block` encoding
includes transactions without sender/public fields (RLP of
`TransactionWithSignature`), while helper encoders can include the public key
when needed for RPC or sync.

## Compact blocks
`CompactBlock` is used for efficient block relay. It includes short IDs derived
from a random nonce, so peers can reconstruct the full block from their mempool.

## Key source files
- `crates/primitives/src/block_header.rs`
- `crates/primitives/src/block.rs`
- `crates/mazzecore/core/src/verification.rs`
