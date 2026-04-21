---
title: "VectorMatrixExtensions"
type: concept
tags: [risc-v, matrix-extensions, data-center]
last_updated: 2026-04-21
sources:
  - understanding-the-risc-v-extensions-for-ai-john-simpson-sifive
---

## Definition
[[VectorMatrixExtensions]](VME)는 [[RiscV]]에 새로운 상태를 추가해, 벡터 입력과 분리된 결과/어큐뮬레이터 경로를 통해 대형 행렬 연산 처리 성능을 높이는 설계군이다.

## Characteristics
- 새로운 상태 추가가 핵심
- 기본적으로 outer-product 기반 연산 구조
- 소프트웨어 루프 조합으로 큰 행렬 계산 구현
- 고정밀도/고연산 밀도 구간에서 높은 처리량 잠재력
- Fat-K류 설계(데이터 타입 변경으로 연산량 증가)로 대역 효율성 개선 가능

## Fit to Workloads
- [[LLM]] prefill 같은 대규모 배치 계산 구간에 적합
- 배치 크기가 1인 decode 구간에서는 효율 저하 가능성 존재

## Risks / Limits
- 하드웨어 규모와 배치 크기 정합이 맞지 않으면 유효성 저하
- 단일 경로 병렬성만으로는 decode 단계에서 효율이 떨어질 수 있음

## Cross-links
- [[RiscVExtensionsForAI]], [[PrefillDecodeSplit]], [[LLM]], [[AttachedMatrixExtensions]]

## Notes
VME는 데이터센터 단계에서 성능 레버리지를 제공하나, 추론 단계별 매칭이 중요하다.