---
title: "NPU v0.1 PRD"
type: source
tags:
  - NPU
  - PRD
  - Architecture
  - Hardware
  - Compiler
  - Runtime
  - EdgeAI
  - RV64
  - RVV
  - IME
  - IREE
  - MLIR
  - SharedScratchpadMemory
  - DMA
  - MMIO
  - HAL
  - Observability

date: 2026-04-19
source_file: raw/NPU/v0.1/NPU_v0.1_PRD.md
sources:
  - npu-v0-1-prd
last_updated: 2026-05-03
---

## Summary
본 문서는 [[NPUv01]] v0.1의 제품 요구사항을 정의하며, global command queue 없이 host 즉시 실행을 중심으로 하는 edge inference baseline를 고정한다. 핵심 가정은 single-tile 기준을 먼저 안정화하고, 이를 기반으로 [[1 2 4 tile SKU]]가 가능한 [[TileBasedNPU]]를 만들되 인터페이스와 실행 계약은 변경하지 않는 것이다. 컴파일러는 [[IREE]]/[[MLIR]] 기반 AOT ELF 경로를 채택하고, HW는 [[RV64GC]] + [[RVV]] + [[IME]] 스타일 행렬 파이프라인 중심으로 설계한다.

## Key Claims
- [[NPUv01]] v0.1은 v0.2와 달리 **global command queue를 배제**하고, host MMIO/doorbell 기반 즉시 실행(`immediate launch`) 모델을 채택한다.
- baseline은 [[RV64GC]]/[[RVV256]]/[[IME]]와 **2 harts/tile**, **2 MB shared SPM(16 banks)**, **3-channel DMA**를 고정값으로 둔다.
- 주요 기능은 [[Kernel]]을 op 단위가 아닌 **fused kernel ELF**로 실행하는 것이며, 이때 [[IREE]]/[[MLIR]] compiler output을 직접 사용한다.
- 성능 목표보다 우선 순위가 높은 것은 `deterministic` 동작, scratchpad 스케줄링 predictability, 통합 디버깅/관측성 확보이다.
- P0~P4와 유사한 검증 게이트를 통해 v0.1 scope 내에서 단계적으로 안정성(`PG-01 ~ PG-06`)을 확보하도록 요구한다.
- v0.1 비목표로 preemption, virtual memory, sparse, compression, cache-coherent multi-tile fabric를 명시적으로 제외해 범위를 고정한다.
- FR에서 `INT8/FP16/BF16/FP32 accumulation`, `matmul/QKV/MLP/LN/softmax/DWConv/PWConv` 연산 커버리지를 포함해 edge 추론 핵심 연산군을 제약 조건화한다.
- v0.1에서 opcode encoding은 provisional이며, 핵심 변경 리스크를 줄이기 위해 multi-tile 정책/보안 hardening 등은 v0.2로 미룬다.

## Key Quotes
> "v0.1의 차별점은 (1) global command queue 제거, (2) architected matrix register file 제거, (3) compiler-managed scratchpad, (4) RVV generic path + late IME tensorization." — 제품 개요

> "v0.1은 기능적 baseline을 고정하고, compiler-visible contract와 HW/SW 인터페이스를 안정화하는 데 초점을 둔다." — 제품 목표와 비목표

## Connections
- [[NPUv01]] — 본 문서의 제품군/구조 대상 프로젝트.
- [[NPU v0.1 ISA Specification]] — ISA 계약을 구현하고 실행 모델을 소프트웨어 계약으로 정합하는 상위 규격 문서.
- [[NPU v0.1 Hardware Architecture]] — 단일 tile baseline의 아키텍처 전제를 공유한다.
- [[NPU v0.1 Implementation Design]] — 본 PRD의 성공 기준을 실행 단계(P0~P4)로 구체화한 구현 문서.
- [[IREE]] / [[MLIR]] — AOT fused kernel 파이프라인 기반 컴파일러 stack.
- [[HAL]] / [[MMIO]] — host launch/remote loader/interrupt-free polling 경로의 핵심 실행 인터페이스.
- [[SharedScratchpadMemory]] / [[DMA]] / [[IME]] / [[RVV]] / [[RVV256]] — 타일 연산 모델의 실행 자원.
- [[PMU]], [[trace]], [[fault report]] — 실행 관측성(성능/오류) 요구사항.
- [[DeterministicExecution]] / [[BarrierSynchronization]] — v0.1에서 요구되는 예측성 및 경로 재현성 기반.

## Contradictions
- 기존 [[NPUv01]] 문서군과 충돌하지 않는다. 본 문서는 동일 baseline을 제품화 관점에서 확정하고, opcode encoding/보안 하드닝/멀티테넌시 확장을 v0.2로 이관해 안정성 우선순위를 강화한다는 점이 기존 구현·아키텍처 문서의 방향성과 일치한다.
