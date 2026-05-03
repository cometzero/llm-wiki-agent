---
title: "Embedded ELF"
type: concept
tags:
  - Compiler
  - Runtime
  - MLIR
  - IREE
  - NPU
  - EdgeAI
sources:
  - npu-v0-1-sw-architecture
last_updated: 2026-05-03
---

## Summary
[[EmbeddedELF]]는 v0.1 단계에서 [[IREE]]/[[MLIR]] AOT 파이프라인을 통해 생성되는 실행 가능한 펌웨어 형식으로, host runtime이 로드·파라미터 채움·실행 completion을 수행하는 단위를 말한다.

[[NPUv01]] context에서 [[EmbeddedELF]]는 kernel variant와 specialization 정보를 담고, `nputile` [[HAL]] driver의 `remote_elf_loader`를 통해 device memory로 적재된다.

## Relationship to NPU v0.1
- [[NPU v0.1 Software Architecture]]는 embedded ELF 경로를 단일 tile baseline에서 정합성 높은 실행 단위로 고정한다.
- compile-time specialization (`vlen_bits`, `spm_bytes`, `hart_count`, `ime_tile_class`)은 같은 모델에 대해 서로 다른 ELF variant를 허용한다.
- 개발 초기에는 system-linked artifact 노출을 통해 asm/IR inspection을 허용하고, 회귀 안정화 후 embedded 기본값으로 전환한다.

## Key Terms
- **Kernel params**: host→device 전달용 메타데이터와 포인터 집합.
- **Metadata variant**: 특성별 specialization constant 기반 실행별 분기.
- **Loader**: [[MMIO]] 또는 플랫폼 저장 경로를 통해 기기로 적재.
