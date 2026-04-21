---
title: "ONNX-MLIR 기반 추론 컴파일 파이프라인"
type: source
tags: [ai, compiler, inference, llvm, onnx, mlir, ibm]
date: 2026-04-20
source_file: raw/Technology/LilysAI/le-onnx.pdf.md
last_updated: 2026-04-20
---

## Summary
본 문서는 [[ONNX-MLIR]]이 [[ONNX]] 모델을 [[MLIR]]와 [[LLVM]] 기반 파이프라인으로 변환해 추론용 바이너리/라이브러리로 최적화하는 오픈소스 컴파일러 프로젝트임을 설명한다. 모델은 ONNX 다이얼렉트에서 [[Krnl]]를 거쳐 [[Affine]]/[[Std]]를 통과한 뒤 LLVM 다이얼렉트로 내려와 실행 가능한 산출물로 만들어진다. 또한 IBM의 [[IBM]] 메인프레임용 가속기 [[zAIU]] 및 [[zDNN]], 그리고 다른 하향 경로(TOSA, [[StableHLO]])를 지원해 하드웨어 적응력을 높인다. 마지막으로 버퍼 재사용, 대규모 상수 메모리 처리, LLVM 호출 경량화로 컴파일 성능/메모리 사용량을 줄이는 방법을 제시한다.

## Key Claims
- [[ONNX-MLIR]]은 [[ONNX]] 모델을 MLIR로 변환한 뒤 LLVM 최적화와 코드 생성 파이프라인을 통해 하드웨어에서 바로 실행 가능한 바이너리로 만드는 오픈소스 컴파일러 프로젝트다.
- 코어 파이프라인은 `ONNX 다이얼렉트 -> Krnl -> Affine/Std -> LLVM`의 단계적 변환이며, 핵심 명령은 각각 `--convert-onnx-to-krnl`, `--convert-krnl-to-affine`, `--convert-all-to-llvm`이다.
- ONNX 버전 호환성은 최신 연산자 버전 중심으로 처리되며, 과거 버전은 재작성 규칙으로 최근 버전으로 정규화되어 변환된다.
- 메모리 버퍼 최적화, 상수 메모리 처리, LLVM 도구 단계의 상수 외부화 튜닝을 통해 컴파일 효율과 실행 효율을 개선한다.
- [[IBM]] [[zAIU]](특히 [[IBM]] [[Telum]] 기반) 경로를 지원하고, 이에 맞춘 고수준 [[zHigh]] 및 저수준 [[zLow]] 다이얼렉트 경로와 [[zTensor]] 표현을 둔다.
- 단일 입력형 `ONNX`뿐 아니라 다양한 연산자 타입 확장(예: uint8/int8 계열)과 멀티 아키텍처( x86, ARM, IBM Power, IBM Z )를 고려한다.

## Key Quotes
> "ONNX-MLIR은 ONNX AI 모델을 최적화된 바이너리로 컴파일한다." — source

> "LLVM 다이얼렉트에서 실행 가능한 바이너리/라이브러리를 생성한다." — source

> "ONNX 다이얼렉트는 ONNX 명세로부터 자동 생성되며, Python 스크립트로 연산자 정의가 만들어진다." — source

> "MLIR에 새로운 버퍼링 기능이 도입되면서 ONNX-MLIR도 이를 사용하도록 업데이트되었다." — source

## Connections
- [[ONNX]] — 입력 모델 포맷으로 사용되며 다이얼렉트 변환의 기준점이다.
- [[MLIR]] — 상위에서 하위 컴파일러 변환을 구조화하는 핵심 IR 프레임워크다.
- [[LLVM]] — 저수준 최적화와 코드 생성의 표준 엔진으로 사용된다.
- [[ONNX-MLIR]] — 본 문서의 중심 프로젝트이다.
- [[IBM]] — 프로젝트 기원, 기여 생태계, 그리고 zAIU 연계의 배경 주체이다.
- [[zAIU]] — IBM Z 머신 온칩 AI 가속기 최적화 경로를 지원한다.
- [[zDNN]] — zAIU 연동 API 계층으로 사용된다.
- [[Telum]] — IBM zAIU 탑재 시스템 맥락에서 언급되는 하드웨어 플랫폼이다.
- [[IBMZ]] — 하드웨어 지원 대상 맥락에서 주요 환경이다.
- [[Krnl]], [[Affine]], [[StableHLO]], [[TOSA]] — 다이얼렉트/변환 단계의 핵심 구성 요소다.
- [[AIOptimization]] — 버퍼링, 상수 처리, 컴파일 시간 개선이 다루는 성능 최적화 범주이다.

## Contradictions
- No explicit contradiction with existing wiki pages was identified during this ingest pass.