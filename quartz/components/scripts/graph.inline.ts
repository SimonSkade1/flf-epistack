import type { ContentDetails } from "../../plugins/emitters/contentIndex"
import {
  SimulationNodeDatum,
  SimulationLinkDatum,
  Simulation,
  forceSimulation,
  forceManyBody,
  forceCenter,
  forceLink,
  forceCollide,
  forceRadial,
  zoomIdentity,
  select,
  drag,
  zoom,
} from "d3"
import { Text, Graphics, Application, Container, Circle } from "pixi.js"
import { Group as TweenGroup, Tween as Tweened } from "@tweenjs/tween.js"
import { registerEscapeHandler, removeAllChildren } from "./util"
import { FullSlug, SimpleSlug, getFullSlug, resolveRelative, simplifySlug } from "../../util/path"
import { D3Config } from "../Graph"

type GraphicsInfo = {
  color: string
  gfx: Graphics
  alpha: number
  active: boolean
}

type NodeData = {
  id: SimpleSlug
  text: string
  tags: string[]
  nodeType?: string
} & SimulationNodeDatum

/**
 * EpiStack node types. Each gets a `--node-<type>` CSS variable (quartz/styles/custom.scss)
 * so the graph and the in-text link colours stay in sync from one definition.
 */
const NODE_TYPES = [
  "source",
  "data-basis",
  "observation",
  "hypothesis",
  "hypothesis-cluster",
  "correlation-group",
  "evidence-link",
  "argument",
  "cluster-review",
  "main-report",
] as const

type SimpleLinkData = {
  source: SimpleSlug
  target: SimpleSlug
}

type LinkData = {
  source: NodeData
  target: NodeData
} & SimulationLinkDatum<NodeData>

type LinkRenderData = GraphicsInfo & {
  simulationData: LinkData
}

type NodeRenderData = GraphicsInfo & {
  simulationData: NodeData
  label: Text
  /** untruncated title, swapped in while the node is hovered */
  fullText: string
  /** what the label shows when nothing is hovered */
  shortText: string
}

/**
 * EpiStack filenames are long ("H-1 - SARS-CoV-2 first infected humans via
 * zoonotic spillover at the Huanan market"), so full labels collide with their
 * neighbours' and the graph becomes unreadable. Cut at a word boundary when
 * there's one near the limit, keeping the `H-1 -` style id prefix intact.
 */
function truncateLabel(text: string, max: number): string {
  if (!max || text.length <= max) return text
  const slice = text.slice(0, max)
  const lastSpace = slice.lastIndexOf(" ")
  const cut = lastSpace > max * 0.6 ? slice.slice(0, lastSpace) : slice
  return cut.trimEnd() + "…"
}

/** Label shown on a filter chip for nodes with no `type:` frontmatter. */
const UNTYPED = "other"

const graphFilterKey = "graph-hidden-types"
function getHiddenTypes(): Set<string> {
  try {
    return new Set(JSON.parse(localStorage.getItem(graphFilterKey) ?? "[]"))
  } catch {
    return new Set()
  }
}
function setHiddenTypes(hidden: Set<string>) {
  localStorage.setItem(graphFilterKey, JSON.stringify([...hidden]))
}

/** Tag nodes aren't EpiStack nodes, so they're never filtered. */
function nodeTypeOf(url: SimpleSlug, data: Map<SimpleSlug, ContentDetails>): string | null {
  if (url.startsWith("tags/")) return null
  return data.get(url)?.nodeType ?? UNTYPED
}

const localStorageKey = "graph-visited"
function getVisited(): Set<SimpleSlug> {
  return new Set(JSON.parse(localStorage.getItem(localStorageKey) ?? "[]"))
}

function addToVisited(slug: SimpleSlug) {
  const visited = getVisited()
  visited.add(slug)
  localStorage.setItem(localStorageKey, JSON.stringify([...visited]))
}

type TweenNode = {
  update: (time: number) => void
  stop: () => void
}

