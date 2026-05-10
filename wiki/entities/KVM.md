---
title: "KVM"
type: entity
tags:
  - 가상화
  - Linux
  - 가속기
  - 하이퍼바이저
sources:
  - qemu-에뮬레이터-내부-구조-tcg-메모리-디바이스-모델링-및-디버깅
last_updated: 2026-05-10
---

## 정체성

[[KVM]](Kernel-based Virtual Machine)은 리눅스 커널 기반 하이퍼바이저 가속 기술이다. [[QEMU]]에서 게스트와 호스트 아키텍처가 같은 경우, [[TCG]]보다 빠른 직접 실행 경로로 동작한다.

## 핵심 기능

- 하드웨어 가상화 지원 시 실행 경로 가속.
- 사용자 공간 QEMU 프로세스를 보완해 전체 가상화 성능 향상.
- 가속기(accelerator) 계층으로 `-enable-kvm` 등의 옵션으로 활성화.

## 최신 소스 연결

- [[qemu-에뮬레이터-내부-구조-tcg-메모리-디바이스-모델링-및-디버깅]]에서 [[QEMU]] 동작 모드(동일 아키텍처 KVM 경로 vs TCG 변환 경로)를 구분.

## 연계 개념

- [[QEMU]]
- [[QOM]]
- [[Virtualization]]