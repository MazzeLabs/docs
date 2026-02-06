# Getting Started with Mazze Testnet

This quick start is aligned with [Setup Guide](setup-guide.md).

## Fast path (Docker recommended)

1. Edit `run/hydra.toml`:
   - `public_address = "<your-public-ip>"` (or leave empty for auto-detect).
   - `mining_author = "<your-base32-mazze-address>"` (optional; required for mining).
2. Start services:

```bash
sudo docker compose up -d
```

3. Check logs:

```bash
sudo docker compose logs node | tail -n 200
sudo docker compose logs miner | tail -n 200
```

4. Verify node ID:

```bash
sudo docker compose logs node | grep "Self node id:" | tail -n 1
```

5. Open CLI and verify status:

```bash
./run/mazze-cli.sh status
./run/mazze-cli.sh summary
```

## Next steps

- Wallet operations: [Mazze CLI](mazze-cli.md)
- Mining configuration: [Mining Guide](mining.md)
- RPC checks and integration: [RPC Guide](rpc.md)
- Log monitoring: [Viewing Mazze Logs](viewing-logs.md)
