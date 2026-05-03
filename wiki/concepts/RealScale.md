---
title: "RealScale"
type: concept
tags:
  - Interconnect
  - C2C
  - LPU
  - RackScaleSystem
  - DeterministicExecution
sources:
  - nvidia-groq-3-lpx-everything-we-know-storagereview-com
last_updated: 2026-05-03
---

## Definition
[[RealScale]]는 LPX 전력/통신 경로에서 언급되는 chip-to-chip C2C 인터커넥트 패턴으로, 소프트웨어가 명시적으로 데이터 이동을 스케줄링하는 점대점 라우팅 계열이다.

## Claims from Source
- 헤더 기반 동적 중재보다 고정/예측 가능한 링크 이용이 가능하다는 설명이 반복되어 deterministic 실행에 유리하다고 제시됨.
- NVIDIA C2C와 다른 동작 모델로, cache-coherency 중심 스택이 아닌 점대점 스케줄링 중심 특성으로 구분됨.
- LPX 랙의 트레이 내/랙 간 통신 도메인에서 대역폭 밀도 설계의 핵심으로 등장.

## Relations
- [[C2C]] — RealScale의 기본 계열.
- [[DeterministicExecution]] — 예측 가능한 흐름 제어의 근거.
- [[LPXRack]] — RealScale 링크가 집약되는 확장 도메인.
- [[NVIDIADynamo]] — 상위 오케스트레이션에서 실질적으로 링크 사용 패턴을 제어.