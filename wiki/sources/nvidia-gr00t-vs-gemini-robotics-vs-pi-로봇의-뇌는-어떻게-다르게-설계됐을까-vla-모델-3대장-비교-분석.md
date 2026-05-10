---
title: "NVIDIA GR00T vs Gemini Robotics vs Physical Intelligence π: VLA 모델 3대장 비교 분석"
type: source
tags: [NVIDIA, GR00T, Google, GeminiRobotics, PhysicalIntelligence, VLA, Robotics, HumanoidRobotics, FoundationModel, CrossEmbodiment, FlowMatching, HierarchicalPolicy]
date: 2026-05-10
sources:
  - nvidia-gr00t-vs-gemini-robotics-vs-pi-로봇의-뇌는-어떻게-다르게-설계됐을까-vla-모델-3대장-비교-분석
last_updated: 2026-05-10
source_file: raw/Robotics/LilysAI/nvidia-gr00t-vs-gemini-robotics-vs-pi-로봇의-뇌는-어떻게-다르게-설계됐을까-vla-모델-3대장-비교-분석.md
source_hash: f2cfc5331139d51c
---

## Summary
이 문서는 로봇 일반 지능의 핵심 아키텍처로 주목받는 [[NVIDIA|NVIDIA]]의 [[NVIDIAGR00T]], [[Google|구글]]의 [[GeminiRobotics]], [[PhysicalIntelligencePi]]의 VLA 계열을 한눈에 비교한다. 세 모델은 모두 시각-언어 입력에서 로봇 행동으로 가는 연결을 추구하지만, 설계 철학은 각각 다르다.

[[NVIDIAGR00T]]는 휴머노이드 중심의 범용 파운데이션 모델을 목표로 하며, 고수준 이해와 저수준 제어를 **이원 구조**로 분리한다. [[GeminiRobotics]]는 추론과 실행을 분리한 뒤 **Thinking Before Acting(행동 전 내부 추론)**을 도입하고, 모션 트랜스퍼로 인바디먼트 간 이전을 강화한다. [[PhysicalIntelligencePi]]는 파운데이션 정책 자체를 핵심으로 두고, 플로우 기반 액션 표현, 계층적 제어, 지식 보존 및 장시간 작업 메모리로 일반화와 실용성의 균형을 밀어붙인다.

각 모델의 공통 분모는 모두 “로봇 AI에서 데이터 제약을 어떻게 넘어서느냐”와 “한 번의 로봇에서 배운 것이 여러 몸체/작업으로 얼마나 잘 전이되느냐”라는 문제에서 출발하며, 다중 모달 지도 학습의 다음 단계로 진입한 상태다.

## Key Claims
- [[NVIDIAGR00T]]의 GR00T N1은 [[VisionLanguageAction]](VLA) 기반으로 [[System2|상위 언어-인지]]와 [[System1|저수준 제어]]를 분리한 구조를 보여주며, 인바디먼트(로봇 몸체)별 적응 레이어를 둔다.
- [[NVIDIAGR00T]]는 웹 영상/시뮬레이션/실기체 텔레오퍼레이션 데이터를 피라미드 형태로 결합해 학습한다. 아래로 갈수록 데이터 양은 늘고, 위로 갈수록 로봇 특이성은 증가한다.
- [[NVIDIAGR00T]] N1.5는 기존 VLM(예: [[VLM]])을 완전 재학습하지 않고 잠재 표현을 안정적으로 연결해 언어 지시 추종과 grounding 성능을 개선했다.
- [[NVIDIAGR00T]] N1.6은 동작 데이터 규모와 인바디먼트 다양성을 늘려 [[HumanoidRobotics]] 환경으로의 확장성과 다작업 대응을 강화했다.
- [[GeminiRobotics]]는 추론 계층/행동 계층 분리를 통해 대형 추론 모델의 지연 부담을 완화하면서, 온보드에서는 짧은 반응 주기를 위한 행동 디코더를 별도로 사용한다.
- [[GeminiRobotics]] 1.5에서 "[[ThinkingBeforeActing]]"를 통해 복잡 과제를 단계적 계획-실행-피드백 루프로 분해하고, [[MotionTransfer]]로 서로 다른 로봇 간 동작 지식을 이동시키려 한다.
- [[GeminiRobotics]]의 ER(Embodied Reasoning) 계열은 시공간 이해와 계획 능력에 집중해, 정교 동작 이전에 "무엇을 할지"를 판단하는 추론 과정을 강화한다.
- [[PhysicalIntelligencePi]]는 [[FlowMatching]]과 같은 연속 액션 생성 기법을 기반으로 한 [[MacroAction]]-스타일의 고주파 제어를 추구해 정교 조작에서 강점을 보인다.
- [[PhysicalIntelligencePi]]의 Fast 계열은 액션 토큰화를 주파수 도메인에서 압축해 학습 효율을 크게 개선하면서 제너럴리스트 정책 성능을 유지했다.
- [[PhysicalIntelligencePi]]의 0.5/0.6은 [[HierarchicalPolicy]], [[KnowledgeInsulation]], 긴 작업 기억 구조를 점진적으로 도입해 오픈월드 일반화, 계층 제어, 장기작업 유지 성능을 보완한다.

## Key Quotes
> "범용 로봇 AI의 성능은 데이터 범위만으로는 해결되지 않고, 인바디먼트 확장과 제어 표현의 적절한 결합이 핵심이다." — source interpretation

> "생각한 뒤 행동한다(Thinking Before Acting)는 로봇에서 추론 계층과 실행 계층을 실용적으로 분리한다." — source interpretation

> "파이는 언어 이해를 잃지 않으면서 로봇 동작 정책을 더 빨리 학습하기 위해 지식 보존을 구조적으로 강화한다." — source interpretation

## Connections
- [[NVIDIA]] — [[NVIDIAGR00T]]의 출처인 기업 및 로봇 전략의 중심.
- [[NVIDIAGR00T]] — 본 문서의 NVIDIA 계열 VLA 모델.
- [[System1]], [[System2]] — [[NVIDIAGR00T]]의 이원 제어 구조를 설명하는 개념적 골격.
- [[Google]] — [[GeminiRobotics]]의 출처 기업.
- [[GeminiRobotics]] — 추론-행동 분리와 모션 전이의 구현 사례.
- [[PhysicalIntelligence]] — 파이(π) 계열 출처 기업/연구조직.
- [[PhysicalIntelligencePi]] — VLA 파운데이션 정책의 대표 구현군.
- [[VLA]] — 세 모델의 공통 기반인 비전-언어-행동 프레임워크.
- [[ActionChunking]] — 연속 제어 안정성 확보에 반복적으로 활용되는 핵심 패턴.
- [[CrossEmbodimentTransfer]] — 세 모델 공통의 성능 병목/확장성 축.
- [[KnowledgeInsulation]] — [[PhysicalIntelligencePi]]의 장기 학습 품질 유지 전략.
- [[ThinkingBeforeActing]] — [[GeminiRobotics]]의 핵심 차별화 전략.

## Contradictions
- 기존 자료들에서 일부는 모듈형 파이프라인의 장점을 강조해 왔으나 본 문서는 특히 장면-행동 연결 손실을 줄이기 위해 통합형 혹은 계층형 정책을 강조한다. 이는 완전한 모순이라기보다 엔지니어링 트레이드오프의 선택 순위 차이로 정리한다.
