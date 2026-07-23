---
type: argument
id: "A-5"
status: approved
reason_if_not_false: checked
statement: "Both lineage A and lineage B established sustained human transmission without requiring adaptive mutations, implying the progenitor was already efficiently human-transmissible in its animal reservoir and making multiple independent zoonotic spillovers from that reservoir plausible."
source: "[[S-1 - Pekar et al. 2022 — molecular epidemiology of multiple zoonotic origins of SARS-CoV-2]]"
locator: "Discussion"
affects_hypotheses: ["[[H-5 - Early A-B diversity reflects two or more separate zoonotic introductions, not one]]"]
---
If two independently introduced lineages both achieved sustained spread with no shared adaptive changes, then human-transmissibility did not have to evolve after the jump; it pre-existed in the source population. A reservoir carrying already-human-capable virus makes repeated spillover a series of Bernoulli trials rather than a singular fluke: the authors estimate about eight introductions (95% HPD 2-23), most going extinct (77.8% of simulated introductions), were needed to yield the two that established. This raises the prior on two-or-more successful zoonotic introductions relative to a scenario requiring a single unique jump.

## Validity verdict

status: approved; reason_if_not_false: checked.

Chain: (a) both lineages spread with no shared adaptive changes → (b) human-transmissibility pre-existed the jump rather than evolving in humans → (c) with a pre-adapted source and repeated human-reservoir contact, each contact is a Bernoulli trial, so multiple successful introductions become plausible → (d) prior on two-or-more introductions rises relative to a single unique jump. Traced myself: (a)→(b) holds on the premise as granted; (c) is the substantive move, and it checks out probabilistically — a higher per-contact success probability p increases the ratio P(>=2 successes)/P(exactly 1) across many trials, so pre-adaptation does specifically raise multiple-vs-single, not just overall spillover odds. This is scored against H-5 (number of introductions), where the inference holds. Noted defeater for the record, not load-bearing for this scope: "no in-human adaptation needed" is symmetric between an animal reservoir and a lab-passaged/pre-adapted source, so the "animal reservoir" wording does not by itself discriminate zoonosis from lab origin — but that bears on step 8's cross-hypothesis pricing, not on whether the single-vs-multiple inference is valid. Holds as stated.
