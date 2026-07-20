---
type: cluster-review
cluster: "[[HC-2 - Net direction of egg's effect on hard cardiovascular and mortality endpoints]]"
---

#### What the analysis says

**Read this cluster by branch, not by member.** The highest single posterior entry — `H-9` at **0.3489** — is a scoring artifact and must not be reported as "the leading hypothesis". [[H-9 - Moderate habitual egg intake is not associated with increased CVD risk in generally healthy Western adults]] is the narrowest-scope member in the set (healthy Western adults, up to ~1 egg/day). When an observation falls outside a member's scope rider, that member correctly receives a likelihood at or near the anchor (~1) — it genuinely predicts nothing there, so it cannot be wrong. Across five evidence blocks that adds up to relative advantage earned **purely by abstaining**: H-9 scored 0.72 on CG-3 (CKB), 0.55 on CG-4 (PHS), **1.00 on CG-5 (EPIC)**, 0.40 on CG-6 (PURE), and **1.00 on E-21 (pooled Harvard)** — anchor on two of five. It rose because most of the evidence could not touch it, not because the evidence supported it.

Per-member numbers are not comparable within this cluster, and the cluster file says so itself: `H-4`, `H-9`, `H-10` are a *partition of one "null" branch by scope rider*, while `H-2` and `H-3` are undivided directional answers competing against that whole branch. The honest read is branch totals:

| branch | prior | posterior |
|---|---|---|
| **null** (H-4 + H-9 + H-10) | 0.5714 | **0.6389** |
| **direction varies / J-shaped** (H-12) | 0.2000 | **0.3083** |
| **protective** (H-2) | 0.1257 | **0.0388** |
| **harmful** (H-3) | 0.1029 | **0.0141** |

(Members in `HC-2.hypotheses` order, prior `[0.1257, 0.1029, 0.1714, 0.2571, 0.1429, 0.2000]`, posterior `[0.0388, 0.0141, 0.1758, 0.3489, 0.1142, 0.3083]`, five evidence blocks.)

The substantive result is that **both strong directional claims are near-dead**: protective fell 0.126 → 0.039, harmful fell 0.103 → 0.014. Nothing in the evidence set sustains a population-wide direction. The null branch barely moved (0.571 → 0.639) — the evidence did not so much confirm the null as fail to displace it.

