---
title: "HC2022.Google.Pienaar.v1.pdf"
type: source
tags: [MLIR, Compiler, LLVM, TensorFlow, Dialect, Pass, Pattern, TableGen, OpenSource]
date: 2022-01-01
last_updated: 2026-05-10
source_file: raw/AI/LilysAI/hc2022.google.pienaar.v1.pdf.md
source_hash: 152be57931176806
---

## Summary
[[MLIR]](Multi-Level Intermediate Representation)은 다양한 추상화 수준의 표현을 하나의 통합 파이프라인에서 다룰 수 있도록 설계된 컴파일러 인프라이다. 기존의 [[LLVM]] 생태계(예: [[LLVM IR]])와 도메인 특화 IR이 가진 **확장성/재사용성 한계**를 해결하기 위해, 고수준 연산에서 저수준 코드 생성까지 점진적 저수준화를 지원한다.

이 문서는 기존 인프라의 비효율을 줄이고, 도메인 특화 컴파일러 재구축 비용을 획기적으로 낮추기 위한 목적에서 [[MLIR]]의 핵심 원칙(파시모니, 추적성, 점진성), 구성 요소, 패스/패턴 생태계, 커뮤니티 구조를 설명한다.

## Key Claims
- [[MLIR]]은 트리([[AST]])/그래프([[TensorFlow]], [[TFGraph]]/[[HLO]])/저수준 IR([[LLVM IR]])을 단일 철학 아래 다루는 다단계 IR이다.
- [[LLVM]]은 다재다능한 중간 레벨 IR이지만, 고수준/저수준 경계가 넓고 도메인 맞춤 IR을 별도로 만들어야 하는 비용이 크다.
- 많은 도메인 특화 컴파일러는 유사한 패스와 진단 기능을 **각자 재구현**하고 있어 중복 개발이 크며, [[MLIR]]은 이 재사용을 높이려는 전략이다.
- [[MLIR]]의 핵심 원칙은 [[Parsimony|파시모니]], [[Traceability|추적성]], [[Progressivity|점진성]]이며, 이는 **정보 보존과 점진적 저수준화**를 전제로 한다.
- 다이얼렉트([[Dialect]])는 공통 IR 위에서 독립적인 추상화 모듈을 정의하여, 동일 컨텍스트에서 다중 다이얼렉트 연산을 섞어 쓸 수 있다.
- 연산([[Operation]])은 사용자 정의가 기본이며, 고정 내장 개념을 최소화해 확장성을 높인다.
- 패스/변환은 [[TableGen]] 기반 선언적 패턴과 C++ 패턴, 하위 수준 바이트코드 계열의 PDL로 점차 확장되는 이중 구조를 가질 수 있다.
- [[Pass]]는 패턴 묶음 단위로 동작하며, 패스 드라이버([[mlir-opt]])를 통해 반복 테스트와 조합 실행이 가능하다.
- [[MLIR]] 커뮤니티는 [[mlir.dev/forum]], [[mlir.dev/chat]] 같은 채널로 머신러닝·HPC·하드웨어 쪽 반복 이슈를 공유하며 재사용형 IR 생태계를 지향한다.

## Key Quotes
> "MLIR은 다단계 중간 표현(Multi-Level Intermediate Representation)이다."

> "필요 없이 엔티티를 늘리지 말라(Parsimony)는 원칙은 복잡성을 억지로 키우지 않는 설계 기준이다."

> "정보를 파괴하는 것이 아니라 보존하는 것이 더 쉽다."

> "다이얼렉트 간의 저수준화가 쉽고, 서로 다른 다이얼렉트 연산을 동일한 IR 내에서 혼합할 수 있다."

> "패스 드라이버(opt-tool)는 프로젝트 수준에서 반복 실행되고 실험적으로 튜닝된다."

## Connections
- [[MLIR]] — 본 문서의 핵심 주제: 다단계 IR, 다이얼렉트, 패스/패턴, 커뮤니티.
- [[LLVM]] — 기존 기반 인프라의 장점과 한계를 함께 제시하는 기준점.
- [[TensorFlow]] — 초기 적용 배경 중 하나로 [[MLIR]]가 기원한 생태계의 기반.
- [[XLA]] — 도메인 특화 컴파일러의 전형적 사례로, 재사용성과 모듈화 관점에서 비교 가능.
- [[TFLite]] — 경량 추론 컴파일 스택 사례, [[MLIR]] 커뮤니티에서 다루는 도메인 예시 중 하나.
- [[ONNX-MLIR]] — 다중 추상화 연결성의 활용 사례 축.
- [[TableGen]] — [[Dialect]]와 [[Pass]] 스펙을 위한 핵심 선언적 정의 기법.
- [[Operation]], [[Dialect]], [[Pass]], [[Pattern]] — MLIR 구성의 4축.
- [[Clang]], [[Rust]], [[Julia]], [[Swift]], [[Fortran]] — 일반화 가능한 다단계 IR 설계 동기가 되는 기존 언어별 IR 구성 방식의 반면교사 예시.
- [[SSA]] — [[LLVM IR]] 및 컴파일러 분석에서 전제되는 핵심 형태론.

## Contradictions
- 기존 자료의 일부는 [[Domain-specific compiler|도메인 특화 컴파일러]]에서 고수준 최적화를 별도 IR로 해결한다고 보았지만, 본 소스는 이를 [[MLIR]]으로 **재사용 가능한 공통 인프라 축**으로 흡수하면 초기 비용을 줄일 수 있다고 본다. 이는 충돌이라기보다 설계 철학의 전환으로 정리한다.