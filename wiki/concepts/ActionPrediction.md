---
title: "Action Prediction"
type: concept
tags: [Evaluation, ReinforcementLearning, AutonomousVehicle]
last_updated: 2026-05-10
sources:
  - tesla-s-ai-can-explain-itself-ashok-s-mind-blowing-fsd-demo
---

## Summary
[[ActionPrediction]]은 현재 행동(예: 제동/회피/회전) 이후의 단기·중기 결과를 예측해 정책 품질을 판단하는 개념으로, 본 소스에서는 FSD 성능 판단과 안정성 평가의 중심 기준으로 제시된다.

## Key Claims
- 단순 정량 지표만으로는 안전성 보장을 담보하지 못하므로 행동 결과 예측 기반 지표가 필요하다.
- 과거 실패를 재현해 정책이 같은 실수로 돌아가는지를 점검하는 방식은 정책 업데이트의 실질적 가치를 높인다.
- 정책학습의 강화-반복 루프는 행동-결과 연쇄를 압축하여 엣지 케이스 대응력을 강화한다.

## Connections
- [[WorldSimulator]]
- [[PolicyNetwork]]
- [[ClosedLoopEvaluation]]
- [[FSD]]
- [[ReinforcementLearning]]
