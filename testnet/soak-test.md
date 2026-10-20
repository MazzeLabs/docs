---
description: Drive sustained block production and transaction load, and tune GC and storage from the metrics.
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

# Soak test

The soak harness drives sustained block production and transaction load while it writes metrics for GC and database tuning.

## Run

{% stepper %}
{% step %}
### Build a release binary

```bash
cargo build --release
```
{% endstep %}

{% step %}
### Start the soak node

```bash
TARGET_BPS=8 TX_PERIOD_US=1000 TXGEN_ACCOUNT_COUNT=200 ./run/start-soak.sh
```
{% endstep %}

{% step %}
### Stop it

```bash
kill "$(cat run/soak_pid.txt)"
```
{% endstep %}
{% endstepper %}

## Metrics

Metrics are appended to `logs/metrics-soak.log`. Useful groups:

| Group | Signals |
| --- | --- |
| `sync_graph` | `arena_size`, `old_era_frontier_size`, `not_ready_frontier_size` |
| `consensus_worker_queue` | `queued`, `enq_tps`, `deq_tps` |
| `timer` | `consensus::state_commit_time_expdec.*` |
| `storage_mpt` | `cache_hit_rate_pct`, `cache_misses`, `db_loads` |

## Tuning knobs

| Variable | Default | Controls |
| --- | --- | --- |
| `MDBX_MAP_SIZE_MB` | 65536 | MDBX map size |
| `BLOCK_CACHE_GC_MS` | | Block cache GC period |
| `STORAGE_MAX_OPEN_SNAPSHOTS` | | Open snapshot limit |
| `STORAGE_MAX_OPEN_MPT_COUNT` | | Open MPT limit |
| `STORAGE_DELTA_MPTS_CACHE_SIZE` | | Delta MPT cache size |
| `STORAGE_DELTA_MPTS_CACHE_START_SIZE` | | Delta MPT cache initial size |
| `STORAGE_DELTA_MPTS_SLAB_IDLE_SIZE` | | Delta MPT slab idle size |

## Reading the signals

| You see | It means | Try |
| --- | --- | --- |
| `sync_graph.old_era_frontier_size` climbing steadily | GC is lagging | Lower the BPS or run GC more often |
| `consensus_worker_queue.queued` growing | Consensus backpressure | Lower the transaction rate or add CPU |
| Low `storage_mpt.cache_hit_rate_pct` with high `db_loads` | MPT cache too small | Raise the MPT cache sizes |

## Notes

* `TARGET_BPS` sets `dev_block_interval_ms`. You can also set `BLOCK_INTERVAL_MS` directly.
* `generate_tx` runs only in `dev` and `test` modes. The script sets `mode = "dev"` by default.
* `BOOTNODES` is empty by default, for an isolated run. Set it to join a network.
* `cache_hit_rate_pct` is derived from the access and DB-load counters of the MPT cache.
