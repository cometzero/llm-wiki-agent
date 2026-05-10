---
title: "Linux Kernel"
type: entity
tags:
  - 운영체제
  - 커널
  - 가상화
  - 디버깅
sources:
  - qemu-에뮬레이터-내부-구조-tcg-메모리-디바이스-모델링-및-디버깅
last_updated: 2026-05-10
---

## 정체성

[[LinuxKernel]](실제 표기: [[Linux Kernel]])는 리눅스 커널 전체를 가리키며, QEMU 게스트 환경에서 부트/드라이버/디바이스 연동 실험의 핵심 대상이다.

## 이번 소스와의 연결

- QEMU에서 `bzImage` 빌드 및 `-kernel` 인자로 실행.
- [[KVM]] 경로 및 non-KVM 경로에서 게스트 부팅 비교가 가능.
- 커널 디버깅 단계에서는 `-s -S`, `-no-kaslr`, `vmlinux` 심볼을 활용한 GDB remote 디버깅이 핵심이다.

## 연계 개념

- [[QEMU]]
- [[KVM]]
- [[GDB]]
- [[Debugging]]