#!/usr/bin/env python3
"""Prepare Hugging Face weekly-best paper candidates for a Hermes cron job.

The script intentionally only discovers and scores candidates. The Hermes agent that
runs after this script selects 1-2 papers, translates/analyzes them, writes raw
markdown files, ingests them into llm-wiki-agent, commits, and pushes.
"""

from __future__ import annotations

import datetime as dt
import html as html_lib
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from zoneinfo import ZoneInfo

REPO = Path(__file__).resolve().parents[1]
RAW_BASE = REPO / "raw"
STATE_DIR = RAW_BASE / "hf_weekly_best_papers"
STATE_PATH = STATE_DIR / "state.json"

TOPIC_TERMS = {
    # autonomous driving / end-to-end AD
    "autonomous driving": 8,
    "self-driving": 8,
    "end-to-end autonomous": 8,
    "e2e autonomous": 8,
    "driving": 4,
    "traffic": 3,
    "nuplan": 5,
    "waymo": 4,
    "carla": 4,
    "bev": 4,
    "occupancy": 4,
    "trajectory": 3,
    "planning": 3,
    "planner": 3,
    # VLA / VLM / multimodal action
    "vision-language-action": 10,
    "vision language action": 10,
    "vla": 8,
    "vision-language": 5,
    "vision language": 5,
    "vlm": 6,
    "multimodal": 3,
    "action grounding": 6,
    "embodied": 4,
    "robotics": 4,
    # NPU / acceleration / edge inference
    "npu": 10,
    "neural processing unit": 10,
    "accelerator": 5,
    "edge ai": 5,
    "on-device": 5,
    "quantization": 4,
    "compilation": 3,
    "compiler": 3,
}


def fetch(url: str) -> str:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Hermes llm-wiki-agent weekly paper monitor)",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        },
    )
    with urllib.request.urlopen(req, timeout=40) as resp:
        return resp.read().decode("utf-8", "ignore")


def parse_hf_week(url: str) -> list[dict]:
    page = fetch(url)
    best = None
    for match in re.finditer(r'data-props="([^"]*)"', page):
        raw = html_lib.unescape(match.group(1))
        if "dailyPapers" not in raw or "periodType" not in raw:
            continue
        try:
            props = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if isinstance(props, dict) and props.get("dailyPapers"):
            if best is None or len(props["dailyPapers"]) > len(best.get("dailyPapers", [])):
                best = props
    if not best:
        return []
    out = []
    for rank, item in enumerate(best.get("dailyPapers", []), start=1):
        paper = item.get("paper", {}) or {}
        pid = paper.get("id") or ""
        if not pid:
            continue
        authors = paper.get("authors") or []
        if authors and isinstance(authors[0], dict):
            author_names = [a.get("name") or a.get("fullname") or "" for a in authors]
        else:
            author_names = [str(a) for a in authors]
        keywords = paper.get("ai_keywords") or []
        text = "\n".join(
            str(x or "")
            for x in [
                paper.get("title"),
                paper.get("summary"),
                paper.get("ai_summary"),
                " ".join(map(str, keywords)),
            ]
        ).lower()
        score = 0
        matched = []
        for term, weight in TOPIC_TERMS.items():
            # Avoid false positives for short acronyms such as NPU/VLA/VLM/BEV
            # matching inside ordinary words like "input".
            if re.search(r"(?<![a-z0-9-])" + re.escape(term) + r"(?![a-z0-9-])", text):
                score += weight
                matched.append(term)
        upvotes = int(paper.get("upvotes") or 0)
        out.append(
            {
                "rank": rank,
                "id": pid,
                "title": paper.get("title") or item.get("title") or pid,
                "authors": [a for a in author_names if a],
                "summary": paper.get("summary") or item.get("summary") or "",
                "ai_summary": paper.get("ai_summary") or "",
                "ai_keywords": keywords,
                "upvotes": upvotes,
                "score": score,
                "matched_terms": matched,
                "hf_url": f"https://huggingface.co/papers/{pid}",
                "arxiv_abs_url": f"https://arxiv.org/abs/{pid}",
                "arxiv_pdf_url": f"https://arxiv.org/pdf/{pid}",
                "arxiv_html_url": f"https://arxiv.org/html/{pid}",
                "project_page": paper.get("projectPage"),
                "github_repo": paper.get("githubRepo"),
            }
        )
    return sorted(out, key=lambda x: (x["score"], x["upvotes"]), reverse=True)


ARXIV_ID_RE = re.compile(r"(?<!\d)(\d{4}\.\d{4,5})(?:v\d+)?(?!\d)")


def normalize_paper_id(value: str) -> str | None:
    """Return a stable arXiv/HF paper id without version suffix."""
    match = ARXIV_ID_RE.search(value or "")
    if not match:
        return None
    return match.group(1)


def state_processed_ids() -> set[str]:
    if not STATE_PATH.exists():
        return set()
    try:
        state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    except Exception:
        return set()
    ids = set()
    for raw_id in state.get("processed_paper_ids", []):
        pid = normalize_paper_id(str(raw_id))
        if pid:
            ids.add(pid)
    return ids


def extract_metadata_block(text: str) -> str:
    """Extract likely frontmatter/header text to avoid treating references as analyzed papers."""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[: end + 4]
    # Include the opening region where title/source metadata normally lives, but
    # not full References sections where cited-but-not-analyzed arXiv IDs appear.
    return "\n".join(text.splitlines()[:80])


