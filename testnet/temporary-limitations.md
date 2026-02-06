# Temporary Limitations

This page tracks current operational caveats for the Zurich development phase.

## Known constraints

- Logging verbosity is higher (DEBUG), so log size grows quickly.
- Behavior can differ across modes (`dev` vs normal PoW modes).
- Dev mode may use custom intervals (`dev_block_interval_ms`) and should not be treated as production throughput.
- Mining availability depends on config (`mining_author`, `mining_type`, stratum settings).

## What to do during testing

- Monitor logs continuously ([Viewing Mazze Logs](viewing-logs.md)).
- Keep config under version control (`run/hydra.toml`, `run/log.yaml`).
- Recreate containers after config changes:

```bash
sudo docker compose up -d --force-recreate
```

- Validate chain progress with RPC/CLI (`mazze_getStatus`, `./run/mazze-cli.sh summary`).

## Cadence note

Current operational target used in docs is **4 BPS**, but effective observed cadence can vary with network conditions and selected mode.
