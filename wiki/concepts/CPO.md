---
title: "Co-Packaged Optics (CPO)"
type: concept
tags: [interconnect, networking, compute-clusters]
last_updated: 2026-04-21
sources:
  - gtc-2026-the-inference-kingdom-expands
---

## Definition
[[CPO]]는 광학 컴포넌트(특히 스위치/랙 간 연결)를 패키지 및 시스템 경로에 더 밀접히 통합해 스케일업 경계에서 신호 품질과 대역폭을 확보하는 설계 접근이다.

## Source-Observed Pattern
- NVIDIA은 구리 기반이 가능한 구간은 구리 우선, 필수 구간은 광학 우선이라는 혼합 철학을 강조한다.
- Rubin→Rubin Ultra→Feynman 경로에서 랙 간 CPO 적용 범위가 확대되지만, 구체적 랙 내 적용은 세대/시점별로 가변적이다.

## Architectural Significance
- NVLink/스위치와의 결합 설계에서 제조 비용, 신뢰성, 광학/구리 PoR의 타이밍 조절이 성능 및 TCO를 좌우한다.
- 장거리/고밀도 연결이 증가하는 world-size 시스템에서 랙 간 병목 완화의 핵심 수단으로 간주됨.

## Connections
- [[Rubin]], [[Oberon]], [[Feynman]], [[Kyber]], [[NVLink]], [[SpectrumX]], [[World Size]]

## Contradictions
- No strong contradiction; confirms prior interpretation of 인터커넥트가 성능보다 공정·비용 제약과 동시 결정된다는 관점.