The second real finding, and the more interesting one, is [[H-12 - Egg's net effect on hard cardiovascular and mortality endpoints is not a single population-wide direction]] at **0.3083**, up from 0.20. This is **not** leftover probability mass. H-12's statement is substantive — a non-monotonic / J-shaped effect, null-to-protective at moderate intake in low-baseline-intake populations, harmful at high intake or in diabetics — and CG-4 (PHS) **anchored on it at 1.0**, i.e. of all six members H-12 best predicted the observed mortality-without-events pattern. A residual that the strongest single block picks out as its best explanation has stopped being a residual.

What did the updating work: CG-3 (CKB) is the only block that anchors on H-2 (1.0) and is what kept the protective member alive at all against a set that otherwise punishes it; CG-4 (PHS) and CG-6 (PURE) are what killed H-2 (0.15, 0.12) and H-3 (0.75 then 0.15); CG-5 (EPIC) is near-flat across the board (0.70–1.15) and did little; E-21 (pooled Harvard) mildly favours the broad-scope nulls and H-4. CG-6 (PURE) is the only block that anchors on [[H-10 - Egg intake has no material effect on blood lipids, CVD, or mortality across diverse global populations]] (1.0), which is why the global-null member did not fall further.

One prior-side driver worth naming: [[A-3 - Attenuation on excluding early follow-up indicates reverse causation drives EPIC egg-IHD signal]] was **corrected at step 6**, and this materially weakened [[H-4 - Egg intake is essentially neutral for ischemic heart disease]]. The original argument conflated *loss of statistical significance* on dropping the first 4 years of follow-up with *movement of the point estimate*; dropping 4 years cuts case count and hence power, so significance loss is expected even under a constant true HR. Post-correction the argument supports only "reverse causation contributes", not "reverse causation drives". Consequently H-4 earned ~1.15x on CG-5 (EPIC) rather than the 2–3x a clean reverse-causation signature would have earned, and it lands at 0.1758.

#### What the model may not capture

The cluster's central structural defect is **shipped unfixed and is visible in the output**: mixing scope-partitioned members with whole-scope members in one exclusive set makes the posterior vector uninterpretable member-by-member. The cluster file's `exclusivity` field flags the strain honestly (H-4, H-9, H-10 "could co-hold"), and the prior block handles it correctly by pricing the branch first and then splitting. But **step 8 does not carry that structure through**: each likelihood is stated per member, so the abstention advantage accrues to whichever member has the narrowest rider, and nothing downstream renormalises it away. This is a pipeline-level fault, not an egg-specific one — any cluster containing a narrow-scope member will show it. The fix is either merging the null branch into one member with the scope discussion in prose (a step-4 re-carve) or requiring likelihoods to be stated per *branch* (a step-8 convention change). Neither is step 9's to make.

Related: the **branch totals inherit the prior's internal split** (0.45 / 0.30 / 0.25 of the null branch to H-9 / H-4 / H-10), which the prior block itself calls "a scope judgement and the weakest part of this block". Since the evidence then re-weights those shares by abstention rather than by fit, the within-branch ordering (H-9 > H-4 > H-10) should be read as carrying almost no information.

Is the answer on the list? The four branches — protective, harmful, null, direction-varies — do exhaust *direction*, so the set is close to exhaustive on its own framing. The framing is where the risk sits. Every member treats "egg intake" as the causal variable; none isolates **what eggs displace or accompany**. If the real causal object is the meal (eggs-with-bacon-and-white-toast in Western cohorts vs eggs-as-scarce-protein in CKB and PURE), then every member is mis-specified and the CKB/Western divergence is a confound artifact rather than a dose or population effect. The prior block explicitly parks this inside H-12 ("it also absorbs answers nobody here modelled (e.g. the effect is entirely about what eggs displace, not eggs)"), which is a reasonable place to put it but means H-12's 0.3083 is doing two very different jobs — J-shaped dose-response and total exposure mis-specification — that would have quite different implications. An unlisted "the exposure is wrong" answer would be **more** consequential than any listed one, because it would invalidate the cluster rather than answer it.

Second framing risk: all five evidence blocks are observational cohorts. The whole cluster therefore prices *associations* and asks arguments to carry the causal step. Residual confounding by healthy-user status is the standing alternative to every one of these results simultaneously, and it is not a member — it lives scattered across [[A-2 - Mortality-without-events pattern in PHS points to residual confounding, not causal egg harm]] and A-3. A single systematic confounding failure would move all six likelihoods in a correlated way that the independent-block form cannot express.

Third: the surrogate link to HC-1 is set to near-zero influence (`depends_on` calls it "judged weak"). That is defensible — the whole contest is whether the LDL change reaches events — but it means a large, well-established lipid effect from HC-1 contributes essentially nothing to the harmful member here, which is a strong modelling choice made in one line of prose.

#### What would help

1. A likelihood convention that neutralises scope-abstention — restating CG-3..CG-6 and E-21 against the *null branch as one member* and reporting the branch posterior directly. **Does not exist** (it is a pipeline convention, not information); it would change this cluster's presentation more than any datum.
2. Randomised hard-endpoint trial data on egg intake at ≥1/day over years. **Does not exist** — and almost certainly never will, which is the deepest limit on this cluster and on any cluster like it.
3. The dose-response curves (not the categorical HRs) from CKB, PURE and the Harvard pooled analysis, put on one axis. This is what would actually discriminate H-12 from the null branch, and H-12 at 0.3083 is currently the finding least supported by curve-level detail. **Exists, unread.**
4. Whether CKB's protective signal survives adjustment for total protein and for socioeconomic status — in a population where eggs were a scarce, income-marked food, this is the single most likely explanation of the CKB/Western divergence. **Unclear** whether the published models report it.
5. Diabetic-subgroup event data at high intake, which is H-3's most credible content and the part H-12 currently absorbs. **Exists, unread.**

#### Confusions and contradictions

CG-3 (CKB) and CG-6 (PURE) point in genuinely opposite directions and the analysis does not resolve it. CKB anchors on H-2 (protective, 1.0) and scores H-3 at 0.10; PURE anchors on H-10 (global null, 1.0) and scores H-2 at 0.12. Both are large, well-conducted cohorts, and both include low-and-middle-income populations — so the easy reconciliation ("Western vs non-Western") does not work. Multiplied together they roughly cancel, and the cluster's output silently absorbs a real disagreement as an absence of signal. Whether the truth is "the effect differs between Chinese and multi-country populations" (H-12) or "one of these cohorts is confounded" (null branch) is precisely what this cluster cannot tell, and precisely what its answer turns on.

The PHS pattern is the second unresolved thing: mortality raised without a corresponding rise in cardiovascular *events*. A-2 reads this as residual confounding; CG-4's anchoring on H-12 at 1.0 reads it as effect-modification. Both readings are in the model at once, in different places, and they are not compatible. I cannot tell which is right from the material here, and the cluster ships that way.

Finally, the run's evidence set is five cohort blocks, all of which appear in the same review literature and several of which share investigators and analytic conventions with each other. Whatever systematic bias that literature carries — in FFQ handling, in covariate choice, in which null results got published at all — is common-mode across the entire cluster and is not priced anywhere.
