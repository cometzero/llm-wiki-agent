---
title: "SiFive"
type: entity
tags: [company, riscv, open-architecture]
last_updated: 2026-04-21
sources:
  - understanding-the-risc-v-extensions-for-ai-john-simpson-sifive
---

## Overview
[[SiFive]]는 [[RiscV]] 생태계의 하드웨어/아키텍처 관점에서 AI 대응 ISA 논의를 촉진하는 조직으로 정리된다. 본 자료에서는 AI 가속 요구(행렬 연산, 정밀도 지원, 워크로드 적합성)에 맞춘 확장 선택 논의의 맥락에서 핵심적으로 언급된다.

## Relevance
- AI 가속을 위한 ISA 제안의 적용성과 수용성을 판단할 때, 엣지/데이터센터 분기와 정밀도 트레이드오프를 함께 고려해야 함을 보여주는 사례 제공.
- [[RiscVExtensionsForAI]] 프레임의 맥락에서 [[FP8]]·[[FP64]] 처리량 및 대역폭 병목을 함께 다루는 엔지니어링 논리를 정립.

## Key Connections
- [[RiscV]], [[RiscVExtensionsForAI]]
- [[JohnSimpson]]
- [[VectorBatchProduct]], [[IntegratedMatrixExtensions]], [[VectorMatrixExtensions]], [[AttachedMatrixExtensions]]

## Notes
특정 제품 라인보다는 ISA 확장 전략과 생태계 연계 맥락으로 기술해야 하며, 본 항목은 벤더 홍보성이 아니라 기술 분류 프레임의 정합성 유지에 초점을 둔다.