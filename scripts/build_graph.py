#!/usr/bin/env python3
"""Export one EpiStack analysis as a navigable model graph (graph.json).

The graph the Obsidian/Quartz link-graph draws is *structural* — every note is a
node and every wikilink an edge, all the same weight. This exporter draws the
*epistemic model* instead:

  - evidence-links are EDGES (observation → hypothesis-cluster), not nodes, and
    each carries the likelihood-ratio vector it contributes to the Bayesian
    update — so you can see which hypotheses a datum supports and by how much;
  - hypotheses carry their prior and posterior probability (recomputed from the
    notes by the very same runner that the pipeline uses, ../content/v1/pipeline/
    runner/run.py — never hand-copied);
  - node URLs are the real Quartz slugs, read out of a built
    public/static/contentIndex.json, so a click in the viewer opens the note.

Usage:
    python3 scripts/build_graph.py <analysis-dir> \
        [--content-index public/static/contentIndex.json] \
        [--content-root content] \
        [--out quartz/static/model/graph.json] \
        [--self-check]

`--self-check` re-runs run.py's own composition and asserts our posteriors match
its printed numbers, so a math divergence fails loudly instead of shipping.
"""

import argparse
import json
import pathlib
import re
import sys

import yaml

# --- reuse the pipeline runner verbatim (single source of Bayesian truth) -----
REPO = pathlib.Path(__file__).resolve().parent.parent
RUNNER = REPO / "content" / "v1" / "pipeline" / "runner"
sys.path.insert(0, str(RUNNER))
import run as runner  # noqa: E402  (path set above)

# Node-type colours — mirrors quartz/styles/custom.scss so the viewer is
# self-contained. Keep in sync if the SCSS palette changes.
NODE_COLORS = {
    "source": {"light": "#1d4ed8", "dark": "#7aa2f7"},
    "data-basis": {"light": "#0e7490", "dark": "#22d3ee"},
    "observation": {"light": "#15803d", "dark": "#4ade80"},
    "hypothesis": {"light": "#6d28d9", "dark": "#b39dfa"},
    "hypothesis-cluster": {"light": "#a21caf", "dark": "#e879f9"},
    "evidence-link": {"light": "#b45309", "dark": "#fbbf24"},
    "correlation-group": {"light": "#78350f", "dark": "#fdba74"},
    "argument": {"light": "#be123c", "dark": "#fb7185"},
    "cluster-review": {"light": "#475569", "dark": "#94a3b8"},
    "main-report": {"light": "#0f172a", "dark": "#e2e8f0"},
}

ID_RE = re.compile(r"([A-Za-z]+-\d+)")
WIKILINK_RE = re.compile(r"\[\[\s*([^\]]+?)\s*\]\]")


def first_id(text):
    """Leading node id in a string, e.g. '[[H-2 - Moderate ...]]' -> 'H-2'."""
    m = ID_RE.match(text.strip())
    return m.group(1) if m else None


def wikilink_ids(value):
    """All node ids referenced by a frontmatter value (str, list, or nested)."""
    out = []
    if value is None:
        return out
    if isinstance(value, str):
        for target in WIKILINK_RE.findall(value):
            wid = first_id(target)
            if wid:
                out.append(wid)
        # bare id (e.g. source: S-12 without wikilink brackets)
        if not out:
            m = ID_RE.fullmatch(value.strip().strip('"'))
            if m:
                out.append(m.group(1))
    elif isinstance(value, (list, tuple)):
        for item in value:
            out.extend(wikilink_ids(item))
    return out


def split_frontmatter(text):
    """Return (frontmatter_dict, body_str). Empty dict if no frontmatter."""
    if not text.startswith("---"):
        return {}, text
    lines = text.splitlines()
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return {}, text
    fm_text = "\n".join(lines[1:end])
    body = "\n".join(lines[end + 1 :])
    try:
        fm = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError:
        fm = {}
    if not isinstance(fm, dict):
        fm = {}
    return fm, body


