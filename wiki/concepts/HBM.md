---
title: "HBM"
type: concept
tags:
  - memory
  - hardware
  - AI infrastructure
  - inference
sources:
  - 구글-turboquant-ai-메모리-6배-줄여도-된다-메모리-압축-기술의-진짜-의미-hot-warm-cold-kv-cache-의-차이-메모리-슈퍼사이클
last_updated: 2026-05-03
---

## Summary
[[HBM]]은 AI 추론에서 고대역폭이 요구되는 [[KVCache]]·모델 중간 상태 처리에 중요한 메모리 계층이다.

## Role in LLM Inference
[[HBM]] 병목은 긴 문맥 처리, 동시 세션 확장, 대규모 추론에서 비용과 지연에 직접 영향을 준다. 따라서 메모리 압축 기법인 [[TurboQuant]], [[KVTC]], [[KVCacheCompression]]의 효과를 판단할 때 기준 자원으로 작동한다.

## Relations
- [[KVCache]], [[KVCacheCompression]], [[InferenceOptimization]], [[AIInfrastructure]], [[MemorySupercycle]]
