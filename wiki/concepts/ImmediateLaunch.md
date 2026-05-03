---
title: "Immediate Launch"
type: concept
tags:
  - Runtime
  - HAL
  - MMIO
  - NPU
  - ExecutionModel
sources:
  - npu-v0-1-sw-architecture
last_updated: 2026-05-03
---

## Summary
[[ImmediateLaunch]]는 command queue 없이 host가 직접 [[MMIO]]/[[DoorbellLaunch]] 트리거로 커널 실행을 시작하는 방식이다. [[NPUv01]] v0.1에서 이 방식은 실행 경로를 단순화하고 deterministic 동작을 확보하는 핵심 수단으로 채택된다.

runtime은 command buffer를 단지 내부 표현으로 기록한 뒤 launch 시점에 즉시 실행형 dispatch로 변환한다. 따라서 scheduling은 kernel runtime의 동적 큐잉 로직이 아니라 compile-time contract와 host-triggered control plane에 의해 결정된다.

## Key Characteristics
- **Host-driven control plane**: launch 신호는 host에서 doorbell/MMIO 기반으로 시작.
- **No global queue**: v0.1 기준, 제품 스펙과 정합되는 queue-less 모델.
- **Low software complexity**: runtime의 역할을 launch/완료 수집, 파라미터 설정, fault/trace 수집으로 축소.
- **Predictability**: 통제 가능한 실행 경로 덕분에 회귀/관측을 빠르게 닫을 수 있음.

## Connections
- [[NPU v0.1 Software Architecture]]
- [[NPUv01]]
- [[HAL]]
- [[Runtime]]
- [[PMU]]
- [[Trace]]
