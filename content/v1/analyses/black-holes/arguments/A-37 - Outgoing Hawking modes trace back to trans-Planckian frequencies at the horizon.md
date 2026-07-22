---
id: A-37
type: argument
statement: "In the standard derivation, an outgoing Hawking quantum observed at late times traces back, through the exponential red-shift at the horizon, to field modes of formally unbounded (trans-Planckian) frequency near the horizon - so the derivation formally invokes physics at scales where quantum field theory in curved spacetime cannot be trusted, the technical origin of the 'trans-Planckian problem'."
source: "[[S-59 - Unruh 1976 — Notes on black-hole evaporation]]"
locator: "mode analysis within the rederivation (per step-2 source record; full text pp. 870-892 paywalled - not independently verified in this pass)"
affects_hypotheses: ["[[H-26 - Black holes emit a real thermal Hawking flux independent of collapse details]]"]
status: approved
reason_if_not_false: checked
---
Reasoning (depth-limited):

1. Outgoing wave packets reaching infinity at late time t originate as modes hugging the horizon, blue-shifted by a factor growing as e^{κt}; traced back far enough, their locally measured frequency exceeds the Planck frequency without bound.
2. The semiclassical derivation therefore assumes the free-field mode structure holds at arbitrarily high frequencies; if unknown Planck-scale physics modifies the dispersion relation or mode content there, the thermal-flux conclusion could in principle change.
3. This is the recurring principal technical objection (Jacobson, Helfer, Unruh-Wald) to treating Hawking evaporation as fully secure; Unruh 1976, by making the mode structure of the derivation explicit, is the canonical primary source of the problem (and much later work, including Unruh's own analogue-gravity results, addresses whether the flux survives modified dispersion).
4. Provenance caveat: the full text is paywalled; this node's attribution of the explicit trans-Planckian mode-tracing to this paper follows the step-2 source record and standard secondary literature, not a fresh read - treat locator-level specifics accordingly.

## Step 6 — validity verdict

**approved / checked.** Reconstruction — premises: (i) an outgoing packet observed at retarded time u traces back through the horizon region with blueshift growing as e^(kappa*u) (from the geometric-optics relation between affine parameter and retarded time, lambda ~ -C e^(-kappa*u)), so its locally measured frequency exceeds any bound; (ii) the semiclassical derivation assumes free-field mode structure at those frequencies. Conclusion: the derivation formally invokes physics outside the trust region of QFT in curved spacetime — the trans-Planckian problem. The exponential-blueshift step is elementary once the near-horizon geometry is granted, and the conclusion is deliberately weak ("formally invokes", "could in principle change") — no stronger claim is smuggled in. Valid as stated; the provenance caveat (attribution to this specific paper vs the secondary literature) is a sourcing issue already flagged in the body, not a validity failure. Traced directly.
