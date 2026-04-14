#!/usr/bin/env python3
"""
Ingest a source document into the LLM Wiki.

Usage:
    python tools/ingest.py <path-to-source>
    python tools/ingest.py raw/articles/my-article.md

The LLM reads the source, extracts knowledge, and updates the wiki:
  - Creates wiki/sources/<slug>.md
  - Updates wiki/index.md
  - Updates wiki/overview.md (if warranted)
  - Creates/updates entity and concept pages
  - Appends to wiki/log.md
  - Flags contradictions
"""

import os
import sys
import json
import hashlib
import re
from pathlib import Path
from datetime import date

import os

REPO_ROOT = Path(__file__).parent.parent
WIKI_DIR = REPO_ROOT / "wiki"
LOG_FILE = WIKI_DIR / "log.md"
INDEX_FILE = WIKI_DIR / "index.md"
OVERVIEW_FILE = WIKI_DIR / "overview.md"
SCHEMA_FILE = REPO_ROOT / "CLAUDE.md"


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()[:16]


def read_file(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def call_llm(prompt: str, max_tokens: int = 8192) -> str:
    try:
        from litellm import completion
    except ImportError:
        print("Error: litellm not installed. Run: pip install litellm")
        sys.exit(1)
        
    model = os.getenv("LLM_MODEL", "claude-3-5-sonnet-latest")
    
    kwargs = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}]
    }
    
    if max_tokens:
        kwargs["max_tokens"] = max_tokens

    response = completion(**kwargs)
    return response.choices[0].message.content


def write_file(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"  wrote: {path.relative_to(REPO_ROOT)}")


def build_wiki_context() -> str:
    parts = []
    if INDEX_FILE.exists():
        parts.append(f"## wiki/index.md\n{read_file(INDEX_FILE)}")
    if OVERVIEW_FILE.exists():
        parts.append(f"## wiki/overview.md\n{read_file(OVERVIEW_FILE)}")
    # Include a few recent source pages for contradiction checking
    sources_dir = WIKI_DIR / "sources"
    if sources_dir.exists():
        recent = sorted(sources_dir.glob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True)[:5]
        for p in recent:
            parts.append(f"## {p.relative_to(REPO_ROOT)}\n{p.read_text()}")
    return "\n\n---\n\n".join(parts)


def parse_json_from_response(text: str) -> dict:
    # Strip markdown code fences if present
    text = re.sub(r"^```(?:json)?\s*", "", text.strip())
    text = re.sub(r"\s*```$", "", text.strip())
    # Find the outermost JSON object
    match = re.search(r"\{[\s\S]*\}", text)
    if not match:
        raise ValueError("No JSON object found in response")
    return json.loads(match.group())


def update_index(new_entry: str, section: str = "Sources"):
    content = read_file(INDEX_FILE)
    if not content:
        content = "# Wiki Index\n\n## Overview\n- [Overview](overview.md) — living synthesis\n\n## Sources\n\n## Entities\n\n## Concepts\n\n## Syntheses\n"
    section_header = f"## {section}"
    if section_header in content:
        content = content.replace(section_header + "\n", section_header + "\n" + new_entry + "\n")
    else:
        content += f"\n{section_header}\n{new_entry}\n"
    write_file(INDEX_FILE, content)


def append_log(entry: str):
    existing = read_file(LOG_FILE)
    write_file(LOG_FILE, entry.strip() + "\n\n" + existing)


