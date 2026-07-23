---
type: argument
id: 'A-65'
status: approved
reason_if_not_false: checked
statement: Because an unmodified wild bat virus (BANAL-236) binds human ACE2 with affinity equal to or greater than early SARS-CoV-2 and enters/replicates in human cells, high-affinity human-ACE2 tropism does not require passage or engineering, undercutting the premise that SARS-CoV-2's RBD needed lab adaptation to use hACE2.
source: '[[S-52 - Temmam et al. 2022 Nature — BANAL Laos bat coronaviruses]]'
locator: Results / Discussion
affects_observations:
- '[[O-69 - BANAL RBDs match 15-16 of 17 hACE2-contact residues vs only 11-17 for RaTG13]]'
- '[[O-70 - BANAL RBDs bind human ACE2 ~3x more strongly than early SARS-CoV-2; BANAL-236 RBD-hACE2 crystal near-identical]]'
- '[[O-71 - A wild, unmodified BANAL-236 enters and replicates in human cells via hACE2]]'
affects_hypotheses: ["[[H-41 - Natural zoonotic spillover with no research involvement]]"]
---

Because an unmodified wild bat virus (BANAL-236) binds human ACE2 with affinity equal to or greater than early SARS-CoV-2 and enters/replicates in human cells, high-affinity human-ACE2 tropism does not require passage or engineering, undercutting the premise that SARS-CoV-2's RBD needed lab adaptation to use hACE2.

## Reasoning

A central plank of lab-adaptation arguments is that a bat virus would need to be adapted (by serial passage or engineering) before binding human ACE2 efficiently. Temmam et al. present a counterexample from nature: BANAL-236, isolated from a wild bat with no laboratory manipulation, has an RBD whose 17-residue ACE2 interface differs from SARS-CoV-2 by only two residues, binds hACE2 with a Kd three times lower than early SARS-CoV-2, and mediates entry and replication in human cell lines through hACE2 (specifically neutralised by anti-SARS-CoV-2 sera). Since a naturally occurring, unadapted virus already achieves human-cell infectivity comparable to the pandemic strain, that phenotype provides no evidence for - and removes the necessity of - a lab-adaptation step for the RBD.

## Validity verdict — approved (checked)

This is a clean necessity-refutation (modus tollens on a "must be adapted" claim). The premise being attacked is "a bat sarbecovirus RBD would need serial passage or engineering before it can bind human ACE2 with high affinity and enter human cells." Premises granted: BANAL-236 is a wild, unmanipulated isolate; its RBD differs from SARS-CoV-2 at only 2 of 17 hACE2-contact residues, binds hACE2 with a ~3x lower Kd, and mediates hACE2-dependent entry/replication in human cell lines. A single genuine natural instance of the phenotype falsifies a universal necessity claim, so "high-affinity hACE2 tropism does not require lab adaptation" follows validly. Probed undercutting defeaters: (a) BANAL-236 is not identical to SARS-CoV-2's RBD — irrelevant, since the refuted claim is about whether *any* unadapted bat RBD can achieve high hACE2 affinity, which BANAL-236 settles; (b) BANAL-236 lacks the furin cleavage site — irrelevant, because the statement scopes the conclusion narrowly to RBD/hACE2 use, not to the FCS. No defeater survives against the scoped conclusion. Note the conclusion is correctly modest — it removes a *necessity*/adaptation-required premise; it does not affirmatively establish natural origin (absence of necessity ≠ evidence of natural spillover), and the statement stays within that bound. Conditional on premises, the inference holds. Approved; checked via the reconstruction above.
