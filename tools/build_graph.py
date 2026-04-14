#!/usr/bin/env python3
"""
Build the knowledge graph from the wiki.

Usage:
    python tools/build_graph.py               # full rebuild
    python tools/build_graph.py --no-infer    # skip semantic inference (faster)
    python tools/build_graph.py --open        # open graph.html in browser after build

Outputs:
    graph/graph.json    — node/edge data (cached by SHA256)
    graph/graph.html    — interactive vis.js visualization

Edge types:
    EXTRACTED   — explicit [[wikilink]] in a page
    INFERRED    — Claude-detected implicit relationship
    AMBIGUOUS   — low-confidence inferred relationship
"""

import re
import json
import hashlib
import argparse
import webbrowser
from pathlib import Path
from datetime import date

import os

try:
    import networkx as nx
    from networkx.algorithms import community as nx_community
    HAS_NETWORKX = True
except ImportError:
    HAS_NETWORKX = False
    print("Warning: networkx not installed. Community detection disabled. Run: pip install networkx")

REPO_ROOT = Path(__file__).parent.parent
WIKI_DIR = REPO_ROOT / "wiki"
GRAPH_DIR = REPO_ROOT / "graph"
GRAPH_JSON = GRAPH_DIR / "graph.json"
GRAPH_HTML = GRAPH_DIR / "graph.html"
CACHE_FILE = GRAPH_DIR / ".cache.json"
LOG_FILE = WIKI_DIR / "log.md"
SCHEMA_FILE = REPO_ROOT / "CLAUDE.md"

# Node type → color mapping
TYPE_COLORS = {
    "source": "#4CAF50",
    "entity": "#2196F3",
    "concept": "#FF9800",
    "synthesis": "#9C27B0",
    "unknown": "#9E9E9E",
}

EDGE_COLORS = {
    "EXTRACTED": "#555555",
    "INFERRED": "#FF5722",
    "AMBIGUOUS": "#BDBDBD",
}


