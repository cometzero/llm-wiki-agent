---
title: "DeepSeek"
type: entity
tags:
  - LLM
  - AI
  - Inference
  - SpeculativeDecoding
last_updated: 2026-05-03
sources:
  - an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference-nvidia-technical-blog
---

## Overview

[[DeepSeek]]는 다중 토큰 예측 계열인 [[DeepSeekMTP]]을 통해 경량 내부 헤드 구조로 여러 미래 토큰을 동시에 예측하는 [[SpeculativeDecoding]] 변형을 제시한 LLM 계열로 언급된다.

## Role in Inference Optimization

이 문서에서 [[DeepSeek]]는 기존 [[DraftModel]]-[[TargetModel]] 방식과 유사하게 성능 향상을 노리지만, 별도의 전문 드래프트 모델 없이 내부 헤드들의 순차적 예측으로 후보 토큰을 제안하는 방식으로 정리된다. 이는 하드웨어와 검증 경로의 구성에 따라 [[AcceptanceRate]]/지연에 영향을 준다.

## Connections
- [[SpeculativeDecoding]] — 다중 토큰 후보 제안 전략의 대표 사례로 소개됨.
- [[DeepSeekMTP]] — 본 문서의 MTP 구현을 대표하는 하위 기술.
- [[LLM]], [[InteractiveInference]] — 생성 속도 개선 적용 대상.

## Notes

현재 위키에 반영된 내용에서 [[DeepSeek]]는 제품명/모델군의 정체성과 함께 [[Multi-Token Prediction]] 기반 추론 가속 축에 위치한다.