async function renderGraph(graph: HTMLElement, fullSlug: FullSlug, depthOverride?: number) {
  const slug = simplifySlug(fullSlug)
  const visited = getVisited()
  removeAllChildren(graph)

  let {
    drag: enableDrag,
    zoom: enableZoom,
    depth,
    scale,
    repelForce,
    centerForce,
    linkDistance,
    fontSize,
    opacityScale,
    removeTags,
    showTags,
    focusOnHover,
    enableRadial,
    initialScale,
    labelMaxChars,
    collidePadding,
  } = JSON.parse(graph.dataset["cfg"]!) as D3Config

  const startScale = initialScale ?? 1
  const maxLabelChars = labelMaxChars ?? 0
  const collidePad = collidePadding ?? 0
  // On hover the label swaps to its full (untruncated) title; wrap it past this
  // width (local text px) so a long EpiStack name breaks into a few centred lines
  // instead of one box that spans the graph. Set a few characters wider than a
  // truncated resting label (~0.5em/char) so resting labels never wrap but any
  // title longer than the truncation does.
  const labelWrapWidth = ((maxLabelChars || 34) + 6) * fontSize * 15 * 0.5

  // Labels fade in as you zoom. Tuned so a bounded neighbourhood (which fits at
  // k≳1) shows near-solid labels, while the ~290-node whole-vault view (fits at
  // k≈0.3–0.5) keeps them hidden — otherwise it's an unreadable wall of text.
  // Stock Quartz divides by 3.75, leaving labels at ~0.2 even at 2×.
  const labelAlphaAt = (k: number) => Math.min(Math.max((k * opacityScale - 0.5) / 0.5, 0), 1)

  if (depthOverride !== undefined) {
    depth = depthOverride
    // the radial ring layout only makes sense for the whole-vault view; for a
    // bounded neighbourhood keep the plain force layout centred on the page
    if (depthOverride >= 0) enableRadial = false
  }

  const data: Map<SimpleSlug, ContentDetails> = new Map(
    Object.entries<ContentDetails>(await fetchData).map(([k, v]) => [
      simplifySlug(k as FullSlug),
      v,
    ]),
  )
  const links: SimpleLinkData[] = []
  const tags: SimpleSlug[] = []
  const validLinks = new Set(data.keys())

  const tweens = new Map<string, TweenNode>()
  for (const [source, details] of data.entries()) {
    const outgoing = details.links ?? []

    for (const dest of outgoing) {
      if (validLinks.has(dest)) {
        links.push({ source: source, target: dest })
      }
    }

    if (showTags) {
      const localTags = details.tags
        .filter((tag) => !removeTags.includes(tag))
        .map((tag) => simplifySlug(("tags/" + tag) as FullSlug))

      tags.push(...localTags.filter((tag) => !tags.includes(tag)))

      for (const tag of localTags) {
        links.push({ source: source, target: tag })
      }
    }
  }

  const neighbourhood = new Set<SimpleSlug>()
  const wl: (SimpleSlug | "__SENTINEL")[] = [slug, "__SENTINEL"]
  if (depth >= 0) {
    while (depth >= 0 && wl.length > 0) {
      // compute neighbours
      const cur = wl.shift()!
      if (cur === "__SENTINEL") {
        depth--
        wl.push("__SENTINEL")
      } else {
        neighbourhood.add(cur)
        const outgoing = links.filter((l) => l.source === cur)
        const incoming = links.filter((l) => l.target === cur)
        wl.push(...outgoing.map((l) => l.target), ...incoming.map((l) => l.source))
      }
    }
  } else {
    validLinks.forEach((id) => neighbourhood.add(id))
    if (showTags) tags.forEach((tag) => neighbourhood.add(tag))
  }

  // Drop node types the user has filtered out. Done on the neighbourhood set
  // (not on `nodes`) so the link filter below stays consistent — filtering
  // `nodes` alone would leave links pointing at nodes that no longer exist.
  const hiddenTypes = getHiddenTypes()
  if (hiddenTypes.size > 0) {
    for (const url of [...neighbourhood]) {
      // the current page always stays, even if its type is filtered out —
      // otherwise "hide all" would blank the very node you're looking at
      if (url === slug) continue
      const t = nodeTypeOf(url, data)
      if (t && hiddenTypes.has(t)) neighbourhood.delete(url)
    }
  }

  const nodes = [...neighbourhood].map((url) => {
    const text = url.startsWith("tags/") ? "#" + url.substring(5) : (data.get(url)?.title ?? url)
    return {
      id: url,
      text,
      tags: data.get(url)?.tags ?? [],
      nodeType: data.get(url)?.nodeType,
    }
  })
  const graphData: { nodes: NodeData[]; links: LinkData[] } = {
    nodes,
    links: links
      .filter((l) => neighbourhood.has(l.source) && neighbourhood.has(l.target))
      .map((l) => ({
        source: nodes.find((n) => n.id === l.source)!,
        target: nodes.find((n) => n.id === l.target)!,
      })),
  }

  const width = graph.offsetWidth
  const height = Math.max(graph.offsetHeight, 250)

  // we virtualize the simulation and use pixi to actually render it
  const simulation: Simulation<NodeData, LinkData> = forceSimulation<NodeData>(graphData.nodes)
    .force("charge", forceManyBody().strength(-100 * repelForce))
    .force("center", forceCenter().strength(centerForce))
    .force("link", forceLink(graphData.links).distance(linkDistance))
    // the collider is a circle around the dot, so it can't model a label's width;
    // the padding is a blunt "keep some air between nodes" that, together with the
    // raised linkDistance, is what actually stops titles overlapping
    .force("collide", forceCollide<NodeData>((n) => nodeRadius(n) + collidePad).iterations(3))

  const radius = (Math.min(width, height) / 2) * 0.8
  if (enableRadial) simulation.force("radial", forceRadial(radius).strength(0.2))

  // precompute style prop strings as pixi doesn't support css variables
  const cssVars = [
    "--secondary",
    "--tertiary",
    "--gray",
    "--light",
    "--lightgray",
    "--dark",
    "--darkgray",
    "--bodyFont",
  ] as const
  const computedStyleMap = cssVars.reduce(
    (acc, key) => {
      acc[key] = getComputedStyle(document.documentElement).getPropertyValue(key)
      return acc
    },
    {} as Record<(typeof cssVars)[number], string>,
  )

  // EpiStack node-type palette, read from the same CSS variables the link colours use
  const typeColorMap: Record<string, string> = {}
  for (const t of NODE_TYPES) {
    const v = getComputedStyle(document.documentElement).getPropertyValue(`--node-${t}`).trim()
    if (v) typeColorMap[t] = v
  }

  // calculate color. The current page keeps its own type colour — it's set apart
  // by size and a contrasting ring instead (see nodeRadius and the ring below),
  // so you still see what kind of node you're on.
  const color = (d: NodeData) => {
    if (d.id.startsWith("tags/")) {
      return computedStyleMap["--tertiary"]
    } else if (d.nodeType && typeColorMap[d.nodeType]) {
      // type colour wins over the visited/unvisited distinction: which kind of node
      // something is matters more here than whether you happen to have opened it
      return typeColorMap[d.nodeType]
    } else if (visited.has(d.id)) {
      return computedStyleMap["--tertiary"]
    } else {
      return computedStyleMap["--gray"]
    }
  }

  function nodeRadius(d: NodeData) {
    const numLinks = graphData.links.filter(
      (l) => l.source.id === d.id || l.target.id === d.id,
    ).length
    const base = 2 + Math.sqrt(numLinks)
    // the current page is drawn bigger so it reads as the anchor of the view —
    // this plus a thin ring is what sets it apart, now that it keeps its type colour
    return d.id === slug ? base * 1.3 : base
  }

  // declared up here (rather than next to the zoom setup) because renderLabels reads it
  let currentTransform = zoomIdentity
  // set as soon as the reader pans/zooms/drags, so the settle-time auto-fit never
  // yanks the view out from under them
  let userAdjustedView = false
  let hoveredNodeId: string | null = null
  let hoveredNeighbours: Set<string> = new Set()
  const linkRenderData: LinkRenderData[] = []
  const nodeRenderData: NodeRenderData[] = []
  function updateHoverInfo(newHoveredId: string | null) {
    hoveredNodeId = newHoveredId

    if (newHoveredId === null) {
      hoveredNeighbours = new Set()
      for (const n of nodeRenderData) {
        n.active = false
      }

      for (const l of linkRenderData) {
        l.active = false
      }
    } else {
      hoveredNeighbours = new Set()
      for (const l of linkRenderData) {
        const linkData = l.simulationData
        if (linkData.source.id === newHoveredId || linkData.target.id === newHoveredId) {
          hoveredNeighbours.add(linkData.source.id)
          hoveredNeighbours.add(linkData.target.id)
        }

        l.active = linkData.source.id === newHoveredId || linkData.target.id === newHoveredId
      }

      for (const n of nodeRenderData) {
        n.active = hoveredNeighbours.has(n.simulationData.id)
      }
    }
  }

  let dragStartTime = 0
  let dragging = false

  function renderLinks() {
    tweens.get("link")?.stop()
    const tweenGroup = new TweenGroup()

    for (const l of linkRenderData) {
      let alpha = 1

      // if we are hovering over a node, we want to highlight the immediate neighbours
      // with full alpha and the rest with default alpha
      if (hoveredNodeId) {
        alpha = l.active ? 1 : 0.2
      }

      l.color = l.active ? computedStyleMap["--gray"] : computedStyleMap["--lightgray"]
      tweenGroup.add(new Tweened<LinkRenderData>(l).to({ alpha }, 200))
    }

    tweenGroup.getAll().forEach((tw) => tw.start())
    tweens.set("link", {
      update: tweenGroup.update.bind(tweenGroup),
      stop() {
        tweenGroup.getAll().forEach((tw) => tw.stop())
      },
    })
  }

  function renderLabels() {
    tweens.get("label")?.stop()
    const tweenGroup = new TweenGroup()

    const defaultScale = 1 / scale
    const activeScale = defaultScale * 1.45
    // the current page's label rests a hair larger than the rest so it reads as
    // the anchor — nowhere near the hover blow-up
    const currentRestScale = defaultScale * 1.15

    // The zoom handler fades labels in as you zoom in; this is the alpha a label
    // returns to once nothing is hovered. Mirrors the formula in the zoom handler.
    const baselineAlpha = labelAlphaAt(currentTransform.k)

    for (const n of nodeRenderData) {
      const nodeId = n.simulationData.id
      const isHovered = hoveredNodeId === nodeId
      const isCurrent = nodeId === slug
      // show the titles of adjacent nodes too, so hovering reads the neighbourhood
      const isNeighbour = hoveredNodeId !== null && hoveredNeighbours.has(nodeId)

      // the hovered node is the one you're trying to read, so it gets its full
      // title back, is scaled up, and is lifted above every other label. The
      // current node's n.shortText is already its full title.
      const wantedText = isHovered ? n.fullText : n.shortText
      if (n.label.text !== wantedText) n.label.text = wantedText
      if (isHovered) {
        labelsContainer.setChildIndex(labelBackdrop, labelsContainer.children.length - 1)
        labelsContainer.setChildIndex(n.label, labelsContainer.children.length - 1)
      }

      let targetAlpha = baselineAlpha
      let targetScale = isCurrent ? currentRestScale : defaultScale
      if (isHovered) {
        targetAlpha = 1
        targetScale = activeScale
      } else if (isNeighbour) {
        targetAlpha = 1
      }

      tweenGroup.add(
        new Tweened<Text>(n.label).to(
          {
            alpha: targetAlpha,
            scale: { x: targetScale, y: targetScale },
          },
          100,
        ),
      )
    }

    tweenGroup.getAll().forEach((tw) => tw.start())
    tweens.set("label", {
      update: tweenGroup.update.bind(tweenGroup),
      stop() {
        tweenGroup.getAll().forEach((tw) => tw.stop())
      },
    })
  }

  function renderNodes() {
    tweens.get("hover")?.stop()

    const tweenGroup = new TweenGroup()
    for (const n of nodeRenderData) {
      let alpha = 1

      // if we are hovering over a node, we want to highlight the immediate neighbours
      if (hoveredNodeId !== null && focusOnHover) {
        alpha = n.active ? 1 : 0.2
      }

      tweenGroup.add(new Tweened<Graphics>(n.gfx, tweenGroup).to({ alpha }, 200))
    }

    tweenGroup.getAll().forEach((tw) => tw.start())
    tweens.set("hover", {
      update: tweenGroup.update.bind(tweenGroup),
      stop() {
        tweenGroup.getAll().forEach((tw) => tw.stop())
      },
    })
  }

  function renderPixiFromD3() {
    renderNodes()
    renderLinks()
    renderLabels()
  }

  tweens.forEach((tween) => tween.stop())
  tweens.clear()

  const app = new Application()
  await app.init({
    width,
    height,
    antialias: true,
    autoStart: false,
    autoDensity: true,
    backgroundAlpha: 0,
    preference: "webgpu",
    resolution: window.devicePixelRatio,
    eventMode: "static",
  })
  graph.appendChild(app.canvas)

  const stage = app.stage
  stage.interactive = false

  const labelsContainer = new Container<Text | Graphics>({ zIndex: 3, isRenderGroup: true })
  const nodesContainer = new Container<Graphics>({ zIndex: 2, isRenderGroup: true })
  const linkContainer = new Container<Graphics>({ zIndex: 1, isRenderGroup: true })
  stage.addChild(nodesContainer, labelsContainer, linkContainer)

  // Plate drawn behind the hovered label only. Lives inside labelsContainer (not
  // its own layer) so z-order against the other labels is exact: on hover it is
  // pushed to the top, then the hovered label is pushed above it — so the name
  // you're reading sits on a clean background instead of on top of links, dots
  // and half a dozen other titles.
  const labelBackdrop = new Graphics({ interactive: false, eventMode: "none" })
  labelsContainer.addChild(labelBackdrop)

  for (const n of graphData.nodes) {
    const nodeId = n.id
    // the current page always shows its full title (it's the anchor of the view);
    // everyone else is truncated until hovered
    const shortText = nodeId === slug ? n.text : truncateLabel(n.text, maxLabelChars)

    const label = new Text({
      interactive: false,
      eventMode: "none",
      text: shortText,
      alpha: 0,
      anchor: { x: 0.5, y: 1.2 },
      style: {
        fontSize: fontSize * 15,
        fill: computedStyleMap["--dark"],
        fontFamily: computedStyleMap["--bodyFont"],
        align: "center",
        wordWrap: true,
        wordWrapWidth: labelWrapWidth,
      },
      resolution: window.devicePixelRatio * 4,
    })
    // current page's label sits a hair larger than the rest (see renderLabels)
    label.scale.set((nodeId === slug ? 1.15 : 1) / scale)

    let oldLabelOpacity = 0
    const isTagNode = nodeId.startsWith("tags/")
    const gfx = new Graphics({
      interactive: true,
      label: nodeId,
      eventMode: "static",
      hitArea: new Circle(0, 0, nodeRadius(n)),
      cursor: "pointer",
    })
      .circle(0, 0, nodeRadius(n))
      .fill({ color: isTagNode ? computedStyleMap["--light"] : color(n) })
      .on("pointerover", (e) => {
        updateHoverInfo(e.target.label)
        oldLabelOpacity = label.alpha
        if (!dragging) {
          renderPixiFromD3()
        }
      })
      .on("pointerleave", () => {
        updateHoverInfo(null)
        label.alpha = oldLabelOpacity
        if (!dragging) {
          renderPixiFromD3()
        }
      })

    if (isTagNode) {
      gfx.stroke({ width: 2, color: computedStyleMap["--tertiary"] })
    }

    // thin ring around the current page's node — black on the light theme, white
    // on the dark one (--dark is the theme's foreground), so it pops against the
    // background whatever its type colour
    if (nodeId === slug) {
      gfx.stroke({ width: 1.5, color: computedStyleMap["--dark"] })
    }

    nodesContainer.addChild(gfx)
    labelsContainer.addChild(label)

    const nodeRenderDatum: NodeRenderData = {
      simulationData: n,
      gfx,
      label,
      fullText: n.text,
      shortText,
      color: color(n),
      alpha: 1,
      active: false,
    }

    nodeRenderData.push(nodeRenderDatum)
  }

  for (const l of graphData.links) {
    const gfx = new Graphics({ interactive: false, eventMode: "none" })
    linkContainer.addChild(gfx)

    const linkRenderDatum: LinkRenderData = {
      simulationData: l,
      gfx,
      color: computedStyleMap["--lightgray"],
      alpha: 1,
      active: false,
    }

    linkRenderData.push(linkRenderDatum)
  }

  if (enableDrag) {
    select<HTMLCanvasElement, NodeData | undefined>(app.canvas).call(
      drag<HTMLCanvasElement, NodeData | undefined>()
        .container(() => app.canvas)
        .subject(() => graphData.nodes.find((n) => n.id === hoveredNodeId))
        .on("start", function dragstarted(event) {
          if (!event.active) simulation.alphaTarget(1).restart()
          event.subject.fx = event.subject.x
          event.subject.fy = event.subject.y
          event.subject.__initialDragPos = {
            x: event.subject.x,
            y: event.subject.y,
            fx: event.subject.fx,
            fy: event.subject.fy,
          }
          dragStartTime = Date.now()
          dragging = true
          userAdjustedView = true
        })
        .on("drag", function dragged(event) {
          const initPos = event.subject.__initialDragPos
          event.subject.fx = initPos.x + (event.x - initPos.x) / currentTransform.k
          event.subject.fy = initPos.y + (event.y - initPos.y) / currentTransform.k
        })
        .on("end", function dragended(event) {
          if (!event.active) simulation.alphaTarget(0)
          event.subject.fx = null
          event.subject.fy = null
          dragging = false

          // if the time between mousedown and mouseup is short, we consider it a click
          if (Date.now() - dragStartTime < 500) {
            const node = graphData.nodes.find((n) => n.id === event.subject.id) as NodeData
            const targ = resolveRelative(fullSlug, node.id)
            window.spaNavigate(new URL(targ, window.location.toString()))
          }
        }),
    )
  } else {
    for (const node of nodeRenderData) {
      node.gfx.on("click", () => {
        const targ = resolveRelative(fullSlug, node.simulationData.id)
        window.spaNavigate(new URL(targ, window.location.toString()))
      })
    }
  }

  const minZoom = 0.15
  const maxZoom = 4
  const canvasSelection = select<HTMLCanvasElement, NodeData>(app.canvas)
  const zoomBehaviour = zoom<HTMLCanvasElement, NodeData>()
    .extent([
      [0, 0],
      [width, height],
    ])
    .scaleExtent([minZoom, maxZoom])
    // enableZoom === false still needs the behaviour installed so we can set the
    // initial transform through it; just refuse every user-driven gesture
    .filter(() => enableZoom)
    .on("zoom", ({ transform, sourceEvent }) => {
      // a real gesture means the reader has taken over — stop auto-fitting
      if (sourceEvent) userAdjustedView = true
      currentTransform = transform
      stage.scale.set(transform.k, transform.k)
      stage.position.set(transform.x, transform.y)

      // zoom adjusts opacity of labels too
      const scaleOpacity = labelAlphaAt(transform.k)
      const activeNodes = nodeRenderData.filter((n) => n.active).flatMap((n) => n.label)

      for (const label of labelsContainer.children) {
        if (label !== labelBackdrop && !activeNodes.includes(label as Text)) {
          label.alpha = scaleOpacity
        }
      }
    })

  canvasSelection.call(zoomBehaviour)

  /** Transform that puts world point (wx, wy) at the centre of the viewport at scale k. */
  function centredTransform(k: number, wx: number, wy: number) {
    return zoomIdentity.translate(width / 2 - k * wx, height / 2 - k * wy).scale(k)
  }

  // start zoomed in rather than at k=1: at k=1 a small neighbourhood is a few dots
  // adrift in an empty box with every label at alpha 0
  zoomBehaviour.transform(canvasSelection, centredTransform(startScale, width / 2, height / 2))

  /**
   * Once the force layout settles, frame what's actually there: fills the box for
   * a big graph, and for a two-node neighbourhood zooms in to `initialScale`
   * rather than further. Skipped the moment the reader pans or zooms themselves.
   */
  function fitToContent() {
    if (userAdjustedView) return
    const positioned = graphData.nodes.filter(
      (n) => Number.isFinite(n.x) && Number.isFinite(n.y),
    )
    if (positioned.length === 0) return

    const xs = positioned.map((n) => n.x! + width / 2)
    const ys = positioned.map((n) => n.y! + height / 2)
    const minX = Math.min(...xs)
    const maxX = Math.max(...xs)
    const minY = Math.min(...ys)
    const maxY = Math.max(...ys)

    // labels hang off their node, so leave more room than the dots need
    const pad = Math.min(width, height) * 0.12 + 24
    const k = Math.min(
      (width - 2 * pad) / Math.max(maxX - minX, 1),
      (height - 2 * pad) / Math.max(maxY - minY, 1),
      startScale,
    )
    const clamped = Math.min(Math.max(k, minZoom), maxZoom)
    zoomBehaviour.transform(
      canvasSelection,
      centredTransform(clamped, (minX + maxX) / 2, (minY + maxY) / 2),
    )
  }

  // keep the view framed *while* the layout expands, not just once it stops, so
  // the graph never spends its first seconds spilling out of the box
  let tickCount = 0
  simulation.on("tick", () => {
    if (++tickCount % 4 === 0) fitToContent()
  })
  simulation.on("end", fitToContent)

  /**
   * Redrawn every frame because the label it sits under keeps moving (and keeps
   * resizing while the hover tween scales it up / swaps in the full title).
   */
  function drawLabelBackdrop() {
    labelBackdrop.clear()
    if (hoveredNodeId === null) return
    const hovered = nodeRenderData.find((n) => n.simulationData.id === hoveredNodeId)
    if (!hovered || hovered.label.alpha <= 0.01) return

    const { label } = hovered
    const padX = 6 * label.scale.x
    const padY = 3 * label.scale.y
    // anchor is {x: 0.5, y: 1.2}: the text sits above the node, horizontally centred
    labelBackdrop
      .roundRect(
        label.x - label.width / 2 - padX,
        label.y - label.height * 1.2 - padY,
        label.width + 2 * padX,
        label.height + 2 * padY,
        4 * label.scale.x,
      )
      .fill({ color: computedStyleMap["--light"], alpha: 0.92 })
      .stroke({ color: computedStyleMap["--lightgray"], width: 1, alpha: 0.9 })
    labelBackdrop.alpha = label.alpha
  }

  let stopAnimation = false
  function animate(time: number) {
    if (stopAnimation) return
    for (const n of nodeRenderData) {
      const { x, y } = n.simulationData
      if (!x || !y) continue
      n.gfx.position.set(x + width / 2, y + height / 2)
      if (n.label) {
        n.label.position.set(x + width / 2, y + height / 2)
      }
    }

    for (const l of linkRenderData) {
      const linkData = l.simulationData
      l.gfx.clear()
      l.gfx.moveTo(linkData.source.x! + width / 2, linkData.source.y! + height / 2)
      l.gfx
        .lineTo(linkData.target.x! + width / 2, linkData.target.y! + height / 2)
        .stroke({ alpha: l.alpha, width: 1, color: l.color })
    }

    drawLabelBackdrop()

    tweens.forEach((t) => t.update(time))
    app.renderer.render(stage)
    requestAnimationFrame(animate)
  }

  requestAnimationFrame(animate)
  return () => {
    stopAnimation = true
    app.destroy()
  }
}

