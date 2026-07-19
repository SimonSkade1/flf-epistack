---
type: hypothesis-cluster
id: HC-1
hypotheses:
  - "[[H-3 - Direct predation by arriving humans drove the extinction]]"
  - "[[H-11 - Indirect human impact through burning and habitat transformation drove the extinction]]"
  - "[[H-21 - Climate-driven aridification drove the extinction]]"
  - "[[H-42 - Some driver not listed above dominated]]"
exclusivity: "each names a different dominant driver of one extinction pulse; at most one can have dominated"
exhaustive_by_construction: false
independence: "the sole cluster in this demo; its prior factorizes trivially — a real run would state why the driver question is independent of, e.g., the arrival-chronology cluster"
depends_on: []
question: "What was the dominant driver of the Sahul megafauna extinction pulse (~45-40 ka)?"
relevance: "this cluster is essentially the main question restated as a mutually-exclusive answer set"
external_consensus: "the field currently leans toward a human-climate synergy with humans as the proximate trigger; recorded here for step 9-10 comparison, mixed into no weight below"
---

The top-level map of the analysis: one sub-question, four mutually-exclusive answers, ordered by id with the residual last. The order below is the **vector index** every prior and likelihood addresses members by — frozen at step 4.

![[H-3 - Direct predation by arriving humans drove the extinction]]

![[H-11 - Indirect human impact through burning and habitat transformation drove the extinction]]

![[H-21 - Climate-driven aridification drove the extinction]]

![[H-42 - Some driver not listed above dominated]]

## Carving

1. **Exclusive.** Each member names a *different* dominant driver of a single pulse; the question is which one dominated, so at most one holds. A synergy in which two drivers genuinely co-dominate is not expressible here — that limitation is flagged in [[CR-1 - Review of HC-1, dominant driver of the extinction pulse]].
2. **Not exhaustive by construction**, so [[H-42 - Some driver not listed above dominated]] (residual, last) closes the space: "some driver outside this framing, or a combination no member captures."
3. **Discriminability held H-3 and H-11 apart.** They share the human-arrival trigger but [[O-22 - Three megafauna genera persist more than 5 kyr after first human arrival]] separates them, so they are distinct members, not a merge.

## Prior

```python
# HC-1 prior — dominant driver of the Sahul megafauna extinction pulse. Members in HC-1.hypotheses order.
# Numbers illustrative and uncalibrated; each weight is a Fermi product with its reason on the line.
p_human_broad = 0.62          # across island/continental megafaunal first-contact faunas, arrival-linked
                              # collapse is the modal outcome — base rate for "a human driver at all"
# H-3 direct predation: the human branch, kill-off leading edge.
p_direct_given_human = 0.35   # share of human-driven cases led by direct predation rather than habitat
                              # change; naive-prey systems favour it, but Sahul's slow-breeding taxa cut against a pure kill-off
w_H3 = p_human_broad * p_direct_given_human
# H-11 indirect human impact: the human branch, habitat-squeeze pathway (complement within the branch).
p_indirect_given_human = 0.65 # fire-driven habitat change is the better-evidenced human pathway on this continent
w_H11 = p_human_broad * p_indirect_given_human
# H-21 climate aridification: a driver independent of arrival.
p_climate_base = 0.45         # climate-only megafaunal collapses do occur; base rate before argument A-31
arg_A31_discount = 0.62       # A-31 (approved, prior-shaping): no comparable pulse at earlier, equally-arid
                              # terminations lowers a climate-only prior — a discount, not zero (earlier terminations are poorly dated)
w_H21 = p_climate_base * arg_A31_discount
# H-42 residual: a driver outside the human/climate framing (disease, trophic cascade) or an unmodelled combination.
w_residual = 0.10             # how often questions framed this tightly as human-vs-climate miss the driver
                              # entirely; argued base rate, NOT one minus the others
prior("HC-1", [w_H3, w_H11, w_H21, w_residual])
```

Weights `[0.217, 0.403, 0.279, 0.100]` → prior `[0.22, 0.40, 0.28, 0.10]`. Override any factor and re-run to price it, e.g. `--set HC-1:arg_A31_discount=1.0` removes the earlier-terminations argument and lifts the climate share.