def read_file(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def call_llm(prompt: str, model_env: str, default_model: str, max_tokens: int = 4096) -> str:
    try:
        from litellm import completion
    except ImportError:
        print("Error: litellm not installed. Run: pip install litellm")
        import sys
        sys.exit(1)
        
    model = os.getenv(model_env, default_model)
    response = completion(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens
    )
    return response.choices[0].message.content


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def all_wiki_pages() -> list[Path]:
    return [p for p in WIKI_DIR.rglob("*.md")
            if p.name not in ("index.md", "log.md", "lint-report.md")]


def extract_wikilinks(content: str) -> list[str]:
    return list(set(re.findall(r'\[\[([^\]]+)\]\]', content)))


def extract_frontmatter_type(content: str) -> str:
    match = re.search(r'^type:\s*(\S+)', content, re.MULTILINE)
    return match.group(1).strip('"\'') if match else "unknown"


def page_id(path: Path) -> str:
    return path.relative_to(WIKI_DIR).as_posix().replace(".md", "")


def edge_id(src: str, target: str, edge_type: str) -> str:
    return f"{src}->{target}:{edge_type}"


def load_cache() -> dict:
    if CACHE_FILE.exists():
        try:
            return json.loads(CACHE_FILE.read_text())
        except (json.JSONDecodeError, IOError):
            return {}
    return {}


def save_cache(cache: dict):
    GRAPH_DIR.mkdir(parents=True, exist_ok=True)
    CACHE_FILE.write_text(json.dumps(cache, indent=2))


def build_nodes(pages: list[Path]) -> list[dict]:
    nodes = []
    for p in pages:
        content = read_file(p)
        node_type = extract_frontmatter_type(content)
        title_match = re.search(r'^title:\s*"?([^"\n]+)"?', content, re.MULTILINE)
        label = title_match.group(1).strip() if title_match else p.stem
        body = re.sub(r"^---\n.*?\n---\n?", "", content, flags=re.DOTALL)
        preview_lines = [line.strip() for line in body.splitlines() if line.strip()]
        preview = " ".join(preview_lines[:3])[:220]
        nodes.append({
            "id": page_id(p),
            "label": label,
            "type": node_type,
            "color": TYPE_COLORS.get(node_type, TYPE_COLORS["unknown"]),
            "path": str(p.relative_to(REPO_ROOT)),
            "markdown": content,
            "preview": preview,
        })
    return nodes


def build_extracted_edges(pages: list[Path]) -> list[dict]:
    """Pass 1: deterministic wikilink edges."""
    # Build a map from stem (lower) -> page_id for resolution
    stem_map = {p.stem.lower(): page_id(p) for p in pages}
    edges = []
    seen = set()
    for p in pages:
        content = read_file(p)
        src = page_id(p)
        for link in extract_wikilinks(content):
            target = stem_map.get(link.lower())
            if target and target != src:
                key = (src, target)
                if key not in seen:
                    seen.add(key)
                    edges.append({
                        "id": edge_id(src, target, "EXTRACTED"),
                        "from": src,
                        "to": target,
                        "type": "EXTRACTED",
                        "color": EDGE_COLORS["EXTRACTED"],
                        "confidence": 1.0,
                    })
    return edges


def build_inferred_edges(pages: list[Path], existing_edges: list[dict], cache: dict) -> list[dict]:
    """Pass 2: API-inferred semantic relationships."""
    new_edges = []

    # Only process pages that changed since last run
    changed_pages = []
    for p in pages:
        content = read_file(p)
        h = sha256(content)
        entry = cache.get(str(p))
        
        if not isinstance(entry, dict) or entry.get("hash") != h:
            changed_pages.append(p)
        else:
            # Page unchanged: load its inferred edges from cache perfectly
            src = page_id(p)
            for rel in entry.get("edges", []):
                rel_type = rel.get("type", "INFERRED")
                new_edges.append({
                    "id": edge_id(src, rel["to"], rel_type),
                    "from": src,
                    "to": rel["to"],
                    "type": rel_type,
                    "title": rel.get("relationship", ""),
                    "label": "",
                    "color": EDGE_COLORS.get(rel_type, EDGE_COLORS["INFERRED"]),
                    "confidence": float(rel.get("confidence", 0.7)),
                })

    if not changed_pages:
        print("  no changed pages — skipping semantic inference")
        return []

    print(f"  inferring relationships for {len(changed_pages)} changed pages...")

    # Build a summary of existing nodes for context
    node_list = "\n".join(f"- {page_id(p)} ({extract_frontmatter_type(read_file(p))})" for p in pages)
    existing_edge_summary = "\n".join(
        f"- {e['from']} → {e['to']} (EXTRACTED)" for e in existing_edges[:30]
    )

    for p in changed_pages:
        content = read_file(p)[:2000]  # truncate for context efficiency
        src = page_id(p)

        prompt = f"""Analyze this wiki page and identify implicit semantic relationships to other pages in the wiki.

Source page: {src}
Content:
{content}

All available pages:
{node_list}

Already-extracted edges from this page:
{existing_edge_summary}

Return ONLY a JSON array of NEW relationships not already captured by explicit wikilinks:
[
  {{"to": "page-id", "relationship": "one-line description", "confidence": 0.0-1.0, "type": "INFERRED or AMBIGUOUS"}}
]

Rules:
- Only include pages from the available list above
- Confidence >= 0.7 → INFERRED, < 0.7 → AMBIGUOUS
- Do not repeat edges already in the extracted list
- Return empty array [] if no new relationships found
"""
        raw = call_llm(prompt, "LLM_MODEL_FAST", "claude-3-5-haiku-latest", max_tokens=1024)
        raw = raw.strip()
        raw = re.sub(r"^```(?:json)?\s*", "", raw)
        raw = re.sub(r"\s*```$", "", raw)

        try:
            inferred = json.loads(raw)
            valid_rels = []
            for rel in inferred:
                if isinstance(rel, dict) and "to" in rel:
                    rel_type = rel.get("type", "INFERRED")
                    new_edges.append({
                        "id": edge_id(src, rel["to"], rel_type),
                        "from": src,
                        "to": rel["to"],
                        "type": rel_type,
                        "title": rel.get("relationship", ""),
                        "label": "",
                        "color": EDGE_COLORS.get(rel_type, EDGE_COLORS["INFERRED"]),
                        "confidence": float(rel.get("confidence", 0.7)),
                    })
                    valid_rels.append(rel)
            
            # Save properly to cache
            cache[str(p)] = {
                "hash": sha256(content),
                "edges": valid_rels
            }
        except (json.JSONDecodeError, TypeError, ValueError):
            pass

    return new_edges


def detect_communities(nodes: list[dict], edges: list[dict]) -> dict[str, int]:
    """Assign community IDs to nodes using Louvain algorithm."""
    if not HAS_NETWORKX:
        return {}

    G = nx.Graph()
    for n in nodes:
        G.add_node(n["id"])
    for e in edges:
        G.add_edge(e["from"], e["to"])

    if G.number_of_edges() == 0:
        return {}

    try:
        communities = nx_community.louvain_communities(G, seed=42)
        node_to_community = {}
        for i, comm in enumerate(communities):
            for node in comm:
                node_to_community[node] = i
        return node_to_community
    except Exception:
        return {}


COMMUNITY_COLORS = [
    "#E91E63", "#00BCD4", "#8BC34A", "#FF5722", "#673AB7",
    "#FFC107", "#009688", "#F44336", "#3F51B5", "#CDDC39",
]


def render_html(nodes: list[dict], edges: list[dict]) -> str:
    """Generate self-contained vis.js HTML."""
    nodes_json = json.dumps(nodes, indent=2)
    edges_json = json.dumps(edges, indent=2)

    legend_items = "".join(
        f'<span style="background:{color};padding:3px 8px;margin:2px;border-radius:3px;font-size:12px">{t}</span>'
        for t, color in TYPE_COLORS.items() if t != "unknown"
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>LLM Wiki — Knowledge Graph</title>
<script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
<style>
  body {{ margin: 0; background: #1a1a2e; font-family: sans-serif; color: #eee; }}
  #graph {{ width: 100vw; height: 100vh; }}
  #controls {{
    position: fixed; top: 10px; left: 10px; background: rgba(0,0,0,0.7);
    padding: 12px; border-radius: 8px; z-index: 10; max-width: 260px;
  }}
  #controls h3 {{ margin: 0 0 8px; font-size: 14px; }}
  #search {{ width: 100%; padding: 4px; margin-bottom: 8px; background: #333; color: #eee; border: 1px solid #555; border-radius: 4px; }}
  #controls p {{ margin: 8px 0 0; font-size: 11px; color: #9ea3b0; line-height: 1.5; }}
  #drawer {{
    position: fixed; top: 0; right: 0; width: clamp(480px, 33vw, 720px); max-width: 100vw; height: 100vh;
    background: rgba(7, 10, 24, 0.96); border-left: 1px solid rgba(255,255,255,0.08);
    box-shadow: -18px 0 36px rgba(0,0,0,0.35); z-index: 20; display: none;
    flex-direction: column; backdrop-filter: blur(10px);
  }}
  #drawer.open {{ display: flex; }}
  #drawer-header {{
    padding: 18px 18px 12px; border-bottom: 1px solid rgba(255,255,255,0.08);
  }}
  #drawer-topline {{
    display: flex; align-items: flex-start; justify-content: space-between; gap: 12px;
  }}
  #drawer-title {{ margin: 0; font-size: 20px; line-height: 1.2; }}
  #drawer-close {{
    background: transparent; color: #9ea3b0; border: 0; font-size: 24px; line-height: 1;
    cursor: pointer; padding: 0;
  }}
  #drawer-meta {{ margin-top: 8px; font-size: 12px; color: #9ea3b0; }}
  #drawer-path {{ margin-top: 6px; font-size: 12px; color: #72788a; word-break: break-all; }}
  #drawer-preview {{
    margin-top: 12px; font-size: 13px; color: #d7d9e0; line-height: 1.6;
  }}
  #drawer-related {{
    padding: 12px 18px 0; font-size: 12px; color: #9ea3b0;
  }}
  #drawer-related-list {{
    display: flex; flex-wrap: wrap; gap: 8px; margin-top: 8px;
  }}
  .related-chip {{
    background: rgba(255,255,255,0.08); color: #f1f2f7; border: 1px solid rgba(255,255,255,0.08);
    border-radius: 999px; font-size: 12px; padding: 5px 10px; cursor: pointer;
  }}
  #drawer-content {{
    flex: 1; min-height: 0; padding: 14px 18px 18px; overflow: auto;
  }}
  #drawer-markdown {{
    color: #e6e8ef; font-size: 13px; line-height: 1.72;
  }}
  #drawer-markdown h1, #drawer-markdown h2, #drawer-markdown h3,
  #drawer-markdown h4, #drawer-markdown h5, #drawer-markdown h6 {{
    margin: 1.2em 0 0.55em; line-height: 1.3; color: #fff;
  }}
  #drawer-markdown h1 {{ font-size: 24px; }}
  #drawer-markdown h2 {{ font-size: 20px; }}
  #drawer-markdown h3 {{ font-size: 17px; }}
  #drawer-markdown p {{
    margin: 0 0 0.95em;
  }}
  #drawer-markdown ul, #drawer-markdown ol {{
    margin: 0 0 1em 1.35em; padding: 0;
  }}
  #drawer-markdown li {{
    margin: 0.35em 0;
  }}
  #drawer-markdown hr {{
    border: 0; border-top: 1px solid rgba(255,255,255,0.1); margin: 1.2em 0;
  }}
  #drawer-markdown blockquote {{
    margin: 0 0 1em; padding: 0.85em 1em; border-left: 3px solid rgba(101, 181, 255, 0.8);
    background: rgba(255,255,255,0.04); color: #d7d9e0; border-radius: 0 10px 10px 0;
  }}
  #drawer-markdown pre {{
    margin: 0 0 1em; white-space: pre-wrap; word-break: break-word; line-height: 1.55;
    font-size: 12px; color: #e6e8ef; background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.06); border-radius: 10px; padding: 16px;
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  }}
  #drawer-markdown code {{
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    font-size: 0.92em; background: rgba(255,255,255,0.08); padding: 0.16em 0.38em;
    border-radius: 6px; color: #ffde91;
  }}
  #drawer-markdown pre code {{
    background: transparent; padding: 0; color: inherit; border-radius: 0;
  }}
  #drawer-markdown .wikilink {{
    color: #86c8ff; font-weight: 600;
  }}
  @media (max-width: 960px) {{
    #drawer {{
      width: 100vw;
    }}
  }}
  #stats {{ position: fixed; top: 10px; right: 10px; background: rgba(0,0,0,0.7); padding: 10px; border-radius: 8px; font-size: 12px; }}
