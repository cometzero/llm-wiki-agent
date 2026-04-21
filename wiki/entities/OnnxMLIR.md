---
title: "ONNX-MLIR"
type: entity
tags: [compiler, onnx, mlir, inference]
sources: ["le-onnx-pdf"]
last_updated: 2026-04-20
---

## Summary
[[ONNX-MLIR]]은 [[ONNX]] 모델을 컴파일해 추론용 바이너리/라이브러리로 변환하는 오픈소스 프로젝트다. 상위 수준 모델 표현에서 저수준 코드 생성까지 [[MLIR]]/[[LLVM]] 기반 파이프라인을 제공해 하드웨어 이식성과 성능 최적화를 동시에 추구한다.

## Key Facts
- IBM Research를 중심으로 시작되어 현재 다수의 외부 기여자(AMD, ByteDance, Groq, Microsoft 등)가 참여하는 오픈소스 프로젝트다.
- 핵심 변환 경로는 `ONNX -> Krnl -> Affine/Std -> LLVM`이고, ONNX 연산자 버전 호환을 위한 재작성 규칙을 갖춘다.
- IBM Z 계열의 [[zAIU]] 경로를 포함해 x86, ARM, Power, IBM Z 등 멀티 아키텍처 배포를 지원한다.
- 성능 최적화 측면에서 버퍼링, 상수 메모리 처리, LLVM 호출 비용 절감이 주요 실행 엔지니어링 포인트다.

## Connections
- [[ONNX]], [[MLIR]], [[LLVM]], [[Krnl]], [[Affine]], [[zAIU]], [[IBM]], [[IBMZ]]
- 성능 주제: [[AIOptimization]], [[InferenceOptimization]], [[CompilerOptimization]]