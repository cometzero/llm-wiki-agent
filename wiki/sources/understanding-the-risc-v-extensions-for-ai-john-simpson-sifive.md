---
title: "Understanding the RISC-V Extensions for AI - John Simpson, SiFive"
type: source
tags:
  - riscv
  - ai-hardware
  - instruction-set-architecture
  - inference
  - matrix-accelerators
date: 2026-04-21
source_file: raw/AI/LilysAI/understanding-the-risc-v-extensions-for-ai-john-simpson-sifive.md
last_updated: 2026-04-21
sources:
  - understanding-the-risc-v-extensions-for-ai-john-simpson-sifive
---

## Summary
본 문서는 [[RiscV]] 생태계에서 AI 워크로드 가속을 위해 제안된 ISA 확장 계열을 분류하고, 워크로드 특성에 따라 확장 방식이 달라져야 한다는 점을 정리한다. 기본 축은 행렬 곱셈 가속, 데이터 타입 확장, 그리고 벡터 기반 대비 완전 행렬 상태 기반의 아키텍처 트레이드오프다.

핵심은 하나의 확장으로 모든 AI 도메인을 만족시키는 것이 아니라, 엣지에서는 오버헤드가 낮고 점진적으로 채택 가능한 접근이 유리하며, 데이터센터에서는 더 큰 행렬 상태 기반 확장이 유리하다는 점이다. 특히 [[LLM]]의 prefill/decode 단계 특성이 하드웨어 선택에 직접적인 영향을 주므로, 같은 모델이라도 실행 단계에 맞는 ISA-매칭이 필요하다.

또한 기존 [[RiscVVector]]의 역할이 사라지지 않으며, [[FP8]], [[FP16]], [[FP32]] 포함한 폭넓은 정밀도 지원과 컴파일러 생태계(LLVM, GCC)가 동반되어야 AI 소프트웨어 스택의 채택 비용이 낮아진다고 본다.

## Key Claims
- [[RiscV]]의 AI 확장은 AI/ML 보급 확대에 따라, 행렬 곱셈 가속과 데이터 타입 지원을 위한 ISA 정규화가 핵심 과제이다.
- 본문은 AI 확장을 4개 축으로 구분한다: [[VectorBatchProduct]], [[IntegratedMatrixExtensions]], [[VectorMatrixExtensions]], [[AttachedMatrixExtensions]].
- [[RiscVVector]]는 계속 존재하며, layer norm, softmax, soft cap 연산과 같이 행렬 곱셈이 아닌 연산도 충분히 중요하기 때문에 소거되지 않는다.
- [[VectorBatchProduct]]는 새로운 상태를 거의 추가하지 않아 빠른 채택이 가능하고, 소프트웨어 래핑으로 확장성이 높다.
- [[IntegratedMatrixExtensions]]는 비교적 간결한 하드웨어 변경으로 성능을 올리며, 벡터 레지스터 길이에 따라 산술 강도가 개선된다.
- [[VectorMatrixExtensions]]와 [[AttachedMatrixExtensions]]는 더 큰 행렬 상태/어큐뮬레이터 개념을 도입해 높은 처리량을 목표로 하며, 특히 대형 데이터센터 워크로드에서 유리한 편이다.
- LLM은 prefill 단계와 decode 단계의 연산 특성이 달라 같은 확장이 모든 단계에 최적은 아니며, decode는 작은 배치 환경에서 효율 저하가 발생할 수 있다.
- 엣지 도메인에서는 [[VectorBatchProduct]] 또는 [[IntegratedMatrixExtensions]]가 현실적이고, 데이터센터에서는 [[VectorMatrixExtensions]] 또는 [[AttachedMatrixExtensions]]가 적합하다는 결론이 제시된다.
- FP64는 처리량을 큰 폭으로 감소시킬 수 있어, 고정밀 경로 사용 시 성능 모델링이 필요하다.

## Key Quotes
> "RISC-V는 ISA 확장을 통해 커스텀 연산을 더 쉽게 추가할 수 있었고, 이것이 AI/ML 시장 채택의 핵심 동력이었다."

> "계산 병목을 넘어서려면 연산 크기를 확장해야 하지만, 대역폭 병목이 존재하면 작은 연산이 현실적으로 더 적합한 구간이 있다."

> "엣지에서는 새로운 상태를 덜 요구하는 확장이 유리하고, 데이터센터에서는 더 큰 행렬 상태 기반 확장이 오히려 유리하다."

> "LLM decode는 배치 1에서 자주 동작하므로, 모든 대형 행렬 상태 기반 가속이 동일한 비효율을 보일 수 있다."

## Connections
- [[RiscV]] — 본 문서의 중심 ISA 플랫폼.
- [[RiscVVector]] — 기존의 핵심 벡터 기반 연산 축으로 계속 유지.
- [[VectorBatchProduct]] — 초기/빠른 채택형 확장.
- [[IntegratedMatrixExtensions]] — 엣지 적합성과 구현 단순성을 강조하는 확장군.
- [[VectorMatrixExtensions]] — outer product 기반, 높은 처리량 지향의 데이터센터형 옵션.
- [[AttachedMatrixExtensions]] — 가장 공격적이며, 별도 행렬 상태/어큐뮬레이터를 활용한 고성능 옵션.
- [[JohnSimpson]] — 발표자/저자.
- [[SiFive]] — 발표자 소속 조직으로 ISA 주도/생태계 관점에서 중요.
- [[LLM]] — prefill/decode 단계 분리가 확장 선택 기준을 결정.
- [[FP8]] — AI 워크로드에서 데이터 타입 비용·정밀도 균형의 핵심 포인트.

## Contradictions
- 기존 [[RiscV]]/AI 서술과 충돌은 없으며, 오히려 기존 자료의 "AI 가속은 하드웨어-소프트웨어 동시 설계가 필요"라는 결론을 워크로드-단계별 ISA 선택 프레임으로 정교화한다.