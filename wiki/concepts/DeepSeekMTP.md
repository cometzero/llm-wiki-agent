---
title: "DeepSeek Multi-Token Prediction (MTP)"
type: concept
tags:
  - LLM
  - Decoding
  - InferenceOptimization
  - SpeculativeDecoding
sources:
  - an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference-nvidia-technical-blog
last_updated: 2026-05-03
---

## 정의

[[DeepSeekMTP]]는 [[DeepSeek]] 계열에서 사용된 추측 디코딩 변형으로, 모델 내부의 다중 헤드가 연속적인 여러 미래 토큰을 한 번에 예측하도록 훈련되는 방식이다. 이 경우 각 헤드가 다음 토큰, 그다음 토큰, 다음 다음 토큰을 예측한다.

## 동작 특징

- 외부 별도 드래프트 모델이 없어도 다중 토큰 후보를 생성하려는 아키텍처적 접근.
- 토큰 일치 규칙으로 타겟 검증 단계에서 정합된 앞부분만 채택.
- 하드웨어/스케줄링 관점에서 드래프팅 구조와 검증 구조가 결합되어 있어 수락율 튜닝 포인트가 존재한다.

## 비교

[[EAGLE3]]가 피처 외삽/드래프팅 헤드 기반 트리 구조를 택하는 반면, [[DeepSeekMTP]]는 다중 헤드 예측 체인을 통해 유사한 목표(동시 후보 제시)를 달성한다.

## 출처 연계

본 개념은 해당 NVIDIA 기술 문서의 2.3 절에서 기존 [[SpeculativeDecoding]]의 동급 기법으로 정리되며, 토큰 예측 다중성의 실무 성능/검증 균형을 이해할 때 참조된다.