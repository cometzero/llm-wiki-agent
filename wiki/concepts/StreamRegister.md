---
title: "Stream Register"
type: concept
tags:
  - Interconnect
  - DataMovement
  - LPU
  - DeterministicExecution
sources:
  - nvidia-groq-3-lpx-everything-we-know-storagereview-com
last_updated: 2026-05-03
---

## Definition
Stream register는 LPU 내 기능 단위 간 순차 이동 경로의 개념으로, 동/서로 정렬된 단일 홉 이동 패턴을 통해 연산 유닛 간 데이터의 정확한 시간적 정렬을 돕는 것으로 설명된다.

## Role
- 고정 크기 버퍼/벡터 데이터가 규칙적으로 이동해 컴파일러가 지연을 정량 예측.
- 런타임 의존 스케줄링보다 컴파일 타임 결정론 설계를 강화.

## Relations
- [[1DInterconnect]] — stream register가 동작하는 인터커넥트 환경.
- [[DeterministicExecution]] — 이동 경로의 고정성과 예측성.
- [[FFN]] — 반복 디코드 유닛 이동의 타이밍 정합.