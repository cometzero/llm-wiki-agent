## [2026-04-16] ingest | Bulk corpus sync

- Rebuilt `wiki/index.md` and `wiki/overview.md` after confirming all raw markdown sources are represented in `wiki/sources/`.
- Corpus status: 64 sources, 91 entities, 65 concepts.

# Wiki Log

Append-only chronological record of all operations.

Format: `## [YYYY-MM-DD] <operation> | <title>`

Parse recent entries: `grep "^## \[" wiki/log.md | tail -10`

---

## [2026-04-18] graph | Knowledge graph rebuilt

221 nodes, 1880 edges (1117 extracted, 763 inferred).
