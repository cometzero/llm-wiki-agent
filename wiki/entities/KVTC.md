---
title: "KVTC"
type: entity
tags:
  - NVIDIA
  - KV cache
  - compression
  - inference
  - memory hierarchy
last_updated: 2026-05-03
sources:
  - 구글-turboquant-ai-메모리-6배-줄여도-된다-메모리-압축-기술의-진짜-의미-hot-warm-cold-kv-cache-의-차이-메모리-슈퍼사이클
---

## 개요

[[KVTC]](KV Cache Transformed Coding)는 [[NVIDIA]]가 제시한 KV 캐시 압축 접근으로, 주로 즉시 사용이 줄어든 [[KVCache]](콜드 KV) 영역을 압축해 저장/복구 효율을 높이는 구조다.

## 핵심 포인트

- 모델 웨이트 변경 없이 KV 상태 압축을 시도한다.
- 장면 전체가 아니라 비활성 구간을 타깃으로 해도 전체 메모리 사용량을 줄일 수 있다.
- PCA 기반 축약, 적응형 양자화, 엔트로피 코딩을 조합한 압축 구조를 갖는 것으로 설명된다.
- 본소스에서는 [[Google]]의 [[TurboQuant]]와 비교되어, "콜드 중심" vs "핫 중심" 압축 포지션으로 구분된다.

## 연결

- [[HotWarmColdKVCache]]
- [[KVCacheCompression]]
- [[NVIDIA]]
- [[InferenceOptimization]]
- [[AIInfrastructure]]
- [[HBM]]