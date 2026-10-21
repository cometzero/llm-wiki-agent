---
title: "MorphAct 참고문헌 지도"
type: "source"
tags: ["VLA", "robotics", "hf-weekly", "contextual-parameterization"]
sources: ["morphact-2610-20019-references"]
date: "2026-10-21"
last_updated: "2026-10-21"
source_file: "raw/Robotics/HuggingFaceWeeklyPapers/2026-W43/morphact-2610-20019/references.md"
source_hash: "82d06fa1160993f4"
---

## Summary
Semantic Scholar references endpoint와 원문 bibliography에 근거해 핵심 아홉 편을 정리한다. HyperNetworks/HY-WU의 weight generation, π 계열/X-VLA의 native action interface, PCGrad의 conflict, benchmark의 metric semantics를 구분한다.

## Key Claims
- Hypernetwork와 LoRA 자체의 발명 대신 perception/action generation coupling이 차별점이다.
- 각 문헌은 MorphAct와의 관계를 설명하며 원논문 전체의 독립 재현을 주장하지 않는다.

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