/**
 * Node-type filter chips for the global graph.
 *
 * Lives in `.global-graph-outer` rather than `.global-graph-container`, because
 * renderGraph() calls removeAllChildren() on its own container — anything put
 * inside it would be wiped on every re-render.
 *
 * The filter applies to the local sidebar graph too, so "show me only
 * hypotheses and evidence" holds while you browse. The chips are the only place
 * to undo that, but the global graph is always one click away in the sidebar.
 */
async function buildGraphFilters(outer: HTMLElement, onChange: () => Promise<void>) {
  const data = await fetchData
  const counts = new Map<string, number>()
  for (const [slug, details] of Object.entries(data) as [FullSlug, ContentDetails][]) {
    if (simplifySlug(slug).startsWith("tags/")) continue
    const t = details.nodeType ?? UNTYPED
    counts.set(t, (counts.get(t) ?? 0) + 1)
  }

  // known types first, in pipeline order, then anything unexpected, then "other"
  const present = [...counts.keys()]
  const ordered = [
    ...NODE_TYPES.filter((t) => present.includes(t)),
    ...present.filter((t) => !NODE_TYPES.includes(t as never) && t !== UNTYPED).sort(),
    ...(present.includes(UNTYPED) ? [UNTYPED] : []),
  ]

  let container = outer.querySelector(".graph-filters") as HTMLElement | null
  if (!container) {
    container = document.createElement("div")
    container.className = "graph-filters"
    outer.prepend(container)
  }
  removeAllChildren(container)

  const hidden = getHiddenTypes()

  const label = document.createElement("span")
  label.className = "graph-filters-label"
  label.textContent = "Show"
  container.appendChild(label)

  for (const type of ordered) {
    const chip = document.createElement("button")
    chip.className = "graph-filter"
    chip.dataset.nodeType = type
    chip.setAttribute("aria-pressed", String(!hidden.has(type)))
    chip.title = hidden.has(type) ? `Show ${type} nodes` : `Hide ${type} nodes`

    const swatch = document.createElement("span")
    swatch.className = "graph-filter-swatch"
    chip.appendChild(swatch)
    chip.appendChild(document.createTextNode(type))

    const count = document.createElement("span")
    count.className = "graph-filter-count"
    count.textContent = String(counts.get(type) ?? 0)
    chip.appendChild(count)

    chip.addEventListener("click", async () => {
      const cur = getHiddenTypes()
      cur.has(type) ? cur.delete(type) : cur.add(type)
      setHiddenTypes(cur)
      await onChange()
      await buildGraphFilters(outer, onChange)
    })

    container.appendChild(chip)
  }

  const sep = document.createElement("span")
  sep.className = "graph-filters-sep"
  container.appendChild(sep)

  // "hide all" then click one type = solo that type, without unchecking the rest
  const hideAll = document.createElement("button")
  hideAll.className = "graph-filter-bulk"
  hideAll.textContent = "hide all"
  hideAll.disabled = ordered.every((t) => hidden.has(t))
  hideAll.addEventListener("click", async () => {
    setHiddenTypes(new Set(ordered))
    await onChange()
    await buildGraphFilters(outer, onChange)
  })
  container.appendChild(hideAll)

  const showAll = document.createElement("button")
  showAll.className = "graph-filter-bulk"
  showAll.textContent = "show all"
  showAll.disabled = hidden.size === 0
  showAll.addEventListener("click", async () => {
    setHiddenTypes(new Set())
    await onChange()
    await buildGraphFilters(outer, onChange)
  })
  container.appendChild(showAll)
}

