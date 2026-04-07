# LLM Wiki Agent — Schema & Workflow Instructions

This document defines how Claude maintains this wiki. Follow these conventions exactly in every session.

## Directory Layout

```
raw/          # Immutable source documents — never modify these
wiki/         # Claude owns this layer entirely
  index.md    # Catalog of all pages — update on every ingest
  log.md      # Append-only chronological record
  overview.md # Living synthesis across all sources
  sources/    # One summary page per source document
  entities/   # People, companies, projects, products
  concepts/   # Ideas, frameworks, methods, theories
graph/        # Auto-generated graph data — regenerate with build_graph.py
tools/        # CLI scripts
```

## Page Format

Every wiki page uses this frontmatter:

```yaml
---
title: "Page Title"
type: source | entity | concept | synthesis
tags: []
sources: []       # list of source slugs that inform this page
last_updated: YYYY-MM-DD
---
```

Use `[[PageName]]` wikilinks to link to other wiki pages. These are parsed by build_graph.py.

---

## Ingest Workflow

Triggered when user runs: `python tools/ingest.py <source-path>`

Steps (in order):
1. Read the source document fully
2. Write `wiki/sources/<slug>.md` — title, date, key claims, key quotes, tags, links to entity/concept pages
3. Update `wiki/index.md` — add entry under the correct section
4. Update `wiki/overview.md` — revise synthesis if the source adds new perspectives, themes, or contradicts prior conclusions
5. Update existing entity pages that this source mentions; create new entity pages if needed
6. Update existing concept pages that this source discusses; create new concept pages if needed
7. Flag any contradictions with existing wiki content in the log entry
8. Append to `wiki/log.md` with this prefix format: `## [YYYY-MM-DD] ingest | <Title>`

### Source Page Format

```markdown
---
title: "Source Title"
type: source
tags: []
date: YYYY-MM-DD
source_file: raw/...
---

## Summary
2–4 sentence summary.

## Key Claims
- Claim 1
- Claim 2

## Key Quotes
> "Quote here" — context

## Connections
- [[EntityName]] — how they relate
- [[ConceptName]] — how it connects

## Contradictions
- Contradicts [[OtherPage]] on: ...
```

---

## Query Workflow

Triggered when user runs: `python tools/query.py "<question>"`

Steps:
1. Read `wiki/index.md` to identify relevant pages
2. Read the relevant pages
3. Synthesize an answer with inline citations as wikilinks: `[[PageName]]`
4. Ask the user if they want the answer filed as a new synthesis page in `wiki/`

---

## Lint Workflow

Triggered when user runs: `python tools/lint.py`

Check for:
- **Orphan pages** — wiki pages with no inbound `[[links]]` from other pages
- **Contradictions** — claims that conflict across pages
- **Stale summaries** — pages not updated after newer sources changed the picture
- **Missing entity pages** — entities mentioned in 3+ pages but lacking their own page
- **Broken links** — `[[WikiLinks]]` pointing to pages that don't exist
- **Data gaps** — important questions the wiki cannot answer — suggest new sources to find

Output a lint report as markdown.

---

## Graph Workflow

Triggered when user runs: `python tools/build_graph.py`

- Pass 1: Parse all `[[wikilinks]]` in wiki pages → deterministic edges tagged `EXTRACTED`
- Pass 2: Call Claude API to infer implicit relationships not captured by wikilinks → edges tagged `INFERRED` with confidence score
- Tag ambiguous relationships as `AMBIGUOUS`
- Use Louvain community detection to cluster nodes
- Output `graph/graph.json` and `graph/graph.html`
- Cache by SHA256 of page content — only reprocess changed pages

---

## Naming Conventions

- Source slugs: `kebab-case` matching the source filename
- Entity pages: `TitleCase.md` (e.g. `OpenAI.md`, `SamAltman.md`)
- Concept pages: `TitleCase.md` (e.g. `ReinforcementLearning.md`, `RAG.md`)
- Source pages: `kebab-case.md`

## Index Format

```markdown
# Wiki Index

## Overview
- [Overview](overview.md) — living synthesis

## Sources
- [Source Title](sources/slug.md) — one-line summary

## Entities
- [Entity Name](entities/EntityName.md) — one-line description

## Concepts
- [Concept Name](concepts/ConceptName.md) — one-line description

## Syntheses
- [Analysis Title](syntheses/slug.md) — what question it answers
```

## Log Format

Each entry starts with `## [YYYY-MM-DD] <operation> | <title>` so it's parseable:

```
grep "^## \[" wiki/log.md | tail -10
```

Operations: `ingest`, `query`, `lint`, `graph`
