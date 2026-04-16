---
title: "InferenceX v2: NVIDIA Blackwell Vs AMD vs Hopper"
type: source
tags: ["ai", "semiconductors", "inference"]
date: 2026-04-16
source_file: "raw/AI/SemiAnalysis/InferenceX v2_ NVIDIA Blackwell Vs AMD vs Hopper - Formerly InferenceMAX.md"
---

## Summary
최신 AI 추론 하드웨어와 시스템 구성을 비교한 SemiAnalysis 자료로, Blackwell, Hopper, AMD 계열 칩의 처리량과 비용 효율을 Prefill/Decode, 병렬화, 분산 추론 관점에서 분석한다. 단순 칩 스펙보다 워크로드 특성에 맞는 시스템 설계가 중요하다는 메시지가 강하다.

## Key Claims
- LLM 추론 성능 비교는 단순 FLOPS보다 prefill, decode, 메모리, 네트워크 구성이 더 중요하다.
- [[DisaggregatedPrefill]]과 [[InferenceOptimization]] 전략은 실제 서비스 비용 효율을 크게 바꾼다.
- Blackwell, Hopper, AMD의 경쟁은 칩 자체보다 시스템 아키텍처와 소프트웨어 최적화까지 포함해 봐야 한다.

## Key Quotes
> LLM 추론 시 고려해야 할 핵심 요소들을 명확히 제시하고, 어떤 칩과 기술 조합이 특정 워크로드에 가장 적합한지 구체적인 데이터를 통해 알려줍니다.

## Connections
- [[NVIDIA]] — Blackwell과 Hopper의 공급자
- [[AMD]] — 비교 대상 가속기 공급자
- [[InferenceOptimization]] — 추론 효율화의 상위 개념
- [[DisaggregatedPrefill]] — 문서가 반복적으로 강조하는 핵심 기법

## Contradictions
- No direct contradiction identified in this first ingest pass.
