# How to Add the Mazze Testnet to Metamask

This page has been updated to avoid stale hardcoded values.

## Recommended approach

Use your **current RPC endpoint and chain settings** from your active environment configuration rather than old static values.

- For local development, get RPC ports from `run/hydra.toml`.
- For operational checks, validate connectivity first with [RPC Guide](rpc.md) and [Mazze CLI](mazze-cli.md).

## Steps

1. Open MetaMask and choose **Add network**.
2. Fill network fields using the RPC endpoint and chain ID currently used by your node/environment.
3. Save and switch network.
4. Verify connectivity by sending a read-only call (for example with `eth_chainId` from [RPC Guide](rpc.md)).

## Important

If your environment is updated, network values may change. Always trust active configuration and RPC validation over old screenshots/tutorial constants.
