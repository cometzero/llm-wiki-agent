---
title: "EAGLE3"
type: concept
tags:
  - llm
  - inference
  - acceleration
  - speculative-techniques
sources:
  - eagle-3-scaling-up-inference-acceleration-of-large-language-models-via-training-time-test
last_updated: 2026-04-21
---

# EAGLE3

## 정의
[[EAGLE3]]는 대규모 언어 모델(LLM) 추론을 가속화하기 위한 기법으로, 입력 토큰 예측을 직접 수행하고 학습 시점에서 추론 동작을 모사하는 [[TrainingTimeTest]]를 결합한다.

## 핵심 메커니즘
- 특징 예측 기반의 제약 완화: 기존 단일 수준 feature 예측 위주의 방식에서 벗어나 직접 토큰 예측.
- 층간 특징 결합: [[MultiLayerFeatureFusion]]을 통해 저/중/고 레이어 정보를 통합.
- 스케일링 정합성: 훈련 데이터/학습 토큰이 증가함에 따라 추론 속도 향상이 나타난다고 주장됨.

## 실험 요약
- [[Vicuna-13B]]/[[HumanEval]]: 약 6.47x
- [[LLaMA-3.1-8B]]/[[MT-bench]]: 약 4.40x
- [[LLaMA-3.3-70B]]/[[GSM8K]]: 약 4.34x

## 연결 페이지
- [[TrainingTimeTest]]
- [[MultiLayerFeatureFusion]]
- [[InferenceOptimization]]
- [[LLM]]
- [[Token-level Prediction]]