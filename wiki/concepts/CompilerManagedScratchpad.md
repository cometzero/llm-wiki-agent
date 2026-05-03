---
title: "Compiler Managed Scratchpad"
type: concept
tags:
  - Memory
  - Compiler
  - NPU
  - Banking
  - Scheduling
sources:
  - npu-v0-1-prd
  - npu-v0-1-hw-architecture
last_updated: 2026-05-03
---

## Definition
[[CompilerManagedScratchpad]]은 scratchpad를 cache처럼 투명하게 다루지 않고, 컴파일러가 [[SharedScratchpadMemory]] 배치와 bank coloring, activation/weight/output/temp 구획을 명시적으로 계획해 운용하는 방식이다.

## In v0.1 NPU context
`NPUv01` v0.1에서는 `2 MB shared scratchpad`와 `16 banks`를 기준으로 하며, 운영 모델은 아래를 강조한다.
- 연산자별 operand/result 배치의 deterministic 스케줄링
- bank conflict 완화를 위한 bank coloring
- intermediate DDR spill 최소화(`PG-04`)
- on-chip execution 우선(가능한 경우 external memory 접근 회피)

## Relation
- [[NPUv01]] baseline architecture에서 핵심 자원 계약.
- [[IME]]/[[RVV]] kernel의 성능 일관성 확보에 직접 기여.
- [[IREE]]/[[MLIR]] backend pass design에서 SPM planner 역할과 연결.
