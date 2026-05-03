---
title: "KVCacheCompression"
type: concept
tags:
  - KV cache
  - memory compression
  - inference
  - transformers
sources:
  - 구글-turboquant-ai-메모리-6배-줄여도-된다-메모리-압축-기술의-진짜-의미-hot-warm-cold-kv-cache-의-차이-메모리-슈퍼사이클
last_updated: 2026-05-03
---

## Summary
[[KVCacheCompression]]은 [[LLM]] [[Attention]] 기반 추론에서 캐시 상태 메모리를 줄이기 위한 다양한 압축·변환 기법군을 말한다.

## Typical Methods
- 핫/콜드 분리 기반의 이질적 처리 전략.
- 양자화/저차원 변환/엔트로피 코딩 결합.
- 압축 이후에도 [[Attention]] 정합성을 유지하려는 보정 또는 보존 설계.

## Why It Matters
메모리 병목은 단순 연산량만큼이나 중요하다. 특히 긴 문맥 대화 및 에이전트형 작업에서 [[KVCache]] 크기는 [[HBM]] 사용량, 동시 처리량, 지연시간과 강하게 연동된다.

## Related Concepts
- [[TurboQuant]], [[KVTC]], [[HotWarmColdKVCache]], [[PolarQuant]], [[InferenceOptimization]]
