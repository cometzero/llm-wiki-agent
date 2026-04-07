# LLM Wiki Agent

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

**A personal knowledge base that builds and maintains itself.** Drop in source documents — articles, papers, notes — and the LLM reads them, extracts the knowledge, and integrates everything into a persistent, interlinked wiki. You never write the wiki. Claude does.

Unlike RAG systems that re-derive knowledge from scratch on every query, LLM Wiki Agent compiles knowledge once and keeps it current. Cross-references are pre-built. Contradictions are flagged at ingest time. Every new source makes the wiki richer.

## How It Works

```
You drop a source → Claude reads it → wiki pages are created/updated → graph is rebuilt

You ask a question → Claude reads relevant wiki pages → synthesizes answer with citations
```

Three layers:

- **`raw/`** — your source documents (immutable, you own this)
- **`wiki/`** — Claude-maintained markdown pages (Claude writes, you read)
- **`graph/`** — auto-generated knowledge graph visualization

## Quick Start

```bash
git clone https://github.com/SamurAIGPT/llm-wiki-agent.git
cd llm-wiki-agent
```

Open it in your coding agent — **no API key or Python setup needed**:

```bash
claude      # Claude Code
codex       # OpenAI Codex
opencode    # OpenCode / Pear AI
gemini      # Gemini CLI
```

Each agent reads its config file automatically (`CLAUDE.md`, `AGENTS.md`, or `GEMINI.md`) and follows the same workflows. Then just talk to it:

```
# Claude Code — slash commands:
/wiki-ingest raw/articles/my-article.md
/wiki-query what are the main themes across all sources?
/wiki-lint
/wiki-graph

# Any agent — plain English works too:
"Ingest this paper: raw/papers/my-paper.md"
"What does the wiki say about X?"
"Check for contradictions"
"Build the knowledge graph"
```

| Agent | Config file |
|---|---|
| [Claude Code](https://claude.ai/code) | `CLAUDE.md` + `.claude/commands/` |
| [OpenAI Codex](https://openai.com/codex) | `AGENTS.md` |
| OpenCode / Pear AI | `AGENTS.md` |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | `GEMINI.md` |

> **Standalone use** (without a coding agent): `pip install -r requirements.txt`, set `ANTHROPIC_API_KEY`, then use `python tools/ingest.py`, `python tools/query.py`, etc.

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

## Commands

### Claude Code (primary — no API key)

| Slash command | What it does |
|---|---|
| `/wiki-ingest <file>` | Read a source, update wiki pages, append to log |
| `/wiki-query <question>` | Search wiki, synthesize answer with citations |
| `/wiki-lint` | Check for orphans, broken links, contradictions, gaps |
| `/wiki-graph` | Build knowledge graph (`graph.json` + `graph.html`) |

Or describe what you want in plain English — Claude Code follows `CLAUDE.md` and does the right thing.

### Standalone Python (optional — requires `ANTHROPIC_API_KEY`)

| Command | What it does |
|---|---|
| `python tools/ingest.py <file>` | Ingest a source |
| `python tools/query.py "<question>"` | Query the wiki |
| `python tools/query.py "<question>" --save` | Query and file answer back |
| `python tools/lint.py` | Lint the wiki |
| `python tools/build_graph.py` | Build graph |
| `python tools/build_graph.py --no-infer` | Build graph (skip inference, faster) |
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

### Research

Going deep on a topic over weeks or months — reading papers, articles, reports.

```
# Each paper you read gets ingested:
/wiki-ingest raw/papers/attention-is-all-you-need.md
/wiki-ingest raw/papers/llama2.md
/wiki-ingest raw/papers/rag-survey.md

# Wiki builds up entity pages (e.g. "Meta AI", "Google Brain") and
# concept pages (e.g. "Attention Mechanism", "RLHF") automatically.

# Ask synthesis questions across everything you've read:
/wiki-query "What are the main approaches to reducing hallucination?"
/wiki-query "How has context window size evolved across models?"

# Check where your knowledge has gaps:
/wiki-lint
# → "No sources on mixture-of-experts — consider reading the Mixtral paper"
```

By the end of a research project you have a structured, interlinked reference that reflects everything you've read — not a folder of PDFs you'll never reopen.

---

### Reading a Book

File each chapter as you go. Build out pages for characters, themes, plot threads.

```
# After each chapter:
/wiki-ingest raw/book/chapter-01-the-beginning.md
/wiki-ingest raw/book/chapter-02-the-conflict.md

# Wiki creates pages like:
# entities/ElonMusk.md, entities/Tesla.md
# concepts/FirstPrinciplesThinking.md

# Mid-book:
/wiki-query "How has the protagonist's motivation evolved?"
/wiki-query "What contradictions exist in the author's argument so far?"

# End of book — build the graph:
/wiki-graph
# Open graph.html → see every character/theme/event and how they connect
```

Think fan wikis like the Tolkien Gateway — thousands of interlinked pages. You can build something like that as you read, with the agent doing all the cross-referencing.

---

### Personal Knowledge Base

Track goals, health, psychology, self-improvement — file journal entries, articles, podcast notes.

```
# File your journal entries:
/wiki-ingest raw/journal/2026-01-week1.md
/wiki-ingest raw/journal/2026-01-week2.md

# File articles and podcast notes that resonated:
/wiki-ingest raw/articles/huberman-sleep-protocol.md
/wiki-ingest raw/articles/atomic-habits-summary.md

# Ask introspective questions:
/wiki-query "What patterns show up in my journal entries about energy levels?"
/wiki-query "What habits have I tried and what was the outcome?"

# The wiki builds a structured picture of you over time —
# entities like "Sleep", "Exercise", "Deep Work" accumulate evidence
# from every source you've filed.
```

---

### Business / Team Intelligence

Feed in meeting transcripts, Slack exports, project docs, customer calls.

```
# Onboard new context:
/wiki-ingest raw/meetings/q1-planning-transcript.md
/wiki-ingest raw/docs/product-roadmap-2026.md
/wiki-ingest raw/calls/customer-interview-acme.md

# Wiki creates pages for projects, people, decisions, recurring themes.

# Ask strategic questions:
/wiki-query "What feature requests have come up most across customer calls?"
/wiki-query "What decisions were made in Q1 planning and what was the rationale?"

# Lint catches things like:
# → "Project X mentioned in 5 pages but no dedicated page"
# → "Roadmap contradicts customer interview on priority of feature Y"
```

The wiki stays current because the agent does the maintenance no one on the team wants to do.

---

### Competitive Analysis / Due Diligence

Track a company, market, or technology area over time.

```
# Feed in everything you find:
/wiki-ingest raw/competitors/openai-announcements.md
/wiki-ingest raw/competitors/anthropic-blog-posts.md
/wiki-ingest raw/market/ai-funding-report-q1.md

# Wiki builds entity pages per company, concept pages per technology.

# Ask comparison questions:
/wiki-query "How do OpenAI and Anthropic differ in their approach to safety?"
/wiki-query "Which companies have announced multimodal models in the last 6 months?"

# Save the answer back as a reusable synthesis:
/wiki-query "Competitive landscape summary as of today" --save
```

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
