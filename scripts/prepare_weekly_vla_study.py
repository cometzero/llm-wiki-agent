#!/usr/bin/env python3
import json
import os
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

REPO = Path(os.environ.get("VLA_STUDY_REPO", "/home/ubuntu/.openclaw/workspace/llm-wiki-agent"))
BASE = REPO / "raw" / "vla_study"
CURRICULUM = BASE / "curriculum.json"
STATE = BASE / "state.json"

def slug(s: str) -> str:
    out = []
    for ch in s.lower():
        if ch.isalnum():
            out.append(ch)
        elif ch in " -_/":
            out.append("-")
    text = "".join(out)
    while "--" in text:
        text = text.replace("--", "-")
    return text.strip("-")[:80] or "vla-study"

def main():
    tz = ZoneInfo("Asia/Seoul")
    today = datetime.now(tz).date().isoformat()
    curriculum = json.loads(CURRICULUM.read_text(encoding="utf-8"))
    state = json.loads(STATE.read_text(encoding="utf-8"))
    already = state.get("last_completed_date") == today
    next_week = int(state.get("next_week", 1))
    total = int(state.get("total_weeks", len(curriculum["weeks"])))
    if next_week > total:
        next_week = 1
    week = curriculum["weeks"][next_week-1]
    target = BASE / "weeks" / f"week-{next_week:02d}-{slug(week['title'])}-{today}.md"
    print(json.dumps({
        "date": today,
        "repo": str(REPO),
        "base_dir": str(BASE),
        "state_path": str(STATE),
        "curriculum_path": str(CURRICULUM),
        "already_completed_today": already,
        "last_completed_date": state.get("last_completed_date"),
        "last_completed_file": state.get("last_completed_file"),
        "week": week,
        "week_number": next_week,
        "total_weeks": total,
        "target_markdown_path": str(target),
        "next_week_after_completion": 1 if next_week >= total else next_week + 1,
        "commit_message": f"docs: add VLA study week {next_week:02d} ({today})"
    }, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
