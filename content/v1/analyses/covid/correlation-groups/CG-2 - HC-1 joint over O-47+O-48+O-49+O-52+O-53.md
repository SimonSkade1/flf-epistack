---
type: correlation-group
id: CG-2
to: "[[HC-1 - Origin of SARS-CoV-2 — natural zoonosis vs research-related incident]]"
members:
  - "[[E-53 - O-47 × HC-1 — DOE low-confidence lab assessment]]"
  - "[[E-54 - O-48 × HC-1 — FBI moderate-confidence lab assessment]]"
  - "[[E-55 - O-49 × HC-1 — split low-confidence IC verdict]]"
  - "[[E-56 - O-52 × HC-1 — FBI director on-record lab assessment]]"
  - "[[E-57 - O-53 × HC-1 — classified low-confidence assessments, DOE independent reasoning]]"
---

Joint likelihood for correlated observations O-47, O-48, O-49, O-52, O-53 (shared basis: D-6). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-2 (HC-1) — ONE joint estimate over members E-53+E-54+E-55+E-56+E-57. All five observations are the SAME
# witness: the US-IC origin assessments, all sourced from S-84 and resting on the classified pool D-6 (rule 1).
# So this is priced as one correlated signal — the DOE low-confidence lab lean (O-47), the FBI moderate-confidence
# lab lean (O-48/O-52 Wray on-record), the split 8-agency verdict (O-49: 2 lab, 4 natural, several unresolved,
# all low confidence), and the classified/low-confidence caveats (O-53) — NOT five independent votes (A-74:
# FBI+DOE share the classified pool, count as materially less than two independent lines).
# Members in HC-1.hypotheses order: [H-41 natural zoonosis, H-42 unmodified-collection leak, H-43 engineered
# leak, H-44 residual]. This is INSTITUTIONAL TESTIMONY on {research bloc H-42/H-43} vs {natural H-41}; the
# "lab incident / lab leak" language is agnostic WITHIN the lab bloc (the IC disclaims engineering evidence,
# while DOE cites "nature of Wuhan research"), so it does NOT discriminate H-42 from H-43 — that split is the
# genome edges' job (CG-4). Anchored on H-41 = 1 (rule 7); the two lab members share one ratio.
lik_ic_H41 = 1.0   # anchor: a true natural origin readily produces exactly this pattern — a body with real
                   # access that still cannot converge and self-rates low/moderate confidence is the signature
                   # of NON-DECISIVE underlying intelligence (A-75), and the capable agencies can lean lab on
                   # circumstantial grounds (Wuhan location, WIV research) even absent a real leak.
lik_ic_H42 = 1.3   # 1.3x as expected as under H-41: a WEAK lab lean. The two lab-leaning agencies (FBI, DOE)
                   # are the most scientifically capable, so competence-weighting lifts their lean above a bare
                   # 2-of-8 headcount (A-73) — but that push is nearly washed out: 4 agencies lean natural, all
                   # low confidence, the lab conclusion is "not conclusive," and the two lab votes are not
                   # independent (A-74). Net a modest tilt, not a strong one.
lik_ic_H43 = 1.3   # same ratio as H-42 (see header): "lab incident" testimony is neutral between an unmodified
                   # collection leak and an engineered leak — the IC has not asserted engineering, so this
                   # signal boosts the whole research bloc together and leaves the H-42/H-43 split untouched.
lik_ic_H44 = 1.15  # residual, unconstrained → middling (rule 3): a fair share of unlisted histories carry a
                   # lab element (e.g. a lab-modified virus escaping into animals then spilling over) that would
                   # also read "lab-ish" to the IC, so it sits between the natural anchor and the lab bloc rather
                   # than at either extreme; setting it at 1.0 would deny any lab-flavored unlisted cause.
t_ic = 0.65        # cap = min trust_score over {O-47,O-48,O-49,O-52,O-53} = 0.72 (all via S-84). The bare FACT
                   # that FBI/DOE hold lab-favoring positions is solid (Wray on record, WSJ→NPR) — 0.72 already
                   # marks down for the assessments being classified/unassessable. Docked a touch further to
                   # 0.65 per A-75: this testimony's ORIGIN-relevance rests on reasoning I cannot inspect, and
                   # DOE's lean leans partly on fragile absence-of-evidence (no host animal found — could reflect
                   # blocked sampling), bounding how far the bare positions carry beyond their face value.
evidence("HC-1", ["O-47", "O-48", "O-49", "O-52", "O-53"], [lik_ic_H41, lik_ic_H42, lik_ic_H43, lik_ic_H44], t=t_ic)
```

`E-53`, `E-54`, `E-55`, `E-56`, `E-57` each carry `group: [[CG-2]]` and no `## Likelihood` block of their own — this node holds the single joint block; Obsidian surfaces it on each edge as a backlink.
