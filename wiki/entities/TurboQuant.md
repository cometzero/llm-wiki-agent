---
title: "TurboQuant"
type: entity
tags:
  - Google
  - LLM
  - inference
  - memory
  - kv-cache
  - compression
last_updated: 2026-05-03
sources:
  - 구글-turboquant-ai-메모리-6배-줄여도-된다-메모리-압축-기술의-진짜-의미-hot-warm-cold-kv-cache-의-차이-메모리-슈퍼사이클
---

## 개요

[[TurboQuant]]는 [[Google]]가 제시한 [[LLM]] 추론 최적화 기술로, 추론 중 사용 중인 [[KVCache]](특히 핫 KV)를 축소해 [[HBM]]/메모리 부담을 낮추고 처리 속도를 높이는 것을 목표로 한다.

## 핵심 개념

- 현재 활성 상태인 KV를 그대로 줄이는 핫 경로 압축 전략을 사용한다.
- 압축 시 [[Attention]]에서 토큰 간 관계(코릴레이션/내적 유사도)를 가능한 유지하려고 설계한다.
- [[Google]] 설명에서 FP16 대비 최대 6배 압축과 HBM 기준 최대 8배 속도 향상을 주장한다.
- [[PolarQuant]]를 포함한 다단계 압축을 통해 대규모 비트 축소와 품질 안정화의 균형을 맞춘다.

## 위치 맥락

[[TurboQuant]]은 [[NVIDIA]]의 [[KVTC]]와 비교될 때, 압축 대상이 "현재 사용 중인 핫 KV"라는 점에서 구분된다. 두 기술은 각각 핫/콜드 구분에 따라 상호 보완적으로 쓰일 수 있다.

## 연결

- [[KVCache]]
- [[KVCacheCompression]]
- [[HotWarmColdKVCache]]
- [[InferenceOptimization]]
- [[Google]]
- [[NVIDIA]]
- [[KVTC]]
- [[PolarQuant]]