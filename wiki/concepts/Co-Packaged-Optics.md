---
title: "Co-Packaged Optics"
type: concept
tags: [interconnect, datacenter, networking, optics]
last_updated: 2026-04-20
sources: [gtc-2026-the-inference-kingdom-expands]
---

## Definition
[[CPO|Co-Packaged Optics]]는 랙/칩 간 고대역 광학 결합을 위해 전자 패키지와 광학 결합부를 함께 설계하는 상호연결 전략이다.

## Policy Signal from Source
- [[NVIDIA]]는 CPO를 랙 내(필요 최소화)보다는 랙 간 대규모 확장 구간에 더 적극 적용하는 형태를 보인다.
- 구리 연결이 가능한 구간은 구리로 두고, 필수 구간에 광학을 배치한다는 비용-신뢰성-성능 균형을 제시한다.

## Source Context
- Rubin Ultra, Feynman 전환 단계에서 NVL 구간별 적용 범위가 상이하며, 일부 구간은 포트폴리오 단위로 변경 가능성이 크다.
- NVLink 및 Spectrum 계열 네트워크와 결합 시 실제 도입 범위는 검증 단계에서 조정될 가능성이 있다고 본다.

## Implications
- 고밀도 GPU 랙 확장에서 구리만으로는 한계가 생기므로, CPO는 세계 규모(world size) 확장의 핵심 선택지로 작동한다.
- 도입 시 비용(특히 광학 트랜시버)과 TCO, 신뢰성 트레이드오프가 공존한다.
