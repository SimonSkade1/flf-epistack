---
type: hypothesis-cluster
id: "HC-1"
question: "Did SARS-CoV-2 first infect humans through natural zoonotic spillover, or through a research-related incident — and if research-related, did it involve an unmodified or a laboratory-manipulated virus?"
hypotheses:
  - "[[H-41 - Natural zoonotic spillover with no research involvement]]"
  - "[[H-42 - Research-related leak of an unmodified naturally-evolved virus (zoonotic collection)]]"
  - "[[H-43 - Research-related origin of a laboratory-manipulated virus (engineered lab leak)]]"
  - "[[H-44 - The origin is something not listed here]]"
exclusivity: "The members partition the virus's route into humans by two nested binary distinctions — was research activity involved in the human introduction, and (if so) was the virus laboratory-manipulated — so at most one holds: no-research/natural (H-41), research/natural-virus (H-42), research/manipulated-virus (H-43), or none-of-these (residual)."
exhaustive_by_construction: false
independence: "Origin is the root question; its prior is a base rate over emergence mechanisms that does not require first fixing the number of introductions (HC-2) or the market's role (HC-3). The reverse dependences — those clusters' answers co-varying with origin — are recorded in their depends_on, not here."
depends_on: []
relevance: "This is the main question of the analysis."
---
The primary cluster: the mutually-exclusive answers to the run's main question. All object-level empirical evidence — viral genome structure and engineering signatures, natural-relative and recombination genetics, early-case geography, phylodynamics, and institutional/documentary records — attaches here at step 5 with a per-member likelihood breakdown.

![[H-41 - Natural zoonotic spillover with no research involvement]]

![[H-42 - Research-related leak of an unmodified naturally-evolved virus (zoonotic collection)]]

![[H-43 - Research-related origin of a laboratory-manipulated virus (engineered lab leak)]]

![[H-44 - The origin is something not listed here]]

## Carving

**Exclusivity.** Two questions define the space: (1) was research activity part of how the virus reached humans? (2) if so, had the virus been modified in a lab? H-41 answers no to (1); H-42 answers yes to (1) and no to (2); H-43 answers yes to both. Exactly one can be the actual causal history of the first human infection, so the members are pairwise exclusive; the residual (H-44) holds the probability of any history none of them captures (e.g. a manipulated virus that reached humans by a non-research route).

**Not exhaustive by construction — residual required.** H-41 ∪ H-42 ∪ H-43 covers {natural-route/natural-virus, research-route/natural-virus, research-route/manipulated-virus} but not, for instance, a lab-modified virus escaping into animals and later spilling over naturally, or a mechanism outside this corpus; H-44 catches these, so the prior sums to one honestly. An analysis-failure that mis-modelled the natural-vs-research or modified-vs-natural boundary (e.g. treating serial passage as "not manipulation") would show up as probability that belongs in the residual, and would most plausibly be mis-assigned between H-42 and H-43.

**Why the genome "engineered-vs-natural" question is NOT a separate cluster.** The step-3 pile contained a large set of genome hypotheses (engineered: in-vitro assembly, chimera, serial passage, DEFUSE furin insertion; natural: natural evolution, natural recombination, animal-vs-human adaptation locus). Carving these as their own cluster would re-partition this one — "engineered genome" ≈ H-43, "natural genome" ≈ H-41 ∪ H-42 — and would double-count the genome evidence. Instead the engineered hypotheses are merged into H-43 and the natural ones into H-41 (H-42 shares their natural genome); the genome observations then discriminate H-43 from the natural members here, at step 5, exactly once.

**Why the bottom-line verdicts are merged in, not co-members.** Rootclaim's scenario split (H-1/H-2/H-3/H-4), Judge Eric's adjudication (H-12/H-13), Weissman's synthesis (H-17), and the US-IC assessments (H-27/H-28) are analysts'/institutions' conclusions *about* origin, not distinct object-level mechanisms. Placing a verdict beside the object-level answer it asserts would break MECE and double-count, so each is merged into the member it concludes for (Rootclaim/Judge/Andersen/IC-plurality zoonosis → H-41; Rootclaim zoonotic-collection → H-42; Rootclaim-GoF/bioweapon, Weissman, FBI-DOE → H-43). Weissman's numeric prior (H-18) is a base-rate *parameter*, not an origin answer, and is left for step 7 rather than forced in as a member.

## Prior

