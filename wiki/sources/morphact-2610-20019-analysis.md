---
title: "MorphAct 분석"
type: "source"
tags: ["VLA", "robotics", "hf-weekly", "contextual-parameterization"]
sources: ["morphact-2610-20019-analysis"]
date: "2026-10-21"
last_updated: "2026-10-21"
source_file: "raw/Robotics/HuggingFaceWeeklyPapers/2026-W43/morphact-2610-20019/analysis.md"
source_hash: "c43bd8402fc49106"
---

## Summary
현재 context에 의존하는 effective parameter와 upstream/downstream representation의 정합성을 numerical action VLA 관점에서 분석한다. robot manipulation evidence를 driving/NPU deployment evidence와 분리한다.

## Key Claims
- 입력은 vision observation·instruction·robot state이며 출력은 host policy의 continuous action chunk다.
- Meta-World Avg.는 난이도 group의 동일 가중 평균으로 task-weighted mean과 다르다.
- context-conditioned dynamic weights는 uncertainty·cache freshness·safety filter·device profiling을 별도로 요구한다.

## Provenance
- [MorphAct v1](https://arxiv.org/html/2610.20019v1), read 2026-10-21. All performance claims are author-reported, not independently reproduced.
- NVIDIA ingest failed with HTTP 410; bounded Codex fallback unavailable because CLI is absent. Materialized deterministically from the complete new raw deliverable.

## Key Quotes
- 직접 인용 대신 독자적인 한국어 요약과 분석을 사용합니다.

## Connections
- [[MorphAct]] — method entity
- [[ContextualParameterGeneration]] — coupled dynamic adaptation
- [[LoRA]] — low-rank update representation

## Contradictions
- No direct contradiction identified. Closed-loop manipulation success does not establish vehicle safety, general OOD robustness, or NPU latency.
