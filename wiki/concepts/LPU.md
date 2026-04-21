---
title: "LPU (Language Processing Unit)"
type: concept
tags: [inference-hardware, nvidia, architecture]
last_updated: 2026-04-21
sources:
  - gtc-2026-the-inference-kingdom-expands
---

## Definition
[[LPU]]는 대규모 토큰 디코드에서 저지연 처리를 목표로, 연산을 단일 목적 slice(예: VXM/MEM/SXM/MXM)로 분리한 추론 가속 코어군을 뜻한다.

## Source Key Traits
- 단일 계층 SRAM 기반 구조로 예측 가능성(결정론성)과 컴파일러 스케줄링 친화성이 높아짐.
- 메모리 대역폭 대비 계산 분산에서 디코드 병목 완화에 유리.
- 처리량 한계(주로 SRAM 및 DRAM 오프로딩 제약) 때문에 GPU와의 결합이 실제 운영에서 필수적.

## Variants (observed)
- LP30: 14세대 기반의 본격 통합 경로로, 온칩 SRAM 비중 강화.
- LP35: 소프트웨어-출시 시간 단축형 마이너 업데이트 성격.
- LP40: TSMC N3P 및 NVLink 통합, 하이브리드 본딩 DRAM로 메모리 확장성 강화 계획.

## Connections
- [[AFD]], [[CPO]], [[LPX]], [[Speculative Decoding]], [[Groq]], [[NVIDIA]]

## Contradictions
- No explicit contradiction identified.