/**
 * Expanded-graph view state. Deliberately NOT persisted: every page load starts
 * at the local neighbourhood (distance 1) — the whole-vault view is opt-in per
 * look, so expanding the graph never dumps the full vault on you by default.
 */
let globalGraphDepth = 1
let globalGraphWholeVault = false

/**
 * Distance slider (1–3) + whole-vault toggle for the expanded graph. Lives in
 * `.global-graph-outer` for the same reason as the filter chips: renderGraph()
 * wipes its own container on every re-render.
 */
function buildDepthControls(outer: HTMLElement, onChange: () => Promise<void>) {
  let container = outer.querySelector(".graph-depth-controls") as HTMLElement | null
  if (!container) {
    container = document.createElement("div")
    container.className = "graph-depth-controls"
    outer.appendChild(container)
  }
  removeAllChildren(container)

  const sliderWrap = document.createElement("label")
  sliderWrap.className = "graph-depth-slider"
  sliderWrap.classList.toggle("inactive", globalGraphWholeVault)
  sliderWrap.title = "How many links away from the current page to show"

  const label = document.createElement("span")
  label.textContent = "Distance"
  sliderWrap.appendChild(label)

  const slider = document.createElement("input")
  slider.type = "range"
  slider.min = "1"
  slider.max = "3"
  slider.step = "1"
  slider.value = String(globalGraphDepth)
  sliderWrap.appendChild(slider)

  const value = document.createElement("span")
  value.className = "graph-depth-value"
  value.textContent = String(globalGraphDepth)
  sliderWrap.appendChild(value)

  const wholeVault = document.createElement("button")
  wholeVault.className = "graph-whole-vault"
  wholeVault.textContent = "Show whole vault"
  wholeVault.setAttribute("aria-pressed", String(globalGraphWholeVault))

  // live value readout while dragging; re-render only on release ("change"),
  // so we don't tear down and rebuild the pixi canvas on every tick
  slider.addEventListener("input", () => {
    value.textContent = slider.value
  })
  slider.addEventListener("change", async () => {
    globalGraphDepth = parseInt(slider.value)
    // touching the slider always means "show me the neighbourhood"
    globalGraphWholeVault = false
    wholeVault.setAttribute("aria-pressed", "false")
    sliderWrap.classList.remove("inactive")
    await onChange()
  })

  wholeVault.addEventListener("click", async () => {
    globalGraphWholeVault = !globalGraphWholeVault
    wholeVault.setAttribute("aria-pressed", String(globalGraphWholeVault))
    sliderWrap.classList.toggle("inactive", globalGraphWholeVault)
    await onChange()
  })

  container.appendChild(sliderWrap)
  container.appendChild(wholeVault)
}

