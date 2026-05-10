---
title: "LLVMTranslationDialectInterface"
type: concept
tags:
  - Compiler
sources: []
last_updated: 2026-05-10
---

## Summary
[[LLVMTranslationDialectInterface]]는 다이얼렉트의 연산을 [[LLVM]] 하위 표현으로 번역하기 위한 규약형 인터페이스다.

## Key Operations
- `translateOperation`: 개별 연산 번역 수행.
- `amendOperation`: 다이얼렉트/타깃 특수 정보를 반영해 후처리 조정.
- `convertParameter`: 함수 파라미터 메타데이터 등 특수 규칙 전달.

## Connections
- [[MLIR]]
- [[LLVM IR]]
- [[Dialect]]
- [[OpenMP]]
- [[NVVM]]

## Importance
- 대규모 다이얼렉트 스위치 대신 모듈형 번역 책임 분산을 가능하게 하여 유지보수성과 확장성을 높인다.