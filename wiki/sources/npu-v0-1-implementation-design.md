---
title: "NPU v0.1 Implementation Design"
type: source
tags:
  - NPU
  - RTL
  - Compiler
  - Runtime
  - DV
  - Bring-Up
  - Verification
  - NPUv01
  - IME
  - SharedScratchpadMemory
  - DMA
  - MMIO
  - IREE
  - HAL
  - PMU
date: 2026-04-19
source_file: raw/NPU/v0.1/NPU_v0.1_Implementation_Design.md
sources:
  - npu-v0-1-implementation-design
last_updated: 2026-05-03
---

## Summary
본 문서는 [[NPUv01]] v0.1을 대상으로 [[RTL]], [[Compiler]], [[Runtime]], [[DV]], 통합 테스트의 구현 범위와 분해, 그리고 단계적 [[BringUp]]·안정화 계획을 정의한다. 설계의 우선순위는 기능 시연보다 재현 가능한 baseline 확립에 두고, single-tile 기반으로 **작게 시작해 명확히 연결**한다는 원칙을 따른다.

v0.1은 [[RV64]]/[[RVV]] + [[IME]]-style matrix path, 공유 [[SharedScratchpadMemory]], 3-channel [[DMA]], no command queue 전제로 설계되며, SW는 [[IREE]] + [[MLIR]] 기반 AOT [[Kernel]]/ELF 파이프라인에 맞춘 plugin과 외부 HAL driver를 제공한다. 구현은 단계적으로 `RVV-only`를 먼저 안정화하고, 이후 [[IME]] tensorization과 성능 관측을 추가하는 방식으로 진행한다.

## Key Claims
- [[NPUv01]] v0.1의 구현 기준은 single-tile RTL baseline으로, 2-hart tile, shared SPM(2MB/16 banks), 3-channel [[DMA]], barrier/event 체계를 고정하고 향후 다중 확장을 지연한다.
- 구현 범위는 SW/SR 인터페이스 명세가 먼저고, [[command queue]]는 배제한 즉시 실행(doorbell + immediate launch) 모델을 따른다.
- repository ownership은 RTL(`rtl/`), DV(`dv/`), compiler plugin(`compiler/plugins/riscv_ime/`), runtime(`runtime/nputile/`), tests(`tests/`)로 분리하여 산출물 책임을 명확화한다.
- 개발 단계는 P0~P4로 고정한다: 모델링, RVV-only bring-up, IME enable, end-to-end 통합, hardening(PG-01~06)이며 각 단계는 회귀 green 상태에서만 다음 단계로 진행한다.
- RTL 구현은 parameterization보다 먼저 reference 동작을 고정한다. 하드웨어/소프트웨어 파이프라인은 고정된 채널 수·bank 수·hart 수를 가진 기준 구현을 먼저 맞춘다.
- 인터페이스 freeze 우선순위는 `Launch MMIO`, `DMA MMIO`, `CSR`, `SPM local address`, `IME intrinsic API`, `Kernel param block`으로, opcode encoding freeze보다 선행한다.
- 성능 최적화는 P3 이후만 수행하고, P1부터 PMU/trace 기반 관측 지표 수집을 포함한다.
- open issue(예: opcode encoding, interrupt detail, SPM protection, multi-tile partitioning)는 baseline 동작을 위협하지 않는 범위에서 분리 관리한다.

## Key Quotes
> "v0.1 구현은 기능 시연보다 baseline 고정과 재현 가능한 bring-up에 우선순위를 둔다." — 구현 범위 원칙

> "RTL baseline은 parameterization보다 명확한 reference implementation을 우선한다. 즉 bank 수, hart 수, VLEN, DMA 채널 수를 우선 고정하고 이후 공통화/parameterization을 수행." — 구현 철학

> "각 phase는 regression green 상태에서만 다음 단계로 진행한다." — 단계진행 가드

## Connections
- [[NPUv01]] — 본 문서의 구현 대상 프로젝트 전체를 규정한다.
- [[NPU v0.1 ISA Specification]] — 본 문서의 구현 규격이 계층적으로 정합되도록 ISA 동작 의미를 상위에서 정의한다.
- [[NPU v0.1 Hardware Architecture]] — 제어 평면 및 tile/matrix/메모리 계층의 하드웨어 가정을 실현하기 위한 SW/HW 분해 계획을 제공한다.
- [[IREE]] / [[MLIR]] — plugin 등록, pass pipeline, AOT ELF 배포 경로의 핵심 도구 체인이다.
- [[Runtime]] / [[HAL]] / [[MMIO]] — 런타임의 즉시 실행, remote ELF load, MMIO 접근 구조를 연결한다.
- [[DV]] / [[Verification]] / [[PMU]] — 회귀, fault injection, trace, profiling을 통해 v0.1 sign-off를 보증한다.
- [[BringUp]] — P0~P4 단계별 통합 전략으로 구현 일정의 중심 축을 제공한다.

## Contradictions
- 기존 [[NPU v0.1 ISA Specification]] 및 [[NPU v0.1 Hardware Architecture]]와 충돌하지 않으며, 오히려 ISA/아키텍처를 실행 가능한 구현 산출물 기준으로 구체화한다.
