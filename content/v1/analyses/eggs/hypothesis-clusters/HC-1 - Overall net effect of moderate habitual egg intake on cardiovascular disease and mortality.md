---
type: hypothesis-cluster
id: HC-1
hypotheses:
  - "[[H-6 - Moderate egg consumption causally lowers CVD risk in Chinese adults]]"
  - "[[H-21 - Moderate egg intake has no causal effect on CVD risk overall]]"
  - "[[H-27 - Higher dietary cholesterol - egg intake causally raises CVD and mortality risk (dose-response)]]"
  - "[[H-44 - An intermediate egg intake of about 3 to 6 per week minimizes CVD and mortality risk with harm at both lower and higher intake]]"
  - "[[H-49 - Some other overall egg-CVD relationship]]"
exclusivity: "Each names an incompatible sign or shape for the population dose-response - protective, flat, monotonically harmful, or U-shaped - so at most one can summarize the typical effect (a genuine region-flip is the separate HC-2 question and would send weight to the residual)."
exhaustive_by_construction: false
independence: "The net direction/shape is a different quantity from whether the effect varies by region (HC-2), which agent carries it (HC-5), or whether the framing is well-posed (HC-10); knowing those does not fix the base rate of the sign, so the prior factorizes with the residual absorbing the region-flip case."
depends_on:
  - "HC-2: a genuine region-flip means no single overall verdict - weight then flows to this cluster's residual H-49; only approximately independent"
  - "HC-10: if egg-health is comparator-contingent/ill-posed, a single unconditional overall verdict is undercut"
  - "HC-5: the harmful pole (H-27) bundles egg-cholesterol causality shared with the operative-exposure cluster"
question: "What is the net causal effect of moderate habitual egg intake (up to ~1 egg/day) on cardiovascular disease and all-cause mortality?"
relevance: "This is the spine of the main question's 'overall ... and at what level' clauses."
---

![[H-6 - Moderate egg consumption causally lowers CVD risk in Chinese adults]]

![[H-21 - Moderate egg intake has no causal effect on CVD risk overall]]

![[H-27 - Higher dietary cholesterol - egg intake causally raises CVD and mortality risk (dose-response)]]

![[H-44 - An intermediate egg intake of about 3 to 6 per week minimizes CVD and mortality risk with harm at both lower and higher intake]]

![[H-49 - Some other overall egg-CVD relationship]]

## Carving

The sub-question is the net causal effect of moderate habitual egg intake on hard cardiovascular and mortality endpoints, read as the typical population dose-response curve. The four named members are mutually incompatible signs/shapes of that curve: causal protection (H-6), a flat null (H-21), a monotonic dose-dependent increase (H-27), and a U-shape with a moderate optimum around 3-<6/week (H-44). H-6 and H-27 carry population tags (Chinese / US) that reflect their evidentiary base, not a scope that would let both hold at once; if the sign genuinely flips by population that is the separate modification question (HC-2), and under that scenario none of the single-verdict members is globally correct, so probability flows to the residual H-49. Non-exhaustive: the residual also covers non-monotonic shapes other than the simple U. The Kadoorie/PURE/Western-cohort and dietary-cholesterol observations discriminate these members; the same Asian evidence also informs HC-2, which is permitted because level and heterogeneity are orthogonal axes rather than two slices of one question.
