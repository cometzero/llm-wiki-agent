---
title: "NVIDIA GTC 2026"
type: source
tags:
  - NVIDIA
  - GTC2026
  - CUDA
  - AIFactory
  - AINative
  - AgenticSystems
  - OpenClaw
  - VeraRubin
  - Blackwell
  - GraceBlackwell
  - Groq3LPX
  - DSX
  - NeuralRendering
  - QDF
  - QVS
  - TokenEconomy
date: 2026-05-03
source_file: raw/Nvidia/LilysAI/nvidia-gtc-keynote-2026.md
last_updated: 2026-05-03
---

## Summary
[[NVIDIA]]의 [[JensenHuang]]는 GTC 2026에서 AI 시대의 핵심 동력으로 [[AIFactory]], [[AgenticSystems]], [[PhysicalAI]]의 세 축을 제시하며, 계산 비용 절감과 반응성 중심의 추론 인프라로의 전환을 강조했다.

본 키노트는 [[CUDA]]의 20주년을 기점으로 [[TensorCores]], [[CUDA X]], [[NVLink]], [[VeraRubin|Vera Rubin]], [[Groq3LPX]]가 결합된 전체 시스템 관점의 진화를 설명하고, 추론 중심 AI 시대에서 토큰 단가·처리량·지연의 균형이 가장 중요한 경쟁 지표가 됐다고 정리한다.

또한 단일 GPU 개선을 넘어, 데이터센터를 전력 제약 하의 [[AIFactory]]로 전환하고, 오케스트레이션 가능한 디지털 트윈 운영([[DSX]])까지 확장해 AI 인프라의 안정성과 경제성을 동시에 다뤘다.

## Key Claims
- [[AIInfrastructure]] 수요는 훈련 중심에서 추론 중심으로 급격히 이동했으며, 추론 수요는 과거 대비 100만 배 규모의 변화를 만들 만큼 빠르게 확대되었다.
- [[NVIDIA]]는 [[CUDA]]/[[CUDA X]] 생태계를 통해 플랫폼과 툴체인을 확장해, 플랫폼 사용량 증가가 선순환으로 작동한다고 제시한다.
- [[GenerativeAI]]의 확산과 [[ReasoningAI]], [[AgenticSystems|agentic systems]] 성장으로 “AI 팩토리”가 대규모 연산 자원 최적화의 중심 개념이 되었다.
- 토큰당 비용, 토큰 속도, 토큰 처리량이 AI 공급망 가치와 수익성의 핵심 지표가 됐고, 이는 추론 아키텍처 설계의 공통 KPI가 되었다.
- [[Blackwell]]에서 [[VeraRubin]]로 진화하면서 랙 스케일 아키텍처(전력, 메모리, NVLink, 냉각)가 추론 수익성의 중심 변수로 통합되었다.
- [[Groq3LPX]] 통합은 prefill/attention과 decode(특히 FFN-MoE 구간)의 분리 최적화를 통해 낮고 예측 가능한 토큰 생성 지연을 노린 이기종 추론 전략이다.
- [[GraceBlackwell|Grace Blackwell Nvlink 72]]는 극단적인 공동 설계 기반의 동시성·지연·처리량 균형 개선을 목표로 한 아키텍처 단계로 제시되었다.
- 데이터 센터는 파일 저장소가 아니라 [[AIFactory]]로 재정의되며, 전력 제약 내에서 [[TokensPerWatt]]을 극대화하는 운영이 핵심이 되었다.
- [[QDF]]와 [[QVS]]는 구조화된 데이터와 비정형 데이터 가속의 핵심 라이브러리로 제시되어 AI 데이터 처리의 이중축을 완성한다.
- [[OpenClaw]]는 에이전트 운영 체제로 제시되며, 기업용 보안 모델과 [[NemoClaw]] 레퍼런스 구조를 통해 확장성을 추구한다.
- [[PhysicalAI]]/로봇 섹션에서 [[Alpamayo]], [[Cosmos]], [[Groot]] 같은 모델·시뮬레이션 스택이 자율주행과 휴머노이드 확장에 핵심으로 제시되었다.
- 우주 데이터센터(행성/궤도 규모) 구상과 [[Omniverse]] 기반 시뮬레이션은 AI 인프라의 공간 확장 개념을 지표 중심으로 확장한다.

## Key Quotes
> "AI 시대는 생성, 추론, 에이전트가 결합되며 컴퓨팅이 훈련에서 추론으로 중심이 이동했다."

> "데이터센터는 이제 파일을 보관하는 곳이 아니라 토큰을 생성하는 팩토리다."

> "최고의 구조는 처리량뿐 아니라 예측 가능한 토큰 지연을 함께 최적화하는 구조다."

## Connections
- [[NVIDIA]] — 전체 아키텍처/플랫폼/생태계의 중심 주체.
- [[JensenHuang]] — 이번 연설의 핵심 발표자.
- [[CUDA]], [[CUDA X]] — 에코시스템 기반 확산 장치.
- [[TensorCores]], [[TensorCoreLibrary|CUDA X libraries]] — 핵심 가속·알고리즘 계층.
- [[NVIDIAOpenSource]] — 오픈 모델과 도구 생태계 공고화 맥락(소셜/엔터프라이즈 확장).
- [[Groq3LPX]] — decode 분리형 추론 성능 최적화의 핵심 하드웨어.
- [[VeraRubin]], [[Blackwell]], [[NVIDIA Vera Rubin NVL72]] — 차세대 랙스케일 추론 기반.
- [[GraceBlackwell]], [[NVLink]] — 대역폭/지연 최적화를 위한 시스템 단계 진화.
- [[AIFactory]], [[TokensPerWatt]], [[TokenEconomy]] — 비용·성능 가치지표 프레임.
- [[DSX]], [[DigitalTwin]], [[MaxQ]] — AI 팩토리 설계·운영 자동화.
- [[OpenClaw]], [[NemoClaw]], [[OpenClawOS]] — 에이전트 시스템 운영 체제 관점의 운영 계층.
- [[PhysicalAI]], [[Alpamayo]], [[Cosmos]], [[Groot]], [[IsaacLab]], [[Newton]], [[Nemotron]] — 로보틱스/물리 AI 확장 축.
- [[QDF]], [[QVS]], [[StructuredData]], [[UnstructuredData]] — 데이터 처리 패러다임 확대.
- [[AIAutonomy]], [[Robotics]], [[RoboTaxiReady]], [[AutonomousVehicle]] — 물리 AI 적용 사례군.

## Contradictions
- 기존 위키의 기존 NVIDIA 추론 인프라 서사와 직접 충돌하지 않는다. 본 소스는 동일 계열의 추론/추론 지연 체제를 [[AIFactory]]와 [[TokenEconomy]] 중심의 운영 경제성 프레임으로 확장한다.
- 일부 수치(예: 수요 급증 배율)는 과장될 가능성이 있으나, 기존 문헌의 방향성(추론 수요 중심, 지연 민감도 강화)과 모순되기보다는 보완한다.
