---
title: "AttachedMatrixExtensions"
type: concept
tags: [risc-v, matrix-extensions, high-performance]
last_updated: 2026-04-21
sources:
  - understanding-the-risc-v-extensions-for-ai-john-simpson-sifive
---

## Definition
[[AttachedMatrixExtensions]](AM)는 행렬 연산 A/B/C를 위한 별도 상태군을 기본 구성으로 두는 RISC-V AI 확장군이다.

## Characteristics
- 거의 완전한 새로운 행렬-전용 상태/어큐뮬레이터 구조를 가짐
- 벡터 유닛의 유무에 덜 의존
- 메모리 직접 로드/스토어 경로가 필요해 데이터 이동 구조 설계가 중요
- 설계 공간이 가장 넓고, 상향 성능 잠재력도 높음

## Best Use Cases
- 데이터센터형 고성능 AI 추론/학습 인프라에서 유리
- prefill 중심의 대형 행렬 처리에서 높은 처리량

## Tradeoffs
- 구현 복잡도와 면적/설계 비용이 높음
- 디코드의 저배치 구간에서는 반드시 별도 매칭/스케줄링 필요

## Cross-links
- [[RiscVExtensionsForAI]], [[VectorMatrixExtensions]], [[LLM]], [[FP64]]

## Practical Note
최고 성능을 추구하는 옵션이지만, 채택 이전에 소프트웨어 스택과 메모리 계층의 경제성을 함께 검토해야 한다.