</style>
</head>
<body>
<div id="controls">
  <h3>LLM Wiki Graph</h3>
  <input id="search" type="text" placeholder="Search nodes..." oninput="searchNodes(this.value)">
  <div>{legend_items}</div>
  <div style="margin-top:8px;font-size:11px;color:#aaa">
    <span style="background:#555;padding:2px 6px;border-radius:3px;margin-right:4px">──</span> Explicit link<br>
    <span style="background:#FF5722;padding:2px 6px;border-radius:3px;margin-right:4px">──</span> Inferred
  </div>
  <p>Click a node to highlight its connected neighbors and view the markdown on the right. Click the background to restore the full graph.</p>
</div>
<div id="graph"></div>
<aside id="drawer">
  <div id="drawer-header">
    <div id="drawer-topline">
      <h2 id="drawer-title"></h2>
      <button id="drawer-close" onclick="clearSelection()" aria-label="Close drawer">×</button>
    </div>
    <div id="drawer-meta"></div>
    <div id="drawer-path"></div>
    <div id="drawer-preview"></div>
  </div>
  <div id="drawer-related">
    Related nodes
    <div id="drawer-related-list"></div>
  </div>
  <div id="drawer-content">
    <div id="drawer-markdown"></div>
  </div>
</aside>
<div id="stats"></div>
<script>
const nodes = new vis.DataSet({nodes_json});
const edges = new vis.DataSet({edges_json});
const originalNodes = {nodes_json};
const originalEdges = {edges_json};
const adjacency = new Map();
const searchInput = document.getElementById("search");
const nodeMap = new Map(originalNodes.map(node => [node.id, node]));
let activeNodeId = null;

