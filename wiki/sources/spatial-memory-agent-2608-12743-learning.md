---
title: "Spatial Memory Agent 학습 노트: verifier-grounded procedure retrieval"
type: source
tags: [spatial-memory, vision-language-model, embodied-ai, learning-guide, training-free]
date: 2026-08-19
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W33/spatial-memory-agent-2608-12743/learning.md
source_hash: f7029697a92d9a87
---

## Summary
이 학습 노트는 Spatial Memory Agent(SMA)의 verifier-grounded procedure retrieval을 구현 관점에서 설명한다. 핵심은 동결된 VLM이 검증된 공간 경험을 정답 replay가 아닌 재사용 가능한 절차 교훈으로 저장하고, semantic relevance와 방문 기반 Transfer Reliability Score를 함께 사용해 새 공간 문제에 주입하는 것이다.

## Key Concepts
- memory card는 task, 요약, transferable lesson, 방문 횟수, 누적 reward, 신뢰도를 보관한다.
- low-visit prior를 둔 TRS 보정은 일회성 성공·실패에 대한 과신을 줄인다.
- read-only deployment는 평가/운영 중 memory writeback을 막아 leakage와 online contamination을 분리한다.
- 로봇·VLA 시스템에서는 procedure memory를 controller가 아닌 spatial reasoning guidance로 취급하고 downstream safety gate를 둬야 한다.

## Practical Notes
구현 시 카드 provenance, verifier version, retrieval event를 추적하고, deduplication·trusted writer·counterfactual credit assignment를 고려한다. 이 노트의 원본은 한국어 학습 자료이며 수식, Mermaid 흐름도, 자가 점검 질문을 포함한다.

## Source
- Original raw note: `raw/Robotics/HuggingFaceWeeklyPapers/2026-W33/spatial-memory-agent-2608-12743/learning.md`
- arXiv: https://arxiv.org/abs/2608.12743
