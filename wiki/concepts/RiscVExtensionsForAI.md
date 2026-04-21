---
title: "RiscVExtensionsForAI"
type: concept
tags: [risc-v, architecture, matrix-acceleration, ai-hardware]
last_updated: 2026-04-21
sources:
  - understanding-the-risc-v-extensions-for-ai-john-simpson-sifive
---

## Definition
[[RiscVExtensionsForAI]]는 AI 모델의 행렬 연산, 정밀도 처리, 배치 특성 대응을 위해 [[RiscV]] ISA 위에 제안되는 여러 하드웨어 확장군을 통칭한다.

## Core Idea
AI 확장은 단일 솔루션이 아니라 도메인-워크로드 별 선택이 필요하며, 특히 다음이 핵심이다.
- 기존 [[RiscVVector]]의 연속 유지
- 데이터 타입 확장(FP8/FP16/FP32 등)과 비용-정확도 균형
- 워크로드의 prefill/decode 특성에 대한 대응
- 엣지와 데이터센터의 설계 제약(면적, 대역폭, 배치 크기) 분기

## Current Family Set
- [[VectorBatchProduct]]
- [[IntegratedMatrixExtensions]]
- [[VectorMatrixExtensions]]
- [[AttachedMatrixExtensions]]

## Practical Guidance
- 배치 크기가 작고 빠른 채택이 필요한 경우: [[VectorBatchProduct]] 또는 [[IntegratedMatrixExtensions]]
- 대규모 행렬 연산 및 데이터센터 지향: [[VectorMatrixExtensions]], [[AttachedMatrixExtensions]]
- [[FP64]] 사용이 잦은 경로는 처리량 저하를 초래하므로 별도 추정 필요

## Cross-links
- [[LLM]], [[PrefillDecodeSplit]], [[RiscVVector]], [[ContextLength]], [[DataCenterAI], [EdgeAI]]

## Status
본 개념은 기존 [[AIInfrastructure]] 논의에서 AI 성능의 병목을 계산/대역폭/정밀도 세 축으로 분해하는 근거를 ISA 레벨에서 제공한다.