function hexToRgba(color, alpha) {{
  if (!color) return `rgba(255, 255, 255, ${{alpha}})`;
  const normalized = color.replace("#", "");
  const value = normalized.length === 3
    ? normalized.split("").map(ch => ch + ch).join("")
    : normalized;
  const intValue = Number.parseInt(value, 16);
  const r = (intValue >> 16) & 255;
  const g = (intValue >> 8) & 255;
  const b = intValue & 255;
  return `rgba(${{r}}, ${{g}}, ${{b}}, ${{alpha}})`;
}}

function escapeHtml(text) {{
  return (text || "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}}

function stripFrontmatter(markdown) {{
  return (markdown || "").replace(/^---\\n[\\s\\S]*?\\n---\\n?/, "");
}}

function renderInlineMarkdown(text) {{
  let html = escapeHtml(text);
  html = html.replace(/\\[\\[([^\\]]+)\\]\\]/g, '<span class="wikilink">[[$1]]</span>');
  html = html.replace(/`([^`]+)`/g, "<code>$1</code>");
  html = html.replace(/\\*\\*([^*]+)\\*\\*/g, "<strong>$1</strong>");
  html = html.replace(/\\*([^*]+)\\*/g, "<em>$1</em>");
  return html;
}}

function renderMarkdown(markdown) {{
  const lines = stripFrontmatter(markdown).split(/\\r?\\n/);
  const html = [];
  let paragraph = [];
  let listType = null;
  let listItems = [];
  let quoteLines = [];
  let inCodeBlock = false;
  let codeLines = [];

  function flushParagraph() {{
    if (!paragraph.length) return;
    html.push(`<p>${{renderInlineMarkdown(paragraph.join(" "))}}</p>`);
    paragraph = [];
  }}

  function flushList() {{
    if (!listType || !listItems.length) return;
    const items = listItems.map(item => `<li>${{renderInlineMarkdown(item)}}</li>`).join("");
    html.push(`<${{listType}}>${{items}}</${{listType}}>`);
    listType = null;
    listItems = [];
  }}

  function flushQuote() {{
    if (!quoteLines.length) return;
    html.push(`<blockquote>${{quoteLines.map(line => renderInlineMarkdown(line)).join("<br>")}}</blockquote>`);
    quoteLines = [];
  }}

  function flushCode() {{
    if (!codeLines.length) {{
      html.push("<pre><code></code></pre>");
      return;
    }}
    html.push(`<pre><code>${{escapeHtml(codeLines.join("\\n"))}}</code></pre>`);
    codeLines = [];
  }}

  for (const rawLine of lines) {{
    const line = rawLine.replace(/\\t/g, "    ");
    const trimmed = line.trim();

    if (trimmed.startsWith("```")) {{
      flushParagraph();
      flushList();
      flushQuote();
      if (inCodeBlock) {{
        flushCode();
        inCodeBlock = false;
      }} else {{
        inCodeBlock = true;
      }}
      continue;
    }}

    if (inCodeBlock) {{
      codeLines.push(rawLine);
      continue;
    }}

    if (!trimmed) {{
      flushParagraph();
      flushList();
      flushQuote();
      continue;
    }}

    const headingMatch = trimmed.match(/^(#{1,6})\\s+(.+)$/);
    if (headingMatch) {{
      flushParagraph();
      flushList();
      flushQuote();
      const level = headingMatch[1].length;
      html.push(`<h${{level}}>${{renderInlineMarkdown(headingMatch[2])}}</h${{level}}>`);
      continue;
    }}

    if (/^(-{3,}|\\*{3,})$/.test(trimmed)) {{
      flushParagraph();
      flushList();
      flushQuote();
      html.push("<hr>");
      continue;
    }}

    const quoteMatch = trimmed.match(/^>\\s?(.*)$/);
    if (quoteMatch) {{
      flushParagraph();
      flushList();
      quoteLines.push(quoteMatch[1]);
      continue;
    }}
    flushQuote();

    const unorderedMatch = trimmed.match(/^[-*]\\s+(.+)$/);
    if (unorderedMatch) {{
      flushParagraph();
      if (listType && listType !== "ul") flushList();
      listType = "ul";
      listItems.push(unorderedMatch[1]);
      continue;
    }}

    const orderedMatch = trimmed.match(/^\\d+\\.\\s+(.+)$/);
    if (orderedMatch) {{
      flushParagraph();
      if (listType && listType !== "ol") flushList();
      listType = "ol";
      listItems.push(orderedMatch[1]);
      continue;
    }}

    flushList();
    paragraph.push(trimmed);
  }}

  if (inCodeBlock) flushCode();
  flushParagraph();
  flushList();
  flushQuote();
  return html.join("");
}}

