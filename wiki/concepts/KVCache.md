---
title: "KV Cache"
type: concept
tags: [ai-ml, attention, inference, optimization]
sources: [2026-05-24-day30-ai-ml-learning-review]
last_updated: 2026-05-24
---

## Definition

[[KVCache]]는 Transformer가 이전 token의 key/value 계산 결과를 저장해 다음 token 생성에 재사용하는 캐시이다. Attention 계산의 중복을 방지하여 LLM 서빙을 더 빠르고 효율적으로 만든다.

## Key Concepts

### Why KV Cache Matters
LLM은 답변을 한 토큰씩 생성한다. 각 단계에서 이전 모든 token과의 attention을 다시 계산하면 매우 비효율적이다. [[KVCache]]는 이미 계산한 key/value를 저장하여 재사용한다.

### Example
"나는 오늘 학교에 갔다" 생성 시:
1. "나는" 예측
2. "나는 오늘" 예측 → KV cache로 "나는" 계산 재사용
3. "나는 오늘 학교에" 예측 → KV cache로 "나는", "오늘" 계산 재사용

### Impact
- 긴 대화, 긴 문서 요약, agent workflow에서 효과 큼
- GPU 메모리 관리 중요 (긴 문맥 = 큰 cache)
- LLM 서빙의 핵심 최적화 기술 중 하나

## Common Misconception
[[KVCache]]는 모델의 "기억력"이 아니다. 대화 내용을 이해해 장기 기억으로 저장하는 것이 아니라, 같은 생성 과정에서 이전 token의 attention 계산을 재사용하는 실행 최적화이다.

## Connections
- [[Serving]] — LLM 서빙 핵심 최적화
- [[InferenceOptimization]] — 속도/효율성 향상
- [[Throughput]] — 처리량 향상 가능

## Practical Notes

[[KVCache]]를 잘 쓰지 않으면 이미 계산한 attention 정보를 계속 다시 계산하게 되어 매우 비효율적이다. 긴 문서를 다루는 RAG 시스템에서 특히 중요하다.
