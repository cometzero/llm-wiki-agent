---
title: "VectorBatchProduct"
type: concept
tags: [risc-v, vector-extensions, ai-isa]
last_updated: 2026-04-21
sources:
  - understanding-the-risc-v-extensions-for-ai-john-simpson-sifive
---

## Definition
[[VectorBatchProduct]]는 기존 [[RiscVVector]]를 기반으로 추가 상태를 거의 요구하지 않으면서 행렬 곱셈을 소프트웨어 래핑으로 처리하는 RISC-V AI 확장 접근이다.

## Characteristics
- **New state**: 최소화(거의 없음)
- Dot-product 기반의 다중 계산(예: 8중 병렬 결과) 패턴
- GEM/GEV 등 일반 행렬·벡터 곱에서 활용 가능
- [[FP8]], [[FP16]], [[FP32]] 연산 경로 지원이 명시되는 설계 그룹
- 빠른 트랙 채택성이 높아 초기 상용성 기대치가 높음

## Tradeoffs
- 하드웨어 오버헤드는 낮으나, 매우 큰 행렬 곱셈은 소프트웨어 루프에 의존
- 대역폭이 제한된 소규모 연산·엣지 디바이스 구간에서 유리

## Relations
- [[RiscVExtensionsForAI]]의 4개 축 중 하나
- [[RiscVVector]]와 [[EdgeAI]]에 자연스럽게 결합

## Notes
본 개념은 단순성이 큰 장점이므로 빠른 적응성이 필요할 때 우선 검토 대상이 된다.