for (const node of originalNodes) {{
  adjacency.set(node.id, new Set());
}}
for (const edge of originalEdges) {{
  if (!adjacency.has(edge.from)) adjacency.set(edge.from, new Set());
  if (!adjacency.has(edge.to)) adjacency.set(edge.to, new Set());
  adjacency.get(edge.from).add(edge.to);
  adjacency.get(edge.to).add(edge.from);
}}

const container = document.getElementById("graph");
const network = new vis.Network(container, {{ nodes, edges }}, {{
  nodes: {{
    shape: "dot",
    size: 12,
    font: {{ color: "#eee", size: 13 }},
    borderWidth: 2,
  }},
  edges: {{
    width: 1.2,
    smooth: {{ type: "continuous" }},
    arrows: {{ to: {{ enabled: true, scaleFactor: 0.5 }} }},
  }},
  physics: {{
    stabilization: {{ iterations: 150 }},
    barnesHut: {{ gravitationalConstant: -8000, springLength: 120 }},
  }},
  interaction: {{ hover: true, tooltipDelay: 200 }},
}});

document.getElementById("stats").textContent =
  `${{nodes.length}} nodes · ${{edges.length}} edges`;

function searchNodes(q) {{
  applyFilters(q, activeNodeId);
}}

function clearSelection() {{
  activeNodeId = null;
  closeDrawer();
  applyFilters(searchInput.value, null);
}}

