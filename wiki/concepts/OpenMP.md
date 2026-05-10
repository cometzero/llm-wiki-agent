---
title: "OpenMP"
type: concept
tags:
  - Compiler
  - Parallelism
sources: []
last_updated: 2026-05-10
---

## Summary
[[OpenMP]]는 병렬 구문/런타임 모델로, MLIR에서 LLVM로 번역할 때는 아웃라인링, 런타임 호출, 스택/영역 정합이 핵심 이슈가 된다.

## Key Points
- MLIR-LLVM 변환 파이프라인은 OpenMP 지원을 위해 모듈 변환 객체와 스택 기반 접근을 도입했다.
- 기존 OpenMP 프런트엔드/IR 빌더 코드를 재사용하면서 LLVM 백엔드로 내려오는 방식으로 통합 비용을 낮췄다.
- 복합 영역 구조를 가진 nested 구조 모델이 MLIR의 중첩 영역(`region`)과 잘 맞는다.

## Connections
- [[MLIR]]
- [[LLVM]]
- [[LLVM IR]]
- [[LLVMTranslationDialectInterface]]
- [[Dialect]]

## Notes
- 소스는 OpenMP을 다이얼렉트 확장의 성공 사례로 다루되, 추가 다이얼렉트 확장 전에는 공통 정합 전략이 필요함을 강조한다.