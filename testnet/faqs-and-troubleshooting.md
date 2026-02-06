# FAQs and Troubleshooting

## FAQs

### Q1: What is the current block cadence target?

**A:** Current operational target in this docs set is **4 BPS**. Effective cadence can vary by mode and network conditions.

### Q2: What is the fastest supported setup path?

**A:** Docker Compose (`sudo docker compose up -d`) from [Setup Guide](setup-guide.md).

### Q3: How do I control mining behavior?

**A:** Configure `run/hydra.toml` using `mining_type` (`stratum`, `cpu`, `disable`), `mining_author`, and stratum fields. See [Mining Guide](mining.md).

### Q4: How do I inspect chain health quickly?

**A:** Run:

```bash
./run/mazze-cli.sh status
./run/mazze-cli.sh summary
```

and use `mazze_getStatus` from [RPC Guide](rpc.md).

### Q5: Which section is canonical for privacy implementation?

**A:** `privacy/` is canonical.

## Troubleshooting

### Issue 1: Node starts but chain does not advance

- Confirm RPC responds (`./run/mazze-cli.sh status`).
- If mining is expected, verify `mining_author` and `mining_type`.
- In stratum mode, confirm `stratum_secret`, miner connectivity, and worker logs.

### Issue 2: Miner running but no accepted work

- Check node and miner logs ([Viewing Mazze Logs](viewing-logs.md)).
- Confirm `stratum_address`, `stratum_port`, and secrets match.
- Validate thread settings (`NUM_THREADS`, `RANDOMX_FULL_MEM`) where relevant.

### Issue 3: CLI commands fail

- Verify `RPC_URL` points to active endpoint.
- Ensure HTTP RPC is enabled in `run/hydra.toml`.
- Check if local-only RPC port is used by your setup.

### Issue 4: Config changes have no effect in Docker

Apply config by recreating containers:

```bash
sudo docker compose up -d --force-recreate
```
