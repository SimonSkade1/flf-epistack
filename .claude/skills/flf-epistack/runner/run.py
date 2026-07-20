"""Runner for the FLF epistemic stack.

Extracts the python blocks from an analysis's markdown notes, runs them, and
composes each cluster's posterior. Implements the contract in the step 7 and
step 8 modes of the flf-epistack skill and nothing else.

Generic tooling: it reads an analysis directory given on the command line and
writes nothing into it. See ../SKILL.md for how the pipeline invokes it and
what steps 7/8 must write into the notes for it to run.

Usage:
    python3 run.py <analysis-dir> [--set BLOCK:var=value ...]
    python3 test_run.py          # self-check against the specs' published numbers
"""

import re
import sys
import pathlib

HEADING = re.compile(r"^##\s+(Prior|Likelihood)\s*$")
FENCE = re.compile(r"^```python\s*$")
ASSIGN = re.compile(r"^\s*([A-Za-z_]\w*)\s*=")
# Blocks are arithmetic over named variables and the two registrar calls.
# Anything that could reach outside that is a determinism hole (criterion 14).
BANNED = re.compile(r"\b(import|open|eval|exec|globals|locals|__\w+__)\b")


def extract(text, block_id):
    """Yield (kind, block_id, source) for each ## Prior / ## Likelihood block.

    One fenced block per heading; a second fence under the same heading is not
    part of the contract and is ignored.
    """
    out, lines, kind, i = [], text.splitlines(), None, 0
    while i < len(lines):
        line = lines[i]
        h = HEADING.match(line)
        if h:
            kind = h.group(1).lower()
        elif line.startswith("## "):
            kind = None
        elif kind and FENCE.match(line):
            body, j = [], i + 1
            while j < len(lines) and not lines[j].startswith("```"):
                body.append(lines[j])
                j += 1
            out.append((kind, block_id, "\n".join(body)))
            kind, i = None, j
        i += 1
    return out


def apply_overrides(source, block_id, overrides):
    """--set BLOCK:name=value. The note is authoritative, so an override
    rewrites the assignment in place — the variable is used further down its
    own block."""
    out = []
    for line in source.splitlines():
        m = ASSIGN.match(line)
        if m and (block_id, m.group(1)) in overrides:
            indent = line[: len(line) - len(line.lstrip())]
            line = f"{indent}{m.group(1)} = {overrides[(block_id, m.group(1))]!r}"
        out.append(line)
    return "\n".join(out)


class Model:
    def __init__(self):
        self.weights = {}   # hc -> relative weights, HC.hypotheses order
        self.ev = {}        # hc -> [(obs, lik, t)]

    # ---- the two calls a block may make -------------------------------

    def prior(self, hc, w):
        if hc in self.weights:
            raise ValueError(f"{hc}: prior registered twice")
        w = [float(x) for x in w]
        if not all(x > 0 for x in w):
            raise ValueError(f"{hc}: every weight must be strictly positive")
        self.weights[hc] = w

    def evidence(self, hc, obs, lik, t):
        lik = [float(x) for x in lik]
        if not all(x > 0 for x in lik):
            raise ValueError(f"{hc}: every likelihood must be strictly positive")
        if not 0 <= float(t) <= 1:
            raise ValueError(f"{hc}: t={t} outside [0, 1]")
        self.ev.setdefault(hc, []).append((list(obs), lik, float(t)))

    # ---- composition (step 8 owns it; implemented once, here) ---------

    def prior_of(self, hc):
        w = self.weights[hc]
        s = sum(w)
        return [x / s for x in w]

    def posterior(self, hc):
        p = self.prior_of(hc)
        k = len(p)
        acc = list(p)
        for obs, lik, t in self.ev.get(hc, []):
            if len(lik) != k:
                raise ValueError(
                    f"{hc}: likelihood vector has {len(lik)} entries, prior has {k}")
            marg = sum(p[j] * lik[j] for j in range(k))   # anchor: normalised prior
            for i in range(k):
                acc[i] *= t * lik[i] + (1 - t) * marg
        s = sum(acc)
        return [x / s for x in acc]

    def clusters(self):
        return sorted(self.weights)


def run(notes_dir, overrides=None):
    overrides = overrides or {}
    blocks = []
    for f in sorted(pathlib.Path(notes_dir).rglob("*.md")):
        blocks += extract(f.read_text(), f.stem.split(" ")[0])
    # Priors before likelihoods; then by block id. Order is fixed, so a run is
    # reproducible and edges within a cluster commute anyway (the mixture
    # anchor is the prior, never the running posterior).
    blocks.sort(key=lambda b: (0 if b[0] == "prior" else 1, b[1]))

    m = Model()
    for kind, bid, src in blocks:
        bad = BANNED.search(src)
        if bad:
            raise ValueError(f"{bid}: '{bad.group()}' is not allowed in a block")
        env = {"prior": m.prior, "evidence": m.evidence, "__builtins__": {}}
        exec(compile(apply_overrides(src, bid, overrides), f"<{kind}:{bid}>", "exec"), env)
    return m


def main(argv):
    if not argv:
        print(__doc__.strip())
        return 1
    notes_dir, overrides = argv[0], {}
    for arg in argv[1:]:
        if arg == "--set":
            continue
        block_var, _, value = arg.partition("=")
        block, _, var = block_var.partition(":")
        overrides[(block, var)] = float(value)

    m = run(notes_dir, overrides)
    for hc in m.clusters():
        pri = [round(x, 4) for x in m.prior_of(hc)]
        post = [round(x, 4) for x in m.posterior(hc)]
        n = len(m.ev.get(hc, []))
        print(f"{hc}  prior {pri}  posterior {post}  ({n} evidence block(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
