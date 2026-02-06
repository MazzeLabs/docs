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

# Node types and light protocol

Mazze supports multiple node types that trade storage for sync cost.

## Node types
- `Archive` - keeps full historical state and receipts.
- `Full` - keeps recent state and snapshots, prunes older history.
- `Light` - relies on witnesses/blame verification and remote state proofs.

The node type is encoded on the wire and affects sync preferences.

## Light protocol
The light protocol provides:
- Block/receipt proofs and witnesses for light clients.
- Peer type validation to avoid incompatible requests.

Light nodes are more conservative about which peers they accept and what data
they trust, using the `blame` field and witness checks.

## Key source files
- `crates/mazzecore/core/src/node_type.rs`
- `crates/mazzecore/core/src/light_protocol/handler/mod.rs`
- `crates/mazzecore/core/src/light_protocol/provider.rs`
- `crates/mazzecore/core/src/consensus/consensus_inner/blame_verifier.rs`
