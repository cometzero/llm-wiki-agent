---
title: "Multi-Layer Feature Fusion"
type: concept
tags:
  - llm
  - model-architecture
  - inference-optimization
sources:
  - eagle-3-scaling-up-inference-acceleration-of-large-language-models-via-training-time-test
last_updated: 2026-04-21
---

# Multi-Layer Feature Fusion

## 정의
[[MultiLayerFeatureFusion]]은 LLM의 단일 레이어 피처만 쓰는 방식에서 벗어나, 저레벨/중레벨/고레벨 특징을 통합해 예측 품질과 안정성을 개선하는 접근이다.

## EAGLE-3 적용 맥락
[[EAGLE3]] 파이프라인에서 다층 특징 융합은 직접 토큰 예측 과정의 컨텍스트를 강화해 수용률 급락을 완화하고 속도 개선을 유지하는 데 기여한다고 요약된다.

## 효과
- 의미 표현 정보량 증가
- 단계별 예측 신뢰성 유지
- 추론 가속 스케일링과의 병행 가능성

## 연결 페이지
- [[EAGLE3]]
- [[TrainingTimeTest]]
- [[InferenceOptimization]]
- [[LLM]]