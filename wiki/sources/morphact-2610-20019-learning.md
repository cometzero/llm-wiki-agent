---
title: "MorphAct 핵심 기술 학습"
type: "source"
tags: ["VLA", "robotics", "hf-weekly", "contextual-parameterization"]
sources: ["morphact-2610-20019-learning"]
date: "2026-10-21"
last_updated: "2026-10-21"
source_file: "raw/Robotics/HuggingFaceWeeklyPapers/2026-W43/morphact-2610-20019/learning.md"
source_hash: "3391e0f39d91a7bb"
---

## Summary
dynamic low-rank update, representation coupling, gradient의 두 경로, flow velocity target, context/solver의 서로 다른 clock을 예제로 설명한다. pure-Python low-rank residual 예제와 Q&A를 포함한다.

## Key Claims
- generated A/B는 optimizer가 직접 갱신하는 independent parameter가 아닌 generator의 differentiable output이다.
- frozen backbone도 입력/condition에 대한 gradient 전파는 유지해야 한다.
- chunk latency의 역수와 measured control rate를 혼동하지 않는다.

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