# --- provenance-tracking Model: which note block produced each evidence() ----
class TracedModel(runner.Model):
    def __init__(self):
        super().__init__()
        self.by_block = {}  # block id (E-* or CG-*) -> {"hc","lik","t"}
        self._bid = None

    def evidence(self, hc, obs, lik, t):
        super().evidence(hc, obs, lik, t)
        if self._bid is not None:
            self.by_block[self._bid] = {
                "hc": hc,
                "lik": [float(x) for x in lik],
                "t": float(t),
            }


def run_model(analysis_dir):
    """Mirror runner.run() but keep block provenance. Returns TracedModel."""
    blocks = []
    for f in sorted(pathlib.Path(analysis_dir).rglob("*.md")):
        bid = f.stem.split(" ")[0]
        blocks += runner.extract(f.read_text(), bid)
    blocks.sort(key=lambda b: (0 if b[0] == "prior" else 1, b[1]))

    m = TracedModel()
    for kind, bid, src in blocks:
        bad = runner.BANNED.search(runner.code_only(src))
        if bad:
            raise ValueError(f"{bid}: '{bad.group()}' is not allowed in a block")
        m._bid = bid
        env = {"prior": m.prior, "evidence": m.evidence, "__builtins__": {}}
        exec(compile(src, f"<{kind}:{bid}>", "exec"), env)
    m._bid = None
    return m


def sluggify(s):
    """Replicates Quartz's sluggify (quartz/util/path.ts). Verified against a
    full build's contentIndex: 0 mismatches over 1552 slugs. Computing slugs
    here (instead of reading contentIndex) lets graphs be generated in one pass,
    before the Quartz build, so a newly-added analysis needs no bootstrap build."""
    segs = []
    for seg in s.split("/"):
        seg = re.sub(r"\s", "-", seg)
        seg = seg.replace("&", "-and-").replace("%", "-percent")
        seg = seg.replace("?", "").replace("#", "")
        segs.append(seg)
    return re.sub(r"/$", "", "/".join(segs))


def slug_of(rel):
    """Content-relative file path (e.g. 'v1/.../H-1 - x.md') -> '/' + Quartz slug."""
    rel = rel.strip("/")
    if rel.endswith(".md"):
        rel = rel[:-3]
    elif rel.endswith(".html"):
        rel = rel[:-5]
    slug = sluggify(rel)
    if slug.endswith("_index"):
        slug = slug[:-6] + "index"
    return "/" + slug


def verify_slugs(content_index_path, computed):
    """Cross-check computed node urls against a built contentIndex, if present.
    Returns list of (id, computed, actual) mismatches (empty = all good)."""
    idx = json.loads(pathlib.Path(content_index_path).read_text())
    by_fp = {}
    for slug, meta in idx.items():
        fp = meta.get("filePath")
        if fp:
            key = fp[:-3] if fp.endswith(".md") else fp
            by_fp[key] = "/" + slug
    bad = []
    for rel_noext, url in computed.items():
        actual = by_fp.get(rel_noext)
        if actual is not None and actual != url:
            bad.append((rel_noext, url, actual))
    return bad


