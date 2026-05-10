---
title: "동적 바이너리 변환 (Dynamic Binary Translation)"
type: concept
tags:
  - Virtualization
  - Runtime
  - Emulation
sources:
  - qemu-에뮬레이터-내부-구조-tcg-메모리-디바이스-모델링-및-디버깅
last_updated: 2026-05-10
---

## 정의

동적 바이너리 변환은 실행 중 게스트 아키텍처 코드를 타깃 아키텍처 실행 코드로 변환하는 기법이다.

## 적용 장점

- 하드웨어가 아닌 소프트웨어 경로로 타깃이 다른 CPU 간 실행 가능.
- 번역 캐시를 통한 반복 실행 최적화.
- 하드웨어 가상화가 불가하거나 비지원 경로에서 실질적 대체 수단.

## QEMU에서의 형태

[[QEMU]]에서는 [[TCG]]가 핵심 엔진으로, 번역 블록 단위(`TB`) 변환/캐싱/체이닝한다.

## 연결 항목

- [[TCG]]
- [[TranslationBlock]]
- [[CodeCache]]
- [[KVM]]