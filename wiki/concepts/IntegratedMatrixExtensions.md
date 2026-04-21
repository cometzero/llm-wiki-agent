---
title: "IntegratedMatrixExtensions"
type: concept
tags: [risc-v, matrix-extensions, edge]
last_updated: 2026-04-21
sources:
  - understanding-the-risc-v-extensions-for-ai-john-simpson-sifive
---

## Definition
[[IntegratedMatrixExtensions]](IME)는 [[RiscVVector]] 기반에서 벗어나지 않으면서 행렬 곱셈 효율을 높이기 위한 설계군이다.

## Characteristics
- 여러 제안 옵션을 포함하는 패밀리
- 일반적으로 별도 대형 상태 추가가 적고, Vtype 확장으로 구현 비용을 억제
- 벡터 레지스터 길이 증가에 따라 산술 강도 개선
- 소프트웨어 루프를 통해 확장 가능한 큰 행렬 처리 가능

## Ideal Domain
- 작은 면적/낮은 복잡도에서 시작해야 하는 [[EdgeAI]] 처리기
- 비용/면적 제약이 강한 임베디드 계열

## Tradeoffs
- 쓰기 비트 수 관리가 병목이 될 수 있어 하드웨어 투명 제어가 중요
- 매우 큰 연산을 직접 처리하기보다 균형형/단계형 구조가 유리

## Cross-links
- [[RiscVExtensionsForAI]], [[VectorBatchProduct]], [[VectorMatrixExtensions]]

## Current Status
IME는 초기 채택성 측면에서 유리하고, 데이터센터로 확장할 때는 [[VectorMatrixExtensions]]/[[AttachedMatrixExtensions]]와의 경계 판단이 필요하다.