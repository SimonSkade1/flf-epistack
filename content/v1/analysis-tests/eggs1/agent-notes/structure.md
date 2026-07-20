# Hypothesis structure (step 4b) — cluster inventory

Main question: *Is habitual egg consumption net beneficial, harmful, or neutral for human health — overall, for whom, and at what level of intake?*

## Cluster inventory (top-level map)

1. [[HC-1 - Magnitude and mechanism of egg's effect on atherogenic blood lipids]] — *How large is habitual egg / dietary-cholesterol's effect on atherogenic blood lipids, and by what mechanism?* (surrogate-endpoint arm)
2. [[HC-2 - Net direction of egg's effect on hard cardiovascular and mortality endpoints]] — *What is the net direction of egg intake's effect on hard CVD / mortality endpoints?* (hard-endpoint arm)
3. [[HC-3 - Whether egg's effect varies by subgroup or individual responder type]] — *Does egg's health effect vary systematically across subgroups / individuals, or is it homogeneous?* (the "for whom" arm)

## Membership (frozen order: ascending id, residual last)

- HC-1: H-1, H-5, H-8, H-11 (residual)
- HC-2: H-2, H-3, H-4, H-9, H-10, H-12 (residual)
- HC-3: H-6, H-7, H-13 (residual)

## Counts

- H in (from 4a active set): 10
- active after 4b: 13 (10 originals + 3 residuals minted here)
- merged: 0 (4a's bookkeeping; 4b does no merging)
- dropped: 0
- clusters: 3
- residuals minted: 3 (H-11, H-12, H-13); constructed complements: 0

## Exclusivity-strain notes (pipeline feedback)

1. HC-2 (primary, flagged): the three null members H-4, H-9, H-10 all assert a ~null direction and differ only by endpoint/population scope (IHD + reverse-causation; healthy Western adults ≤1/day; diverse global populations). They are scope-refinements of one "null" answer, not pairwise mutually-exclusive rivals. Kept as separate members (4a deemed them discriminable; 4b does no merging); exclusivity holds across the direction *poles* (protective/harmful/null), with the null mass partitioned by scope rather than three independent competitors. Step 7 priors on the three should be read as a partition of the null branch.
2. HC-3 (secondary): H-6 (diabetic subgroup not harmed) and H-7 (intrinsic responder trait) are two different heterogeneity axes and can co-hold; accepted mild non-exclusivity under the fast-test cap rather than splitting into two thin clusters. Cleaner production carve = two clusters.
3. HC-1 (minor): H-5 and H-8 both predict a *small* lipid effect via different mechanisms (poor absorption vs saturation); overlap accepted as mechanism-refinements of the "small" branch (discriminable by absorption vs dose-response observations).

generated: 2026-07-20