def discrimination(lik):
    """How informative an LR vector is: log-spread between best and worst fit.
    Anchor is 1.0 (best), so this is -log(min); 0 means uninformative."""
    import math

    lo = min(lik)
    return round(-math.log(lo), 3) if lo > 0 else 0.0


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("analysis_dir")
    ap.add_argument("--content-index", default="public/static/contentIndex.json")
    ap.add_argument("--content-root", default="content")
    ap.add_argument("--out", default="quartz/static/model/graph.json")
    ap.add_argument("--self-check", action="store_true")
    args = ap.parse_args(argv)

    analysis_dir = pathlib.Path(args.analysis_dir).resolve()
    content_root = (REPO / args.content_root).resolve()
    slug_computed = {}  # rel-noext -> url, for optional contentIndex cross-check

    # ---- 1. parse every note into a node -----------------------------------
    nodes = {}  # id -> node dict
    fm_by_id = {}  # id -> frontmatter (for edge building)
    url_by_id = {}  # id -> url (all typed files, incl. edge-only E/CG)
    main_id = None
    for f in sorted(analysis_dir.rglob("*.md")):
        text = f.read_text()
        fm, body = split_frontmatter(text)
        ntype = fm.get("type")
        if not ntype:
            continue  # non-node markdown (problem-log, etc.)

        nid = fm.get("id")
        nid = str(nid).strip().strip('"') if nid is not None else None
        if not nid:
            nid = f.stem.split(" ")[0]
        if ntype == "cluster-review":
            # these notes carry no id and all begin "Analysis of ..."; key them
            # by the cluster they review so the three don't collide on one id.
            cl = wikilink_ids(fm.get("cluster"))
            nid = f"review-{cl[0]}" if cl else f"review-{f.stem[:20]}"
        if ntype == "main-report":
            nid = "MAIN"
            main_id = "MAIN"

        rel = f.relative_to(content_root).as_posix()
        rel_noext = rel[:-3] if rel.endswith(".md") else rel
        url = slug_of(rel)
        slug_computed[rel_noext] = url

        title = fm.get("statement") or fm.get("title") or f.stem
        if ntype == "main-report":
            m = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
            if m:
                title = m.group(1).strip()

        fm_by_id[nid] = fm
        url_by_id[nid] = url
        # evidence-links render as EDGES (observation -> cluster, or observation
        # -> correlation-group when grouped), so they are not emitted as nodes
        # (their frontmatter is kept above for edge building). Correlation-groups
        # ARE nodes: each is one joint witness its member observations feed into.
        if ntype == "evidence-link":
            continue

        node = {
            "id": nid,
            "type": ntype,
            "label": f.stem if ntype != "main-report" else "Main question",
            "title": str(title),
            "url": url,
        }
        if ntype == "source" and "trust_score" in fm:
            node["trust"] = fm.get("trust_score")
        if ntype == "hypothesis":
            cl = wikilink_ids(fm.get("cluster"))
            node["cluster"] = cl[0] if cl else None
        if ntype == "correlation-group":
            node["label"] = nid
            node["to"] = (wikilink_ids(fm.get("to")) or [None])[0]
            node["members"] = wikilink_ids(fm.get("members"))
        nodes[nid] = node

    # ---- 2. Bayesian model: priors, posteriors, per-edge LRs ----------------
    model = run_model(analysis_dir)

    # member id order per cluster, from HC.hypotheses frontmatter
    members_of = {}
    for nid, fm in fm_by_id.items():
        if fm.get("type") == "hypothesis-cluster":
            members_of[nid] = wikilink_ids(fm.get("hypotheses"))

    # attach prior/posterior to hypotheses and clusters
    for hc in model.clusters():
        pri = model.prior_of(hc)
        post = model.posterior(hc)
        members = members_of.get(hc, [])
        if hc in nodes:
            nodes[hc]["members"] = members
            nodes[hc]["priors"] = [round(x, 4) for x in pri]
            nodes[hc]["posteriors"] = [round(x, 4) for x in post]
            nodes[hc]["nEvidence"] = len(model.ev.get(hc, []))
        for i, mid in enumerate(members):
            if mid in nodes and i < len(post):
                nodes[mid]["prior"] = round(pri[i], 4)
                nodes[mid]["posterior"] = round(post[i], 4)

    # ---- 3. edges -----------------------------------------------------------
    edges = []
    seen = set()

    def add_edge(kind, src, dst, **extra):
        if src not in nodes or dst not in nodes or src == dst:
            return
        key = (kind, src, dst, extra.get("id"))
        if key in seen:
            return
        seen.add(key)
        e = {"kind": kind, "source": src, "target": dst}
        e.update(extra)
        edges.append(e)

    def mk_lik(lik_block):
        members = members_of.get(lik_block["hc"], [])
        lik = lik_block["lik"]
        favors = None
        if members and len(members) == len(lik):
            favors = members[max(range(len(lik)), key=lambda i: lik[i])]
        return {
            "members": members,
            "lr": [round(x, 4) for x in lik],
            "trust": round(lik_block["t"], 4),
            "favors": favors,
            "discrimination": discrimination(lik),
        }

    for nid, fm in fm_by_id.items():
        t = fm.get("type")
        if t == "evidence-link":
            frm = wikilink_ids(fm.get("from"))
            to = wikilink_ids(fm.get("to"))
            gid = (wikilink_ids(fm.get("group")) or [None])[0]
            arg_ids = wikilink_ids(fm.get("arguments"))
            prior = fm.get("used_for_prior") is True
            if not (frm and to):
                continue
            if gid and gid in nodes:
                # grouped: the observation feeds the correlation-group (one joint
                # witness); the CG -> cluster edge (below) carries the update.
                add_edge(
                    "ingroup", frm[0], gid, id=nid, url=url_by_id.get(nid),
                    label=nid, arguments=arg_ids, prior=prior,
                )
            else:
                # standalone evidence-link: its own edge into the cluster.
                extra = {
                    "id": nid, "url": url_by_id.get(nid), "label": nid,
                    "arguments": arg_ids, "group": None, "prior": prior,
                }
                lb = model.by_block.get(nid)
                if lb:
                    extra["likelihood"] = mk_lik(lb)
                add_edge("evidence", frm[0], to[0], **extra)
        elif t == "correlation-group":
            # one joint evidence edge from the CG node into its cluster.
            to = (wikilink_ids(fm.get("to")) or [None])[0]
            members = wikilink_ids(fm.get("members"))
            prior = any(
                fm_by_id.get(m, {}).get("used_for_prior") is True for m in members
            )
            if to and to in nodes and nid in nodes:
                extra = {
                    "id": nid, "url": url_by_id.get(nid), "label": nid,
                    "group": nid, "prior": prior, "members": members,
                }
                lb = model.by_block.get(nid)
                if lb:
                    extra["likelihood"] = mk_lik(lb)
                add_edge("evidence", nid, to, **extra)
        elif t == "observation":
            for s in wikilink_ids(fm.get("source")):
                add_edge("cites", nid, s)
            for d in wikilink_ids(fm.get("data_basis")):
                add_edge("data-basis", nid, d)
        elif t == "hypothesis":
            for s in wikilink_ids(fm.get("source")):
                add_edge("cites", nid, s)
        elif t == "argument":
            for o in wikilink_ids(fm.get("affects_observations")):
                add_edge("argument", nid, o)
            for s in wikilink_ids(fm.get("source")):
                add_edge("cites", nid, s)
        elif t == "source":
            for d in wikilink_ids(fm.get("data_basis")):
                add_edge("data-basis", nid, d)
        elif t == "cluster-review":
            for c in wikilink_ids(fm.get("cluster")):
                add_edge("review", nid, c)

    # cluster membership + aggregate-to-main, synthesized from structure
    for hc, members in members_of.items():
        for mid in members:
            add_edge("member", hc, mid)
        if main_id:
            add_edge("aggregate", hc, main_id)

    # ---- 4. self-check against run.py's own output --------------------------
    if args.self_check:
        ref = runner.run(str(analysis_dir))
        for hc in ref.clusters():
            a = [round(x, 4) for x in ref.posterior(hc)]
            b = nodes.get(hc, {}).get("posteriors")
            assert a == b, f"posterior mismatch {hc}: run.py={a} ours={b}"
        idxp = REPO / args.content_index
        if idxp.exists():
            bad = verify_slugs(idxp, slug_computed)
            for r, c, a in bad[:5]:
                print(f"  slug drift: {r}\n    computed {c}\n    index    {a}", file=sys.stderr)
            assert not bad, f"{len(bad)} computed slugs disagree with contentIndex"
            tail = "; slugs match contentIndex"
        else:
            tail = " (contentIndex absent; slugs unchecked)"
        print(f"self-check OK: {len(ref.clusters())} clusters match run.py{tail}", file=sys.stderr)

    # ---- 5. write -----------------------------------------------------------
    graph = {
        "analysis": {
            "id": analysis_dir.name,
            "dir": analysis_dir.relative_to(REPO).as_posix(),
            "main": main_id,
        },
        "nodeColors": NODE_COLORS,
        "nodes": list(nodes.values()),
        "edges": edges,
    }
    out_path = REPO / args.out
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(graph, indent=2, ensure_ascii=False))

    missing = [n["id"] for n in nodes.values() if not n["url"]]
    print(
        f"wrote {out_path.relative_to(REPO)}: {len(nodes)} nodes, {len(edges)} edges"
        + (f"; {len(missing)} without url ({missing[:6]}...)" if missing else "; all nodes have urls"),
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
