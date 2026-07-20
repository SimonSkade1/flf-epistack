"""Build correlation-group (CG) nodes from shared data bases, at step-5 consolidation.

Two step-5 evidence-link edges into the *same* cluster are correlated when their
observations rest on a shared data basis (they intersect on a `[[D-N]]`/`[[S-N]]`
node). Correlation is basis-set *intersection*, which is not transitive, so the
right unit to judge jointly is a whole connected component of edges linked by
shared bases -- not a per-basis clique. This script computes those components
per cluster and materialises each one (>= 2 edges) as a `correlation-group`
(`CG-N`) node that owns the single joint likelihood block step 8 later writes.

For every such component it:
  - mints (or reuses) a `CG-N` node in `correlation-groups/` carrying `to` (the
    cluster) and `members` (the edges);
  - writes `group: "[[CG-N ...]]"` onto each member edge (the edge's pointer to
    where its joint likelihood lives).

It is derive-and-reconcile, so re-running is safe: a component whose member set
already has a CG node reuses it *untouched* (body preserved, so step 8's block
survives); a component with no CG node gets a fresh id; a CG node whose member
set no longer exists moves to `correlation-groups/orphan/`. Edge `group` fields
are recomputed from scratch each run. Run once, after every step-5 cluster-child
has returned, in the same consolidation pass as `attach_argument_backlinks.py`
(fixed order between the two) and before `link_state` is set.

An observation's basis set is its own `data_basis` (a step-3 override) else its
source's `data_basis`; an absent-and-source-less, empty, or `unknown` basis
rests on no shared node and is never correlated.

Usage:
    python3 build_correlation_groups.py <analysis-dir>
"""

import argparse
import collections
import pathlib
import re
import sys

# Captures the id at the head of an Obsidian wikilink, e.g. [[O-14 - title]] -> O-14.
WIKILINK = re.compile(r"\[\[\s*([A-Za-z]+-\d+)")
# A top-level frontmatter key line (not an indented block-list continuation).
KEY = re.compile(r"^([A-Za-z0-9_-]+)\s*:")
ILLEGAL = re.compile(r'[/\\:*?"<>|]')

Edge = collections.namedtuple("Edge", "id from_obs to path")


# ---- frontmatter helpers (shared shape with attach_argument_backlinks.py) ----

def split_note(text):
    """Return (frontmatter, body_with_delims) or (None, text) if there is no frontmatter."""
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    return text[4:end], text[end + 1 :]


def fm_segments(fm):
    """Split frontmatter into ordered (key, raw_lines) segments, each field intact."""
    segments, key, lines = [], None, []
    for line in fm.split("\n"):
        m = KEY.match(line)
        if m and not line[:1].isspace():
            if lines or key is not None:
                segments.append((key, lines))
            key, lines = m.group(1), [line]
        else:
            lines.append(line)
    if lines or key is not None:
        segments.append((key, lines))
    return segments


def field_ids(text, key):
    """Ids linked in one frontmatter field, or None if the field is absent.

    `None` (absent) and `[]` (present but empty / `unknown`) are kept distinct:
    an observation with an explicit empty `data_basis` overrides its source with
    "rests on nothing", whereas an absent `data_basis` inherits the source's.
    """
    fm, _ = split_note(text)
    if fm is None:
        return None
    for k, raw in fm_segments(fm):
        if k == key:
            return WIKILINK.findall("\n".join(raw))
    return None


def id_of(path):
    m = re.match(r"^([A-Za-z]+-\d+) - ", path.name)
    return m.group(1) if m else None


def link_of(path):
    return "[[%s]]" % path.stem


def num_key(node_id):
    """Sort ids by (prefix, number) so output is stable and human-ordered."""
    prefix, num = node_id.rsplit("-", 1)
    return (prefix, int(num))


def set_single(text, key, link):
    """Return `text` with frontmatter `key` set to one inline link, or removed if link is None.

    The field is (re)written last in the frontmatter, so repeated runs are stable.
    """
    fm, body = split_note(text)
    if fm is None:
        return text
    out = []
    for k, raw in fm_segments(fm):
        if k != key:
            out.extend(raw)
    while out and out[-1].strip() == "":
        out.pop()
    if link:
        out.append('%s: "%s"' % (key, link))
    return "---\n" + "\n".join(out) + "\n" + body


# ---- basis resolution --------------------------------------------------------

def basis_of(obs_id, index, cache):
    """The observation's basis set: its own `data_basis` override, else its source's."""
    if obs_id in cache:
        return cache[obs_id]
    result = set()
    p = index.get(obs_id)
    if p is not None:
        text = p.read_text()
        db = field_ids(text, "data_basis")
        if db is None:  # no override -> inherit the source's data_basis
            src = field_ids(text, "source") or []
            sp = index.get(src[0]) if src else None
            if sp is not None:
                db = field_ids(sp.read_text(), "data_basis") or []
        result = set(db or [])
    cache[obs_id] = result
    return result


# ---- union-find over edges linked by a shared basis node ---------------------

class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        self.parent.setdefault(x, x)
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[ra] = rb


def cg_content(cg_id, to_link, member_links, obs_ids, basis_ids):
    """The markdown for a freshly minted CG node (frontmatter + a one-line body)."""
    lines = ["---", "type: correlation-group", "id: %s" % cg_id,
             'to: "%s"' % to_link, "members:"]
    lines += ['  - "%s"' % ml for ml in member_links]
    lines += ["---", ""]
    lines.append(
        "Joint likelihood for correlated observations %s (shared basis: %s). "
        "Step 8 writes the single `## Likelihood` block here; the member edges "
        "point back via `group`." % (", ".join(obs_ids), ", ".join(basis_ids)))
    lines.append("")
    return "\n".join(lines)


