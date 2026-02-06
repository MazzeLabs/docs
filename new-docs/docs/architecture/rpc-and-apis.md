# RPC and APIs

Mazze exposes a JSON-RPC interface over HTTP, WebSocket, and TCP. Handlers are
implemented in the `client` crate and call into consensus and storage.

## Namespaces
- `mazze_*` - core chain queries, blocks, receipts, balances, logs, and DAG
  tips.
- `debug_*` - execution tracing and diagnostics.
- `trace_*` - transaction and block traces.
- `txpool_*` - pending pool status and contents.

## Query path
Most RPCs resolve through:
- `ConsensusGraph` for chain/epoch context.
- `BlockDataManager` for headers, receipts, and rewards.
- State DB for balances, storage, and contract code.

## Configuration
RPC ports and limits are configured in `client/src/configuration.rs`, including
HTTP/WS/TCP ports, thread counts, and max payload sizes.

## Key source files
- `crates/client/src/rpc/impls/mazze/mazze_handler.rs`
- `crates/client/src/rpc/impls/mazze/common.rs`
- `crates/client/src/rpc/traits/mazze_space/mazze.rs`
- `crates/client/src/configuration.rs`