let localGraphCleanups: (() => void)[] = []
let globalGraphCleanups: (() => void)[] = []

function cleanupLocalGraphs() {
  for (const cleanup of localGraphCleanups) {
    cleanup()
  }
  localGraphCleanups = []
}

function cleanupGlobalGraphs() {
  for (const cleanup of globalGraphCleanups) {
    cleanup()
  }
  globalGraphCleanups = []
}

document.addEventListener("nav", async (e: CustomEventMap["nav"]) => {
  const slug = e.detail.url
  addToVisited(simplifySlug(slug))

  async function renderLocalGraph() {
    cleanupLocalGraphs()
    const localGraphContainers = document.getElementsByClassName("graph-container")
    for (const container of localGraphContainers) {
      localGraphCleanups.push(await renderGraph(container as HTMLElement, slug))
    }
  }

  await renderLocalGraph()
  const handleThemeChange = () => {
    void renderLocalGraph()
  }

  document.addEventListener("themechange", handleThemeChange)
  window.addCleanup(() => {
    document.removeEventListener("themechange", handleThemeChange)
  })

  const containers = [...document.getElementsByClassName("global-graph-outer")] as HTMLElement[]

  // the expanded graph defaults to the local neighbourhood; -1 = whole vault
  const expandedDepth = () => (globalGraphWholeVault ? -1 : globalGraphDepth)

  async function renderGlobalGraph() {
    const slug = getFullSlug(window)
    for (const container of containers) {
      container.classList.add("active")
      const sidebar = container.closest(".sidebar") as HTMLElement
      if (sidebar) {
        sidebar.style.zIndex = "1"
      }

      const graphContainer = container.querySelector(".global-graph-container") as HTMLElement
      registerEscapeHandler(container, hideGlobalGraph)
      if (graphContainer) {
        const rerenderExpanded = async () => {
          cleanupGlobalGraphs()
          globalGraphCleanups.push(await renderGraph(graphContainer, slug, expandedDepth()))
        }

        globalGraphCleanups.push(await renderGraph(graphContainer, slug, expandedDepth()))
        buildDepthControls(container, rerenderExpanded)

        // toggling a type re-renders the expanded graph in place, and the local
        // sidebar graph too so both agree on what's shown
        await buildGraphFilters(container, async () => {
          await rerenderExpanded()
          await renderLocalGraph()
        })
      }
    }
  }

  function hideGlobalGraph() {
    cleanupGlobalGraphs()
    for (const container of containers) {
      container.classList.remove("active")
      const sidebar = container.closest(".sidebar") as HTMLElement
      if (sidebar) {
        sidebar.style.zIndex = ""
      }
    }
  }

  async function shortcutHandler(e: HTMLElementEventMap["keydown"]) {
    if (e.key === "g" && (e.ctrlKey || e.metaKey) && !e.shiftKey) {
      e.preventDefault()
      const anyGlobalGraphOpen = containers.some((container) =>
        container.classList.contains("active"),
      )
      anyGlobalGraphOpen ? hideGlobalGraph() : renderGlobalGraph()
    }
  }

  const containerIcons = document.getElementsByClassName("global-graph-icon")
  Array.from(containerIcons).forEach((icon) => {
    icon.addEventListener("click", renderGlobalGraph)
    window.addCleanup(() => icon.removeEventListener("click", renderGlobalGraph))
  })

  document.addEventListener("keydown", shortcutHandler)
  window.addCleanup(() => {
    document.removeEventListener("keydown", shortcutHandler)
    cleanupLocalGraphs()
    cleanupGlobalGraphs()
  })
})
