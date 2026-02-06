# Shielded transactions

Shielded transfers are encoded as native transactions with a special payload
that targets the shielded pool contract.

## Transaction type
- Shielded transactions are represented as
  `TypedNativeTransaction::Shielded`.
- The payload (`data`) contains the encoded shielded proof and bundle inputs.

## Validation rules
The verifier enforces these constraints for shielded transactions:
- The transaction must be unsigned.
- The action must be `Call` to the shielded pool address.
- `value` must be zero (transfers happen inside the pool).
- `gas_price` must be zero (the proof includes a fee field).
- The payload must not be empty.

The RPC call request builder also enforces recipient, value, and payload checks
before building a shielded transaction.

## Sender derivation
Shielded transactions are unsigned. The node derives a synthetic sender address
from the transaction hash (`SignedTransaction::new_shielded`).

## Transaction pool behavior
- Shielded transactions are stored in a dedicated `shielded_pool` map (no nonce
  ordering).
- The packer selects shielded transactions after packing normal native and EVM
  transactions, respecting remaining gas and block size limits.

