---
title: "TableGen"
type: concept
tags: [MLIR, DeclarativeSpec, CompilerTooling]
last_updated: 2026-05-10
sources: [hc2022-google-pienaar-v1-pdf]
---

## 한 줄 요약
[[TableGen]]은 MLIR 연산/다이얼렉트/패스 정의를 선언적으로 기술하기 위한 스펙 생성 DSL/도구다.

## 장점
- 반복적인 C++ 수기 정의 대신 규격화된 기술 방식 제공.
- 연산 불변성, 파서/프린터/폴더/검증 등 정의를 일관되게 유지.

## MLIR 적용
- 본 소스는 TensorFlow, TFLite, MLIR 코어 연산의 다수가 ODS/유사 경로로 정의된다고 언급한다.

## 연결
- [[MLIR]], [[Dialect]], [[Pass]], [[Operation]]