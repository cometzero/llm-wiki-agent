---
title: "John Simpson"
type: entity
tags: [person, riscv, si-five]
last_updated: 2026-04-21
sources:
  - understanding-the-risc-v-extensions-for-ai-john-simpson-sifive
---

## Overview
[[JohnSimpson]]은 [[RiscV]] 기반 AI 가속 ISA 확장 제안을 설명한 발표/문서의 핵심 발표자이다. AI 모델 규모 성장에 따라 [[RiscV]]가 필요로 하는 행렬 연산 및 정밀도 지원 확장 방향을 정리하고, 확장 전략을 엣지/데이터센터 워크로드로 구분하여 제시한 것으로 정리된다.

## Key Contributions
- AI용 행렬 곱셈 가속의 네이티브 접근을 위해 ISA 제안군을 비교 프레임으로 제시.
- [[VectorBatchProduct]], [[IntegratedMatrixExtensions]], [[VectorMatrixExtensions]], [[AttachedMatrixExtensions]]의 차이를 워크로드 단계(pre- fill/decode)에 맞춰 설명.
- [[RiscVVector]]의 지속적 필요성과 컴파일러 스택([[LLVM]], [[GCC]]) 중요성을 강조.

## Connections
- [[RiscV]], [[SiFive]], [[RiscVExtensionsForAI]], [[LLM]]
- [[AIInfrastructure]], [[VectorBatchProduct]], [[IntegratedMatrixExtensions]]

## Notes
이 항목은 기술적 저자 중심의 인물 페이지로, 제품/회사 중심 설명보다 제안 프레임 정리와 기술 분류에 기여한 위치를 보존한다.