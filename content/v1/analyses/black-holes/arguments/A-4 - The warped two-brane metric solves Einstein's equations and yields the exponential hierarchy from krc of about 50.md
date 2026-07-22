---
id: A-4
type: argument
statement: "An exact solution of the 5D Einstein equations with two 3-branes of opposite tension bounding a slice of AdS5 exists, in which the 4D Planck mass is essentially independent of the compactification radius while every visible-brane mass parameter is rescaled by e^(-k rc pi) - so krc ~ 11-12, i.e. k rc pi ~ 35 (an O(10) input, no large number; the paper's own 'krc ~ 50' phrasing is consistent only as M rc ~ 50 with k a factor of a few below M) generates the full 10^15 weak-Planck hierarchy."
source: "[[S-19 - Randall, Sundrum 1999 — warped 5D hierarchy (RS1)]]"
locator: "§3-4, eqs. (6)-(21)"
affects_hypotheses: ["[[H-4 - A single warped extra dimension (RS1) generates the weak-Planck hierarchy exponentially]]"]
status: corrected
reason_if_not_false: checked
---
## Reasoning

1. Ansatz ds^2 = e^(-2 sigma(phi)) eta_mn dx^m dx^n + rc^2 dphi^2 on S^1/Z_2 with branes at phi = 0, pi. The 55-Einstein equation gives sigma' = rc sqrt(-Lambda/24M^3) (requires Lambda < 0), and the delta-function (mn) equations are solved only if the brane tensions and bulk cosmological constant are tuned to a single scale k - V_hid = -V_vis = 24 M^3 k, Lambda = -24 M^3 k^2 - yielding sigma = k rc |phi|, an AdS5 slice (the same relations that arise in the 5D Horava-Witten effective theory). Trusted for k < M so bulk curvature stays sub-Planckian.
2. Integrating out phi - M_Pl^2 = (M^3/k)(1 - e^(-2 k rc pi)) - depends only weakly on rc for large krc.
3. The visible-brane induced metric carries the warp factor - g_vis = e^(-2 k rc pi) g-bar - so after canonical normalization any fundamental mass parameter m_0 on the visible brane becomes the physical mass m = e^(-k rc pi) m_0 (shown explicitly for the Higgs vev, and general since all operators rescale by conformal weight).
4. Hence e^(k rc pi) ~ 10^15, i.e. krc ~ 50, converts near-Planckian inputs v_0, k, M, 1/rc into TeV-scale visible physics. Equivalently (coordinate rescaling x -> e^(k rc pi) x) the weak scale is fundamental and M_Pl is the derived large scale, produced by the small graviton wave-function overlap with our brane.

A consistency demonstration - it establishes that the warped hypothesis is a genuine solution with no large input hierarchies, not that the geometry is realized. Caveat noted in the paper - the modulus rc must be stabilized (mass at least ~10^-4 eV), a problem not solved there.

## Step 6 — validity verdict

**corrected / checked.** The solution chain retraces cleanly: the 55-equation fixing sigma' (requiring Lambda < 0), the delta-function junction conditions tuning V_hid = -V_vis = 24 M^3 k and Lambda = -24 M^3 k^2 to give sigma = k rc |phi|; M_Pl^2 = (M^3/k)(1 - e^(-2 k rc pi)) from integrating out phi; and the conformal rescaling m = e^(-k rc pi) m_0, shown for the Higgs vev and general by conformal weight. The numeric step fails as stated: e^(k rc pi) ~ 1e15 gives k rc pi = ln(1e15) ~ 35, i.e. krc ~ 11 — not 50 (krc = 50 would give e^(-50 pi) ~ 1e-68). The source itself writes "we only require krc ~ 50" (p. 5, after Eq. (21)), in tension with its own Eq. (21) by the same arithmetic; its introduction's consistent figure is that the ratio of the 5D Planck scale to mu_c = 1/rc "is only of order 50", i.e. M rc ~ 50, which matches krc ~ 11 when k sits the required factor of a few below M (sub-Planckian curvature, k < M). Statement corrected to krc ~ 11-12; the qualitative conclusion — an O(10-50), non-hierarchical input generates the full ~1e15 hierarchy — is unaffected, as is everything downstream that uses only the exponential mechanism. Arithmetic and junction-condition algebra checked directly.

## Original

An exact solution of the 5D Einstein equations with two 3-branes of opposite tension bounding a slice of AdS5 exists, in which the 4D Planck mass is essentially independent of the compactification radius while every visible-brane mass parameter is rescaled by e^(-k rc pi) - so krc ~ 50 (an O(50) input, no large number) generates the full 10^15 weak-Planck hierarchy.
