---
title: "TFLite"
type: entity
tags: [AI, EdgeInference, Compiler, Runtime]
last_updated: 2026-05-10
sources: [hc2022-google-pienaar-v1-pdf]
---

## 개요
[[TFLite]]는 경량 추론 대상 실행 환경용 TensorFlow 계열 도구로, 도메인/플랫폼 제약에 맞춘 컴파일링크 최적화가 요구되는 경우가 많다.

## MLIR과의 연결
- 본 소스의 사례 맥락에서 [[TFLite]]는 도메인 특화 컴파일러 계열의 예로 등장하며, 각 계층별 추상화 재정의 비용이 문제될 수 있음을 보여주는 지표 중 하나다.
- 공통 패스/다이얼렉트 전략이 정착되면 [[MLIR]] 기반으로 동일 인프라 안에서 여러 추론 경로를 관리하기 쉬워질 수 있다.

## 관련 링크
- [[MLIR]]
- [[TensorFlow]]
- [[Dialect]]
- [[Pass]]