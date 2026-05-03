---
title: "Groq"
type: entity
tags:
  - company
  - ai-chip
  - inference
  - architecture
last_updated: 2026-05-03
sources:
  - hotchips34-groq-abts-final-pdf
---

## 개요
[[Groq]]는 추론 중심의 AI 시스템에서 높은 예측 가능성과 낮은 지연 시간을 목표로 [[StreamingTensorProcessor|소프트웨어 정의 스트리밍 텐서 처리 아키텍처]]를 전개한 회사/플랫폼이다.

## 핵심 특징
- [[StreamingTensorProcessor]] 기반 아키텍처를 통해 연산기를 단순화하고, 캐시 비의존 메모리 모델을 통해 성능 변동을 줄이는 방향을 채택했다.
- [[GroqChip]] 계열은 기능 유닛 분할([[ICU]], [[MXM]], [[VXM]], [[SXM]], [[MEM]])과 소프트웨어 제어 인터페이스를 결합한다.
- [[C2C]]/[[RealScale]] 기반 분산 동작에서 글로벌 동기화와 라우팅을 소프트웨어가 통제해 결정론적 성능을 유지하려고 한다.

## 주요 문헌 연결
- [[hotchips34-groq-abts-final-pdf]] — 결정론 기반 TSP/ISA/스케줄링/신뢰성의 핵심 기술 상세.
- [[groq-inference-tokenomics-speed-but-at-what-cost]] — 비용 효율/성능-지연 트레이드오프 맥락.
- [[NVIDIA Groq 3 LPX 소개[](#introducing_nvidia_groq_3_lpx )]] — [[NVIDIA]] 생태계에서의 협업·경쟁 위치.

## 연결 페이지
- [[StreamingTensorProcessor]]
- [[GroqChip]]
- [[DeterministicExecution]]
- [[SoftwareDefinedHardware]]
- [[AIInfrastructure]]
- [[TCO]]