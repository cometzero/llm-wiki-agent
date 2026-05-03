---
title: "Doorbell Launch"
type: concept
tags:
  - execution model
  - control plane
  - accelerator
sources:
  - npu-v0-1-hw-architecture
last_updated: 2026-05-03
---

## 정의
Doorbell launch는 host가 장치/타일에게 실행 시작 이벤트를 쓰기(signal)로 알리는 시작 방식이다. queue 기반 스케줄러 없이 MMIO/레지스터 기반으로 실행을 트리거한다.

## v0.1 적용
- no global command processor
- host가 ELF upload/launch/complete/fault 흐름을 직접 관리
- tile 내부 harts가 DMA, compute, barrier 동작을 오케스트레이션

## 장점
- 제어 평면 단순화
- 초기 bring-up/디버깅에서 의도 전달이 명시적
- queue depth/dispatch reordering 문제를 축소

## 연관 링크
- [[NPUv01]], [[TileBasedNPU]], [[DMA]], [[BarrierSynchronization]], [[MMIO]]