def collect_existing_analysis_ids() -> dict[str, list[str]]:
    """Find papers that already have analysis material in raw/wiki.

    This is intentionally conservative: all ids in paths count, and ids in
    frontmatter/header metadata count. Full-body scanning is only enabled for this
    automation's own folders, where every paper folder is an analyzed deliverable.
    """
    roots = [RAW_BASE, REPO / "wiki" / "sources"]
    found: dict[str, list[str]] = {}
    for root in roots:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if path.is_dir():
                pid = normalize_paper_id(str(path.relative_to(REPO)))
                if pid:
                    found.setdefault(pid, []).append(str(path.relative_to(REPO)))
                continue
            if path.suffix.lower() not in {".md", ".json", ".txt"}:
                continue
            rel = str(path.relative_to(REPO))
            pid = normalize_paper_id(rel)
            if pid:
                found.setdefault(pid, []).append(rel)
            try:
                text = path.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue
            scan_text = extract_metadata_block(text)
            # Our generated paper folders are all analyzed deliverables, so a
            # full scan there is safe and catches older metadata variants.
            if "HuggingFaceWeeklyPapers" in rel:
                scan_text = text
            for match in ARXIV_ID_RE.finditer(scan_text):
                found.setdefault(match.group(1), []).append(rel)
    return {pid: sorted(set(paths)) for pid, paths in found.items()}


def iso_week_label(day: dt.date) -> str:
    iso = day.isocalendar()
    return f"{iso.year}-W{iso.week:02d}"


def main() -> int:
    now_kst = dt.datetime.now(ZoneInfo("Asia/Seoul"))
    today = now_kst.date()
    week_days = [today, today - dt.timedelta(days=7)]
    seen_weeks = []
    weeks = []
    for day in week_days:
        label = iso_week_label(day)
        if label in seen_weeks:
            continue
        seen_weeks.append(label)
        url = f"https://huggingface.co/papers/week/{label}"
        try:
            papers = parse_hf_week(url)
            error = None
        except Exception as exc:  # noqa: BLE001 - surface failures as JSON context
            papers = []
            error = repr(exc)
        weeks.append({"week": label, "url": url, "error": error, "papers": papers})

    state_ids = state_processed_ids()
    existing_analysis = collect_existing_analysis_ids()
    processed_ids_set = state_ids | set(existing_analysis)
    processed_ids = sorted(processed_ids_set)

    # Keep high-scoring papers first, but include a few zero-score top-HF papers so
    # the LLM can catch relevant papers that use unexpected wording. Candidates
    # already present in state or existing raw/wiki analysis are excluded here.
    candidates = []
    excluded_candidates = []
    added = set()
    for w in weeks:
        for p in w["papers"]:
            if p["id"] in processed_ids_set:
                q = dict(p)
                q["week"] = w["week"]
                q["week_url"] = w["url"]
                q["excluded_reason"] = "already analyzed"
                q["analysis_paths"] = existing_analysis.get(p["id"], [])[:8]
                excluded_candidates.append(q)
        positives = [p for p in w["papers"] if p["score"] > 0 and p["id"] not in processed_ids_set]
        fallback = [p for p in w["papers"][:30] if p["id"] not in processed_ids_set]
        for p in positives[:20] + fallback[:10]:
            key = p["id"]
            if key in added:
                continue
            q = dict(p)
            q["week"] = w["week"]
            q["week_url"] = w["url"]
            candidates.append(q)
            added.add(key)
    candidates = sorted(candidates, key=lambda x: (x["score"], x["upvotes"]), reverse=True)[:30]

    payload = {
        "run_date_kst": now_kst.strftime("%Y-%m-%d %H:%M:%S %Z"),
        "repo": str(REPO),
        "raw_base": str(RAW_BASE),
        "state_path": str(STATE_PATH),
        "preferred_raw_roots": {
            "autonomous_driving_vla_vlm": "raw/Robotics/HuggingFaceWeeklyPapers",
            "general_vlm_ai": "raw/AI/HuggingFaceWeeklyPapers",
            "npu_hardware": "raw/Technology/HuggingFaceWeeklyPapers",
        },
        "topic": ["autonomous driving", "VLA", "VLM", "E2E Autonomous Driving", "NPU"],
        "weeks_checked": [{k: v for k, v in w.items() if k != "papers"} | {"paper_count": len(w["papers"])} for w in weeks],
        "processed_paper_ids": processed_ids,
        "processed_paper_sources": {
            "state_json_ids": sorted(state_ids),
            "existing_analysis_ids": sorted(existing_analysis),
            "existing_analysis_paths_sample": {pid: paths[:5] for pid, paths in sorted(existing_analysis.items())[:50]},
        },
        "excluded_candidates_sample": excluded_candidates[:30],
        "candidates": candidates,
        "instructions": [
            "Select 1-2 genuinely relevant papers from candidates only; excluded_candidates_sample are already analyzed and must not be selected.",
            "Before final selection, search the repo for the candidate id and exact/near title. If the id/title already exists in raw/ or wiki/, skip it even if it appears in candidates.",
            "If current ISO week lacks good new matches, use previous week candidates.",
            "After successful ingest/commit/push, append selected IDs to state_path.",
        ],
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
