# Feedback and Reporting Issues

Accurate reports are critical for node/miner/RPC stability.

## What to include in every report

- Environment: Docker or source build
- Config context: relevant `run/hydra.toml` fields (sanitize secrets)
- Exact command executed
- Full error output
- Time range of issue
- Node ID (if available)

## Required logs

### Docker

```bash
docker logs -f mazze-node
docker logs -f mazze-miner
```

### Source build

```bash
tail -n 300 run/logs/mazze-node.log
tail -n 300 run/logs/mazze-miner.log
```

## Useful diagnostic checks

```bash
./run/mazze-cli.sh status
./run/mazze-cli.sh summary
```

And RPC status call from [RPC Guide](rpc.md).

## Where to report

Use the official Mazze support/community channels and include the full context above so issues can be reproduced quickly.
