---
title: "KV Cache"
type: concept
tags: [ai-ml, transformer, optimization]
sources: [2026-05-23-day30-ai-ml-learning-review, 2026-05-22-day30-ai-ml-learning-review]
last_updated: 2026-05-23
---

## Definition
KV Cache는 Transformer attention에서 이전 token들의 key/value 중간값을 저장해 다음 token 생성에 재사용하는 메모리 기법이다.

## Why It Matters
LLM이 token을 하나씩 생성할 때, 이전 token들의 key와 value를 매번 다시 계산하면 낭비가 크다. KV cache는 앞부분의 attention 관련 중간값을 저장해 두어 다음 계산을 빠르게 한다.

## Example
"나는 밥을" 다음에 token을 생성한다고 하자:
1. "먹었다"를 만든 뒤
2. 다시 "나는 밥을 먹었다" 전체를 처음부터 계산하면 느림
3. KV cache는 "나는 밥을"의 attention 관련 중간값을 저장
4. 다음 token 생성 시 저장된 값을 재사용하여 계산 효율화

## Trade-offs
- **장점**: 반복 계산 제거로 속도 향상, latency 감소
- **단점**: 메모리 사용량 증가 (cache 크기가 sequence length에 비례)

## Key Insight
KV cache는 모델을 더 똑똑하게 만드는 것이 아니라, 같은 계산을 더 효율적으로 하게 만드는 기술이다. 품질을 직접 올리는 것이 아니라 속도와 비용에 영향을 준다.

## Connections
- [[InferenceOptimization]] — attention 계산 최적화
- [[Serving]] — 서빙 시 사용되는 기법
- [[Latency]] — cache로 latency 감소
- [[Throughput]] — 효율화로 throughput 향상
