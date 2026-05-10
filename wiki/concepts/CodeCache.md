---
title: "Code Cache"
type: concept
tags:
  - Runtime
  - TCG
  - 캐시
sources:
  - qemu-에뮬레이터-내부-구조-tcg-메모리-디바이스-모델링-및-디버깅
last_updated: 2026-05-10
---

## 정의

코드 캐시는 번역된 실행 블록(TB)을 저장해 두는 메모리 공간이다.

## 동작

- 동일 코드가 반복 실행될 때 재번역 비용 감소.
- 캐시가 가득 차면 제거/재배치 정책(LRU 등)으로 갱신.

## 효과

- 번역 비용과 실행 지연 모두 감소.
- 특히 분기 빈번한 워크로드에서 체감 성능 향상.

## 연결

- [[TCG]]
- [[TranslationBlock]]
- [[Chaining]]
- [[QEMU]]