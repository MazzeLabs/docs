# Rewards and fees

Rewards are computed per epoch and distributed to block authors.

## Reward components
- Base reward from the block-height halving schedule.
- Outlier penalty reduction for outlier blocks.
- Transaction fees distributed to packing authors.
- Burned fees removed from issued supply accounting.

Blocks marked partial invalid receive no reward.

## Explicit net issuance logic
At reward settlement, native supply is adjusted by net mint:

`net_issuance_epoch = total_base_reward_epoch - burnt_fee_epoch`

- If positive, `total_issued` increases by that delta.
- If negative, `total_issued` decreases by the absolute delta.

This is why supply can be deflationary in epochs where burn exceeds mint.

## Fee and burn model
Mazze tracks burned fee paths during execution and in global stats:
- MIP-1559 burn is recorded and subtracted from issued supply.
- Additional burn paths (for example contract-balance burn on specific
  destruction flows) also reduce issued supply.

## Reward execution flow
1. Consensus determines reward epoch and block set.
2. `ConsensusExecutor` gathers reward execution inputs.
3. `process_rewards_and_fees` computes per-block rewards and fees.
4. Burn and mint are netted into issued-supply accounting.
5. Results are persisted in `BlockDataManager`.

## Key source files
- `crates/mazzecore/core/src/consensus/consensus_inner/consensus_executor/mod.rs`
- `crates/mazzecore/core/src/consensus/consensus_inner/consensus_executor/epoch_execution.rs`
- `crates/mazzecore/executor/src/state/state_object/reward.rs`
- `crates/client/src/rpc/impls/mazze/mazze_handler.rs`
