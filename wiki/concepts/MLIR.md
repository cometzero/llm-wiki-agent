---
title: "MLIR"
type: concept
tags:
  - Compiler
sources: []
last_updated: 2026-05-10
---

## Summary
[[MLIR]]은 다중 수준(IR) 컴파일러 중간표현으로, 연산(`ops`), 타입, 속성, [[Dialect]], [[Region]]을 통해 다양한 하드웨어와 프로그래밍 모델을 공통 구조로 다룬다.

## Key Points
- LLVM의 정적 단일 할당(IR) 개념을 확장해 더 높은 수준의 추상화를 제공한다.
- 다이얼렉트 간 번역/하향(`lowering`)이 핵심; 특히 [[LLVM]] 쪽으로의 변환은 [[LLVM IR]]로 이어진다.
- 변환 비용은 `translateOperation`, `amendOperation`, [[Interface]] 기반 확장 훅으로 관리된다.
- 사용자 정의 타입/연산 지원으로 도메인 특화 컴파일러를 빠르게 구성할 수 있다.
- 설계 이력(초기 단순성 vs 현재 복잡성)이 유지비 부담으로 연결되는 구간이 존재한다.

## Connections
- [[LLVM]]
- [[LLVM IR]]
- [[Dialect]]
- [[LLVMTranslationDialectInterface]]
- [[OpenMP]]
- [[NVVM]]
- [[ROCDL]]
- [[TensorFlow]]

## Design Notes
- 본 소스는 MLIR의 초기 단순 번역 설계가 이후 GPU/가속기/프로그래밍 모델 확장 과정에서 [[Dialect]]와 [[Interface]] 중심으로 재구성되었음을 명시한다.
- 장기적으로 새 다이얼렉트 추가는 성능 이득보다 유지비, 이해 비용, 테스트 복잡도를 함께 고려해야 한다.