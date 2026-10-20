---
description: The JSON-RPC namespaces, transports, allowlists and server limits.
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

# RPC and APIs

Mazze serves JSON-RPC over HTTP, WebSocket and TCP. The handlers live in the `client` crate and call into consensus and storage. The server layer is **jsonrpsee 0.26** on tokio 1; method names, pub-sub subscriptions and error codes are the same as before the migration.

## Namespaces

| Namespace | Space | Contents |
| --- | --- | --- |
| `mazze_*` | Native | Chain queries, blocks, receipts, balances, logs, DAG tips, status |
| `eth_*`, `net_version` | eSpace | The Ethereum JSON-RPC API |
| `shielded_*` | Shielded | Status, sections, nullifiers, raw transaction submission. See [Shielded RPC](../privacy/rpc.md). |
| `debug_*`, `trace_*` | Native and eSpace | Execution tracing and diagnostics |
| `txpool_*` | Native | Pending pool status and contents |
| `mazze_subscribe`, `eth_subscribe` | Native, eSpace | Pub-sub over WebSocket and TCP |

## Allowlists

| Setting | Default | Sets |
| --- | --- | --- |
| `public_rpc_apis` | `"safe"` | `safe` = `mazze`, `pubsub`, `txpool`, `shielded`. `all` adds `debug` and `trace`. |
| `public_evm_rpc_apis` | `"evm"` | `evm` = `eth`, `ethpubsub`. `ethdebug` can be added. |

The `test_*` namespace is compiled out of release builds.

{% hint style="warning" %}
**Before you expose RPC publicly**, review `run/hydra.toml`. Never set `public_rpc_apis = "all"` on a public bind address. CORS (`jsonrpc_cors`) no longer defaults to `"all"`.
{% endhint %}

## Server limits

Each limit bounds the memory and work a single client can cause. The per-client request rate is limited separately, by throttling.

| Option | Default |
| --- | --- |
| `jsonrpc_max_batch_size` | 1,000 requests per batch |
| `jsonrpc_max_response_bytes` | 25 MiB (HTTP and TCP) |
| `jsonrpc_http_max_connections` | 1,000 |
| `jsonrpc_ws_max_connections` | 100 |
| `jsonrpc_max_subscriptions_per_connection` | 1,024 |
| `jsonrpc_tcp_max_request_bytes` | 5 MiB per request line |

* HTTP request bodies are capped at 5 MiB, and WebSocket payloads at 10 MiB.
* `jsonrpc_http_threads` is a lower bound on the worker threads of the runtime that all RPC servers share.
* HTTP keeps its CORS policy, closes connections unless `jsonrpc_http_keep_alive` is set, and returns `-32090` for subscriptions over HTTP.
* The TCP endpoints speak newline-delimited JSON-RPC.

## Query path

Most RPCs resolve through:

* `ConsensusGraph` for chain and epoch context;
* `BlockDataManager` for headers, receipts and rewards;
* the state DB for balances, storage and contract code.

The eSpace `finalized` block tag maps to the latest checkpoint.

## Key source files

- `crates/client/src/rpc.rs`
- `crates/client/src/rpc/rpc_apis.rs`
- `crates/client/src/rpc/http_common.rs`
- `crates/client/src/rpc/tcp.rs`
- `crates/client/src/rpc/impls/mazze/mazze_handler.rs`
- `crates/client/src/rpc/impls/shielded.rs`
- `crates/util/rpc-error/src/lib.rs`
- `run/hydra.toml`
