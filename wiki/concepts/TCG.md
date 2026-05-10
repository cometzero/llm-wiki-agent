---
title: "TCG"
type: concept
tags:
  - Virtualization
  - DynamicBinaryTranslation
  - Emulator
sources:
  - qemu-에뮬레이터-내부-구조-tcg-메모리-디바이스-모델링-및-디버깅
last_updated: 2026-05-10
---

## 정의

Tiny Code Generator([[TCG]])는 [[QEMU]]에서 게스트 명령어를 호스트 실행 가능한 코드로 변환하는 핵심 JIT/번역 계층이다.

## 동작 방식

- 게스트 코드 → `변환 블록(Translation Block, TB)` 분할
- 게스트를 [[TCG]] 중간 표현/마이크로 연산으로 변환
- 호스트 타깃 ISA 명령으로 코드 생성
- 번역 결과를 `코드 캐시`에 보관

## 핵심 개념

- 프런트엔드/백엔드 분리
- Virtual registers
- Helper functions
- Prologue/Epilogue
- Chaining

## 소스 연결

- [[qemu-에뮬레이터-내부-구조-tcg-메모리-디바이스-모델링-및-디버깅]]은 TCG의 변환 흐름, 캐시, 스택 처리, 체이닝, 디코딩을 실무 관점으로 정리한다.

## 연결 항목

- [[DynamicBinaryTranslation]]
- [[TranslationBlock]]
- [[CodeCache]]
- [[Chaining]]
- [[QEMU]]
- [[KVM]]