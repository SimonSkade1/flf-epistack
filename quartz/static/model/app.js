/* EpiStack model-graph viewer.
 *
 * Renders one analysis's Bayesian model as a layered DAG:
 *   - evidence-links are EDGES (observation -> hypothesis-cluster), width ∝ how
 *     much the datum discriminates between hypotheses;
 *   - hypotheses show their posterior probability (pie fill + size);
 *   - clicking any node or edge opens the underlying note.
 *
 * Data comes from graph.json (built by scripts/build_graph.py).
 */
;(function () {
  "use strict"

  var DARK = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches
  var THEME = DARK ? "dark" : "light"
  // evidence that informs the prior: a dark, red-leaning orange (distinct from
  // the gold/amber of likelihood-update edges).
  var PRIOR_COLOR = DARK ? "#f9683e" : "#bf360c"

  // edges whose stored orientation is semantic ("O cites S") but whose natural
  // *evidential flow* runs the other way; flip them so the DAG reads left→right
  // roots(sources/data) → observations → clusters → hypotheses → answer.
  var FLIP = { cites: true, "data-basis": true, review: true }
  // structural (non-evidence) edge kinds, drawn thin/muted.
  var STRUCT_STYLE = {
    cites: { color: "#8a94a6", dash: null },
    "data-basis": { color: "#5f9ea0", dash: [3, 4] },
    member: { color: "#9b7bd0", dash: [6, 4] },
    aggregate: { color: "#94a3b8", dash: [2, 5] },
    argument: { color: "#e06c86", dash: [4, 4] },
    review: { color: "#94a3b8", dash: [2, 5] },
  }

  var el = function (id) {
    return document.getElementById(id)
  }

  function fail(msg, err) {
    console.error(msg, err || "")
    var s = el("subtitle")
    if (s) {
      s.textContent = "⚠ " + msg + (err ? ": " + (err.message || err) : "")
      s.style.color = "#dc2626"
      s.style.whiteSpace = "normal"
    }
  }

  function param(name, dflt) {
    var v = new URLSearchParams(window.location.search).get(name)
    return v || dflt
  }

  function typeColor(colors, type) {
    var c = colors[type]
    if (!c) return DARK ? "#9aa1a9" : "#6a7076"
    return c[THEME]
  }

  // build cytoscape elements from graph.json
  function toElements(g) {
    var colors = g.nodeColors
    var elements = []

    // discrimination range for width scaling
    var maxDisc = 0.001
    g.edges.forEach(function (e) {
      if (e.kind === "evidence" && e.likelihood)
        maxDisc = Math.max(maxDisc, e.likelihood.discrimination || 0)
    })

    g.nodes.forEach(function (n) {
      var d = {
        id: n.id,
        type: n.type,
        label: n.label,
        short: n.id,
        title: n.title || "",
        url: n.url || "",
        color: typeColor(colors, n.type),
      }
      if (n.type === "hypothesis" && typeof n.posterior === "number") {
        d.posterior = n.posterior
        d.prior = n.prior
        d.posteriorPct = Math.round(n.posterior * 100)
        d.cluster = n.cluster
        // show id + posterior on the node
        d.disp = n.id + "  " + n.posterior.toFixed(2)
        d.sizeVal = 30 + Math.sqrt(n.posterior) * 52 // area-ish emphasis
      } else {
        d.disp = n.id
        d.sizeVal =
          n.type === "main-report"
            ? 78
            : n.type === "hypothesis-cluster"
              ? 60
              : n.type === "correlation-group"
                ? 36
                : n.type === "source" || n.type === "observation"
                  ? 34
                  : 24
      }
      if (n.type === "correlation-group") {
        d.members = n.members || []
        d.to = n.to
      }
      if (n.type === "hypothesis-cluster") {
        d.members = n.members
        d.posteriors = n.posteriors
        d.priors = n.priors
        d.nEvidence = n.nEvidence
      }
      if (n.type === "source" && typeof n.trust === "number") d.trust = n.trust
      elements.push({ data: d, classes: "n-" + n.type })
    })

    g.edges.forEach(function (e, i) {
      var src = e.source,
        tgt = e.target
      if (FLIP[e.kind]) {
        src = e.target
        tgt = e.source
      }
      var d = {
        id: e.id ? "E_" + e.id : "x" + i,
        kind: e.kind,
        source: src,
        target: tgt,
        url: e.url || "",
        eid: e.id || "",
        prior: !!e.prior,
      }
      if (e.kind === "evidence") {
        d.label = e.id
        d.group = e.group || "" // set = this edge starts at a correlation-group
        d.arguments = e.arguments || []
        d.members = e.members || []
        if (e.likelihood) {
          d.lik = e.likelihood
          d.trust = e.likelihood.trust
          d.favors = e.likelihood.favors
          d.disc = e.likelihood.discrimination || 0
          d.width = 2 + (d.disc / maxDisc) * 8
        } else {
          d.width = 3 // prior-used evidence has no likelihood vector
        }
      } else if (e.kind === "ingroup") {
        d.label = e.id
        d.arguments = e.arguments || []
        d.width = 1.8
      } else {
        d.width = 1.4
      }
      elements.push({ data: d, classes: "e-" + e.kind + (d.prior ? " prior" : "") })
    })
    return elements
  }

  function cyStyle(colors) {
    var faded = DARK ? "#1c1f24" : "#ffffff"
    var edgeText = DARK ? "#cbd2da" : "#2a2f36"
    var CGCOL = colors["correlation-group"][THEME]
    var PRIOR = PRIOR_COLOR
    return [
      {
        selector: "node",
        style: {
          "background-color": "data(color)",
          width: "data(sizeVal)",
          height: "data(sizeVal)",
          label: "data(disp)",
          color: DARK ? "#e6e8ea" : "#1f2328",
          "font-size": 10,
          "font-weight": 600,
          "text-valign": "bottom",
          "text-margin-y": 3,
          "text-halign": "center",
          "text-wrap": "wrap",
          "text-max-width": 120,
          "text-background-color": DARK ? "#14161a" : "#f6f6f4",
          "text-background-opacity": 0.7,
          "text-background-padding": 1,
          "border-width": 1,
          "border-color": faded,
          "overlay-opacity": 0,
        },
      },
      // hypotheses: pie fill = posterior
      {
        selector: "node.n-hypothesis",
        style: {
          "background-color": DARK ? "#2a2438" : "#ece7f6",
          "pie-size": "94%",
          "pie-1-background-color": "data(color)",
          "pie-1-background-size": "data(posteriorPct)",
          "pie-1-background-opacity": 1,
          "border-color": "data(color)",
          "border-width": 1.4,
        },
      },
      {
        selector: "node.n-hypothesis-cluster",
        style: {
          shape: "round-rectangle",
          "text-valign": "center",
          "text-margin-y": 0,
          color: "#ffffff",
          "font-size": 11,
          "font-weight": 700,
          "text-background-opacity": 0,
        },
      },
      {
        selector: "node.n-main-report",
        style: {
          shape: "round-diamond",
          "border-width": 2,
          "border-color": DARK ? "#e2e8f0" : "#0f172a",
          "font-size": 11,
          "font-weight": 700,
        },
      },
      {
        // correlation-group: a joint-witness hub its observations merge into
        selector: "node.n-correlation-group",
        style: {
          shape: "round-hexagon",
          "font-size": 9,
          "font-weight": 700,
          "border-width": 1.4,
          "border-color": CGCOL,
        },
      },
      {
        selector: "node.n-source",
        style: { shape: "round-rectangle" },
      },
      {
        selector: "edge",
        style: {
          width: "data(width)",
          "curve-style": "bezier",
          "line-color": "#9aa1a9",
          "target-arrow-color": "#9aa1a9",
          "target-arrow-shape": "triangle",
          "arrow-scale": 0.85,
          opacity: 0.85,
        },
      },
      {
        selector: "edge.e-evidence",
        style: {
          "line-color": colors["evidence-link"][THEME],
          "target-arrow-color": colors["evidence-link"][THEME],
          label: "data(label)",
          "font-size": 7,
          color: edgeText,
          "text-opacity": 0, // shown on hover/select only
          "text-rotation": "autorotate",
          "text-background-color": DARK ? "#14161a" : "#f6f6f4",
          "text-background-opacity": 0.85,
          "text-background-padding": 1,
        },
      },
    ]
      .concat(
        Object.keys(STRUCT_STYLE).map(function (k) {
          var s = STRUCT_STYLE[k]
          var st = {
            "line-color": s.color,
            "target-arrow-color": s.color,
            opacity: 0.55,
          }
          if (s.dash) {
            st["line-style"] = "dashed"
            st["line-dash-pattern"] = s.dash
          }
          return { selector: "edge.e-" + k, style: st }
        }),
      )
      .concat([
        // observation -> correlation-group feeder edges
        {
          selector: "edge.e-ingroup",
          style: {
            "line-color": CGCOL,
            "target-arrow-color": CGCOL,
            "target-arrow-shape": "triangle",
            "arrow-scale": 0.7,
            opacity: 0.75,
          },
        },
        // evidence that informs the PRIOR rather than the likelihood
        {
          selector: "edge.e-evidence.prior",
          style: {
            "line-color": PRIOR,
            "target-arrow-color": PRIOR,
          },
        },
      ])
      .concat([
        // interaction states
        { selector: ".dim", style: { opacity: 0.12, "text-opacity": 0 } },
        {
          selector: "node.hi",
          style: { "border-width": 3, "border-color": DARK ? "#fbbf24" : "#b45309" },
        },
        {
          selector: "edge.hi",
          style: { opacity: 1, "text-opacity": 1, "z-index": 999 },
        },
        {
          selector: ":selected",
          style: { "border-width": 3, "border-color": DARK ? "#fbbf24" : "#b45309" },
        },
      ])
  }

  // ---------- details panel ----------
  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]
    })
  }

  function probBar(label, prior, post, color) {
    var pct = Math.round(post * 100)
    return (
      '<div class="bar"><span style="width:' +
      pct +
      "%;background:" +
      color +
      '"></span><label><b>' +
      esc(label) +
      "</b><span>" +
      (prior != null ? "prior " + prior.toFixed(2) + " → " : "") +
      "<b>" +
      post.toFixed(3) +
      "</b></span></label></div>"
    )
  }

  function showNodeDetails(cy, node, colors) {
    var d = node.data()
    var html = ""
    html +=
      '<span class="d-type" style="background:' +
      d.color +
      '">' +
      esc(d.type) +
      "</span>"
    html += '<div class="d-id">' + esc(d.short) + "</div>"
    html += '<div class="d-title">' + esc(d.title) + "</div>"
    if (d.url)
      html +=
        '<a class="d-open" href="' + esc(d.url) + '" target="_blank" rel="noopener">open note ↗</a>'

    if (d.type === "hypothesis" && typeof d.posterior === "number") {
      html += '<div class="d-sub">Probability</div>'
      html += probBar("posterior", d.prior, d.posterior, d.color)
      if (d.cluster)
        html +=
          '<div class="d-row"><span class="k">in cluster</span> ' + esc(d.cluster) + "</div>"
    }

    if (d.type === "hypothesis-cluster" && d.posteriors) {
      html +=
        '<div class="d-sub">Members — prior → posterior (' +
        (d.nEvidence || 0) +
        " evidence blocks)</div>"
      d.members.forEach(function (m, i) {
        var mc = colors["hypothesis"][THEME]
        html += probBar(m, d.priors[i], d.posteriors[i], mc)
      })
    }

    if (d.type === "source" && typeof d.trust === "number") {
      html +=
        '<div class="d-row"><span class="k">trust score</span> <b>' +
        d.trust.toFixed(2) +
        "</b></div>"
    }

    if (d.type === "correlation-group") {
      html +=
        '<div class="d-sub">Joint witness</div>' +
        '<div class="d-row">Correlated observations sharing a data basis, treated as <b>one</b> witness and updated ' +
        (d.to ? "into " + esc(d.to) + " " : "") +
        "<b>once</b> (so a shared bias is not counted several times).</div>"
      if (d.members && d.members.length)
        html +=
          '<div class="d-row"><span class="k">members</span> ' +
          d.members.map(esc).join(", ") +
          "</div>"
    }
    renderDetails(html)
  }

  function showEdgeDetails(cy, edge, colors) {
    var d = edge.data()
    var CGCOL = colors["correlation-group"][THEME]
    var PRIOR = PRIOR_COLOR

    // observation -> correlation-group feeder edge
    if (d.kind === "ingroup") {
      var hi =
        '<span class="d-type" style="background:' +
        CGCOL +
        '">correlation-group link</span>' +
        '<div class="d-id">' +
        esc(d.eid) +
        "</div>" +
        '<div class="d-title">' +
        esc(d.source) +
        " &nbsp;→&nbsp; " +
        esc(d.target) +
        ' <span class="d-row"><span class="k">joins this joint witness</span></span></div>'
      if (d.url)
        hi +=
          '<a class="d-open" href="' +
          esc(d.url) +
          '" target="_blank" rel="noopener">open evidence-link ↗</a>'
      renderDetails(hi)
      return
    }
    if (d.kind !== "evidence") {
      renderDetails(
        '<span class="d-type" style="background:#8a94a6">' +
          esc(d.kind) +
          '</span><div class="d-id">' +
          esc(d.source) +
          " → " +
          esc(d.target) +
          "</div>",
      )
      return
    }

    // evidence edge: standalone (from an observation) or joint (from a CG node)
    var isCG = !!d.group
    var lik = d.lik
    var badge = isCG ? CGCOL : d.prior ? PRIOR : colors["evidence-link"][THEME]
    var kindLabel = isCG ? "correlation-group" : "evidence-link"
    var html = ""
    html +=
      '<span class="d-type" style="background:' +
      badge +
      '">' +
      kindLabel +
      (d.prior ? " · prior" : "") +
      "</span>"
    html += '<div class="d-id">' + esc(d.eid) + "</div>"
    html +=
      '<div class="d-title">' +
      esc(d.source) +
      " &nbsp;→&nbsp; " +
      esc(d.target) +
      "</div>"
    if (d.url)
      html +=
        '<a class="d-open" href="' +
        esc(d.url) +
        '" target="_blank" rel="noopener">open ' +
        kindLabel +
        " ↗</a>"
    if (isCG && d.members && d.members.length)
      html +=
        '<div class="d-row"><span class="k">joint witness over</span> ' +
        d.members.map(esc).join(", ") +
        ' <span class="k">(counted once)</span></div>'

    if (d.prior) {
      html +=
        '<div class="d-sub">Role</div><div class="d-row">Informs the <b>prior</b> (base rate) for ' +
        esc(d.target) +
        " — held out of the likelihood so it is not double-counted, so it carries no update vector.</div>"
    } else if (lik) {
      html +=
        '<div class="d-sub">Likelihood ratios <span style="text-transform:none;font-weight:400">(1.00 = best-fit anchor)</span></div>'
      var maxlr = Math.max.apply(null, lik.lr)
      lik.members.forEach(function (m, i) {
        var v = lik.lr[i]
        var w = Math.round((v / maxlr) * 100)
        var fav = m === lik.favors
        html +=
          '<div class="lr-row' +
          (fav ? " favors" : "") +
          '"><div class="lr-id" data-node="' +
          esc(m) +
          '">' +
          esc(m) +
          '</div><div class="bar" style="margin:0"><span style="width:' +
          w +
          "%;background:" +
          (fav ? colors["evidence-link"][THEME] : DARK ? "#3a3f47" : "#c7ccd3") +
          '"></span><label><span></span><span><b>' +
          v.toFixed(2) +
          "</b></span></label></div></div>"
      })
      html +=
        '<div class="d-row" style="margin-top:.5rem"><span class="k">favours</span> <b>' +
        esc(lik.favors || "—") +
        "</b></div>"
      html +=
        '<div class="d-row"><span class="k">trust weight</span> ' +
        (typeof lik.trust === "number" ? lik.trust.toFixed(2) : "—") +
        "</div>"
      html +=
        '<div class="d-row"><span class="k">discrimination</span> ' +
        (typeof d.disc === "number" ? d.disc.toFixed(2) : "—") +
        "</div>"
    }
    if (d.arguments && d.arguments.length)
      html +=
        '<div class="d-row"><span class="k">arguments</span> ' +
        d.arguments.map(esc).join(", ") +
        "</div>"
    renderDetails(html)

    // clicking a member id in the LR list focuses that hypothesis node
    Array.prototype.forEach.call(document.querySelectorAll("#details .lr-id"), function (elm) {
      elm.addEventListener("click", function () {
        var n = cy.getElementById(elm.getAttribute("data-node"))
        if (n && n.length) {
          highlight(cy, n)
          cy.animate({ center: { eles: n }, duration: 250 })
        }
      })
    })
  }

  function renderDetails(html) {
    el("details-body").innerHTML = html
    el("details").classList.remove("hidden")
  }

  // ---------- highlight neighborhood ----------
  function highlight(cy, node) {
    var hood = node.closedNeighborhood()
    cy.elements().addClass("dim")
    hood.removeClass("dim")
    cy.elements().removeClass("hi")
    node.addClass("hi")
    hood.edges().addClass("hi")
  }
  function clearHighlight(cy) {
    cy.elements().removeClass("dim hi")
  }

  // ---------- tooltip ----------
  var tip = null
  function showTip(html, evt, container) {
    tip = tip || el("tooltip")
    tip.innerHTML = html
    tip.classList.remove("hidden")
    var rect = container.getBoundingClientRect()
    var x = evt.originalEvent.clientX - rect.left + 12
    var y = evt.originalEvent.clientY - rect.top + 12
    var maxX = rect.width - tip.offsetWidth - 8
    tip.style.left = Math.min(x, maxX) + "px"
    tip.style.top = y + "px"
  }
  function hideTip() {
    if (tip) tip.classList.add("hidden")
  }

  // ---------- legend ----------
  function buildLegend(cy, g) {
    var colors = g.nodeColors
    var counts = {}
    g.nodes.forEach(function (n) {
      counts[n.type] = (counts[n.type] || 0) + 1
    })
    // sensible epistemic order; hide noisy meta types by default
    var order = [
      "main-report",
      "hypothesis-cluster",
      "hypothesis",
      "correlation-group",
      "observation",
      "source",
      "data-basis",
      "argument",
      "cluster-review",
    ]
    var hiddenByDefault = { "data-basis": 1, argument: 1, "cluster-review": 1 }
    var list = el("legend-list")
    order.forEach(function (type) {
      if (!counts[type]) return
      var li = document.createElement("li")
      li.setAttribute("data-type", type)
      li.innerHTML =
        '<span class="swatch" style="background:' +
        typeColor(colors, type) +
        '"></span>' +
        '<span class="lbl">' +
        type +
        '</span><span class="count">' +
        counts[type] +
        "</span>"
      if (hiddenByDefault[type]) {
        li.classList.add("off")
        applyTypeVisibility(cy, type, false)
      }
      li.addEventListener("click", function () {
        var off = li.classList.toggle("off")
        applyTypeVisibility(cy, type, !off)
      })
      list.appendChild(li)
    })
  }
  function applyTypeVisibility(cy, type, visible) {
    var nodes = cy.nodes(".n-" + type)
    if (visible) nodes.style("display", "element")
    else nodes.style("display", "none")
  }

  // ---------- layout ----------
  function runLayout(cy, rankDir) {
    return cy
      .layout({
        name: "dagre",
        rankDir: rankDir,
        nodeSep: 26,
        edgeSep: 14,
        rankSep: 150,
        ranker: "tight-tree",
        animate: false,
        fit: true,
        padding: 45,
      })
      .run()
  }

  // ---------- main ----------
  function init(g) {
    var colors = g.nodeColors
    el("title").textContent = "EpiStack — " + (g.analysis.id || "model")
    el("subtitle").textContent =
      g.nodes.length + " nodes · " + g.edges.length + " edges · click a node or edge to open its note"
    var dir = g.analysis && g.analysis.main ? g : g
    var mainNode = g.nodes.find(function (n) {
      return n.type === "main-report"
    })
    if (mainNode && mainNode.url) el("opendir").href = mainNode.url
    document.title = "EpiStack model — " + (g.analysis.id || "")

    if (window.cytoscapeDagre) cytoscape.use(window.cytoscapeDagre)

    var cy = cytoscape({
      container: el("cy"),
      elements: toElements(g),
      style: cyStyle(colors),
      wheelSensitivity: 0.25,
      minZoom: 0.15,
      maxZoom: 3.5,
    })
    window.__cy = cy // for tests

    runLayout(cy, param("dir", "TB"))
    var rsel = el("rankdir")
    rsel.value = param("dir", "TB")

    var container = el("cy")

    // hover: tooltip + neighborhood highlight
    cy.on("mouseover", "node", function (e) {
      var d = e.target.data()
      var extra =
        d.type === "hypothesis" && d.posterior != null
          ? '<div class="tt-meta">posterior ' + d.posterior.toFixed(3) + "</div>"
          : d.type === "source" && d.trust != null
            ? '<div class="tt-meta">trust ' + d.trust.toFixed(2) + "</div>"
            : ""
      showTip(
        '<span class="tt-id">' + esc(d.short) + "</span> " + esc(d.title) + extra,
        e,
        container,
      )
      highlight(cy, e.target)
    })
    cy.on("mouseover", "edge", function (e) {
      var d = e.target.data()
      if (d.kind === "evidence") {
        var meta = d.prior
          ? "informs the prior"
          : "discrimination " +
            (d.disc != null ? d.disc.toFixed(2) : "?") +
            (d.favors ? " · favours " + d.favors : "")
        showTip(
          '<span class="tt-id">' +
            esc(d.eid) +
            "</span> " +
            esc(d.source) +
            " → " +
            esc(d.target) +
            '<div class="tt-meta">' +
            meta +
            "</div>",
          e,
          container,
        )
      } else if (d.kind === "ingroup") {
        showTip(
          '<span class="tt-id">' +
            esc(d.eid) +
            "</span> " +
            esc(d.source) +
            " → " +
            esc(d.target) +
            '<div class="tt-meta">joins joint witness ' +
            esc(d.target) +
            "</div>",
          e,
          container,
        )
      } else {
        showTip(
          '<span class="tt-meta">' + esc(d.kind) + ": " + esc(d.source) + " → " + esc(d.target) + "</span>",
          e,
          container,
        )
      }
      e.target.addClass("hi")
      var hood = e.target.connectedNodes()
      cy.elements().addClass("dim")
      e.target.removeClass("dim")
      hood.removeClass("dim")
    })
    cy.on("mousemove", "node,edge", function (e) {
      if (tip && !tip.classList.contains("hidden")) {
        var rect = container.getBoundingClientRect()
        tip.style.left =
          Math.min(
            e.originalEvent.clientX - rect.left + 12,
            rect.width - tip.offsetWidth - 8,
          ) + "px"
        tip.style.top = e.originalEvent.clientY - rect.top + 12 + "px"
      }
    })
    cy.on("mouseout", "node,edge", function () {
      hideTip()
      clearHighlight(cy)
    })

    // select: details panel (single click = select)
    cy.on("select", "node", function (e) {
      showNodeDetails(cy, e.target, colors)
    })
    cy.on("select", "edge", function (e) {
      showEdgeDetails(cy, e.target, colors)
    })
    cy.on("unselect", function () {
      /* keep panel until closed */
    })

    // open note: tap on background clears; double-tap or ctrl/⌘-click opens.
    // Primary "open" affordance: tap the node/edge opens the note in a new tab.
    cy.on("tap", "node", function (e) {
      var url = e.target.data("url")
      if (url) window.open(url, "_blank", "noopener")
    })
    cy.on("tap", "edge", function (e) {
      var url = e.target.data("url")
      if (url) window.open(url, "_blank", "noopener")
    })
    cy.on("tap", function (e) {
      if (e.target === cy) {
        clearHighlight(cy)
        el("details").classList.add("hidden")
      }
    })

    // controls
    el("fit").addEventListener("click", function () {
      cy.animate({ fit: { padding: 40 }, duration: 250 })
    })
    el("reset").addEventListener("click", function () {
      clearHighlight(cy)
      cy.$(":selected").unselect()
      el("details").classList.add("hidden")
    })
    rsel.addEventListener("change", function () {
      runLayout(cy, rsel.value)
    })
    el("details-close").addEventListener("click", function () {
      el("details").classList.add("hidden")
    })

    buildLegend(cy, g)
  }

  // ---------- boot ----------
  window.addEventListener("error", function (e) {
    fail("uncaught error", e.error || e.message)
  })
  function boot() {
    if (typeof cytoscape === "undefined") {
      fail("cytoscape failed to load (vendor/cytoscape.min.js)")
      return
    }
    var file = param("a", param("analysis", "graph")) + ".json"
    fetch(file, { cache: "no-cache" })
      .then(function (r) {
        if (!r.ok) throw new Error("HTTP " + r.status + " for " + file)
        return r.json()
      })
      .then(function (g) {
        try {
          init(g)
        } catch (err) {
          fail("failed to render graph", err)
        }
      })
      .catch(function (err) {
        fail("failed to load " + file, err)
      })
  }

  if (document.readyState === "loading")
    document.addEventListener("DOMContentLoaded", boot)
  else boot()
})()
