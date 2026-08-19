---
title: "SpatialMemoryAgent"
type: concept
tags:
  - embodied-ai
  - vision-language-model
  - spatial-reasoning
  - retrieval
  - memory
  - verification
last_updated: 2026-08-19
---

## 정의

[[SpatialMemoryAgent]]는 frozen [[VisionLanguageModel|VLM]]을 유지한 채, verifier 기반 rollout 결과를 사용해 공간 과제에서 재사용 가능한 절차를 메모리로 축적하고 다음 추론에서 top-k 가이던스로 넣어 성능을 보정하는 framework이다. 핵심은 “retraining”이 아니라, 메모리 정책 학습/갱신이다.

## 핵심 구성

- 메모리 카드: `(task, summary, transferable lesson, visit count n, cumulative reward c, [[TransferReliabilityScore|TRS]])`
- one-pass 기록: 과도한 중복 기록을 방지
- read-only deployment: 학습/쓰기 없이 추론 단계에서 retrieval만 수행

## 작동 원리

1. frozen VLM이 공간 과제 추론
2. verifier가 행동 결과를 채점해 reflection 생성
3. 반영 가능한 절차를 `summary + lesson`으로 압축해 카드화
4. semantic similarity 및 TRS를 결합한 ranking으로 top-k 선택
5. 추론 시 prompt로 card guidance 주입
6. 신규 과제 방문 증거 기반으로 TRS만 갱신

## 실용적 위치

[[SpatialMemoryAgent]]는 
- full retraining 방식 대신
- external tool-heavy planner 의존성을 낮추고
- VLM inference 비용 구조를 크게 바꾸지 않으면서
성능 안정성을 노리는 
**training-free memory adaptation** 축으로 이해한다.

## 장단점

- 장점: low-cost adaptation, 재현성 높은 구조, transfer 적응력
- 리스크: credit assignment 불분해성, 메모리 주입 공격, OOD embedding 한계

## 연관 항목

- [[TransferReliabilityScore]]
- [[PersistentMemory]]
- [[ReflectiveReasoning]]
- [[RetrievalAugmentedPolicy]]
- [[RAG]]
- [[ActionGrounding]]