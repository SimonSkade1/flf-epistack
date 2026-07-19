"""Checks the runner against every number published in the step 7 and step 8
specs. Fixtures are the two micro-examples, copied verbatim into throwaway
notes — so if a spec's numbers and this runner ever disagree, this fails.

    python3 test_run.py
"""

import tempfile
import pathlib
import run as R

# --- fixtures: the two micro-examples, as an analysis would hold them -------

HC2 = '''---
type: hypothesis-cluster
---

## Prior

```python
# HC-2 prior — when did first human occupation of Sahul begin?
p_pre50_sound = 0.35       # 1 of the 3 published pre-50 ka horizons survived re-dating
width_pre50_kyr = 10.0     # 60-50 ka; flat-in-time colonisation prior gives mass by width
w_early = p_pre50_sound * width_pre50_kyr
p_window_sound = 0.80      # three independent dating methods agree across this window
width_window_kyr = 5.0     # 50-45 ka
w_window = p_window_sound * width_window_kyr
p_post45_live = 0.08       # no accepted horizon after 45 ka, but not closed either
width_post45_kyr = 3.0     # 45-42 ka
p_no_single_onset = 0.10   # multi-founder colonisations are common elsewhere
w_residual = p_post45_live * width_post45_kyr + p_no_single_onset * width_window_kyr
prior("HC-2", [w_early, w_window, w_residual])
```
'''

# Step 7's example states HC-1's prior as [0.22, 0.40, 0.28, 0.10] rather than
# deriving it; this stands in for step 8's block on that cluster.
HC1 = '''---
type: hypothesis-cluster
---

## Prior

```python
w_H3 = 0.22    # stand-in for HC-1's own fermi decomposition
w_H11 = 0.40
w_H21 = 0.28
w_H42 = 0.10
prior("HC-1", [w_H3, w_H11, w_H21, w_H42])
```
'''

E14 = '''---
type: evidence-link
---

## Likelihood

```python
# HC-1 — ONE joint estimate for E-14 + E-22: both observations rest on D-4 (rule 1).
p_ages_H3 = 0.30   # fits the tight cluster; fits 3 genera surviving 5 kyr worst
p_ages_H11 = 0.50  # only member predicting both halves of the pattern
p_ages_H21 = 0.10  # aridification predicts ages track the aridity maximum
p_ages_H42 = 0.20  # unlisted driver: neither predicts the pattern nor forbids it
t_dates = 0.55     # cap = min trust_score over {O-14, O-22} = 0.9; docked well below
evidence("HC-1", ["O-14", "O-22"], [p_ages_H3, p_ages_H11, p_ages_H21, p_ages_H42], t=t_dates)
```
'''


def build(tmp):
    d = pathlib.Path(tmp)
    (d / "HC-2 When did first occupation begin.md").write_text(HC2)
    (d / "HC-1 What drove the extinction pulse.md").write_text(HC1)
    (d / "E-14 O-14 to HC-1.md").write_text(E14)
    return d


def close(got, want, tol=5e-5):
    return len(got) == len(want) and all(abs(a - b) < tol for a, b in zip(got, want))


def main():
    failures = []

    def check(name, got, want):
        ok = close(got, want)
        print(f"{'PASS' if ok else 'FAIL'}  {name}")
        if not ok:
            print(f"      got  {[round(x, 4) for x in got]}")
            print(f"      want {want}")
            failures.append(name)

    with tempfile.TemporaryDirectory() as tmp:
        d = build(tmp)

        m = R.run(d)
        # --- step 8's published numbers
        check("step 8: HC-2 prior", m.prior_of("HC-2"), [0.4248, 0.4854, 0.0898])

        m2 = R.run(d, {("HC-2", "p_pre50_sound"): 0.6})
        check("step 8: HC-2 prior, p_pre50_sound -> 0.6",
              m2.prior_of("HC-2"), [0.5587, 0.3724, 0.0689])

        # --- step 7's published numbers
        check("step 7: HC-1 posterior at t=0.55",
              m.posterior("HC-1"), [0.2146, 0.5303, 0.1750, 0.0800])
        check("step 7: HC-1 posterior at t=0.9 (the trust cap)",
              R.run(d, {("E-14", "t_dates"): 0.9}).posterior("HC-1"),
              [0.2112, 0.6132, 0.1083, 0.0673])
        check("step 7: HC-1 posterior at t=1",
              R.run(d, {("E-14", "t_dates"): 1.0}).posterior("HC-1"),
              [0.2102, 0.6369, 0.0892, 0.0637])
        check("step 7: HC-1 posterior at t=0 is exactly the prior",
              R.run(d, {("E-14", "t_dates"): 0.0}).posterior("HC-1"),
              [0.22, 0.40, 0.28, 0.10])

        # --- properties the spec asserts rather than shows
        check("determinism: identical on re-run",
              R.run(d).posterior("HC-1"), m.posterior("HC-1"))

        rev = R.run(d)
        rev.ev["HC-1"] = list(reversed(rev.ev["HC-1"]))
        check("edges commute (anchor is the prior, not the running posterior)",
              rev.posterior("HC-1"), m.posterior("HC-1"))

        # --- the determinism guard actually bites
        (d / "bad.md").write_text("## Prior\n\n```python\nimport os\n```\n")
        try:
            R.run(d)
            print("FAIL  determinism guard rejects `import`")
            failures.append("guard")
        except ValueError as e:
            print(f"PASS  determinism guard rejects `import` ({e})")

    print()
    print(f"{'ALL PASS' if not failures else str(len(failures)) + ' FAILED'}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
