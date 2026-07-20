---
type: argument
id: A-6
statement: "Because the dose-response is concave (square-root), the marginal serum-cholesterol effect of an extra increment of dietary cholesterol falls as baseline intake rises, so linear extrapolation overstates incremental harm at habitual high intakes"
source: "[[S-8 - Serum cholesterol response to changes in the diet - the effect of dietary cholesterol (metabolic-ward dose-response series)]]"
locator: "Results/Discussion"
affects_observations:
  - "[[O-18 - Serum total cholesterol rises with dietary cholesterol (50-1450 mg-d) with diminishing returns, fit by a square-root dose-response]]"
affects_hypotheses:
  - "[[H-8 - Dietary cholesterol's effect on serum cholesterol is real but saturating, small at high habitual intakes]]"
status: approved
reason_if_not_false: checked
---

## Reasoning

The fitted relation is serum cholesterol proportional to the square root of dietary cholesterol dose. The derivative of sqrt(x) is 1/(2*sqrt(x)), a strictly decreasing function of x. Hence the marginal serum-cholesterol rise per additional mg of dietary cholesterol is largest near zero intake and shrinks monotonically as habitual intake grows: adding one egg (~185 mg) to a low-cholesterol diet moves serum cholesterol more than adding the same egg on top of an already-high-cholesterol diet. A linear model, by contrast, assigns a constant marginal effect and therefore overstates the incremental harm of extra eggs for people already eating substantial cholesterol. This is a purely mathematical consequence of the concavity of the fitted curve, independent of the mechanism.

## Step 6 verdict
**approved / checked.** Purely mathematical and verified directly: for S(x) = k*sqrt(x), S'(x) = k/(2*sqrt(x)), which is strictly decreasing on x>0, and S is concave (S'' = -k/(4*x^(3/2)) < 0). Hence the finite increment S(x+185) - S(x) is strictly decreasing in x, which is exactly the claim about an added egg at higher baseline intake, and a linear fit calibrated at low intake necessarily overstates that increment at high intake. Scope caveat that does not affect validity: the conclusion holds only inside the fitted 50-1450 mg/d range, and it is a statement about the fitted curve, not about whether the square-root form is the correct functional description — the latter is a premise, priced downstream.
