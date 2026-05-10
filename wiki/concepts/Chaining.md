---
title: "TCG Chaining"
type: concept
tags:
  - TCG
  - 최적화
  - TB
sources:
  - qemu-에뮬레이터-내부-구조-tcg-메모리-디바이스-모델링-및-디버깅
last_updated: 2026-05-10
---

## 정의

[[Chaining]]은 연속된 [[TranslationBlock]]들이 예외/분기 없이 연결되어 실행될 수 있도록 하는 최적화 기법이다.

## 목적

- TB 사이 prologue/epilogue 호출 횟수 감소.
- 예외 처리 외부 경로를 제외하고 연속 실행 효율 개선.

## QEMU 맥락

- TB가 캐시 적중 시, 기존 chain 가능성 존재.
- 예외 발생 시 정상 경로를 벗어나 제어가 CPU 인터프리터/핸들러로 이동.

## 연결

- [[TCG]]
- [[TranslationBlock]]
- [[CodeCache]]
- [[QEMU]]