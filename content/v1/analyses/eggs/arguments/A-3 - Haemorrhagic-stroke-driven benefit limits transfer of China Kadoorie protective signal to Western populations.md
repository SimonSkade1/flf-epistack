---
id: A-3
type: argument
statement: "Because the aggregate egg-CVD HR is a composition-weighted mixture of endpoint-specific HRs, it is population-specific and not directly portable; the haemorrhagic-stroke-specific protection (0.74, the largest endpoint effect) applies to a smaller CVD share in the West — but since coronary disease (the dominant Western endpoint) is itself protective at 0.86-0.88, this does not establish that overall egg-CVD benefit moves toward null in Western populations, only that the aggregate figure should not be transferred as-is."
source: "[[S-80 - China Kadoorie Biobank egg consumption and CVD (Qin 2018 Heart)]]"
locator: "Discussion (Chinese vs Western CVD profile)"
affects_observations: ["[[O-11 - Daily egg intake associated with 26% lower haemorrhagic stroke incidence in China Kadoorie, strongest endpoint]]", "[[O-9 - Daily egg intake associated with 11% lower total CVD incidence in China Kadoorie Biobank]]"]
affects_hypotheses: ["[[H-6 - Moderate egg consumption causally lowers CVD risk in Chinese adults]]"]
status: corrected
reason_if_not_false: checked
---
The aggregate CVD hazard ratio is a case-count-weighted mixture of the endpoint-specific hazard ratios. In this cohort the daily-vs-rare endpoint HRs span 0.74 (haemorrhagic stroke) to 0.90 (ischaemic stroke), with coronary endpoints at 0.86-0.88; the aggregate 0.89 therefore sits near the ischaemic/coronary end because those endpoints supply most events even here. Crucially, the aggregate is pulled further from 1 wherever haemorrhagic stroke - the endpoint with the largest protective HR - contributes a larger event share.

Haemorrhagic stroke is a much larger fraction of total CVD in Chinese populations than in Western ones, where ischaemic heart disease and ischaemic stroke dominate. Re-weighting the same endpoint-specific HRs to a Western event mix (heavily coronary/ischaemic, HRs 0.88-0.90) would move the aggregate HR toward null relative to the 0.89 seen here. So even granting the endpoint-specific associations at face value, the size of the aggregate protective signal is partly a compositional feature of China's CVD profile and does not straightforwardly generalize.

This is a re-weighting (composition) inference and is valid regardless of whether the underlying endpoint associations are causal or confounded; it bounds how far the causal-protective reading can be exported to other populations but does not by itself adjudicate causation.

## Validity verdict — corrected (checked)

Reconstruction. The aggregate HR is an event-count-weighted mixture of endpoint-specific HRs: haemorrhagic stroke 0.74, coronary 0.86-0.88, ischaemic stroke 0.90, aggregate 0.89. Premise: haemorrhagic stroke is a larger share of CVD in China than in the West. Conclusion (as stated): "much of the aggregate benefit is haemorrhagic-stroke reduction," so re-weighting to a Western (ischaemic/coronary-dominated) mix moves the aggregate toward null and the benefit "need not transfer."

Traced step. The mixture framework is valid, but I traced the arithmetic against the argument's own numbers and two claims fail:
1. "Much of the benefit is haemorrhagic-stroke." The aggregate 0.89 sits at/above the coronary-ischaemic values (coronary 0.86-0.88, ischaemic 0.90), which is only possible if haemorrhagic stroke (0.74) carries a *small* event weight even in China — otherwise the aggregate would be pulled well below 0.86. So haemorrhagic stroke is not carrying "much" of the aggregate protection; its extra pull takes ~0.90 down to ~0.89 only.
2. "Western re-weight moves toward null" — undercutting defeater using the argument's own HRs. Western CVD is dominated by *coronary* disease, and coronary HR here is 0.86-0.88 — itself as protective as, or more than, the aggregate 0.89. A coronary-heavy Western mix would keep the aggregate protective (~0.87), not push it toward null. The body reaches "toward null" only by relabelling the Western mix as "coronary/ischaemic, HRs 0.88-0.90," quietly dropping coronary's protective 0.86 lower bound stated earlier — an inconsistency. Swapping haemorrhagic-stroke events for coronary events does move the aggregate marginally toward null (0.74 → 0.86), but the magnitude is small and the net Western aggregate is indeterminate/possibly still protective because coronary itself protects.

What survives (the corrected claim). The valid residual is compositional only: the aggregate HR is population-specific and shouldn't be transferred as-is, and the haemorrhagic-stroke-*specific* signal applies to fewer Western events. It does not establish that overall egg-CVD benefit shrinks toward null in the West.

## Original

statement: "Because the protective association is strongest for haemorrhagic stroke, which is a far larger share of CVD in China than in the West, much of the aggregate egg-CVD benefit here is haemorrhagic-stroke reduction and need not transfer to populations dominated by ischaemic/coronary disease."
