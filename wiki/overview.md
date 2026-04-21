---
title: "Overview"
type: synthesis
tags: [overview, corpus]
sources: [andrej-karpathy-on-code-agents-autoresearch-and-the-loopy-era-of-ai, the-great-gpu-shortage-rental-capacity-launching-our-h100-1-year-rental-price-index, gtc-2026-the-inference-kingdom-expands, 26년-제조-산업에-ai-적용되면-이렇게-바뀝니다-10년차-대기업-llm-현직자의-솔직한-조ᄋ, project-glasswing-securing-critical-software-for-the-ai-era-anthropic, terafab-keynote-building-ai-chips-for-earth-space, understanding-the-risc-v-extensions-for-ai-john-simpson-sifive]
last_updated: 2026-04-21
---

# Overview

This overview tracks the current shape of the wiki corpus after the latest ingest.

## Corpus Snapshot
- Sources: 84
- Entities: 154
- Concepts: 127
- Syntheses: 0

## Raw Corpus by Top-Level Folder
- `AI`: 20 source documents
- `Finance`: 14 source documents
- `LPC2025`: 18 source documents
- `Nvidia`: 5 source documents
- `OSS2025_Japan`: 22 source documents
- `Robotics`: 2 source documents
- `Technology`: 6 source documents
- `University_Preparation`: 1 source documents
- `Policy`: 1 source documents

## Highest-Coverage Entities
- [[Anthropic]] — referenced by 6 source page(s)
- [[NVIDIA]] — referenced by 6 source page(s)
- [[MonetaryPolicy]] — referenced by 5 source page(s)
- [[LLMAgents]] — referenced by 6 source page(s)
- [[KevinWarsh]] — referenced by 5 source page(s)
- [[SemiAnalysis]] — referenced by 3 source page(s)
- [[OpenClaw]] — [[agent-first software]], 지속형 에이전트 사례로 고빈도 연결성 상승
- [[Tesla]] — 반도체 제조 역량과 우주 엣지 AI 확장 논의에서 최근 급부상
- [[SpaceX]] — 위성·우주 발사·페이로드 인프라를 통한 컴퓨팅 확장 축의 핵심 파트너
- [[Groq]] — GPU와의 추론 분업 전략의 실증축으로 연결성 확대

## Highest-Coverage Concepts
- [[AIAutomation]] — referenced by 6 source page(s)
- [[LLMAgents]] — referenced by 6 source page(s)
- [[AIInfrastructure]] — 가속기, 네트워크, 저장층 통합 관점 강화
- [[InferenceOptimization]] — 비용/지연/처리량 트레이오드 고도화
- [[AFD]] — [[GPU]]-[[LPU]] 분업과 MoE 라우팅 확장으로 추론 단계 분할의 핵심 축
- [[AddressSpaceIsolation]] — 안전형 커널 맥락의 핵심 축으로 계속 유지
- [[TerawattComputing]] — 지상-우주 스케일 확장형 인프라 패러다임
- [[ContextRot]] — 긴 컨텍스트 비용 모델과 추론 인프라 병목을 함께 다루는 교차 축
- [[AIForCybersecurity]] — AI의 공격력 전환에서 방어 운영 체계 통합 강조
- [[ContextMemoryStorage]] — 긴 문맥 추론의 KV 캐시 오프로딩 축으로 신규 핵심화
- [[CPO]] — 스케일업/스케일아웃 경계에서 구리/광학 분기 설계

## Current Shape of the Knowledge Base
- AI 인프라 논의는 추론 단계별 병목(입력 사전처리·Prefill vs. 토큰 반복 Decode) 분리와 하드웨어 역할 분담으로 이동하며, 단일 GPU 성능만으로 성능을 평가하기보다 [[AFD]] 및 계층형 메모리 네트워크를 결합한 설계가 핵심이 되고 있다.
- [[NVIDIA]]의 추론 전략은 [[Groq]] 계열 자산을 LPU로 흡수해 [[GPU]]-[[LPU]] 이원화, 이어서 [[CPO]]/[[CMX]]/[[STX]]로 네트워크·스토리지까지 확장하며, 인퍼런스 스택의 수직 통합을 강화한다.
- 스케일 전략은 구리 기반 랙 내 상호연결을 활용해 비용 효율과 지연을 맞추다가, world-size 확장 시에는 광학으로 점진 이행하는 하이브리드 인터커넥트 철학으로 정교화된다.
- 긴 컨텍스트와 대량 동시 사용자 환경에서는 메모리 계층 확장이 병목 해소의 핵심으로 부상해, [[Vera ETL256]]·[[CMX]]·[[STX]]를 통한 오프로딩 전략이 성능·안정성 경로의 공통화로 정착하는 흐름이다.

## Cross-Source Synthesis Note
- 기존의 추론 성능 논의는 지금 [[LLM]] 스케일링 법칙과 벡터/행렬 가속 하드웨어 확장으로부터, 더 깊이 네트워크-메모리-스토리지 결합 설계로 이동했다.
- [[RiscVExtensionsForAI]]가 ISA 수준의 워크로드 적합성 선택을 제공하는 것처럼, NVIDIA 축은 인퍼런스의 단계별 역할 분할([[AFD]])과 계층형 저장 오프로딩([[CMX]], [[STX]])에서 비용·지연·품질 트레이오드를 동시에 통제하려는 경향을 강화한다.
- 결과적으로 [[LLMAgents]]/소프트웨어 계층의 성능향상을 실현하려면, 하드웨어 인프라 편차(단기 지연 vs. 장기 처리량, 구리 대 광학, HBM 대 DRAM/SSD 오프로드)를 함께 반영한 설계 프레임이 전제되어야 한다.