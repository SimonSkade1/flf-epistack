import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { classNames } from "../util/lang"

// Any page whose slug sits inside an analysis folder, e.g.
//   v1/analysis-tests/eggs1/...   ->  case "eggs1", root "v1/analysis-tests/eggs1"
//   v1/analyses/covid/...         ->  case "covid"
const ROOT_RE = /^(.*(?:analysis-tests|analyses)\/([^/]+))\//

const ModelGraphButton: QuartzComponent = ({
  fileData,
  allFiles,
  displayClass,
}: QuartzComponentProps) => {
  const m = ROOT_RE.exec((fileData.slug ?? "") + "/")
  if (!m) return null
  const [, root, caseName] = m

  // Show the button only for analyses that actually have a model graph. A graph
  // is generated for exactly the folders that contain a main-report note
  // (scripts/build_all_graphs.py), so that presence is the reliable signal —
  // no filesystem coupling from inside a component.
  const hasGraph = allFiles.some(
    (f) => (f.slug ?? "").startsWith(root + "/") && f.frontmatter?.type === "main-report",
  )
  if (!hasGraph) return null

  return (
    <div class={classNames(displayClass, "model-graph-cta")}>
      <a href={`/static/model/${caseName}/`} class="model-graph-btn">
        <span class="mg-icon" aria-hidden="true">
          {/* simple node-link glyph */}
          <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8">
            <circle cx="5" cy="6" r="2.2" />
            <circle cx="5" cy="18" r="2.2" />
            <circle cx="19" cy="12" r="2.2" />
            <line x1="7" y1="7" x2="17" y2="11" />
            <line x1="7" y1="17" x2="17" y2="13" />
          </svg>
        </span>
        <span class="mg-label">
          <b>Show model graph</b>
          <small>interactive Bayesian view — separate from the graph above</small>
        </span>
      </a>
      <div class="mg-note">added after the FLF submission deadline</div>
    </div>
  )
}

ModelGraphButton.css = `
.model-graph-cta { margin-top: 0.5rem; }
.model-graph-btn {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  width: 100%;
  box-sizing: border-box;
  padding: 0.7rem 0.85rem;
  border-radius: 10px;
  text-decoration: none;
  color: var(--dark);
  background: var(--lightgray);
  border: 1px solid var(--gray);
  transition: background 0.15s ease, border-color 0.15s ease, transform 0.05s ease;
}
.model-graph-btn:hover {
  background: var(--secondary);
  border-color: var(--secondary);
  color: var(--light);
}
.model-graph-btn:active { transform: translateY(1px); }
.model-graph-btn .mg-icon {
  flex: none;
  display: inline-flex;
  color: var(--secondary);
}
.model-graph-btn:hover .mg-icon { color: var(--light); }
.model-graph-btn .mg-label { display: flex; flex-direction: column; line-height: 1.25; }
.model-graph-btn .mg-label b { font-size: 0.95rem; }
.model-graph-btn .mg-label small { font-size: 0.72rem; opacity: 0.75; }
.model-graph-cta .mg-note {
  margin-top: 0.3rem;
  font-size: 0.68rem;
  color: var(--gray);
  text-align: center;
}
`

export default (() => ModelGraphButton) satisfies QuartzComponentConstructor
