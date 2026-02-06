# Deploying Smart Contracts on Mazze Testnet

Mazze supports EVM-compatible development workflows, but test configuration must come from your current RPC environment.

## Before deploying

1. Ensure node/RPC are running: [Setup Guide](setup-guide.md), [RPC Guide](rpc.md).
2. Verify chain responsiveness:

```bash
./run/mazze-cli.sh status
```

3. Query EVM chain id from active RPC before hardcoding it in tooling:

```bash
curl -s http://127.0.0.1:58545 \
  -H 'content-type: application/json' \
  --data '{"jsonrpc":"2.0","id":1,"method":"eth_chainId","params":[]}'
```

## Hardhat example (environment-driven)

```javascript
require('@nomicfoundation/hardhat-toolbox');

module.exports = {
  solidity: '0.8.24',
  networks: {
    mazze: {
      url: process.env.MAZZE_RPC_URL,
      accounts: [process.env.PRIVATE_KEY],
      chainId: Number(process.env.MAZZE_CHAIN_ID),
    },
  },
};
```

Use environment variables from your active node deployment, not old static docs values.

## Recommended workflow

- Build and deploy as usual with Hardhat/Foundry/Truffle.
- Use [RPC Guide](rpc.md) for JSON-RPC method checks.
- Use [Mazze CLI](mazze-cli.md) to inspect balances/receipts quickly.
