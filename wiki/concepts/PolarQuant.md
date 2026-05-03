---
title: "PolarQuant"
type: concept
tags:
  - quantization
  - KV cache
  - geometric representation
  - inference optimization
sources:
  - 구글-turboquant-ai-메모리-6배-줄여도-된다-메모리-압축-기술의-진짜-의미-hot-warm-cold-kv-cache-의-차이-메모리-슈퍼사이클
last_updated: 2026-05-03
---

## Summary
[[PolarQuant]]는 벡터를 반경(radius)과 각도(angle) 성분으로 분해해 표현 효율을 높이는 압축 기법이다.

## In Context
본 소스에서는 [[TurboQuant]]의 1차 압축 단계로 제시되며, 큰 구조 정보를 유지하면서 적은 비트로 핵심 값을 보존하는 방식으로 설명된다.

## Effect
- 대형 오차를 큰 폭으로 줄임
- 압축 후 [[Attention]] 연산의 영향도를 줄이기 위해 후단 미세 보정 단계가 결합됨

## Relations
- [[TurboQuant]], [[KVCacheCompression]], [[Attention]], [[InferenceOptimization]]
