---
title: "KVTC"
type: concept
tags:
  - AI inference
  - KV cache
  - memory compression
  - Nvidia
sources:
  - 구글-turboquant-ai-메모리-6배-줄여도-된다-메모리-압축-기술의-진짜-의미-hot-warm-cold-kv-cache-의-차이-메모리-슈퍼사이클
last_updated: 2026-05-03
---

## Summary
[[KVTC]](KV Cache Transformed Coding)은 [[NVIDIA]]가 제시한 [[KVCache]] 압축 기법으로, 사용 중인 데이터가 아닌 비활성 구간(콜드 상태) KV를 압축해 저장하고 재활용한다.

## Key Idea
- 모델 웨이트를 바꾸지 않으면서 메모리 사용량을 낮추는 것이 핵심.
- 접근 패턴이 적은 구간을 압축 대상화해 재활성 시 복원 비용을 수용한다.

## Techniques
- PCA 유사한 차원 축소 아이디어 기반 변환.
- 적응형 양자화(adaptive quantization).
- 엔트로피 코딩(예: 허프만류) 기반의 희소성·빈도 기반 부호화.

## Relations
- [[HotWarmColdKVCache]]에서 콜드 구간 처리에 해당하며, [[TurboQuant]]의 핫 구간 압축과 보완적이다.
- [[InferenceOptimization]] 및 추론 서비스 비용 구조 개선 논의에서 중요한 비교 대상이다.
