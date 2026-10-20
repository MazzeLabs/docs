---
description: Short answers to the questions we hear most.
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

# FAQ

## The chain

<details>

<summary>What is Mazze at a technical level?</summary>

A Proof-of-Work layer 1 whose blocks form a DAG. Consensus (DETS) orders the blocks into epochs, and execution runs epoch by epoch. One chain carries three spaces: Native, eSpace (EVM) and Shielded. See [Three spaces](../overview/three-spaces.md).

</details>

<details>

<summary>What is the block rate?</summary>

The operational target is **4 blocks per second**. The old "1 block per second" figure is out of date. In dev mode the rate depends on `dev_block_interval_ms`.

</details>

<details>

<summary>What consensus and mining model does Mazze use?</summary>

Proof of Work with RandomX. Mining runs in `stratum`, `cpu` or `disable` mode, set in `run/hydra.toml`.

</details>

<details>

<summary>Is Mazze compatible with Ethereum?</summary>

Yes, in eSpace. It runs on revm 40 with the Prague spec and passes all 34,036 Ethereum state tests. MetaMask, Foundry and Hardhat work as usual. See [EVM compatibility](../developers/evm-compatibility.md).

</details>

## Privacy

<details>

<summary>Does Mazze have privacy features?</summary>

Yes. The **shielded space** keeps payments private: owners and amounts are hidden, and only shield-in and shield-out amounts are public. It works end to end on devnet and will be activated on public networks at a set height. See [Shielded space](../privacy/README.md).

</details>

<details>

<summary>Which proof system does the shielded space use?</summary>

**PS-1**, a STARK built with Plonky3 over the KoalaBear field, with FRI and Keccak-256, at 128 bits of proven soundness. It needs no trusted setup and rests only on hash functions, so it is post-quantum. See [Proof system PS-1](../privacy/proof-system.md).

</details>

<details>

<summary>What happened to the Groth16 pool?</summary>

It is superseded. The audit rated its single trusted setup Critical: a leaked trapdoor would allow silent minting. The shielded space removes the trusted setup. The old pool is documented under [Legacy pool](../privacy/legacy-pool.md).

</details>

<details>

<summary>Can someone who sent me a note spend it?</summary>

No. Spending a note needs the owner's spend key `nsk`, which only the recipient's wallet holds. The sender knows the note's contents, not the key.

</details>

<details>

<summary>How do I back up a shielded wallet?</summary>

Keep the 32-byte seed. `restore` rebuilds every self-note (change, shield-ins and claims) from it. Run `claim` after receiving a payment, so that the received value becomes a self-note too. See [Wallet guide](../privacy/wallet.md#back-up-and-restore).

</details>

## Running a node

<details>

<summary>How do I run a node quickly?</summary>

Use Docker Compose, as in the [setup guide](../testnet/setup-guide.md). Configure `run/hydra.toml`, then:

```bash
sudo docker compose up -d
```

</details>

<details>

<summary>How do I mine?</summary>

Set `mining_author`, choose `mining_type` (`stratum` or `cpu`), and start the node and the miner as in the [mining guide](../testnet/mining.md).

</details>

<details>

<summary>Where are the logs?</summary>

Source builds write to the repository-root `logs/` directory. With Docker, use `docker logs -f mazze-node` and `docker logs -f mazze-miner`. See [Viewing logs](../testnet/viewing-logs.md).

</details>

<details>

<summary>My upgraded node will not start. Why?</summary>

The genesis block hash changed. Wipe the local chain state and start again. If the node complains about a missing snapshot parent, the error names the snapshot and the setting to check, `keep_snapshot_before_stable_checkpoint`.

</details>

<details>

<summary>Where do I manage wallets and transfers?</summary>

For native and eSpace accounts, use the Mazze CLI, `./run/mazze-cli.sh`. See [Mazze CLI](../testnet/mazze-cli.md). For the shielded space, use `mazze-shielded-wallet`.

</details>

<details>

<summary>Where can I find RPC details?</summary>

In the [RPC guide](../testnet/rpc.md) (ports, examples, method list) and [RPC and APIs](../architecture/rpc-and-apis.md) (namespaces, allowlists, limits).

</details>

## Token

<details>

<summary>What are the core tokenomics values?</summary>

* Wrapped MAZZE on Ethereum: 4,900,000,000
* Native genesis issuance: 3,900,000,000
* Mining target: 2,500,000,000
* Theoretical native upper bound: 6,400,000,000

See [Tokenomics](../tokenomics/overview.md).

</details>

<details>

<summary>Are fees burned?</summary>

Base fees are burned, MIP-1559 style. Shielded transactions pay one constant fee, and it is burned in full. `mazze_getFeeBurnt` returns the cumulative burned amount.

</details>
