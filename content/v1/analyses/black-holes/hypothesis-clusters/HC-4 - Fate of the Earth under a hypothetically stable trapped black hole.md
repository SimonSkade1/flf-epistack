---
id: HC-4
type: hypothesis-cluster
question: "If a stable or long-lived LHC black hole were captured inside the Earth, what would happen?"
hypotheses:
  - "[[H-8 - An LHC-produced metastable black hole could accrete at the Eddington limit and become catastrophic]]"
  - "[[H-22 - Even hypothetically stable LHC black holes pose no risk to Earth on timescales below the Earth's natural lifetime]]"
  - "[[H-36 - A stable trapped black hole would lead to some outcome not listed here]]"
exclusivity: "Catastrophic Eddington-limited output and macroscopically negligible growth over the Sun's remaining lifetime cannot both describe the same trapped hole; the members are competing accounts of one scenario."
exhaustive_by_construction: false
independence: "All members are conditional on a stable trapped hole, so the cluster's prior ranges over outcomes within that scenario and does not move the base rate of whether the scenario obtains."
depends_on:
  - "HC-3: operative only under a non-evaporating decay outcome — the members are phrased conditionally on stability"
  - "HC-5: both named members' growth estimates lean on the transonic (Bondi-type) accretion law"
relevance: "This is the load-bearing question if a hole is both produced and stable — whether the disaster scenario survives its own accretion physics is where the risk claim is finally decided."
---
![[H-8 - An LHC-produced metastable black hole could accrete at the Eddington limit and become catastrophic]]
![[H-22 - Even hypothetically stable LHC black holes pose no risk to Earth on timescales below the Earth's natural lifetime]]
![[H-36 - A stable trapped black hole would lead to some outcome not listed here]]

Both named members grant the same extreme premise — a non-evaporating hole captured inside the Earth — and then disagree about everything that follows: runaway growth to Eddington-limited steady state with globally dangerous output, versus accretion so slow that nothing macroscopic happens before the Sun ends the question, with every faster channel excluded by the survival of white dwarfs and neutron stars. The residual covers intermediate regimes neither paper describes. The conditional phrasing is what lets this cluster factorize from the production and decay chain; the chain itself is recorded in depends_on rather than by folding the clusters together.

## Prior

```python
# HC-4 prior — fate of the Earth under a hypothetically stable trapped hole. Members in HC-4.hypotheses order:
# [H-8 catastrophic (the danger member: Plaga's Eddington-radiation scenario, and by extension any fast
# catastrophic Earth outcome), H-22 macroscopically negligible over the Sun's remaining lifetime
# (Giddings-Mangano safe), H-36 residual intermediate outcome].
#
# EVIDENCE PARTITION. The prior deliberately rests on FIRST-PRINCIPLES EARTH-ACCRETION physics alone,
# BEFORE the empirical compact-star survival evidence. That basis is the cluster's no-observation arguments
# (`no_observation_arguments.py ... --cluster HC-4`), consulted here and nowhere else: A-47 (approved,
# -> H-22) and A-48 (approved, -> H-22) give the accretion timescales as a function of the crossover radius
# R_C at which gravity turns 4-dimensional; A-7 and A-8 (approved, -> H-8) argue the compact-star exclusion
# has gaps. All SIX inbound E edges carry case-specific compact-star-survival / parameter-window observations
# that DISCRIMINATE H-22 from H-8 (white-dwarf survival E-39, neutron-star survival E-40+E-41 = CG-1,
# cosmic-ray survival E-42, Earth/Sun survival E-43, torsion-balance window E-44) — none is a base rate, so
# all are left UNMARKED for step 8. That is the whole "was the risk put to rest" story: Earth-accretion
# physics alone (this prior) leaves live danger windows open (A-48), and the resolution HINGES on the
# compact-star survival priced at step 8. depends_on HC-3 (stability) and HC-5 (Bondi accretion law) are
# approximations noted here, not imported. Standard constant used only in reasoning: Sun's remaining
# main-sequence lifetime ~5 Gyr (standard stellar evolution).

# The single controlling parameter is R_C. Split the stable-trapped-hole parameter space by it.
# f_macro = fraction where the D-dimensional force law reaches into the MACROSCOPIC regime (R_C >> 200 Ang:
# unwarped D=6 with R_D ~ 5e-2 cm, warped D=5 with R_C near the ~0.2 mm experimental bound). A-48 shows Earth
# is then consumed in ~1e4-1e5 yr << 5 Gyr — genuinely dangerous from Earth accretion alone. Generic
# TeV-gravity expectation puts the crossover at microscopic R_C, so the macroscopic case is a real minority.
f_macro = 0.4          # would be right if ~40% of the plausible (D, warping) space has a macroscopic force law
f_micro = 1 - f_macro  # complement: R_C <~ 200 Ang, the region A-47 covers (identity, not an estimate)

# H-8 — catastrophic / danger. Holds in the macroscopic region, IF the fast accretion there truly runs away
# rather than being throttled. Plaga's specific Eddington-limited mechanism is contested (Giddings-Mangano and
# Koch-Bleicher-Stocker rebut the Eddington-limit reasoning; A-53 denies any Eddington throttle), but A-48's
# un-throttled ~1e4-1e5 yr consumption is a first-principles result, and A-7/A-8 (approved) argue the
# compact-star bounds that would otherwise close this region have gaps (Eddington-invisible holes in compact
# stars; sub-M_min quantum-gravity holes escaping) — so this stays well off zero. Least confident of the three.
p_cat_given_macro = 0.6   # right if, given a macroscopic force law, catastrophe is a bit more likely than not
w_catastrophic = f_macro * p_cat_given_macro   # H-8

# H-22 — negligible over the Sun's remaining lifetime. Holds across the microscopic-R_C region, where A-47
# gives Earth-accretion timescales 3e11 yr (D>=8) to 6.4-94 Gyr (D=7), all >> 5 Gyr, safe from Earth ALONE.
# High but not full: the low end of the D=7 band (6.4 Gyr) only barely clears the solar lifetime, and A-47's
# assumptions are uniformly growth-MAXIMIZING so the safe conclusion is conservative. Most confident member.
p_safe_given_micro = 0.85   # right if H-22's account holds in ~85% of the microscopic-R_C region
w_negligible = f_micro * p_safe_given_micro    # H-22

# H-36 — residual intermediate outcome, priced on its own (rule 4), not as a leftover. Concretely: the
# borderline D=7 case whose ~6.4-94 Gyr band straddles the solar lifetime (damaging on a long but sub-solar
# timescale), or a sub-Eddington-but-nonzero heating regime, or an A-7/A-8 gap that leaves an Earth outcome
# the two papers bracket but neither describes. Given first-principles accretion smoothly interpolates between
# the two named extremes, an unmodelled middle is a real, moderate possibility — more than the residual of a
# sharply dichotomous cluster, less than either named member.
w_residual = 0.13   # ~0.13 : (0.24+0.51) odds vs the named members; ~15% of the mass once normalised

prior("HC-4", [w_catastrophic, w_negligible, w_residual])
```
