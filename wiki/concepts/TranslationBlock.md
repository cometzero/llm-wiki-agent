---
title: "Translation Block"
type: concept
tags:
  - TCG
  - Performance
  - Emulator
sources:
  - qemu-에뮬레이터-내부-구조-tcg-메모리-디바이스-모델링-및-디버깅
last_updated: 2026-05-10
---

## 정의

Translation Block(TB)은 게스트 실행 경로를 작은 단위로 나눈 번역 결과 블록이다.

## 역할

- 자주 실행되는 코드 조각을 캐시한다.
- 캐시 히트 시 재번역 없이 빠르게 재실행.

## 성능 특성

- TB 경계 내에서의 연속 실행은 분기/예외 처리 시점 재진입 비용을 줄인다.
- 반복 실행이 많은 workload에서 번역 오버헤드를 낮춘다.

## 연결

- [[CodeCache]]
- [[TCG]]
- [[Chaining]]
- [[QEMU]]