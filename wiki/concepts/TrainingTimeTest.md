---
title: "Training-Time Test"
type: concept
tags:
  - llm
  - training
  - inference
  - optimization
sources:
  - eagle-3-scaling-up-inference-acceleration-of-large-language-models-via-training-time-test
last_updated: 2026-04-21
---

# Training-Time Test

## 정의
[[TrainingTimeTest]]는 학습 단계에서 추론 과정을 모사해 모델이 추론 단계에서 요구되는 동작을 미리 정렬시키는 기법이다. EAGLE 시리즈에서 활용되어 드래프트 기반 추론 경로의 품질을 높이는 데 사용되었다.

## 목적
- 추론 과정과 유사한 신호를 학습에 반영.
- 단순 사후 튜닝을 넘어서, 단계별 토큰 예측 안정성과 수용률 유지력 강화.

## 핵심 아이디어
- 훈련 중 다음 단계 시뮬레이션을 통해 모델이 실제 추론 루프의 불안정성에 덜 민감해지게 유도.
- [[EAGLE3]]에서 기존 방식 대비 성능/수용률 균형 개선으로 연결.

## 연결 페이지
- [[EAGLE3]]
- [[InferenceOptimization]]
- [[LLM]]