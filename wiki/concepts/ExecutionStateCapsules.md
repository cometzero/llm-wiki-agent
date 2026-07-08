---
title: "Execution-State Capsules"
type: concept
tags: [physical-AI, state-management, KV-cache, on-device, checkpoint-restore]
sources: [embodied-cpp-2607-02501-references]
last_updated: 2026-07-08
---

## Overview
KV cache만 재사용하는 기존 LLM serving과 달리, recurrent state, convolution state, MTP(Multi-Token Prediction) state, metadata까지 포함한 complete restorable state를 graph-bound capsule로 저장/복원하는 기법. Robot policy와 physical AI serving처럼 branching, reset, interrupt가 잦은 on-device setting에서 sub-millisecond restore와 큰 TTFT(Time To First Token) speedup을 달성한다.

## Key Claims
- 기존 LLM serving의 KV cache 재사용 방식으로는 physical AI의 다양한 state 타입을 복원할 수 없음
- Complete restorable state: KV cache + recurrent state + convolution state + MTP state + metadata
- Graph-bound capsule: 실행 그래프에 바인딩된 state 캡슐화
- Use case: branching/reset/interrupt가 잦은 robot policy inference
- Performance: sub-millisecond restore, significant TTFT speedup

## Related Concepts
- [[KVCache]] — 기존 LLM serving 방식, incomplete for physical AI
- [[EmbodiedAI]] — 주요 적용 도메인
- [[OnDeviceInference]] — 타겟 deployment 환경
- [[CheckpointRestore]] — 복원 메커니즘 관련

## Connections
- [[Embodied.cpp]] — latency-first batch-1 physical-AI serving의 배경 연구
- [[vla.cpp]] — predecessor runtime과 대비
