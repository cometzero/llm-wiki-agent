---
title: "Real-Time Aligned Reward"
type: concept
tags: [reward-model, online-reward, alignment]
last_updated: 2026-08-12
source: [deft-rlvr-2608-01755-references]
---

## Summary
[[RealTimeAlignedReward]]는 실시간 추론/결정 과정에서 정렬 신호를 계산적으로 반영하려는 reward 설계 축이다.

## Key idea
- AD/추론-결정 파이프라인에서 batch 보상이 아닌 online 신호는 latency 제약을 동반한다.
- DEFT-RLVR의 structured rubric과 결합 시, 실시간 제약이 있는 환경에서 과도한 탐색을 억제하고 결정을 안정화한다.

## Connections
- [[DEFT-RLVR]]
- RubricBasedEvaluation
- [[RLVR]]
- [[Latency]]

## Key Claims
- 낮은 오버헤드와 안정적인 정합 신호가 동시에 필요하며, reward 설계가 selection bias를 직접 건드린다.

## Contradictions
- 없음.
