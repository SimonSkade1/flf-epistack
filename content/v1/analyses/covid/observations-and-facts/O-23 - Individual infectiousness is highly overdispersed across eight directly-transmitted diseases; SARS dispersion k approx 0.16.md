---
id: O-23
link_state: linked
type: observation
statement: "Fitting Poisson, geometric and negative-binomial offspring distributions to contact-tracing data from eight directly-transmitted human diseases, Lloyd-Smith et al. find individual infectiousness (individual reproductive number nu, gamma-distributed with mean R0 and dispersion k) is highly right-skewed and the homogeneous-Poisson model is almost always strongly rejected: for SARS (Singapore 2003) k=0.16 (90% CI 0.11-0.64), with 73% of cases having nu<1 and 6% having nu>8; measles shows similarly high variation, smallpox and monkeypox intermediate, pneumonic plague slightly less."
source: "[[S-87 - Lloyd-Smith et al. 2005 — Superspreading and the effect of individual variation on disease emergence]]"
locator: "p.355-356, Fig 1 and Supplementary Table 1"
quote: "For the Singapore outbreak, the maximum-likelihood estimate k is 0.16 (90% confidence interval 0.11-0.64) ... the great majority of SARS cases in Singapore were barely infectious (73% had nu < 1) but a small proportion were highly infectious (6% had nu > 8)."
data_basis: ["[[S-87 - Lloyd-Smith et al. 2005 — Superspreading and the effect of individual variation on disease emergence]]"]
---
Empirical offspring distributions from detailed contact-tracing/surveillance datasets for eight directly-transmitted diseases; negative binomial(R0,k) has variance R0(1+R0/k), so smaller k means greater heterogeneity (k->inf Poisson, k=1 geometric).
