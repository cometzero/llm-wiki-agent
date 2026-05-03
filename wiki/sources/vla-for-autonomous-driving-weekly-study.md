---
title: "VLA for Autonomous Driving Weekly Study"
type: source
tags: [VLA, AutonomousDriving, VisionLanguageAction, Safety, Evaluation]
date: 2026-05-03
source_file: raw/vla_study/README.md
sources:
  - vla-for-autonomous-driving-weekly-study
last_updated: 2026-05-03
---

## Summary
이 문서는 [[VisionLanguageActionForAutonomousDriving|VLA(Vision-Language-Action) for Autonomous Driving]] 주간 학습 코퍼스의 운영 규칙과 분석 관점을 정의한다. 매주 화요일 [[Asia/Seoul]] 기준으로 학습 노트를 만들고, 각 주차 자료는 `weeks/week-XX-*.md`에 저장하며, 논문 내용은 한국어 학습 노트 형태로 번역·요약·분석한다.

핵심 분석 축은 [[ActionGrounding]], [[LanguageRole]], [[ClosedLoopEvaluation]], [[Safety]], [[LongTailGeneralization]]이다. 이 코퍼스는 언어가 실제 driving action을 더 안전하고 일반화 가능하게 만드는지, 아니면 설명 가능성만 추가하는지라는 질문을 중심으로 [[MermaidDiagram]], architecture map, evaluation matrix를 활용해 VLA 시스템을 비교·검토하도록 설계된다.

## Key Claims
- 이 코퍼스는 [[VisionLanguageActionForAutonomousDriving]] 주간 학습 자료를 모으는 raw corpus다.
- 매주 화요일 [[Asia/Seoul]] 기준으로 1회 학습 노트를 생성한다.
- 주차별 자료는 `weeks/week-XX-*.md`에 저장한다.
- 각 노트는 논문 내용을 한국어 학습 노트 형태로 번역·요약·분석한다.
- 시각 자료는 Markdown 표, [[MermaidDiagram]], architecture map, evaluation matrix 위주로 구성한다.
- 모든 노트는 [[ActionGrounding]], [[LanguageRole]], [[ClosedLoopEvaluation]], [[Safety]], [[LongTailGeneralization]] 관점으로 분석한다.
- 핵심 질문은 언어가 실제 driving action의 안전성과 일반화에 기여하는지, 아니면 설명 가능성만 덧붙이는지에 있다.
- `curriculum.json`, `state.json`, `template.md`, `weeks/`가 운영의 핵심 파일이다.

## Key Quotes
> "이 모델에서 language는 실제 driving action을 더 안전하고 일반화 가능하게 만드는가, 아니면 설명 가능성을 덧붙이는 역할에 머무는가?"

## Connections
- [[VisionLanguageActionForAutonomousDriving]] — 코퍼스의 중심 연구 주제.
- [[ActionGrounding]] — 언어가 행동으로 어떻게 연결되는지 보는 핵심 분석 축.
- [[LanguageRole]] — VLA에서 언어가 지시, 추론, 설명 중 무엇을 담당하는지 평가하는 축.
- [[ClosedLoopEvaluation]] — 실제 driving 상호작용에서 모델을 검증하는 관점.
- [[Safety]] — 자율주행에서 언어 조건부 행동의 안전성 판단 기준.
- [[LongTailGeneralization]] — 희귀 상황과 엣지 케이스에서의 일반화 성능 축.
- [[MermaidDiagram]] — 학습 노트의 시각화 형식.

## Contradictions
- 기존 위키 내용과 직접 충돌하지 않는다.
- 이 문서는 개별 논문 결과보다 주간 학습 코퍼스의 운영 원칙과 평가 프레임을 정의하는 메타 문서다.
