---
title: "2025 EuroLLVM - Deep Dive into the MLIR to LLVM IR Translation Mechanism"
type: source
tags:
  - MLIR
  - LLVM
  - LLVM IR
  - Compiler
  - Dialect
  - OpenMP
  - NVVM
  - ROCDL
date: 2025-01-01
last_updated: 2026-05-10
source_file: raw/Technology/LilysAI/2025-eurollvm-deep-dive-into-the-mlir-to-llvm-ir-translation-mechanism.md
source_hash: 6cd26b443e9f21d7
---

## Summary
이 소스는 [[MLIR]]에서 [[LLVM]]로의 변환 메커니즘이 어떻게 진화했는지, 그리고 초기 설계 결정이 현재까지 유지되는 구조적 잔재를 정리한다. 핵심은 초기에는 LLVM 호환을 극대화한 단순 매핑 중심 변환에서 시작했지만, [[GPU]], 가속기, OpenMP 같은 다양한 타깃을 받치기 위해 [[Dialect]]와 [[Interface]] 기반의 확장형 변환 구조로 바뀌었다는 점이다.

## Key Claims
- [[MLIR]]은 [[LLVM]]의 정신적 후계자로, 고정 연산 중심의 IR이 아니라 다이얼렉트, 지역성(`regions`), 사용자 정의 타입/연산/속성을 갖는 다중 레벨 표현을 제공한다.
- 초기 MLIR은 실행이 없어 번역 기능만 있었고, [[TensorFlow]] 통합 수요로 LLVM 연결이 필요해지며 LLVM 백엔드와 연결되었다.
- [[LLVM]] 다이얼렉트는 [[MLIR]]의 다른 연산과 [[LLVM IR]] 사이의 중간 계층으로 설계되어 초기 변환을 단순화했다.
- 초기 변환은 함수 서명, 전역 변수, 블록 연산을 직관적으로 매핑하는 비교적 짧은 코드(약 200줄)였으나, [[Phi nodes]]/제어흐름/멀티스레딩/타깃 다양성 확장에서는 한계를 드러냈다.
- 현재는 GPU/가속기([[Nvidia]], [[AMD]]) 및 OpenMP를 지원하기 위해 [[LLVMTranslationDialectInterface]], `translateOperation`, `amendOperation`, `convertParameter` 같은 인터페이스 기반 훅을 확장해 다이얼렉트별 번역 책임을 분산한다.
- 다이얼렉트가 늘수록 성능과 인지적 복잡도 증가(컴파일러 컴파일/변환 비용 증가, 이해 비용 증가)로 인해, 새 다이얼렉트 추가는 더 이상 “무조건 추가”가 아니라 **유용성 기반 심사**가 필요하다.
- 소스는 현재의 많은 역사적 설계 결정이 합리적이었던 반면 지금은 문맥이 사라져 이해가 어렵고, 설계 근거 문서화가 부족해 변경/정리 비용이 높아졌다고 본다.
- [[OpenMP]] 번역은 모듈 변환 객체·스택 기반 처리로 기존 빌더 의존성과 아웃라인/런타임 규칙을 맞춰 통합한다.
- [[Opaque pointers]] 같은 설계 변경은 기존 IR의 변화가 가능함을 보여주며, 적절한 문서화와 마이그레이션 전략이면 기존 인프라를 새 패러다임으로 이행할 수 있다.

## Key Quotes
> "MLIR은 LLVM을 최대한 반영하고, LLVM IR로의 변환을 단순하게 유지하고자 했다."

> "오래된 설계 결정이 현재까지 영향을 미치고 있다."

> "다이얼렉트 추가의 비용은 컴파일 시간과 인지적 비용에서 크며, 유용성을 기준으로 신중히 판단해야 한다."

## Connections
- [[MLIR]] — 본 소스의 중심 프레임워크.
- [[LLVM]] — 타깃 백엔드와 통합되는 상위 컴파일러 인프라.
- [[LLVM IR]] — 최종 목표 IR.
- [[Dialect]] — MLIR 다층성의 핵심 단위.
- [[LLVMTranslationDialectInterface]] — 다이얼렉트별 LLVM 변환을 통합하는 핵심 인터페이스.
- [[TensorFlow]] — 초기 역사에서 MLIR 통합 동기를 제공한 프로젝트.
- [[OpenMP]] — 멀티스레딩/아웃라인링 요구로 LLVM 변환 파이프라인이 확장된 주요 사용 사례.
- [[NVVM]] — Nvidia GPU 내장 ISA/빌딩에 대응한 다이얼렉트 계열.
- [[ROCDL]] — AMD GPU 대응 다이얼렉트 계열.
- [[Opaque pointers]] — LLVM 설계 진화와 마이그레이션 전략 논의의 사례.

## Contradictions
- 기존 [[MLIR]] 관련 소스들(예: `HC2022.Google.Pienaar.v1.pdf`)은 컴파일러의 점진적 재사용성과 확장성 원리를 강조한다. 본 소스는 이를 부정하지 않지만, 특히 초기 설계 산물이 남긴 문맥 상실로 인해 현재 설계가 과도하게 관습 의존적으로 굳어졌다는 점을 더 강하게 비판해 추가 보강(문서화/정당성 증빙) 필요성을 제기한다.