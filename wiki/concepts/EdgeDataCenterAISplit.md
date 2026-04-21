---
title: "EdgeDataCenterAISplit"
type: concept
tags: [ai-workloads, deployment, risc-v]
last_updated: 2026-04-21
sources:
  - understanding-the-risc-v-extensions-for-ai-john-simpson-sifive
---

## Definition
[[EdgeDataCenterAISplit]]은 AI ISA/하드웨어 선택 시 단일 기법이 아니라 배치 특성, 워크로드 단계(prefill/decode), 전력·대역폭 제약을 기준으로 엣지와 데이터센터를 분기해 설계하는 방법론이다.

## Rules
- 엣지: 작은 상태 변경, 빠른 채택, 소규모 연산 효율을 우선
- 데이터센터: 대형 행렬 성능 및 고대역처리 우선
- prefill는 상대적으로 대규모 행렬 처리 최적화, decode는 배치 1 효율을 고려한 보완 필요

## Connections
- [[RiscVExtensionsForAI]], [[VectorBatchProduct]], [[IntegratedMatrixExtensions]], [[VectorMatrixExtensions]], [[AttachedMatrixExtensions]], [[LLM]], [[PrefillDecodeSplit]], [[RiscVVector]]

## Notes
이 개념은 본 소스의 주요 설계 결론을 실행 지침으로 정리한 것으로, 성능 튜닝 시 하드웨어-모델 동시 설계 전략의 출발점이 된다.