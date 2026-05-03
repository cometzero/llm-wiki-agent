---
title: "AIFactory"
type: concept
tags:
  - AIInfrastructure
  - InferenceEconomics
  - NVIDIA
sources:
  - nvidia-gtc-keynote-2026
last_updated: 2026-05-03
---

## Summary
[[AIFactory]]는 AI의 핵심 성능 단위를 “토큰 생산”으로 바꾸는 데이터센터·인프라 운영 개념이다. 과거의 저장/처리형 데이터센터 관점을 벗어나 전력 제약 하에서 고밀도 추론을 지속적으로 출력하는 시스템으로 해석된다.

## Core Ideas
- 데이터센터를 단순 하드웨어 집합이 아니라 토큰 처리 파이프라인으로 모델링한다.
- 경쟁력은 처리량만이 아니라 토큰당 전력 비용과 지연 예측성으로 결정된다.
- [[InferenceOptimization]], [[DSX]], [[NVIDIA]] 오케스트레이션 계층이 함께 결합돼야 한다.

## Connections
- [[TokenEconomy]]
- [[TokensPerWatt]]
- [[Groq3LPX]]
- [[VeraRubin]]
- [[DSX]]

## Inheritance from existing wiki
- 기존 위키의 하드웨어 성능 중심 논의에서 운영경제성 중심 서사로 확장되는 개념이다.
