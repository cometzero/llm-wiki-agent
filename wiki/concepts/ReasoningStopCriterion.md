---
title: "Reasoning Stop Criterion"
type: concept
tags: [reasoning-efficiency, llm-llm-control, stop-criteria]
last_updated: 2026-08-12
source: [deft-rlvr-2608-01755-references]
---

## Summary
[[ReasoningStopCriterion]]는 모델이 언제 추론을 멈춰야 하는지 판단해 unnecessary 탐색을 줄이고 효율을 높이는 축이다.

## Key idea
- 추론이 길수록 성능이 선형으로 향상되지 않으며, unproductive exploration이 커질 수 있다.
- DEFT-RLVR 계열은 candidate 노출 타이밍 제어와 결합해 추론 과잉을 줄이고 decision 정합을 안정화한다.

## Connections
- [[DEFT]]
- [[DEFT-RLVR]]
- [[AD-MCQ]]
- [[AutonomousDrivingVLA]]
- [[Latency]]

## Key Claims
- 적절한 중단 기준은 품질 저하 없이 계산비용과 hallucination을 낮출 수 있다.

## Contradictions
- 없음.
