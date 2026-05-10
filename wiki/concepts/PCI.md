---
title: "PCI"
type: concept
tags:
  - 디바이스 모델링
  - 버스
  - 임베디드
  - QEMU
sources:
  - qemu-에뮬레이터-내부-구조-tcg-메모리-디바이스-모델링-및-디버깅
last_updated: 2026-05-10
---

## 정의

PCI(Peripheral Component Interconnect)는 범용 장치 연결 버스 계열 규격으로, QEMU 장치 모델링에서 중요한 시스템 인터페이스이다.

## QEMU에서의 활용

- `TypeInfo` 기반 장치 타입 등록.
- BAR 등록 및 콜백(`mmio_read/mmio_write/io_read/io_write`)을 통한 I/O 동작 시뮬레이션.
- 게스트에서 `resource`/`config` 접근으로 검증.

## 연결

- [[PCIDevice]]
- [[QEMU]]
- [[MemoryRegion]]
- [[Linux]]
- [[DeviceModeling]]