---
title: "MotorMind 핵심 참고 레퍼런스"
type: source
tags: [huggingface-weekly, robotics, vla, references]
sources: [motormind-2609-38078]
date: 2026-10-07
last_updated: 2026-10-07
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W41/motormind-zero-shot-manipulation-2609-38078/references.md
source_hash: 2a7058ebe25ad2bf
arxiv_id: "2609.38078"
---

## Summary
범용 frozen VLM의 semantic decision을 parameterized mid-level action과 deterministic Controller에 연결한다. sequential execution에 asynchronous monitoring·background memory·explicit outcome verification을 결합하며 LIBERO-PRO와 xArm6에서 zero-shot 조작을 평가한다. Semantic Scholar references endpoint와 원문 bibliography를 대조한 핵심 8편의 식별자·링크와 선택 논문 내 관계를 정리했다. 모든 참고논문을 독립 정독했다는 주장은 하지 않는다.

## Key Claims
- Semantic Scholar references endpoint와 원문 bibliography를 대조한 핵심 8편의 식별자·링크와 선택 논문 내 관계를 정리했다. 모든 참고논문을 독립 정독했다는 주장은 하지 않는다.
- action-boundary stop은 immediate emergency stop이 아니며 local QA·single-seed sensitivity·tabletop SR을 real-road safety로 일반화할 수 없다. 원문 D.1의 task-family count 불일치를 번역에 기록했다.
- 원문과 분석자 deployment 유추를 분리하며 독립 reproduction은 수행하지 않았다.

## Key Quotes
- 긴 원문 인용 대신 raw 번역과 원문 링크를 참조한다.

## Connections
- [[MotorMind]] — 연구 방법과 나머지 세 deliverable을 잇는 중심 페이지.
- [[VisionLanguageModel]] — visual/language decision과 executable action의 연결.
- [[ObservationToActionLoop]] — measured feedback·verification 기반 execution lifecycle.
- [[PerturBot]] — runtime harness와 training-data evidence intervention의 상보적 관계.

## Contradictions and Boundaries
- action-boundary stop은 immediate emergency stop이 아니며 local QA·single-seed sensitivity·tabletop SR을 real-road safety로 일반화할 수 없다. 원문 D.1의 task-family count 불일치를 번역에 기록했다.
- 본 논문은 robotics 연구로 vehicle closed-loop 성능을 직접 입증하지 않는다.

## Source
https://arxiv.org/html/2609.38078v1
