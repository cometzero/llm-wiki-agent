---
title: "ONNX-MLIR"
type: concept
tags: [compilation, ai, inference, onnx, llvm, mlir]
sources: ["le-onnx-pdf"]
last_updated: 2026-04-20
---

## Definition
[[ONNX-MLIR]]은 [[ONNX]] 모델을 하드웨어 친화적 추론 바이너리로 변환하는 컴파일러 파이프라인 개념이다.

## Core mechanism
- ONNX 다이얼렉트로 모델 연산을 표현하고, [[Krnl]] 기반 고급 반복/루프 및 변환 계층으로 내린다.
- 이후 [[Affine]]/[[Std]]에서 스케줄 및 루프/메모리 정규화가 수행되고, 최종적으로 [[LLVM]]로 내려가 실행 산출물이 생성된다.
- 다이얼렉트는 IBM Z, GPU/CPU, 가속기 연계 확장을 위해 여러 하위 경로(TOSA, [[StableHLO]])로 이어질 수 있다.

## Key concerns
- 연산자 버전 처리(예: Squeeze 버전 정규화)
- 인덱스/형상 계산의 정적/동적 처리
- 메모리·버퍼 최적화와 컴파일 시간 최적화
- 가속기 특화 다이얼렉트(zHigh/zLow)와 데이터 레이아웃 인코딩

## Connections
- [[ONNX]], [[MLIR]], [[LLVM]], [[INFERENCEOPTIMIZATION]], [[zAIU]], [[IBMZ]], [[zDNN]]