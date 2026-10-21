---
title: "MorphAct 한국어 기술 해설"
type: "source"
tags: ["VLA", "robotics", "hf-weekly", "contextual-parameterization"]
sources: ["morphact-2610-20019-paper-ko"]
date: "2026-10-21"
last_updated: "2026-10-21"
source_file: "raw/Robotics/HuggingFaceWeeklyPapers/2026-W43/morphact-2610-20019/paper-ko.md"
source_hash: "b06a9f7e3c857284"
---

## Summary
동일 instruction 아래 달라지는 interaction context에 맞춰 vision-language/action module의 low-rank effective weight를 생성한다. adapted VLM representation이 action generator와 native action condition에 함께 쓰이며, 기존 backbone의 action objective를 보존한다. 원문의 비독점 라이선스를 확인해 전면 번역 대신 상세 해설로 구성하고 Appendix와 dense table의 생략을 표시했다.

## Key Claims
- 65 atomic task의 gradient interference 진단은 한 checkpoint 주변의 local evidence이며 rollout safety 증명이 아니다.
- LIBERO·Meta-World·네 physical task의 closed-loop 결과를 보고한다. Sort Hardware는 8→22%로 +14 pp이나 여전히 절대 SR이 낮다.
- π0.5 chunk latency 138.71→164 ms, memory 7.88→9.53 GiB의 overhead가 있다.

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
