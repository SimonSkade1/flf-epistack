---
type: cluster-review
cluster: "[[HC-3 - Whether egg's effect varies by subgroup or individual responder type]]"
---

#### What the analysis says

The cluster asks whether egg's effect varies systematically across people or is essentially homogeneous. Three members: [[H-6 - Two eggs-day does not worsen cardiovascular risk factors in people with type 2 diabetes or prediabetes]] (a named vulnerable subgroup is nonetheless not harmed), [[H-7 - A stable, lifestyle-independent subset of hypo-responders exists for whom dietary cholesterol raises serum cholesterol little]] (an intrinsic responder trait partitions individuals), and residual [[H-13 - Egg's effect is essentially homogeneous across people with no stable protected subgroup or responder class]].

The prior, argued from reference classes alone (no argument node moved it; no inbound edge was marked `used_for_prior`), was `[0.2074, 0.3318, 0.4608]` — homogeneity the single most likely member, with the two heterogeneity axes together at ~0.54. Four evidence blocks updated it to `[0.2407, 0.4183, 0.3410]`.

The movers, by how far their likelihood vectors deviate from flat:

1. [[CG-7 - HC-3 joint over O-16+O-17]] — the responder-reproducibility pair [[E-11 - O-16 × HC-3 — individual cholesterol responsiveness reproducible across repeated trials]] + [[E-12 - O-17 × HC-3 — responsiveness independent of habitual intake and body weight]] — at `[0.85, 1.0, 0.25]` does most of the work in the cluster: it is the only block that strongly penalises homogeneity.
2. [[E-10 - O-8 × HC-3 — egg-mortality association twice as strong in diabetics]] (PHS diabetic subgroup HR 2.01) at `[0.45, 0.95, 1.0]` pushes against H-6 specifically.
3. [[E-9 - O-13 × HC-3 — no lipid difference from 2 eggs-day in prediabetes-T2D]] (DIABEGG) at `[1.0, 0.85, 0.7]` pushes back toward H-6.
4. [[E-13 - O-18 × HC-3 — smooth square-root dose-response across 227 metabolic-ward men]] at `[0.9, 0.7, 1.0]` mildly favours homogeneity.

Net: heterogeneity is modestly favoured over homogeneity, and the cluster moved little — the posterior sits closer to the prior than to any single block's tilt.

**The headline caveat, which limits every number above.** The H-6:H-7 split is not identified by this evidence layer. Step 5 found no observation separating H-6 from H-7 — every edge separates one of them from the residual H-13, none separates them from each other. H-7's 0.418 must therefore not be read as beating H-6's 0.241; that ordering is an artifact of which axis happened to attract more edges, not a claim the evidence supports. Read the pair jointly (0.659 for "the effect is not uniform") and treat the internal split as unpriced. This is logged as a MAJOR and is shipped unfixed.

#### What the model may not capture

The carve is the central defect, and it was flagged at step 4 rather than repaired. H-6 and H-7 are two different heterogeneity axes — a clinically named subgroup versus an intrinsic individual trait — and both can be true simultaneously. Mutual exclusivity is asserted, not real. A production carve would be two clusters (subgroup-vulnerability; responder-heterogeneity), each with its own residual.

The residual is also not behaving as a residual. H-13's statement is a substantive homogeneity claim, not "none of the above", so it competes as a first-class hypothesis and its 0.341 is a real claim about the world rather than leftover mass. Step 8's convention that a residual takes a middling, near-flat likelihood did not fit here: CG-7's child had to argue H-13 down to 0.25 on its merits. That is the right call given what H-13 says, but it means the residual is no longer doing its structural job of absorbing unmodelled answers.

Which raises rule 6 sharply. Is the true answer on the list? Plausibly the real heterogeneity axis, if there is one, is named by neither member — candidates the analysis never weighed include APOE genotype (the classic dietary-cholesterol responder locus), baseline LDL, gut microbiome / TMAO conversion, and background diet composition. Because H-13 is written as a positive homogeneity claim rather than a catch-all, an unlisted axis is *not* cleanly held anywhere in this cluster: it would falsify H-13 while matching neither H-6 nor H-7. My own estimate is that this misallocation is material — perhaps 0.1–0.2 of mass sits on H-13 that a genuine catch-all would hold instead (my number, entering no computation). An unlisted axis is at least as consequential as the listed ones, and arguably more so, since a genotype-defined vulnerable minority is actionable in a way a diffuse responder trait is not.

E-13's evidence is weaker than its vector suggests. A smooth square-root curve fitted across **pooled group means** in 227 metabolic-ward men is fully compatible with wide individual scatter around that curve; group-mean smoothness is close to uninformative about within-person stability. E-13 is therefore only weakly pro-homogeneity, and its opposition to CG-7 may be an aggregation artifact rather than a real disagreement. Separately, [[A-6 - Square-root dose-response implies each additional egg's serum-cholesterol effect shrinks at high baseline intake]] (approved) supplies a rival explanation for CG-7's signal: apparent hypo-response can be within-person concavity — a high-habitual-intake person sitting on the flat part of their own curve — rather than an intrinsic trait. That argument was accepted without its inference traced against CG-7, and if it holds it removes much of the discrimination of the one block the cluster leans on.

Finally, the evidence base is thin: four blocks, with CG-7's reproducibility half resting substantially on a small (n=32) 1987 repeat-challenge study. A cluster whose posterior turns on one small old study is fragile in a way the vector does not show.

#### What would help

1. A within-person repeat-challenge trial (same subjects, two or more separated cholesterol challenges, adherence-controlled, n in the hundreds) reporting the intraclass correlation of response — the single number that would settle H-7 versus H-13 — *unclear* whether a modern adequately-powered one exists; the classic ones are small.
2. Individual-participant data behind the square-root dose-response (O-18), converting its group means into the within-person scatter E-13 cannot currently speak to — *exists, inaccessible*.
3. Effect-modification analyses by APOE genotype in any egg cohort, testing the axis no member names — *exists, unread*.
4. A hard-endpoint RCT in T2D, bridging the E-9/E-10 endpoint mismatch — *does not exist* at the required duration.
5. A step-4 re-carve splitting the cluster in two — an internal fix rather than information, but the highest-value change available to this cluster.

#### Confusions and contradictions

E-9 and E-10 point opposite ways on H-6, and this was priced rather than smoothed. DIABEGG shows an RCT lipid null under 2 eggs/day in prediabetes/T2D (pro-H-6); PHS shows an observational all-cause-mortality HR 2.01 in its diabetic subgroup (anti-H-6). The batch-2 child's reading — that these are not strictly contradictory, since a hard-endpoint observational signal and a 3-month surrogate null differ in both endpoint and confounding structure — is defensible, but it leaves two live stories: either diabetics are differentially harmed on hard endpoints via a pathway lipids do not capture, or the PHS subgroup signal is confounding (sicker diabetics eating differently), in which case H-6 is understated. Nothing in the current evidence set adjudicates between them, and H-6's posterior entry is a compromise rather than a resolution.

CG-7 versus E-13 is the second unresolved pull — reproducible individual responsiveness against a smooth aggregate dose-response — but as argued in part 2 I read that one as an aggregation artifact with a nameable fix (individual-participant data), so it is a part-2/part-3 item rather than an irreducible conflict.
