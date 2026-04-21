---
title: "AI Model Compilation"
type: concept
tags: [ai, inference, compiler, optimization]
sources: ["le-onnx-pdf"]
last_updated: 2026-04-20
---

## Definition
AI 모델 컴파일은 학습된 모델 형식(예: [[ONNX]])을 특정 하드웨어/운영체제 환경에서 효율적으로 실행 가능한 산출물로 변환하는 최적화 전 과정을 말한다.

## Pipeline (source-specific)
- 표준 모델 표현 수용
- 다이얼렉트 변환 (연산/형상 정규화)
- 메모리 및 루프 최적화
- 저수준 코드 생성 및 바이너리 생성
- 런타임 최적화(컴파일 타임과 실행 성능 균형)

## Representative stack
- 모델 형식: [[ONNX]]
- 컴파일 프레임워크: [[MLIR]]
- 코드 생성: [[LLVM]]
- 가속기 경로: [[zAIU]], [[zDNN]]

## Key tradeoffs
- 최신 연산 규격 지원성과 과거 모델 호환성 사이 균형
- 메모리 소비(상수 처리/버퍼링)와 컴파일 지연(LLVM 단계 시간) 사이 균형
- 하드웨어 가변성 대응을 위한 다중 하향 경로 구성