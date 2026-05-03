---
title: "NPU v0.1 Implementation Plan"
type: concept
tags:
  - NPU
  - Implementation
  - Bring-Up
  - RTL
  - Compiler
  - Runtime
  - Verification
sources:
  - npu-v0-1-implementation-design
last_updated: 2026-05-03
---

## 정의
[[NPUv01]] v0.1 Implementation Plan은 single-tile 기준 HW/SW baseline을 먼저 고정하고, 단계적 통합을 통해 엔드투엔드 기능을 검증하는 실행 계획이다. 이 방식은 초기 성능 극대화보다 재현성·결정론적 실행·회귀 안정성을 우선한다.

## 핵심 구성
- **고정 baseline**: 2-hart tile, [[RV64]], [[RVV]], shared [[SharedScratchpadMemory]], [[DMA]] 3채널, barrier/event, PMU.
- **레포 분리**: [[RTL]], [[DV]], compiler plugin, [[Runtime]]/HAL driver, tests를 별도 소유 경계로 나눈다.
- **채택 패턴**: global command queue 대신 immediate launch + MMIO 기반 제어.
- **개발 우선순위**: generic RVV path 우선 동작 확인 후 IME tensorization과 최적화 경로를 추가.

## 단계 (P0~P4)
- P0: MMIO/Scratchpad/DMA/barrier reference model 정합.
- P1: RVV-only 커널 회귀 통과 (LN/softmax/depthwise).
- P2: IME 파이프 연동 및 intrinsic emission.
- P3: IREE backend + HAL + RTL/emulator 통합 데모.
- P4: fault/PMU/trace/perf smoke hardening.

## 의미
[[NPUv01]]의 실행 규격(ISA/아키텍처)과 실제 구현·검증 체계가 정합되는 핵심 연결 고리다. [[BringUp]]/회귀 게이트/관측성은 성능 최적화 이전 조건이다.