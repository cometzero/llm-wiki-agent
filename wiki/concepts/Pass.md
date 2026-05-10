---
title: "Pass"
type: concept
tags: [Compiler, Optimization, Transformation]
last_updated: 2026-05-10
sources: [hc2022-google-pienaar-v1-pdf]
---

## 한 줄 요약
컴파일러 IR 변환을 수행하는 하나의 논리적 단계 집합을 [[Pass]]라고 하며, 성능·크기·정확성 조건을 충족하도록 연속 실행된다.

## 주요 요소
- 동작 대상 타입 (어떤 IR 연산에 적용되는지)
- 설명과 옵션
- 통계/튜닝 지표
- 반복 실행 가능한 테스트 루프

## MLIR 실무
- [[Pass]]는 종종 여러 [[Pattern]]를 묶어 구성된다.
- [[mlir-opt]] 같은 드라이버로 프로젝트별로 조합해 실행할 수 있다.
- 실험을 반복해 최적 경로를 수렴하는 방식이 권장됨.

## 연결
- [[Pattern]], [[PassBase.td]], [[MLIR]], [[Dialect]], [[Compiler]]