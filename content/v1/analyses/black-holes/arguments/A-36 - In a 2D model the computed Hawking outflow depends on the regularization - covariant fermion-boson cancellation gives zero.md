---
id: A-36
type: argument
statement: "In a two-dimensional black-hole model, applying fermion-boson cancellation on the stress-energy tensor reduces the computed energy outflow to zero, while other, noncovariant regularization techniques reproduce the Hawking result - demonstrating that the derived evaporation flux can depend on the choice of regularization scheme, a caveat on the robustness of the semiclassical derivation."
source: "[[S-59 - Unruh 1976 — Notes on black-hole evaporation]]"
locator: "two-dimensional model section (per abstract; full text pp. 870-892 paywalled)"
affects_hypotheses: ["[[H-26 - Black holes emit a real thermal Hawking flux independent of collapse details]]"]
status: approved
reason_if_not_false: checked
---
Reasoning (depth-limited; grounded in the abstract):

1. Computing the expectation value of the stress-energy tensor of a quantum field in a black-hole background requires regularizing divergences; the physical flux should not depend on the scheme.
2. In the 2D model Unruh investigates, a scheme using fermion-boson cancellation on ⟨Tμν⟩ yields zero energy outflow, whereas "other noncovariant techniques give the Hawking result" (abstract).
3. Scheme-dependence of this kind means the evaporation flux, at least in reduced models, is not an unambiguous output of the formalism - an early, technical instance of the derivation-robustness worries (later sharpened as the trans-Planckian problem and related critiques) that bear negatively on treating Hawking evaporation as fully secure.
4. Weight: 2D models omit greybody/backscattering structure of 4D holes; the mainstream resolution favors the covariant 4D calculations that do give a flux, but the point stands as a caveat internal to the primary literature itself.

## Step 6 — validity verdict

**approved / checked.** Reconstruction — premises: in a 2D black-hole model, a fermion-boson-cancellation regularization of the stress tensor gives zero outflow, while other, noncovariant schemes reproduce the Hawking flux. Conclusion: the computed evaporation flux can depend on the regularization scheme — a caveat on the robustness of the semiclassical derivation. Conditional on the premises the step is elementary: two schemes disagreeing on the same quantity *is* scheme-dependence. The conclusion is deliberately modest (a caveat, not "the 4D flux is wrong"), and the body already fences it correctly (2D models omit greybody structure; covariant 4D calculations give a flux). Whether the 2D computations are right is premise-truth, priced downstream. The inferential step itself is traced and valid.
