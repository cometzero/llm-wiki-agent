---
title: "SoftMMU"
type: concept
tags:
  - 메모리
  - 가상화
  - 주소 변환
  - QEMU
sources:
  - qemu-에뮬레이터-내부-구조-tcg-메모리-디바이스-모델링-및-디버깅
last_updated: 2026-05-10
---

## 정의

SoftMMU는 QEMU에서 게스트의 메모리 접근을 소프트웨어적으로 처리하는 메모리 가상화 계층이다.

## 동작

- 게스트 물리주소를 [[AddressSpace]]/[[MemoryRegion]]/[[RAMBlock]] 경로로 추적.
- 최종적으로 호스트 가상주소(HVA), 커널 경로에서는 물리주소(HPA) 변환.

## 적용

- DIMM/DIMM 장치 에뮬레이션, RAM/ROM/DMA/MMIO 분기 처리에 핵심.
- 가상 디바이스 I/O가 실제 커널 콜백과 연결되는 경로의 기반.

## 연결

- [[AddressSpace]]
- [[MemoryRegion]]
- [[RAMBlock]]
- [[HostMemoryBackend]]
- [[QEMU]]