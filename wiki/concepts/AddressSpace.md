---
title: "Address Space"
type: concept
tags:
  - 메모리
  - 가상화
  - 주소 변환
sources:
  - qemu-에뮬레이터-내부-구조-tcg-메모리-디바이스-모델링-및-디버깅
last_updated: 2026-05-10
---

## 정의

Address Space는 동일 주소 공간 안의 여러 [[MemoryRegion]]을 묶어 가상 주소 접근을 모델링하는 추상화다.

## 동작

- root MemoryRegion를 통해 시작.
- 하위 Region 계층을 통해 게스트 주소 번역과 장치/메모리 분할.

## QEMU 맥락

- SoftMMU 경로에서 주소 변환의 핵심 컨테이너.
- 각 주소 공간의 root는 GPA→메모리 노드 매핑의 시작점.

## 연결

- [[SoftMMU]]
- [[MemoryRegion]]
- [[RAMBlock]]
- [[HostMemoryBackend]]
- [[QEMU]]