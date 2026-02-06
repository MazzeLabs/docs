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

# Inflation

Inflation is now modeled in the broader **native issuance** accounting and is fully documented in [Issuance](issuance.md).

### <mark style="color:orange;">Current Rule</mark>

`native_total_issued(t) = genesis_issued + mined_to_date(t) - burnt_to_date(t)`

So inflation cannot be evaluated only from mined rewards; burn paths are part of net issuance.

### <mark style="color:orange;">Current Baseline</mark>

* Native genesis issuance: **3,900,000,000 MAZZE**
* Mining target: **2,500,000,000 MAZZE**
* Theoretical native upper bound: **6,400,000,000 MAZZE**

### <mark style="color:orange;">Where to Read Full Details</mark>

* [Issuance](issuance.md)
* [Bridge Liquidity](bridge-liquidity.md)
