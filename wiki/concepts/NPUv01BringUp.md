---
title: "NPU v0.1 Bring-Up"
type: concept
tags:
  - Bring-Up
  - NPU
  - Verification
  - Regression
  - MMIO
  - PMU
sources:
  - npu-v0-1-implementation-design
last_updated: 2026-05-03
---

## 정의
[[NPUv01]] v0.1 bring-up은 구현이 검증되지 않은 상태에서 성능 최적화나 추가 기능 확장을 금지하고, 단계별로 동작을 고정해 통합한다. 핵심은 각 단계에서 `회귀가 green`인지와 observability를 갖춘 상태를 보장하는 것이다.

## 규칙
- P1 이전에는 opcode encoding freeze를 진행하지 않는다.
- 성능 측정은 `P3` 이후 시작하되 `PMU`/trace 수집은 `P1`부터 반영한다.
- RVV-only 경로를 golden anchor로 유지해 IME path의 수치 정합을 계속 교차 검증한다.
- fault injection, timeout, DMA/address error, barrier misuse 등을 통해 내구성을 검증한다.

## 결과 산출물
- RVV-only 회귀 pass
- IME-enabled matmul/MLP/QKV 또는 동등 난도 커널 pass
- embedded ELF load/launch 데모
- 기본 profiling report(PMU/trace)
- 문서 패키지 패턴: PRD/ISA/HW/SW/Implementation 동기화
