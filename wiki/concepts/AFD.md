---
title: "AFD (Attention FFN Disaggregation)"
type: concept
tags: [inference-architecture, llm, optimization]
last_updated: 2026-04-21
sources:
  - gtc-2026-the-inference-kingdom-expands
---

## Definition
[[AFD]]는 LLM 추론을 [[Prefill]](컨텍스트 입력 처리)와 [[Decode]](토큰 생성 반복)로 나눈 뒤, 처리 성격이 다른 연산 블록을 서로 다른 하드웨어로 분리 배치하는 구조를 뜻한다.

## Core Mechanism
- [[Attention]]은 동적 상태(KV cache) 의존성이 강하고 GPU에 적합.
- FFN은 입력 토큰 종속 계산(상태 비의존) 특성이 강해 [[LPU]]의 결정론적/저지연 처리와 결합하기 유리.
- 디스패치/컴바인 단계의 토큰 라우팅(All-to-All 기반 병렬 처리)가 성능의 핵심 병목으로 작동할 수 있어 핑퐁 파이프라이닝이 요구됨.

## Source Insights
- 본 소스는 디코드 단계 토큰 처리량 증가, MoE 희소화로 인한 토큰 분산 문제 완화, 대역폭 효율 개선을 AFD의 직접 효과로 제시한다.
- GPU의 KV 캐시 병목을 완화하고 LPU의 FFN 처리와 결합해 시스템 전체 토큰 흐름을 늘리는 설계가 목적이다.

## Related Concepts
- [[LPU]], [[GPU]], [[MoE]], [[KVCache]], [[Speculative Decoding]], [[InferenceOptimization]]

## Contradictions
- No explicit contradiction with current wiki; this source adds an implementation-level decomposition detail to prior high-level GPU/LPU comparison frameworks.