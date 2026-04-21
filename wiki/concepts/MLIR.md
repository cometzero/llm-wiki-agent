---
title: "MLIR"
type: concept
tags: [compiler, infra, ai, transformation]
sources: ["le-onnx-pdf"]
last_updated: 2026-04-20
---

## Definition
[[MLIR]]은 다단계 컴파일러 인프라로, 고수준 연산 표현을 하위 수준 연산과 코드 생성 단계로 점진적으로 변환하는 데 쓰이는 언어/프레임워크이다.

## In this corpus
이 문서에서는 [[ONNX-MLIR]]의 핵심 기초 레이어로 사용되어 [[ONNX]] 모델을 하드웨어별로 실행 가능한 형태로 변환한다.

## Key points
- 연산자/형상/타입 정보를 단계적으로 정규화하고 최적화한다.
- 다이얼렉트 간 변환(ONNX, [[Krnl]], [[Affine]], [[LLVM]])의 중간 표현을 제공한다.
- 버퍼링, 상수 처리, 인덱스/형상 추론 문제 해결에 사용되는 유연성을 제공한다.

## Connections
- [[ONNX-MLIR]], [[LLVM]], [[Krnl]], [[ONNX]], [[AICompilation]]