---
title: "Interface"
type: concept
tags:
  - Compiler
sources: []
last_updated: 2026-05-10
---

## Summary
컴파일러에서 [[Interface]]는 특정 IR 노드가 수행해야 할 동작을 구현체가 표준 방식으로 제공하도록 강제하는 추상 규격이다.

## Key Points
- 다이얼렉트별 고정 로직을 인터페이스로 분리하면 중앙 스위치의 유지비를 줄일 수 있다.
- MLIR의 LLVM 변환 설계에서 인터페이스는 다이얼렉트 확장성과 하향( lowering ) 모듈성의 핵심이다.
- `translateOperation`, `amendOperation`, `convertParameter`는 인터페이스 기반 변환 계약의 구체 API로 제시된다.

## Connections
- [[MLIR]]
- [[Dialect]]
- [[LLVMTranslationDialectInterface]]
- [[LLVM IR]]
- [[OpenMP]]

## Implication
- 인터페이스 설계가 명확할수록 설계 결정의 문서화와 리팩터링의 비용이 낮아진다.