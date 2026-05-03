---
title: "HotWarmColdKVCache"
type: concept
tags:
  - KV cache
  - memory hierarchy
  - inference optimization
  - AI memory
sources:
  - 구글-turboquant-ai-메모리-6배-줄여도-된다-메모리-압축-기술의-진짜-의미-hot-warm-cold-kv-cache-의-차이-메모리-슈퍼사이클
last_updated: 2026-05-03
---

## Summary
[[HotWarmColdKVCache]]는 [[KVCache]]를 접근 빈도/활성도에 따라 구분해 처리하는 메모리 계층화 전략이다.

## Core Distinction
- **Hot**: 현재 추론 중 즉시 사용되는 KV를 대상으로 경량화/압축.
- **Cold**: 즉시 사용 빈도가 낮은 KV를 보관 최적화를 위해 다른 방식으로 압축.
- **Warm**: 전이 상태를 구성해 시스템 정책으로 다루는 중간 구간으로 이해할 수 있다.

## Example
- [[TurboQuant]]는 Hot 축의 압축을, [[KVTC]]는 Cold 축의 압축을 강조하는 대표 사례로 제시된다.

## Consequences
- 단기적으로는 메모리 사용량과 지연 감소.
- 장기적으로는 더 긴 문맥·더 많은 동시 세션 처리로 전체 수요를 확대시키는 기반.

## Related Concepts
- [[KVCacheCompression]], [[InferenceOptimization]], [[HBM]], [[LongContext]], [[AIInfrastructure]]