```python
# HC-1 prior — origin of SARS-CoV-2. Members in HC-1.hypotheses order:
# [H-41 natural zoonosis, H-42 research leak of an UNMODIFIED natural virus (zoonotic collection),
#  H-43 research origin of an ENGINEERED virus (lab leak), H-44 residual].
#
# Structure: a LOCATION-FREE base-rate spine (global odds over emergence mechanisms) x named CIRCUMSTANTIAL
# adjustment factors. Both come from the cluster's no-observation arguments (no_observation_arguments.py
# --cluster HC-1) — arguments with NO object-level evidence-edge anywhere, so the prior is their ONLY home
# (rule 6: they enter as reasoning that sets a number, not as terms scored elsewhere).
#   Base-rate spine:  A-6 (Rootclaim historical incidence), A-22/A-23 (Stansifer annualized rates, read
#                     location-free), A-37 (Weissman lab-accident base rate), A-21 (mixture / anti-overconfidence).
#   Circumstantial:   A-8/A-38 (Wuhan location), A-13 (WIV biosafety), A-14 (database offline / RaTG13 rename),
#                     A-15 (China non-transparency), A-16 + A-28 (absence of expected lab evidence / no
#                     whistleblower). These have no evidence-edge, so if not folded in here they are priced
#                     NOWHERE — hence they are included, in BOTH directions.
# EXCLUDED as double-counting object-level edges priced at step 8: furin site (A-11/A-26 -> E-32/E-43/E-47),
# chimera (A-10 -> E-44/E-45), ACE2 / well-adaptedness (A-27, and A-12's adapted-from-earliest -> genome
# edges), DEFUSE feature-match (A-39 -> E-49/E-51), market clustering (A-9/A-24 -> HC-3), ascertainment
# (A-40 -> HC-3), Holmes-photo/DEFUSE temper (A-30 -> HC-3 + genome edges). A-7 (COVID a poor bioweapon) bears
# only on the deliberate-release tail already dropped below; A-29/A-36 are aggregation meta-conclusions, not
# factors. No inbound E edge is marked used_for_prior — everything used here is an argument, not an edge; the
# two base-rate edge candidates are left for step 8 (E-60 SARS-CoV-1 civet precedent is already inside the
# A-6/A-22 reference classes and sits in CG-3 with the discriminating adaptation-series E-61; E-58 Ebola
# reservoir-unfound blunts a specific discriminating datum, P(no reservoir found | H-41)).

# ============================ 1. LOCATION-FREE BASE-RATE SPINE ============================

# ---- H-41 natural zoonotic spillover — the anchor (unit weight). --------------------------------------
# What must be true: a naturally-evolved sarbecovirus crossed to humans via ordinary ecological contact
# (wildlife trade / intermediate host), no research involved. Reference class: novel-pathogen pandemics of
# the last ~40 yr are overwhelmingly natural (SARS-1 2002, MERS 2012, essentially every other emergence) —
# the uncontested majority mechanism, so it anchors at 1 and the research routes are odds against it. Most
# confident member by far.
w_H41 = 1.0

# ---- Base odds of H-43 (engineered lab leak) vs H-41 — a MIXTURE over reference classes, location-free. --
# The three estimates seem to disagree by orders of magnitude, but most of that gap is location: Stansifer's
# headline ~1.88:1-favouring-lab is a WUHAN-CONDITIONED rate. Location is not an evidence-edge, so it enters
# THIS prior explicitly as the circumstantial factor f_wuhan below (section 2); to avoid double-counting it,
# the SPINE is kept location-free (global base rates), and all three classes then agree that global zoonosis
# dominates. Mix them per A-21 (do not bet the prior on a single multiplied point estimate).

# Class 1 — Rootclaim historical incidence (A-6): research-caused novel-virus outbreaks ~never in the record
# vs several natural coronavirus pandemics => accidental lab-escape 0.6% vs zoonotic 78%. (Rootclaim's separate
# 16% bioweapon prior maps to H-43's deliberate tail but is excluded as an acknowledged calibration artifact —
# A-6's own step-6 note flags the 16%-above-0.6% ordering as a miscalibration, not a real prior.)
odds_H43_rootclaim = 0.6 / 78          # A-6 lab-escape : zoonotic historical-incidence odds ~1/130

# Class 2 — Weissman mechanistic lab-accident base rate (A-37): 0.2-1%/yr/BSL-3 leak x WIV risk factors x
# ~50% DEFUSE-active => research-origin prior ~1/100 to 1/200 (this is the pre-outbreak-location L0; Weissman
# prices the Wuhan coincidence separately, as A-38 — which lives in f_wuhan below, not here). Take 1/150 mid.
research_prior_weissman = 1.0 / 150    # A-37 midpoint of the stated 1/100-1/200 band
odds_H43_weissman = research_prior_weissman / (1 - research_prior_weissman)   # ~1/149

# Class 3 — Stansifer's rates read LOCATION-FREE (A-22/A-23): strip the HSM-specific 1/200 from P(Z) and the
# global zoonotic rate is ~1/160/yr; his P(LL)~1/17000 is WIV-specific, so the global lab-leak rate over the
# handful of comparable GoF programs is ~a-few/17000 ~1/5000, giving global odds ~1/30. The more lab-favourable
# reading that survives once his location conditioning is moved into f_wuhan; also absorbs the standard critique
# of A-6 that historical absence cannot bound the recent GoF-scale era.
odds_H43_stansifer_lf = 1.0 / 30       # A-22/A-23 global (location-stripped) lab : zoonotic odds

# Credence over which reference class prices the location-free spine (A-21: spread, do not pick one). The
# fat-tailed class 3 dominates the mean — the honest representation of order-of-magnitude uncertainty.
c_rootclaim  = 0.35                     # well-grounded historical frequency, but blind to the recent GoF ramp
c_weissman   = 0.35                     # mechanistic per-lab base rate; agrees with Rootclaim to within ~2x
c_stansifer  = 1 - c_rootclaim - c_weissman          # 0.30 on the fatter-tailed location-free reading
base_odds_H43_H41 = (c_rootclaim  * odds_H43_rootclaim
                     + c_weissman  * odds_H43_weissman
                     + c_stansifer * odds_H43_stansifer_lf)   # ~1/67 blended, pre-circumstantial

# ---- Base odds of H-42 (unmodified zoonotic-collection leak) vs H-41 — location-free. -----------------
# Shares H-41's natural virus, so it needs the same rare pandemic-capable virus; only the ROUTE differs
# (research handling vs ordinary ecological contact). Anchor: Rootclaim (A-6) zoonotic-collection 6% vs
# zoonotic 78%. This 6% is a global historical prior, i.e. pre-location, matching the spine.
route_share_research = 6.0 / (6.0 + 78.0)             # A-6: ~0.07 of natural-virus emergences are collection-route
base_odds_H42_H41 = route_share_research / (1 - route_share_research)   # ~1/13, pre-circumstantial

# ============================ 2. CIRCUMSTANTIAL ADJUSTMENT FACTORS ========================
# Applied to the research-related members (H-42, H-43) relative to H-41. These no-observation arguments have
# NO evidence-edge, so this prior is their only home. All are approved/corrected, so I weigh their VALIDITY as
# reasoning — but every premise rests on Rootclaim's/Stansifer's low-trust say-so and several are contested, so
# each is softened well below its source's raw multiplier and none moves the weight enormously. The factors act
# on the shared "was this a Wuhan lab incident?" story, common to H-42 and H-43, so they scale the lab BLOC;
# the engineering-specific evidence that separates H-42 from H-43 is the step-8 genome edges, correctly absent.

# PRO-LAB --------------------------------------------------------------------------------
# f_wuhan — the single biggest crux of the whole debate (A-8 Rootclaim; A-38 Weissman, CORRECTED to make the
# ~4.4-logit magnitude contingent on the zoonosis reference class). Rootclaim prices it at ~20x (zoonotic /20,
# lab-escape unchanged); Weissman's raw ~4.4 logits is ~80x. Both are priced MODESTLY here because P(Wuhan |
# zoonosis) is NOT tiny: Wuhan is an 11M megacity, a major transport and wildlife-trade hub, and Huanan market
# trucked in live wildlife — so if zoonotic-spillover probability tracks human population/urbanisation/wildlife
# throughput (A-38's correction), the factor shrinks sharply. Plausible range ~2 (strong zoonosis-hub view) to
# ~20 (Rootclaim) to ~80 (Weissman raw). *** TOP LOAD-BEARING VARIABLE — flagged for steps 9-10. ***
f_wuhan = 5.0                           # modest lab-favouring factor; contested magnitude, wide range
# H-42 is field-collection-linked (the natural virus is sampled in southern-China caves, ~1500km away), so it
# is somewhat less Wuhan-locked than a pure WIV lab-escape. Rootclaim mirrors this: zoonotic-collection /2 vs
# lab-escape unchanged under Wuhan => H-42's Wuhan boost is ~half H-43's (in log terms).
wuhan_h42_share = 0.5                   # A-8: zoo-collection Wuhan boost ~half that of lab-escape

# f_wiv_biosafety (A-13): lax WIV biosafety / prior escapes of other coronaviruses. Rootclaim x2 on the lab
# members; softened — the premise rests largely on contested State-Department cables.
f_wiv_biosafety = 1.5
# f_database (A-14): post-outbreak database taken offline + BtCoV/4991 re-presented as "newly found" RaTG13,
# read as minimising WIV involvement. Rootclaim x2; softened — the offline-database reason (cited hacking) and
# the rename are real but their "consciousness of guilt" reading is contested.
f_database = 1.3
# f_nontransparency (A-15): China restricting WHO access, destroying samples, withholding data. Rootclaim x1.5;
# softened hard — China is opaque by default, so this is weak, near-uninformative evidence of a lab origin.
f_nontransparency = 1.2

# PRO-ZOONOSIS (favouring H-41) ----------------------------------------------------------
# f_absence_records (A-16, the non-whistleblower part): no pre-outbreak SARS-CoV-2 in any database/grant, and
# no immediate cordon of Wuhan — expected under a lab origin, absent here. Rootclaim /2.4 for the whole of A-16;
# the whistleblower slice of A-16 is carried by f_no_whistleblower to avoid double-counting it with A-28.
f_absence_records = 0.6
# f_no_whistleblower (A-28): the secret never escaped despite the many who would have known. Stansifer 1/10
# (himself down-adjusted from 1/64); softened further to ~1/1.8 because a lab origin with few witnesses could
# plausibly stay secret, and absence-of-evidence is weak. This is the shared whistleblower slice of A-16/A-28.
f_no_whistleblower = 0.55

# Net circumstantial multipliers (identical pro-lab/pro-zoonosis cluster for both research members except the
# Wuhan attenuation on H-42). Absent f_wuhan the cluster nets to ~0.77 (slightly pro-zoonosis: the cover-up
# signals A-13/A-14/A-15 are roughly cancelled by the absence-of-evidence signals A-16/A-28) — so essentially
# the ENTIRE circumstantial lab-tilt rests on f_wuhan, which is exactly why it is the crux.
circ_common  = f_wiv_biosafety * f_database * f_nontransparency * f_absence_records * f_no_whistleblower
circ_net_H43 = f_wuhan * circ_common                        # ~3.86
circ_net_H42 = (f_wuhan * wuhan_h42_share) * circ_common    # ~1.93

# ============================ 3. COMPOSE ============================
w_H43 = base_odds_H43_H41 * circ_net_H43       # ~0.058 : 1 vs H-41
w_H42 = base_odds_H42_H41 * circ_net_H42       # ~0.149 : 1 vs H-41
# Cross-check the sub-question's H-42:H-43 split (collection-leak vs GoF-leak): ~2.5:1 collection-favoured —
# a lab handling field-collected sarbecoviruses vastly outnumbers one running GoF, only partly offset by GoF's
# higher per-project chance of yielding a pandemic-capable virus, and slightly compressed by H-42's smaller
# Wuhan boost. The genome evidence at step 8 re-decides this split within the lab bloc.

# ---- H-44 residual — its own argued weight (rule 4), never a leftover; unaffected by circumstantial factors.
# What an unlisted origin looks like: a HYBRID history the three members cannot express (e.g. a lab-modified
# virus escaping into animals then spilling over naturally), a modeling-boundary error mis-placing the
# H-42/H-43 line (serial passage counted as "not manipulation"), or a mechanism no analysis in this corpus
# proposed. The three members cover the mechanism space fairly well, so this is small but real — weighted by
# how often a structured 3-way origin menu still misses the truth; never sanded to 0 (A-21 humility).
odds_H44_H41 = 0.03                     # ~2-3% of the normalised mass; uncommon but non-zero
w_H44 = odds_H44_H41 * w_H41

prior("HC-1", [w_H41, w_H42, w_H43, w_H44])
```

Normalised prior ≈ `[0.809, 0.120, 0.047, 0.024]` for `[H-41, H-42, H-43, H-44]` — zoonosis-favoured (~81%) with a meaningful research-related bloc (H-42+H-43 ≈ 16.7%), before the step-8 genome/institutional discriminating evidence. Two load-bearing drivers, flagged for steps 9-10: (1) `f_wuhan` — the Wuhan-location factor is the single biggest crux; setting it to 1 collapses the research bloc from ~16.7% to ~3.9%, and its defensible range (~2–80) spans most of the live disagreement. (2) `c_stansifer` / `odds_H43_stansifer_lf` — the fat-tailed location-free reference class that sets how high the base spine puts the lab members before any circumstantial adjustment. Within the lab bloc the unmodified-collection member (H-42) outweighs the engineered member (H-43) ~2.5:1 a priori, because the base rate of a lab merely handling field-collected sarbecoviruses exceeds that of one running gain-of-function; the genome evidence at step 8 is what can invert that.
