---
title: "Dialect"
type: concept
tags:
  - Compiler
sources: []
last_updated: 2026-05-10
---

## Summary
[[Dialect]]는 컴파일러 IR에서 특정 도메인/타깃/프로그래밍 모델 전용 연산과 타입 집합을 표현하는 추상 레이어다.

## Key Points
- [[MLIR]]에서 다이얼렉트는 연산 시맨틱스와 하드웨어/API 특성을 지역화한다.
- 초기 LLVM 호환성 전략에서는 LLVM 다이얼렉트가 핵심 중간 계층이었다.
- GPU/가속기/OpenMP 확장 시 `translateOperation` 기반 다이얼렉트 하향 전략으로 폭넓은 구현이 가능해졌다.
- 다이얼렉트 수 증가가 번역 비용과 학습 곡선을 높일 수 있다.

## Connections
- [[MLIR]]
- [[LLVM IR]]
- [[LLVMTranslationDialectInterface]]
- [[NVVM]]
- [[ROCDL]]
- [[OpenMP]]

## Design Guidance from Source
- 다이얼렉트 추가는 “새 기능을 위한 추가”가 아니라 “실제 유틸리티/이식성/공통 최적화 이득”의 정당성으로 판단해야 한다.