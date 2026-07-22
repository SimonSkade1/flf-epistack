---
id: HC-9
type: hypothesis-cluster
question: "Does a cosmic flux of GUT monopoles catalyzing nucleon decay exist at astrophysically relevant levels?"
hypotheses:
  - "[[H-20 - Solar-captured GUT monopoles catalyze proton decay producing a detectable low-energy neutrino flux]]"
  - "[[H-41 - No astrophysically relevant flux of catalyzing GUT monopoles exists]]"
exclusivity: "Either a catalyzing monopole flux at astrophysically relevant levels exists or it does not; the members are a claim and its negation."
exhaustive_by_construction: true
independence: "The existence of such a flux is set by grand unification and cosmology, factorizing from the collider-gravity, strangelet, and vacuum questions."
depends_on: []
relevance: "Monopole catalysis is one of the proposed non-black-hole accelerator disaster mechanisms; this cluster fixes whether its physical premise exists in nature at all."
---
![[H-20 - Solar-captured GUT monopoles catalyze proton decay producing a detectable low-energy neutrino flux]]
![[H-41 - No astrophysically relevant flux of catalyzing GUT monopoles exists]]

The full catalysis scenario — flux, solar capture, Rubakov-Callan catalysis, detectable neutrinos — against its negation (any conjunct failing). Exhaustive by construction: proposition and logical complement. A failure of the analysis would look like the neutrino and trapping searches being insensitive to the actual monopole parameter range for a shared modeling reason, favouring the first member.

## Prior

```python
# HC-9 prior — does a cosmic flux of GUT monopoles catalyzing nucleon decay exist at astrophysically
# relevant levels? Members in HC-9.hypotheses order:
# [H-20 solar-captured catalyzing flux exists & produces a detectable neutrino signal,
#  H-41 no astrophysically relevant catalyzing-monopole flux exists].
# exhaustive_by_construction: proposition and its negation, so there is no residual member (rule 4 N/A).
# Inputs are pure outside view: the realization rate of GUT-scale topological monopoles and, dominating
# everything, the standard cosmological expectation that inflation dilutes any such flux away. No
# no-observation arguments exist for this cluster (no_observation_arguments.py --cluster HC-9 → none).
# The two inbound E edges (E-5, E-11, grouped in CG-6) are the Super-K solar nulls: they DISCRIMINATE
# H-41 from H-20 (a signal-vs-null test), so they are left unmarked for step 8, NOT priced here.

# --- H-41 no astrophysically relevant flux (the anchor, the outside-view default) ---
# What must hold: either grand unification produces no light-enough topological monopoles, or (dominant
# route) inflation dilutes their number density to far below any astrophysical relevance, or catalysis is
# too weak to matter. This is the mainstream expectation — inflation was in large part invented to solve
# the "monopole problem," so a generic post-inflationary universe contains essentially zero GUT monopoles.
# Anchored at unit weight; H-20 is priced as odds against it. Highest-confidence member by far.
w_H41 = 1.0

# --- H-20 catalyzing flux exists and is detectable (priced as a product of factors it all requires) ---
# What must hold jointly: (a) grand unification into a simple group actually produces stable topological
# monopoles; (b) a flux survives to astrophysically relevant levels rather than being inflated away; and
# (c) Rubakov-Callan catalysis proceeds at an unsuppressed, strong-interaction cross section. Reference
# class: GUT-scale new-physics predictions that remain unconfirmed decades on (proton decay still unseen,
# no monopole ever detected). Does NOT cover whether Super-K in particular would have seen it — that is
# the discriminating step-8 evidence, deliberately excluded from the prior. Strongly disfavoured relative
# to H-41; the factor doing almost all the work is the inflation-dilution term.

# (a) A simple-group GUT with nontrivial pi_2 (hence 't Hooft-Polyakov monopoles) is the true high-energy
# theory. Well-motivated (gauge-coupling unification) but not established; proton decay unobserved.
p_gut_monopoles = 0.6

# (b) The monopole flux survives at an astrophysically relevant density instead of being inflated to
# negligibility. This is the crux outside-view factor: standard inflationary cosmology drives the surviving
# abundance many orders of magnitude below relevance, and only special late-transition or low-reheating
# scenarios (production after/at the end of inflation) keep a near-Parker-bound flux. Small by design.
p_flux_survives = 0.10

# (c) Rubakov-Callan catalysis of nucleon decay operates at a strong-interaction-scale cross section for
# solar-captured monopoles. The mechanism is real in principle but its effective astrophysical strength is
# theoretically contested, so roughly even odds it is strong enough to give the posited detectable rate.
p_catalysis_strong = 0.5

w_H20 = p_gut_monopoles * p_flux_survives * p_catalysis_strong   # ~0.03 : 1 vs H-41

prior("HC-9", [w_H20, w_H41])
```

