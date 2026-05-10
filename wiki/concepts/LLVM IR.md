---
title: "LLVM IR"
type: concept
tags:
  - Compiler
sources: []
last_updated: 2026-05-10
---

## Summary
[[LLVM IR]]은 [[LLVM]] 생태계의 중간 표현으로, 최적화/타깃 코드 생성 파이프라인과 맞닿아 있는 정적 정형 IR이다.

## Key Points
- [[MLIR]] 다이얼렉트가 LLVM 스타일로 표현될 때 번역 경로가 단순해진다.
- 초기 MLIR-Lowering은 함수 서명, 전역 심볼, 블록 연산을 비교적 직접적으로 매핑하는 방식이었다.
- 현재는 타깃 다층성 확대에 따라 dialect-specific 변환 규칙이 인터페이스를 통해 조립된다.
- 특정 값 표현, 메타데이터, 파라미터 속성 처리에서 상위 IR의 결정이 최종 LLVM IR 출력에 영향.

## Connections
- [[MLIR]]
- [[LLVM]]
- [[Dialect]]
- [[LLVMTranslationDialectInterface]]

## Note
- 소스 관찰상, 초기 설계의 장점은 단순성과 변환 비용이었고, 현재의 과제는 확장성·복잡도 관리로 이동했다.