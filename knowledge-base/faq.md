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

# FAQ

### <mark style="color:orange;">What is Mazze at a technical level?</mark>

Mazze is a PoW blockchain with a DAG-based structure (DETS in consensus), epoch-based execution, and native + EVM transaction spaces.

### <mark style="color:orange;">What is the current block production cadence?</mark>

Current operational docs use **4 BPS** (4 blocks per second) as the network target. In local dev mode, cadence can differ based on `dev_block_interval_ms` and configuration.

### <mark style="color:orange;">Is "1 block per second" still correct?</mark>

No. That value is outdated and has been replaced in this documentation set.

### <mark style="color:orange;">What consensus/mining model is used?</mark>

Mazze uses Proof of Work with RandomX hashing. Mining can run in `stratum`, `cpu`, or `disable` mode, configured in `run/hydra.toml`.

### <mark style="color:orange;">How do I run a node quickly?</mark>

Use Docker Compose (recommended in the [Setup Guide](../testnet/setup-guide.md)),
configure `run/hydra.toml`, then start with:

```bash
sudo docker compose up -d
```

### <mark style="color:orange;">How do I mine on Mazze?</mark>

Set `mining_author`, choose `mining_type` (`stratum` or `cpu`), and run
node/miner per the [Mining Guide](../testnet/mining.md).

### <mark style="color:orange;">Does Mazze have privacy features today?</mark>

Yes. Privacy is implemented via a shielded pool internal contract with proof-verified shielded transactions.

### <mark style="color:orange;">Which proof system is currently implemented in privacy?</mark>

The current privacy implementation uses **Groth16 over BLS12-381** with a Poseidon Merkle tree.

### <mark style="color:orange;">Where is privacy documentation maintained now?</mark>

Privacy documentation is maintained in the **Privacy** section:
[Overview](../privacy/overview.md), [Shielded Pool](../privacy/shielded-pool.md),
and [Shielded Transactions](../privacy/transactions.md).

### <mark style="color:orange;">Where should I manage wallets and transfers?</mark>

Use `./run/mazze-cli.sh` (Mazze CLI) for wallet creation/import, balance checks, transfers, and shielded operations.

### <mark style="color:orange;">Where can I find RPC details?</mark>

Use the [RPC guide](../testnet/rpc.md) for endpoints, namespaces, and examples.

### <mark style="color:orange;">Where are logs stored?</mark>

For source builds: `run/logs/`.
For Docker: `docker logs -f mazze-node` and `docker logs -f mazze-miner`.

### <mark style="color:orange;">What are the current core tokenomics values?</mark>

- Wrapped MAZZE on Ethereum: 4,900,000,000
- Native genesis issuance: 3,900,000,000
- Mining target: 2,500,000,000
- Theoretical native upper bound: 6,400,000,000

### <mark style="color:orange;">Where should I start reading now?</mark>

- [Architecture](../architecture/README.md)
- [Privacy](../privacy/README.md)
- [Tokenomics](../tokenomics/overview.md)
- [Setup Guide](../testnet/setup-guide.md)
- [Mazze CLI](../testnet/mazze-cli.md)
- [Mining Guide](../testnet/mining.md)