def ingest(source_path: str):
    source = Path(source_path)
    if not source.exists():
        print(f"Error: file not found: {source_path}")
        sys.exit(1)

    source_content = source.read_text(encoding="utf-8")
    source_hash = sha256(source_content)
    today = date.today().isoformat()

    print(f"\nIngesting: {source.name}  (hash: {source_hash})")

    wiki_context = build_wiki_context()
    schema = read_file(SCHEMA_FILE)

    schema = read_file(SCHEMA_FILE)

    prompt = f"""You are maintaining an LLM Wiki. Process this source document and integrate its knowledge into the wiki.

Schema and conventions:
{schema}

Current wiki state (index + recent pages):
{wiki_context if wiki_context else "(wiki is empty — this is the first source)"}

New source to ingest (file: {source.relative_to(REPO_ROOT) if source.is_relative_to(REPO_ROOT) else source.name}):
=== SOURCE START ===
{source_content}
=== SOURCE END ===

Today's date: {today}

Return ONLY a valid JSON object with these fields (no markdown fences, no prose outside the JSON):
{{
  "title": "Human-readable title for this source",
  "slug": "kebab-case-slug-for-filename",
  "source_page": "full markdown content for wiki/sources/<slug>.md — use the source page format from the schema. CRITICAL: Aggressively convert key people, products, concepts and projects into [[Wikilinks]] inline in the text. Omitting [[ ]] for known terms is a failure.",
  "index_entry": "- [Title](sources/slug.md) — one-line summary",
  "overview_update": "full updated content for wiki/overview.md, or null if no update needed",
  "entity_pages": [
    {{"path": "entities/EntityName.md", "content": "full markdown content"}}
  ],
  "concept_pages": [
    {{"path": "concepts/ConceptName.md", "content": "full markdown content"}}
  ],
  "contradictions": ["describe any contradiction with existing wiki content, or empty list"],
  "log_entry": "## [{today}] ingest | <title>\\n\\nAdded source. Key claims: ..."
}}
"""

    print(f"  calling API (model: ...)")
    raw = call_llm(prompt, max_tokens=8192)
    try:
        data = parse_json_from_response(raw)
    except (ValueError, json.JSONDecodeError) as e:
        print(f"Error parsing API response: {e}")
        print("Raw response saved to /tmp/ingest_debug.txt")
        Path("/tmp/ingest_debug.txt").write_text(raw)
        sys.exit(1)

    # Write source page
    slug = data["slug"]
    write_file(WIKI_DIR / "sources" / f"{slug}.md", data["source_page"])

    # Write entity pages
    for page in data.get("entity_pages", []):
        write_file(WIKI_DIR / page["path"], page["content"])

    # Write concept pages
    for page in data.get("concept_pages", []):
        write_file(WIKI_DIR / page["path"], page["content"])

    # Update overview
    if data.get("overview_update"):
        write_file(OVERVIEW_FILE, data["overview_update"])

    # Update index
    update_index(data["index_entry"], section="Sources")

    # Append log
    append_log(data["log_entry"])

    # Report contradictions
    contradictions = data.get("contradictions", [])
    if contradictions:
        print("\n  ⚠️  Contradictions detected:")
        for c in contradictions:
            print(f"     - {c}")

    print(f"\nDone. Ingested: {data['title']}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python tools/ingest.py <path-to-source> [path2 ...] [dir1 ...]")
        sys.exit(1)
        
    paths_to_process = []
    for arg in sys.argv[1:]:
        p = Path(arg)
        if p.is_file() and p.suffix == ".md":
            paths_to_process.append(p)
        elif p.is_dir():
            for f in p.rglob("*.md"):
                if f.is_file():
                    paths_to_process.append(f)
        else:
            import glob
            for f in glob.glob(arg, recursive=True):
                g_p = Path(f)
                if g_p.is_file() and g_p.suffix == ".md":
                    paths_to_process.append(g_p)
                    
    # Deduplicate while preserving order
    unique_paths = []
    seen = set()
    for p in paths_to_process:
        abs_p = p.resolve()
        if abs_p not in seen:
            seen.add(abs_p)
            unique_paths.append(p)

    if not unique_paths:
        print("Error: no markdown files found to ingest.")
        sys.exit(1)
        
    if len(unique_paths) > 1:
        print(f"Batch mode: found {len(unique_paths)} files to ingest.")
        
    for p in unique_paths:
        ingest(str(p))