function closeDrawer() {{
  document.getElementById("drawer").classList.remove("open");
}}

function openDrawer(node, relatedIds) {{
  document.getElementById("drawer").classList.add("open");
  document.getElementById("drawer-title").textContent = node.label;
  document.getElementById("drawer-meta").textContent = `${{node.type}}`;
  document.getElementById("drawer-path").textContent = node.path;
  document.getElementById("drawer-preview").textContent = node.preview || "";
  document.getElementById("drawer-markdown").innerHTML = renderMarkdown(node.markdown || "");

  const relatedList = document.getElementById("drawer-related-list");
  relatedList.innerHTML = "";
  const relatedNodes = originalNodes
    .filter(item => relatedIds.has(item.id) && item.id !== node.id)
    .sort((a, b) => a.label.localeCompare(b.label, "zh-Hans-CN"));

  if (relatedNodes.length === 0) {{
    const empty = document.createElement("span");
    empty.textContent = "No directly connected nodes";
    relatedList.appendChild(empty);
    return;
  }}

  for (const related of relatedNodes) {{
    const chip = document.createElement("button");
    chip.className = "related-chip";
    chip.textContent = related.label;
    chip.onclick = () => focusNode(related.id);
    relatedList.appendChild(chip);
  }}
}}

function applyFilters(query, selectedNodeId) {{
  const lower = (query || "").trim().toLowerCase();
  const relatedIds = selectedNodeId
    ? new Set([selectedNodeId, ...(adjacency.get(selectedNodeId) || [])])
    : null;

  const nodeUpdates = originalNodes.map(node => {{
    const matchesSearch = !lower || node.label.toLowerCase().includes(lower);
    const isRelated = !relatedIds || relatedIds.has(node.id);
    const isActive = selectedNodeId === node.id;
    const isVisible = matchesSearch && isRelated;
    const background = isVisible ? node.color : hexToRgba(node.color, 0.14);
    const border = isVisible ? hexToRgba(node.color, 0.92) : hexToRgba(node.color, 0.22);
    const fontColor = isVisible ? "#f2f3f8" : "rgba(242, 243, 248, 0.2)";

    return {{
      id: node.id,
      color: {{
        background,
        border,
        highlight: {{ background: node.color, border: hexToRgba(node.color, 1) }},
        hover: {{ background: node.color, border: hexToRgba(node.color, 1) }},
      }},
      font: {{ color: fontColor }},
      borderWidth: isActive ? 5 : 2,
      size: isActive ? 18 : 12,
    }};
  }});

  const edgeUpdates = originalEdges.map(edge => {{
    const matchesSearch = !lower
      || nodeMap.get(edge.from)?.label.toLowerCase().includes(lower)
      || nodeMap.get(edge.to)?.label.toLowerCase().includes(lower);
    const isRelated = !relatedIds || relatedIds.has(edge.from) || relatedIds.has(edge.to);
    const touchesActive = selectedNodeId
      && (edge.from === selectedNodeId || edge.to === selectedNodeId);
    const isVisible = matchesSearch && isRelated;

    return {{
      id: edge.id,
      hidden: false,
      width: touchesActive ? 2.8 : isVisible ? 1.2 : 0.6,
      color: isVisible ? edge.color : hexToRgba(edge.color, 0.08),
    }};
  }});

  nodes.update(nodeUpdates);
  edges.update(edgeUpdates);
}}

