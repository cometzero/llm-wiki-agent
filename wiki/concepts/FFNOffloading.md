---
title: "FFN Offloading"
type: concept
tags:
  - InferenceOptimization
  - FFN
  - MoE
  - LPU
  - HeterogeneousInference
sources:
  - nvidia-groq-3-lpx-everything-we-know-storagereview-com
last_updated: 2026-05-03
---

## Definition
FFN 오프로딩은 LLM 추론에서 FFN/[[MoE]] 연산을 전용 가속기로 분리 이전하여 디코드 지연을 낮추고 고정 자원에서 반복 처리를 최적화하는 전략이다.

## Why Source Emphasizes It
- 대형 모델의 FFN 가중치 비중이 95~99%에 가깝고, 디코드 단계의 반복성이 높아 전체 성능 병목의 중심이 된다.
- LPX의 고정 대역폭 SRAM/결정론 처리 경로가 FFN 오프로딩에 유리하다는 실무적 논리를 제시한다.
- 오픈소스 대형 모델별 FFN 파라미터 정량치가 오프로딩 장치 크기(단일 랙 or 멀티랙)를 결정하는 근거로 사용된다.

## Relations
- [[Groq3LPX]] — 실전 오프로딩 플랫폼 후보.
- [[LPU]] — FFN 연산의 핵심 실행 대상.
- [[DecodeDisaggregation]] — 오프로딩 단계가 분리형 디코드 구조 안에서 작동.
- [[SpeculativeDecoding]] — draft 단계에서 FFN 처리속도가 임계값을 정한다.
- [[LPXRack]] — 오프로딩 대상 모델 크기에 따라 멀티랙 요구도를 산정.