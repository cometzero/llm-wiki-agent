# LLM Wiki Agent

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

**A personal knowledge base that builds and maintains itself.** Drop in source documents — articles, papers, notes — and the LLM reads them, extracts the knowledge, and integrates everything into a persistent, interlinked wiki. You never write the wiki. The LLM does.

Unlike RAG systems that re-derive knowledge from scratch on every query, LLM Wiki Agent compiles knowledge once and keeps it current. Cross-references are pre-built. Contradictions are flagged at ingest time. Every new source makes the wiki richer.

## How It Works

```
You drop a source → LLM reads it → wiki pages are created/updated → graph is rebuilt

You ask a question → LLM reads relevant wiki pages → synthesizes answer with citations
```

Three layers:

- **`raw/`** — your source documents (immutable, you own this)
- **`wiki/`** — LLM-maintained markdown pages (Claude writes, you read)
- **`graph/`** — auto-generated knowledge graph visualization

## Quick Start

```bash
git clone https://github.com/SamurAIGPT/GPT-Agent.git
cd GPT-Agent
pip install -r requirements.txt
export ANTHROPIC_API_KEY=your_key_here
```

Add your first source:

```bash
# Drop a source document into raw/
cp my-article.md raw/articles/my-article.md

# Ingest it — LLM reads, extracts, and files knowledge into the wiki
python tools/ingest.py raw/articles/my-article.md
```

Query the wiki:

```bash
python tools/query.py "What are the main themes across all sources?"
python tools/query.py "How does X relate to Y?" --save   # save answer back to wiki
```

Build the knowledge graph:

```bash
python tools/build_graph.py --open   # opens graph.html in browser
```

Health-check the wiki:

```bash
python tools/lint.py --save   # checks for orphans, contradictions, gaps
```

## Architecture

```
raw/                    ← your sources (never modified by LLM)
wiki/
  index.md              ← catalog of all pages (updated on every ingest)
  log.md                ← append-only operation log
  overview.md           ← living synthesis across all sources
  sources/              ← one page per source document
  entities/             ← people, companies, projects
  concepts/             ← ideas, frameworks, methods
  syntheses/            ← answers to queries, filed back as pages
graph/
  graph.json            ← node/edge data (SHA256-cached)
  graph.html            ← interactive vis.js visualization
tools/
  ingest.py             ← process a new source
  query.py              ← ask a question
  lint.py               ← health-check the wiki
  build_graph.py        ← rebuild the knowledge graph
CLAUDE.md               ← schema and workflow instructions for the LLM
```

## Tools

| Command | What it does |
|---|---|
| `python tools/ingest.py <file>` | Read a source, update wiki pages, append to log |
| `python tools/query.py "<question>"` | Search wiki, synthesize answer with citations |
| `python tools/query.py "<question>" --save` | Same, and file the answer back as a wiki page |
| `python tools/lint.py` | Check for orphans, broken links, contradictions, gaps |
| `python tools/build_graph.py` | Build `graph.json` + `graph.html` from wiki |
| `python tools/build_graph.py --no-infer` | Build graph without semantic inference (faster) |
| `python tools/build_graph.py --open` | Build and open in browser |

## The Graph

`build_graph.py` runs two passes:

1. **Deterministic** — parse all `[[wikilinks]]` in every page → explicit edges tagged `EXTRACTED`
2. **Semantic** — Claude infers implicit relationships not captured by wikilinks → edges tagged `INFERRED` (with confidence) or `AMBIGUOUS`

Community detection (Louvain) clusters nodes by topic. The output is a self-contained `graph.html` — open it in any browser. SHA256 caching means only changed pages are reprocessed.

## CLAUDE.md

`CLAUDE.md` is the schema document — it tells the LLM how to maintain the wiki. It defines page formats, ingest/query/lint workflows, naming conventions, and log format. This is the key configuration file. Edit it to customize behavior for your domain.

## What Makes This Different from RAG

| RAG | LLM Wiki Agent |
|---|---|
| Re-derives knowledge every query | Compiles once, keeps current |
| Raw chunks as retrieval unit | Structured wiki pages |
| No cross-references | Cross-references pre-built |
| Contradictions surface at query time (maybe) | Flagged at ingest time |
| No accumulation | Every source makes the wiki richer |

## Use Cases

- **Research** — go deep on a topic over weeks; every paper/article updates the same wiki
- **Reading** — build a companion wiki as you read a book; by the end you have a rich reference
- **Personal knowledge** — file journal entries, health notes, goals; build a structured picture over time
- **Business** — feed in meeting transcripts, Slack threads, docs; LLM does the maintenance no one wants to do

## Tips

- Use [Obsidian](https://obsidian.md) to read/browse the wiki — follow links, check graph view
- Use [Obsidian Web Clipper](https://obsidian.md/clipper) to clip web articles directly to `raw/`
- The wiki is a git repo — you get version history for free
- File good query answers back with `--save` — your explorations compound just like ingested sources

## License

MIT License — see [LICENSE](LICENSE) for details.

## Related

- [graphify](https://github.com/safishamsi/graphify) — graph-based knowledge extraction skill (inspiration for the graph layer)
- [Vannevar Bush's Memex (1945)](https://en.wikipedia.org/wiki/Memex) — the original vision this is related to in spirit
