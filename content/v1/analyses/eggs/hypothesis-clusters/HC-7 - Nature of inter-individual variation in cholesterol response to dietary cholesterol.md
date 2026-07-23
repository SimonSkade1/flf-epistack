---
type: hypothesis-cluster
id: HC-7
hypotheses:
  - "[[H-1 - Plasma-cholesterol response to dietary cholesterol is highly individualized (hypo- vs hyper-responders)]]"
  - "[[H-2 - Feedback down-regulation of absorption and synthesis buffers dietary cholesterol in most people]]"
  - "[[H-35 - Cholesterol responsiveness to dietary cholesterol is a continuous (normally distributed) trait, not a discrete responder-non-responder split]]"
  - "[[H-36 - APOE genotype by itself does not identify dietary-cholesterol hyper-responders]]"
  - "[[H-55 - Some other responder structure]]"
exclusivity: "The primary axis (discrete hypo/hyper split H-1 versus continuous trait H-35) admits at most one true distributional form; the mechanism (H-2) and ApoE-identifiability (H-36) members are the competing best-accounts of that same variation's origin and tag, so the cluster resolves to a single best characterization."
exhaustive_by_construction: false
independence: "The shape of the response variation is independent of the mean lipid effect's base rate (HC-6) - the same feeding data fix different moments; knowing the mean does not set whether the distribution is discrete or continuous."
depends_on:
  - "HC-6: the response distribution is the spread around HC-6's mean effect"
question: "What is the nature of inter-individual variation in the plasma-cholesterol response to dietary cholesterol, and can it be identified?"
relevance: "The core of the 'for whom (hyper-responders / genotype)' clause."
---

![[H-1 - Plasma-cholesterol response to dietary cholesterol is highly individualized (hypo- vs hyper-responders)]]

![[H-2 - Feedback down-regulation of absorption and synthesis buffers dietary cholesterol in most people]]

![[H-35 - Cholesterol responsiveness to dietary cholesterol is a continuous (normally distributed) trait, not a discrete responder-non-responder split]]

![[H-36 - APOE genotype by itself does not identify dietary-cholesterol hyper-responders]]

![[H-55 - Some other responder structure]]

## Carving

The sub-question is what the inter-individual variation in cholesterol response to dietary cholesterol actually is, and whether it can be identified. The primary exclusive axis is the distribution's form - a discrete hypo/hyper split with roughly 31% hyper-responders (H-1) versus a continuous, approximately normal quantitative trait (H-35); these cannot both be the true structure. H-2 characterizes the same variation by its physiological driver (feedback down-regulation of absorption and synthesis, with hyper-response a failure of synthesis suppression) and H-36 denies that ApoE genotype by itself tags it; each competes over what the variation fundamentally is and how to read it, so the cluster resolves to a single best account. Residual H-55 covers a different dominant genetic/microbiome determinant, or largely measurement noise and regression to the mean. Grain caveat: H-2 lies close to H-1's mechanism and H-36 is a negative-predictor claim; they are kept as separate members because distinct observations (synthesis-suppression coupling; the pooled ApoE feeding null) discriminate them and 4a left them un-merged.

## Prior

```python
# HC-7 prior — nature of inter-individual variation in plasma-cholesterol response to dietary cholesterol,
# and whether it can be identified. Members in HC-7.hypotheses order:
#   [H-1 discrete hypo/hyper split (~31% hyper), H-2 feedback down-regulation is the buffering mechanism,
#    H-35 continuous ~normal quantitative trait, H-36 ApoE genotype alone does not identify hyper-responders,
#    H-55 residual (some other structure)].
# no_observation_arguments.py --cluster HC-7 returned none.
# EVIDENCE SPLIT: all five inbound observations are case-specific feeding-study results that DISCRIMINATE the
#   members — the 69/31 metabolic-ward split + synthesis-suppression coupling (CG-23: O-1,O-2), the ~normal
#   response distribution (O-80), the pooled n=395 ApoE null (O-81), the no-difference-by-absorber-phenotype
#   feeding result (O-98). None is an outside-view base rate, so NOTHING is marked used_for_prior; the prior
#   rests on the outside-view biology below and the whole discriminating set is priced at step 8.
# The members characterise the SAME variation along different axes (distributional form, mechanism,
# identifiability); the carving resolves it to a single best account, and 4a kept H-2/H-36 un-merged — so these
# weights are softer than in a clean sign-cluster, which the relative confidences below try to reflect. Odds
# anchored on the continuous-trait member (H-35 = 1.0).

# Anchor — H-35 continuous ~normal trait. Outside view: physiological dose-response traits are almost always
# continuously (polygenic) distributed; apparent responder/non-responder dichotomies are usually a threshold
# cut of such a continuum, and true bimodality is rare. So "the variation is a continuous quantitative trait"
# is the most defensible characterisation of its distributional FORM. Most confident member.
w_continuous = 1.0   # H-35 anchor: continuous is the base-rate distributional form for a biological response trait

# H-2 feedback down-regulation is the buffering mechanism (hyper-response = failed synthesis suppression).
# Cholesterol homeostasis via feedback on fractional absorption and endogenous synthesis is textbook-solid, so
# as an account of the variation's ORIGIN this is strong; the more specific "hyper-response = synthesis-
# suppression failure" half is less certain. Competes as the single best account, close behind continuous.
odds_mechanism_vs_continuous = 0.70   # established feedback physiology as THE characterisation, vs the distributional-form answer
w_mechanism = odds_mechanism_vs_continuous * w_continuous   # H-2

# H-36 ApoE genotype alone does not identify hyper-responders. A negative-predictor claim. Outside view:
# single-locus identification of a quantitative, polygenic trait usually fails, so the negative claim has a high
# base rate of being true — but it is contested in the wider literature (some studies disagree) and is a
# narrower "for-whom" statement than a full characterisation of the variation. Moderate.
odds_apoe_null_vs_continuous = 0.55   # single-gene ID of a quantitative trait usually fails, discounted for wider-literature disagreement
w_apoe_null = odds_apoe_null_vs_continuous * w_continuous   # H-36

# H-1 discrete hypo/hyper split, ~31% hyper. The classic, widely-cited framing (McNamara 69/31). But a genuine
# discrete phenotype (true bimodality) is less likely than a thresholded continuum, so it sits below the
# continuous member on the primary axis. Still a strong candidate given how the literature is framed.
odds_discrete_vs_continuous = 0.50   # a genuinely discrete responder phenotype, vs a threshold cut of a continuum
w_discrete = odds_discrete_vs_continuous * w_continuous   # H-1

# H-55 residual — its OWN argued weight (rule 4). An unmodelled answer looks like: the variation is dominated by
# a DIFFERENT measured determinant (a specific non-ApoE gene, or gut-microbiome TMAO-pathway differences), or it
# is largely measurement noise / regression to the mean rather than any stable trait at all.
w_residual = 0.30   # ~0.30 : 1 vs continuous; a different dominant determinant, or mostly noise

prior("HC-7", [w_discrete, w_mechanism, w_continuous, w_apoe_null, w_residual])
```
