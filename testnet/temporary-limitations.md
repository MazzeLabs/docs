---
description: Known constraints and open issues in the current development phase.
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

# Temporary limitations

This page tracks known constraints in the Zurich development phase.

## Operations

* Logging is at DEBUG level, so logs grow quickly.
* Behaviour differs between modes (`dev` and the PoW modes).
* Dev mode can use custom intervals (`dev_block_interval_ms`). Do not treat it as production throughput.
* Mining depends on the config: `mining_author`, `mining_type` and the Stratum settings.
* A node does not mine with fewer than two peers, except in dev mode.

## Features not active yet

* **Shielded space.** Implemented on the `shielded-space` branch and working on a local devnet. Inactive on public networks until an activation height is set. `shielded_getStatus` reports `active: false` until then.

## Open issues

| Area | Issue |
| --- | --- |
| eSpace | After a contract creation through the live cross-space bridge, `eth_getCode` can return empty: the account has the right `code_hash`, but the code-by-hash entry is missing. Direct eSpace deployments are not affected. |
| RPC | A per-request timeout is not in place yet. Server limits and throttling bound the load a client can cause. |
| Executor tests | Four behavioural-drift tests are ignored while storage-collateral accounting is reviewed. They are not new regressions. |

## While you test

* Watch the logs: [Viewing logs](viewing-logs.md).
* Keep `run/hydra.toml` and `run/log.yaml` under version control.
* Recreate containers after a config change:

```bash
sudo docker compose up -d --force-recreate
```

* Check chain progress with RPC or the CLI: `mazze_getStatus`, `./run/mazze-cli.sh summary`.
