---
title: "GTC 2026 – The Inference Kingdom Expands"
type: source
tags:
  - nvidia
  - inference
  - llm-infrastructure
  - gpu
  - lpu
  - networking
  - storage
date: 2026-04-21
source_file: raw/AI/LilysAI/gtc-2026-the-inference-kingdom-expands.md
last_updated: 2026-04-21
sources:
  - gtc-2026-the-inference-kingdom-expands
---

## Summary
[[NVIDIA]]는 GTC 2026에서 [[Groq]]의 추론 스택 일부를 흡수한 뒤 [[LPU]]와 [[GPU]]를 결합해 [[InferenceOptimization]]을 재정의하는 방향으로 압도적인 추론 인프라 전략을 제시했다. 핵심은 지연시간이 민감한 디코드 단계는 결정론적 연산에 강한 [[LPU]]로 오프로드하고, 메모리 집약적인 계산은 [[GPU]]에 맡기는 [[AFD|Attention FFN Disaggregation (AFD)]] 아키텍처이다.

[[LPU]]는 LP30/LP35/LP40 계열과 LPX 랙 및 LPU 네트워크로 확장되며, LP40에서는 [[NVLink]], 하이브리드 본딩 DRAM, SK하이닉스 공급 등을 통해 엔비디아 IP와의 통합도 강화한다. 동시에 [[CPO(Co-Packaged Optics)|CPO]]는 루틴의 스케일업/스케일아웃에서 광학과 구리의 혼합 전략으로 점진 적용되며, [[Rubin]], [[Oberon]], [[Feynman]], [[Kyber]]와 같은 세대별 랙 전략으로 세계 크기(world size) 확장을 노린다.

또한 [[CMX]]와 [[STX]]를 중심으로 [[KVCache]] 오프로드를 NVMe/스토리지 계층으로 확장해 긴 문맥·에이전트형 워크로드의 컨텍스트 병목을 줄이는 흐름이 강화된다. 즉, 컴퓨팅-네트워킹-스토리지가 하나의 설계면에서 동시에 진화하는 추세로, [[LLM]] 추론이 더 이상 단일 GPU 성능 지표로만 평가되지 않음을 확인한다.

## Key Claims
- [[NVIDIA]]는 Groq의 핵심 IP/팀 자산을 200억 달러 수준의 자금성으로 흡수해 규제 리스크를 낮춘 뒤 약 4개월 내 Vera Rubin 추론 스택 통합 발표를 성사했다.
- [[AFD]]는 Prefill/Decode 단계 분리를 전제해, 디코드에서 [[Attention]] 계열을 [[GPU]]가 담당하고 상태 없는 FFN 연산은 [[LPU]]가 담당하는 단계적 분업을 제안한다.
- 디코드 단계는 [[KVCache]]와 결합되며 배치 확대 시 GPU 활용률이 제한되고, 이를 완화하기 위해 [[MoE]] 토큰 라우팅 기반 병렬성에서 [[AFD]]가 토큰 처리량을 키우는 방안을 제시한다.
- [[LPU]]의 낮은 지연 특성은 [[Speculative Decoding]]과 결합될 때 디코드 단계 지연을 유의미하게 낮추며, 드래프트/검증 흐름에서 추가 토큰 후보를 한 번에 처리한다.
- LP30은 온칩 SRAM 중심의 고대역폭·저지연 설계로 속도 편익을 강화하고, LP40은 NVLink 적합성·하이브리드 본딩 DRAM 등 통합 확장성을 갖춘 세대이다.
- [[LPX]] 랙은 1U 트레이 다수와 FPGA/C2C 이더넷 변환 레이어를 통해 LPU-GPU-CPU 경계를 정형화하며, 구리와 광학을 목적별로 결합하는 대규모 스케일 전략을 확장한다.
- [[CPO]] 로드맵은 Rubin Ultra/Feynman 세대에서 랙 간 CPO 확대를 중심으로 구리 백플레인과 광학을 혼합 적용해 TCO와 신호 무결성 사이의 트레이드오프를 최적화한다.
- [[Vera ETL256]], [[CMX]], [[STX]]는 CPU 과밀화, KV 캐시 오프로드, 스토리지-컴퓨트 연계 표준화를 위한 플랫폼화 장치로 제시되며, 긴 컨텍스트 시대의 병목 완화 축으로 작동한다.
- NVLink/스펙트럼 기반 스위치/메시 토폴로지는 All-to-all 통신량이 큰 추론에서 병목의 본질을 완화하는 핵심 요소로 남는다.

## Key Quotes
> "엔비디아는 Groq LPU 접근을 통해 추론 가속을 위해 GPU와 LPU를 분업하는 설계를 공개했다."

> "디코드는 메모리 바운드이며 단일 토큰 반복 예측에 매우 민감하다."

> "어텐션 상태를 GPU로, 상태 없는 FFN을 LPU로 분리하면 총 처리 토큰 수와 효율이 개선된다."

> "CPO는 가능한 구간은 구리로, 필수 구간은 광학으로 가는 하이브리드가 핵심 원칙이다."

## Connections
- [[NVIDIA]] — 본 소스의 핵심 주체이자 하드웨어-네트워크-스토리지 통합 전략 주도자.
- [[Groq]] — [[LPU]] 계보의 출발점 자산으로, 규제/통합 리스크를 최소화한 인수형 통합의 핵심.
- [[LPU]] — 저지연 디코드 가속 코어로, [[AFD]]에서 결정론적 FFN 분기 처리.
- [[AFD]] — [[Attention]]와 FFN을 분리 처리하는 추론 구조 개념.
- [[Speculative Decoding]] — LPU 가속에서 드래프트 토큰 예측 속도개선에 연결됨.
- [[LPX]] — LPU 랙형 서비스 플랫폼.
- [[CPO]] — 구리 대비 광학 인터커넥트 적용 경계의 분기점.
- [[Oberon]], [[Rubin]], [[Feynman]], [[Kyber]] — 세대별 랙 확장 축.
- [[Vera ETL256]], [[CMX]], [[STX]] — CPU 밀도/컨텍스트 메모리 저장/스토리지 표준화 확장 장치군.
- [[KVCache]], [[NVLink]], [[SpectrumX]], [[NVSwitch]], [[BlueField]] — 메모리, 네트워크 병목 대응의 주요 매개축.
- [[JensenHuang]] — GTC 발표/로드맵 해설에서 전략 리더로 등장.

## Contradictions
- 기존 문서에서 이미 [[SpeculativeDecoding]]의 지연 절감 효과를 전반적으로 제시하고 있으나, 본 소스는 특히 [[LPU]] 결합 시의 구체적 수치·네트워크 토폴로지 제약을 강조한다. 이는 기존 요약의 “원리 중심” 설명과 충돌이 아니라 정밀화로 해석된다.