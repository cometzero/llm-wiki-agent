---
title: "NPUISA"
type: concept
tags:
  - ISA
  - NPU
  - CSR
  - MMIO
  - ABI
  - Barrier
sources:
  - npu-v0-1-isa-spec
last_updated: 2026-05-03
---

## Definition
**NPU ISA**는 [[NPUv01]]과 같은 NPU tile의 커널-가시 명령 체계/제어 인터페이스를 통합한 규격 개념이다. 본 문맥에서 v0.1은 [[RV64]]/[[RVV]] 확장 위에 커스텀 [[XNPUV01]]를 추가하고, matrix 연산·동기화·이벤트·DMA 완료 대기를 프로그래머에게 일관된 의미로 노출한다.

## v0.1 Highlights
- custom opcode space 사용(encoding은 provisional)
- matrix 클래스 고정(`nmmaz`/`nmma`)
- 8-slot barrier/event 모델의 software synchronization
- CSR 목록(`mnpuinfo`, `mspmcfg`, `mbar*`, `mevtwait`, `mdmawait`, `mperfcnt*`) 제공
- DMA는 opcode가 아닌 [[MMIO]]-programmed helper 모델
- v0.1 kernel ABI: `a0`~`a4` register contract

## Why it matters
이 설계는 아키텍처 수준의 유연성과 도구 체인 호환성을 동시에 노리는 방식으로, architected matrix RF 없이 vector 레지스터 그룹을 재사용해 하드웨어 비용을 줄이면서도 compiler 관점에서 tile tensorization을 강제한다.

## Related
- [[NPUv01]]
- [[XNPUV01]]
- [[TileBasedNPU]]
- [[SharedScratchpadMemory]]
- [[IREE]]
- [[MLIR]]
- [[DMA]]
- [[MMIO]]
- [[Kernel]] ABI
