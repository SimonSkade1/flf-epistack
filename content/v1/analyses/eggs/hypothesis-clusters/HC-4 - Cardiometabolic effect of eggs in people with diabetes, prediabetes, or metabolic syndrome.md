---
type: hypothesis-cluster
id: HC-4
hypotheses:
  - "[[H-4 - High egg intake does not harm blood lipids or glycemic control in people with prediabetes-T2D]]"
  - "[[H-19 - Substituting eggs for high-carb breakfast foods improves or does not worsen glycemic-insulin outcomes in adults at risk for T2D]]"
  - "[[H-24 - Egg consumption raises CVD risk specifically in people with type 2 diabetes]]"
  - "[[H-33 - Impaired insulin sensitivity in T2DM deranges cholesterol transport, making egg-derived dietary cholesterol more atherogenic in diabetics]]"
  - "[[H-52 - Some other net egg effect in diabetics]]"
exclusivity: "The exclusive axis is the net cardiometabolic verdict for this population - safe/beneficial versus harmful; the endpoint- and mechanism-level members refine their pole, so at most one net characterization is correct."
exhaustive_by_construction: false
independence: "The effect in people who already have diabetes is a distinct estimand from incident-disease causation in the general population (HC-1/HC-3); its prior does not factor through them."
depends_on: []
question: "In people who already have diabetes, prediabetes, or metabolic syndrome, is habitual egg intake net-harmful, safe, or beneficial cardiometabolically?"
relevance: "Answers the 'for whom (diabetics)' clause - the sharpest RCT-versus-cohort disagreement in the case."
---

![[H-4 - High egg intake does not harm blood lipids or glycemic control in people with prediabetes-T2D]]

![[H-19 - Substituting eggs for high-carb breakfast foods improves or does not worsen glycemic-insulin outcomes in adults at risk for T2D]]

![[H-24 - Egg consumption raises CVD risk specifically in people with type 2 diabetes]]

![[H-33 - Impaired insulin sensitivity in T2DM deranges cholesterol transport, making egg-derived dietary cholesterol more atherogenic in diabetics]]

![[H-52 - Some other net egg effect in diabetics]]

## Carving

The sub-question is the net cardiometabolic effect of habitual eggs in dysglycemic people. The safe/beneficial pole is carried by RCT-grade lipid and glycemic safety at ~12 eggs/week (H-4) and a favourable-to-neutral glycemic response when eggs displace high-carbohydrate breakfasts (H-19); the harm pole by a cohort CVD excess specific to diabetics (H-24) and its proposed mechanism - insulin-resistance-deranged cholesterol transport rendering egg cholesterol more atherogenic (H-33). The live tension is surrogate-safe (interventional) versus hard-endpoint-harm (observational); H-19 and H-33 are the endpoint/mechanism refinements of their respective poles, so the cluster resolves to a single best net verdict. This is a deliberate combination-style cluster kept well under the member ceiling. Residual H-52 covers net benefit or harm confined to a subgroup/endpoint not captured. H-19 sits here (glycemic safety) while its Maki trial-mate H-20 (an LDL worsening) sits in HC-6, because those two endpoints co-hold and therefore cannot be exclusive members of one space.

## Prior

```python
# HC-4 prior — net cardiometabolic verdict of habitual eggs in people with diabetes/prediabetes/
# metabolic syndrome. Members in HC-4.hypotheses order:
# [H-4 surrogate-level safety, H-19 glycemic benefit via substitution, H-24 diabetic-specific CVD harm,
#  H-33 atherogenic-cholesterol mechanism, H-52 residual].
# The exclusive axis (per the note) is the single best NET verdict: safe/beneficial pole (H-4, H-19)
# vs harm pole (H-24, H-33) vs residual. This step prices the OUTSIDE VIEW only — no cluster
# no-observation arguments exist (no_observation_arguments.py --cluster HC-4 returns none), and every
# inbound E edge here is a case-specific, DISCRIMINATING egg observation (the DIABEGG/Maki/Blesso trials,
# the Drouin-Chartier/Jang cohorts, the diabetic-subgroup meta), so NONE is marked used_for_prior and all
# are left for step 8. Weights are relative odds; the harm pole is the unit anchor.

# Harm pole (H-24 + H-33) — anchor. Reference class: dietary "harm specific to metabolic subgroup X"
# claims raised from observational subgroup interactions. Such interactions replicate as genuine causal
# effect-modification maybe ~30% of the time (subgroup/interaction findings in nutritional epidemiology
# are fragile), but diabetic dyslipidemia gives the harm direction real mechanistic plausibility, so it
# is a live pole rather than a long shot.
w_harm_pole = 1.0

# Safe/beneficial pole (H-4 + H-19) as odds vs harm. Modern egg RCTs — including in at-risk populations —
# predominantly show surrogate-level neutrality, and dietary cholesterol's effect on hard CVD endpoints is
# weak and inconsistent; so absent the discriminating trials (priced at step 8) the outside view leans
# safe over harm, but not overwhelmingly given the genuine diabetic signal in the literature.
safe_vs_harm = 1.8   # safe/beneficial pole ~1.8x as likely a priori as the harm pole
w_safe_pole = safe_vs_harm * w_harm_pole

# --- split the safe pole into its two exclusive members ---
# H-4 (broad surrogate lipid/glycemic neutrality) vs H-19 (glycemic improvement when eggs displace
# high-carb breakfasts). If the pole is safe, the broad neutrality verdict is the more likely SINGLE best
# characterisation than the narrower substitution-benefit claim (whose own primary insulin-sensitivity
# endpoint was null), so H-4 takes the larger share.
share_neutral = 0.62   # H-4 : H-19 ~ 0.62 : 0.38 within the safe pole
w_H4  = w_safe_pole * share_neutral            # H-4
w_H19 = w_safe_pole * (1 - share_neutral)      # H-19

# --- split the harm pole into its two exclusive members ---
# H-24 (diabetic-specific CVD-endpoint harm) vs H-33 (the insulin-resistance atherogenic-cholesterol
# mechanism). If the pole is harm, the endpoint-level verdict is the more likely single characterisation
# than the specific, explicitly untested mechanism (the note flags H-33 as speculative, with no
# egg-stratified lipoprotein data in diabetics), so H-24 dominates the pole.
share_endpoint = 0.75   # H-24 : H-33 ~ 0.75 : 0.25 within the harm pole
w_H24 = w_harm_pole * share_endpoint           # H-24
w_H33 = w_harm_pole * (1 - share_endpoint)     # H-33

# H-52 residual — a net cardiometabolic effect none of the four listed members expresses: e.g. a genuine
# net BENEFIT beyond the glycemic-substitution channel, or harm confined to an endpoint/subgroup not
# captured (a specific lipoprotein subclass or event type). Its own argued weight (rule 4), set by how
# often a five-member menu like this misses the operative answer in an open nutrition question — real but
# not dominant.
w_H52 = 0.42   # ~0.42 : 1 vs the harm pole; ~13% of the mass once normalised

prior("HC-4", [w_H4, w_H19, w_H24, w_H33, w_H52])
```
