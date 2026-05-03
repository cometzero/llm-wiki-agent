---
title: "Deconstructing Nvidia’s Vera Rubin — The Successor To Blackwell That’s 10x More Efficient"
type: source
tags:
  - NVIDIA
  - Blackwell
  - VeraRubin
  - AIInfrastructure
  - RackScaleSystem
  - NVLink
  - LiquidCooling
  - HBM4
  - SupplyChain
  - Inference
  - PowerEfficiency
date: 2026-05-03
source_file: raw/Nvidia/LilysAI/deconstructing-nvidia-s-vera-rubin-the-successor-to-blackwell-that-s-10x-more-efficient.md
last_updated: 2026-05-03
sources:
  - deconstructing-nvidia-s-vera-rubin-the-successor-to-blackwell-that-s-10x-more-efficient
---

## Summary
이 문서는 [[NVIDIA]]의 차세대 랙 스케일 AI 시스템인 [[VeraRubin]]을 구성 요소 단위로 해체해 소개한다. 전력당 성능을 극대화하기 위해 설계된 [[VeraRubin]]은 [[Blackwell]] 대비 약 10배 수준의 성능 효율을 목표로 하며, 더 적은 전력 비용으로 더 높은 처리량을 노린다.

핵심은 단순히 더 큰 칩이 아니라, 전체 시스템 아키텍처(칩, 메모리, 전력, 냉각, 네트워킹, 조달망)를 재설계한 [[RackScaleSystem]] 접근이다. 특히 수만 개 부품과 수십 개 파트너사가 참여하는 공급망을 표준 레퍼런스 설계로 통합해 양산성과 확장성을 높인 점이 중요하다.

본 소스는 또한 데이터센터 채택 현실(운영 안정성, 과열 대응, liquid cooling 전환 비용)과 가격-성능의 역설(표면 비용 상승 vs 토큰당 비용 하락)을 함께 다루며, 경쟁사로는 [[AMD]]의 [[Helios]] 공개를 언급한다.

## Key Claims
- [[NVIDIA]]는 기존 [[Blackwell]]를 잇는 차세대 랙 스케일 시스템 [[VeraRubin]]을 10x 수준의 performance-per-watt 효율 향상 목표로 공개했다.
- [[VeraRubin]]는 72 GPU 구성의 랙 단위에서 시작해, 한 시스템에 약 **1.3 million components**와 20개국 이상의 공급망, 80개 이상 공급업체가 참여한 조달 구조를 가진다.
- [[VeraRubin]]은 현재 양산 중이며 하반기 출하를 예고한 뒤, 수요가 지속되는 [[NVIDIA]] 고객군(가령 [[Microsoft]], [[Google]], [[Amazon]], [[Meta]])이 수요 확대로 즉시 반응할 것으로 본다.
- 기본 단일 시스템 단가가 기존 대비 약 25% 인상될 것으로 보이나, 전력당 토큰 처리 효율 개선으로 **토큰당 비용은 하락**한다고 제시한다.
- [[VeraRubin]]는 기존 시스템 대비 더 강한 메모리-연산 통합을 위해 [[HBM4]]를 탑재하고, 슬롯/트레이 구조에서 부품 교체와 모듈 분해가 이전 세대보다 단축되도록 설계했다.
- 핵심 성능/대역폭 동력은 [[NVLink]]와 NVLink 스위치 아키텍처이다. 본문은 스위치 레이트가 Blackwell 대비 상향되었고 NVLink spine과 스파인 케이블 구성이 데이터 이동 병목을 줄인다고 서술한다.
- 시스템 전력은 전체적으로 기존 대비 높아졌지만, 100% 액체 냉각 기반으로 설계되어 에너지 재사용/폐쇄 루프에서의 물 사용은 상대적으로 줄어들 수 있다.
- [[BlueField]] DPU와 [[SpectrumX|Spectrum X]]가 저장/보안 및 랙 간 네트워킹에서 중요 역할을 하며, 대형 AI 팩토리는 다중 랙 관점에서 보안·연결이 함께 설계된다.
- 향후 [[VeraRubin]]은 [[VeraRubinUltra]] 방향으로 확장되어, 72GPU→288GPU급 밀도 증가(약 4배 compute scale, 약 50% 중량 증가)와 케이블링 단순화를 지향한다.
- [[AMD]]의 [[Helios]]가 경쟁 후보로 등장하나, 대형 랙-시스템 복잡도를 감당할 수 있는 생태계 조달, 냉각, 네트워킹 통합이 성능 경쟁의 실전 변수로 남는다.

## Key Quotes
> "about 10 times more performant in terms of performance per watt compared to Blackwell" — [[VeraRubin]]의 성능-전력 핵심 주장.

> "the whole idea... is to have a standard reference design that opens the ecosystem to many partners" — 조달 및 파트너 확장을 위한 랙 설계 원칙.

> "we're requiring AI factories of the future to have a liquid-cooled base architecture" — 운영 전제(시설·전력·냉각) 전환 필요성.

> "there is a big whack-a-mole in supply chain" — 부품·가격 변동과 수급 조정의 현실을 요약한 표현.

## Connections
- [[NVIDIA]] — 플랫폼 주도 기업으로, [[Blackwell]]에서 [[VeraRubin]]으로의 전환을 이끈다.
- [[AMD]] — 차기 랙 규모 시스템 [[Helios]]를 통해 직접적인 벤치마크 경쟁군으로 언급된다.
- [[VeraRubin]] — 이 소스의 중심 아키텍처. [[VeraRubinUltra]]로의 확장 경로를 함께 제시한다.
- [[Blackwell]] — 이전 세대 기준점으로 성능·가격·운영 특성이 비교된다.
- [[NVLink]] — 대규모 GPU 상호연결 및 노드 간 대역폭 스케일의 핵심.
- [[HBM4]] — 고대역폭 메모리 스택 중심의 성능 자원.
- [[RackScaleSystem]] — 컴퓨트/메모리/전력/냉각을 하나의 인프라 단위로 최적화한 설계 개념.
- [[LiquidCooling]] — 클린하고 밀집한 냉각 체계로 열 안정성 및 운영 신뢰성을 높임.
- [[PowerManagement]] — 1.3M 부품/220TB/s급 네트워크/220kW급 랙 전력에 대한 운영 제약의 중심 변수.
- [[AICapacityDemand]] — 최종적으로 토큰 수요 증가와 고객 수요 선형 강화를 가능하게 하는 수요 배경.
- [[JensenWong]] — [[NVIDIA]] CEO의 고객 운영 전략(연간 아키텍처 릴리스) 발언이 핵심 맥락으로 인용된다.

## Contradictions
- 기존 위키의 일반적인 AI 인프라 효율 프레임([[
AIInfrastructure]])과 충돌하지 않으며, 단가 상승과 토큰 단가 하락이 동시 공존할 수 있다는 설명은 기존의 [[PowerEfficiency]]/총소유비용 관점과 정합된다.
