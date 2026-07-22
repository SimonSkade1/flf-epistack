---
id: A-13
type: argument
statement: Via EOS-independent analytic solutions of Einstein's equations, the existence of a 1.97 +/- 0.04 Msun neutron star sets an upper limit on the maximum possible mass density of stable cold matter of <~ 4e15 g cm^-3 (~10 times nuclear saturation density), and excludes every equation of state whose mass-radius curve never reaches 1.97 Msun.
source: "[[S-66 - Demorest et al. 2010 — Shapiro delay measurement of a two-solar-mass neutron star]]"
locator: "p. 6 (citing Lattimer & Prakash, PRL 94, 111101); Fig. 3"
affects_observations: ["[[O-1 - PSR J1614-2230 pulsar mass measured at 1.97 solar masses via Shapiro delay]]"]
affects_hypotheses: ["[[H-1 - Neutron-star matter has a stiff equation of state - no hyperons, bosons, or free quarks near nuclear saturation density]]"]
status: approved
reason_if_not_false: trusted
---
## Reasoning

1. In GR, any EOS for cold matter determines a unique nonrotating mass-radius sequence with a maximum mass; a star observed at mass M excludes every EOS with maximum mass < M. This step is deductive: it needs only that GR describe the star's gravity (which the same system's Shapiro delay presupposes and later systems test).
2. Lattimer & Prakash's EOS-independent analytic bound inverts this: given the largest measured mass, the central density of the maximum-mass configuration cannot exceed a value scaling as M^-2; for M = 1.97 Msun this gives rho_max <~ 4e15 g cm^-3, i.e. ~10 n_s.
3. Consequences drawn in the paper: soft EOSs with hyperon/kaon-condensate softening (e.g. GS1, GM3) fall below the J1614-2230 band and are ruled out; condensed quark matter is constrained but not fully excluded (some strange-quark-matter models survive).
4. The nontrivial content is the quantitative EOS-independent density bound (step 2-3); it converts a single mass number into a universal statement about the densest stable cold matter our world contains.

## Validity verdict (step 6)

Reconstruction: premise 1 = GR determines, per EOS, a maximum nonrotating mass (so an observed 1.97 Msun star excludes every EOS with Mmax below it) - traced, elementary. Premise 2 / load-bearing step = the Lattimer-Prakash EOS-independent analytic bound rho_max ∝ M^-2, giving ~4e15 g/cm3 at 1.97 Msun. That derivation (PRL 94, 111101; Tolman-solution-based) is a specialist GR calculation not feasibly traced here, so the verdict is trusted - on the grounds that the bound is independently reused across the neutron-star EOS literature with no published refutation, not on author identity. The instantiation from the bound to the quoted number is checked.