function focusNode(nodeId) {{
  activeNodeId = nodeId;
  const node = nodeMap.get(nodeId) || nodes.get(nodeId);
  const relatedIds = new Set([nodeId, ...(adjacency.get(nodeId) || [])]);
  applyFilters(searchInput.value, nodeId);
  openDrawer(node, relatedIds);
  network.focus(nodeId, {{
    scale: 1.1,
    animation: {{ duration: 300, easingFunction: "easeInOutQuad" }},
  }});
}}

network.on("click", params => {{
  if (params.nodes.length > 0) {{
    focusNode(params.nodes[0]);
  }} else {{
    clearSelection();
  }}
}});
</script>
</body>
</html>"""


def append_log(entry: str):
    log_path = WIKI_DIR / "log.md"
    entry_text = entry.strip()
    if not log_path.exists():
        log_path.write_text(
            "# Wiki Log\n\n"
            "> Records important additions, revisions, and clarifications in the project knowledge layer. Maintained in append-only mode for agent and human traceability.\n\n"
            f"{entry_text}\n",
            encoding="utf-8",
        )
        return

    existing = read_file(log_path).rstrip()
    if not existing:
        existing = (
            "# Wiki Log\n\n"
            "> Records important additions, revisions, and clarifications in the project knowledge layer. Maintained in append-only mode for agent and human traceability."
        )
    log_path.write_text(existing + "\n\n" + entry_text + "\n", encoding="utf-8")


def build_graph(infer: bool = True, open_browser: bool = False):
    pages = all_wiki_pages()
    today = date.today().isoformat()

    if not pages:
        print("Wiki is empty. Ingest some sources first.")
        return

    print(f"Building graph from {len(pages)} wiki pages...")
    GRAPH_DIR.mkdir(parents=True, exist_ok=True)

    cache = load_cache()

    # Pass 1: extracted edges
    print("  Pass 1: extracting wikilinks...")
    nodes = build_nodes(pages)
    edges = build_extracted_edges(pages)
    print(f"  → {len(edges)} extracted edges")

    # Pass 2: inferred edges
    if infer:
        print("  Pass 2: inferring semantic relationships...")
        inferred = build_inferred_edges(pages, edges, cache)
        edges.extend(inferred)
        print(f"  → {len(inferred)} inferred edges")
        save_cache(cache)

    # Community detection
    print("  Running Louvain community detection...")
    communities = detect_communities(nodes, edges)
    for node in nodes:
        comm_id = communities.get(node["id"], -1)
        if comm_id >= 0:
            node["color"] = COMMUNITY_COLORS[comm_id % len(COMMUNITY_COLORS)]
        node["group"] = comm_id

    # Save graph.json
    graph_data = {"nodes": nodes, "edges": edges, "built": today}
    GRAPH_JSON.write_text(json.dumps(graph_data, indent=2))
    print(f"  saved: graph/graph.json  ({len(nodes)} nodes, {len(edges)} edges)")

    # Save graph.html
    html = render_html(nodes, edges)
    GRAPH_HTML.write_text(html)
    print(f"  saved: graph/graph.html")

    append_log(f"## [{today}] graph | Knowledge graph rebuilt\n\n{len(nodes)} nodes, {len(edges)} edges ({len([e for e in edges if e['type']=='EXTRACTED'])} extracted, {len([e for e in edges if e['type']=='INFERRED'])} inferred).")

    if open_browser:
        webbrowser.open(f"file://{GRAPH_HTML.resolve()}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build LLM Wiki knowledge graph")
    parser.add_argument("--no-infer", action="store_true", help="Skip semantic inference (faster)")
    parser.add_argument("--open", action="store_true", help="Open graph.html in browser")
    args = parser.parse_args()
    build_graph(infer=not args.no_infer, open_browser=args.open)