def next_cg_num(root):
    """Highest existing CG-N anywhere under root, plus one (ids are never reused)."""
    pat = re.compile(r"^CG-(\d+) - ")
    highest = 0
    for p in root.rglob("*.md"):
        m = pat.match(p.name)
        if m:
            highest = max(highest, int(m.group(1)))
    return highest + 1


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("analysis_dir")
    args = ap.parse_args()

    root = pathlib.Path(args.analysis_dir)
    if not root.is_dir():
        sys.exit("no such analysis directory: %s" % root)

    edges_dir = root / "evidence-links"
    cg_dir = root / "correlation-groups"
    cg_orphan = cg_dir / "orphan"

    # 1. Index every node by id, so an observation's source and basis resolve.
    index = {}
    for p in root.rglob("*.md"):
        nid = id_of(p)
        if nid and nid not in index:
            index[nid] = p

    # 2. Read the edges.
    edges = []
    if edges_dir.is_dir():
        for p in sorted(edges_dir.glob("*.md")):
            text = p.read_text()
            frm = field_ids(text, "from") or []
            to = field_ids(text, "to") or []
            if frm and to:
                edges.append(Edge(id_of(p), frm[0], to[0], p))

    # 3. Per cluster, connect edges that share a basis node; keep components >= 2.
    #    desired[(to_hc, frozenset(edge_ids))] = the group's render data.
    basis_cache = {}
    desired = {}
    by_cluster = collections.defaultdict(list)
    for e in edges:
        by_cluster[e.to].append(e)
    for hc, es in by_cluster.items():
        uf = UnionFind()
        edge_basis = {}
        shared = collections.defaultdict(list)  # basis id -> edge ids in this cluster
        for e in es:
            uf.find(e.id)  # register even singletons
            edge_basis[e.id] = basis_of(e.from_obs, index, basis_cache)
            for d in edge_basis[e.id]:
                shared[d].append(e.id)
        for eids in shared.values():
            for other in eids[1:]:
                uf.union(eids[0], other)
        comps = collections.defaultdict(list)
        for e in es:
            comps[uf.find(e.id)].append(e)
        for comp in comps.values():
            if len(comp) < 2:
                continue
            comp.sort(key=lambda e: num_key(e.id))
            key = (hc, frozenset(e.id for e in comp))
            desired[key] = {
                "to_hc": hc,
                "comp": comp,
                "obs_ids": [e.from_obs for e in comp],
                "basis_ids": sorted({d for e in comp for d in edge_basis[e.id]}, key=num_key),
                "member_links": [link_of(e.path) for e in comp],
                "to_link": link_of(index[hc]) if hc in index else "[[%s]]" % hc,
            }

    # 4. Index existing CG nodes (live + orphaned) by (to, members) so re-runs reuse.
    existing = {}
    for folder in (cg_dir, cg_orphan):
        if not folder.is_dir():
            continue
        for p in sorted(folder.glob("*.md")):
            text = p.read_text()
            to = field_ids(text, "to") or []
            if to:
                existing[(to[0], frozenset(field_ids(text, "members") or []))] = p

    # 5. Reconcile: reuse a matching CG untouched, mint a fresh one otherwise.
    minted = 0
    edge_to_cg = {}
    counter = next_cg_num(root)
    for key in sorted(desired, key=lambda k: (num_key(desired[k]["to_hc"]),
                                              min(num_key(o) for o in desired[k]["obs_ids"]))):
        g = desired[key]
        p = existing.get(key)
        if p is not None:
            if p.parent == cg_orphan:  # membership is valid again -> move back
                cg_dir.mkdir(parents=True, exist_ok=True)
                p = p.rename(cg_dir / p.name)
        else:
            cg_id = "CG-%d" % counter
            counter += 1
            title = ILLEGAL.sub("-", "%s joint over %s" % (g["to_hc"], "+".join(g["obs_ids"])))
            cg_dir.mkdir(parents=True, exist_ok=True)
            p = cg_dir / ("%s - %s.md" % (cg_id, title))
            p.write_text(cg_content(cg_id, g["to_link"], g["member_links"], g["obs_ids"], g["basis_ids"]))
            minted += 1
        cg_link = link_of(p)
        for e in g["comp"]:
            edge_to_cg[e.id] = cg_link

    # 6. Orphan any live CG whose member set no longer corresponds to a group.
    orphaned = 0
    if cg_dir.is_dir():
        for p in sorted(cg_dir.glob("*.md")):
            text = p.read_text()
            to = field_ids(text, "to") or []
            k = (to[0] if to else None, frozenset(field_ids(text, "members") or []))
            if k not in desired:
                cg_orphan.mkdir(parents=True, exist_ok=True)
                p.rename(cg_orphan / p.name)
                orphaned += 1

    # 7. Write each edge's `group` (or strip it where the edge is no longer grouped).
    edges_updated = 0
    for e in edges:
        text = e.path.read_text()
        new_text = set_single(text, "group", edge_to_cg.get(e.id))
        if new_text != text:
            e.path.write_text(new_text)
            edges_updated += 1

    print("correlation groups (>=2 edges): %d" % len(desired))
    print("CG nodes minted: %d" % minted)
    print("CG nodes moved to correlation-groups/orphan/: %d" % orphaned)
    print("edges with `group` rewritten: %d" % edges_updated)


if __name__ == "__main__":
    main()
