---
title: "Week 01. VLA for AD 지형도와 taxonomy"
type: source
tags: [VLA, AutonomousDriving, VisionLanguageAction, Safety, Evaluation, Survey, Taxonomy]
date: 2026-04-28
source_file: raw/vla_study/weeks/week-01-vla-for-ad-지형도와-taxonomy-2026-04-28.md
sources:
  - week-01-vla-for-ad-지형도와-taxonomy-2026-04-28
last_updated: 2026-05-03
---

## Summary
이 문서는 [[VisionLanguageActionForAutonomousDriving|VLA for Autonomous Driving]] 연구 지형을 정리한 1주차 학습 노트다. 핵심 메시지는 자율주행의 다음 축이 단순한 [[VisionAction|VA]]가 아니라, 시각 이해를 언어적 reasoning과 executable action까지 연결하는 [[VisionLanguageActionForAutonomousDriving|VLA]]이며, 이 분야는 [[EndToEndVLA]]와 [[DualSystemVLA]]라는 두 설계 축으로 읽어야 한다는 점이다.

문서는 [[ActionGrounding]]을 중심 기준으로 삼아 textual action, numerical action, explicit guidance, implicit transfer를 비교하고, open-loop와 closed-loop 평가의 차이도 함께 정리한다. 또한 데이터셋, 벤치마크, 학습 레시피, long-tail safety risk를 하나의 taxonomy 안에 배치해 이후 주차 자료를 꽂아 넣을 좌표계를 제공한다.

## Key Claims
- VLA for autonomous driving의 핵심은 "무엇을 봤는가"를 "왜 그렇게 판단했는가"와 "어떤 trajectory/action으로 실행할 것인가"까지 연결하는 것이다.
- 이 분야의 현재 지형도는 크게 [[VisionAction|VA]] → [[VisionLanguageActionForAutonomousDriving|End-to-End VLA]] → [[DualSystemVLA|Dual-System VLA]]로 읽을 수 있다.
- [[VisionAction|VA]]는 vision to action direct mapping에 강하지만, 내부 reasoning이 불투명하고 distribution shift에 취약하다.
- [[VisionLanguageActionForAutonomousDriving|VLA]]는 vision, language-grounded reasoning, executable output을 통합해 해석 가능성과 일반화 가능성을 높이려 한다.
- [[EndToEndVLA]]는 perception, reasoning, planning을 하나의 모델에 통합하는 방식이다.
- [[DualSystemVLA]]는 느린 VLM reasoning과 빠른 planner/control을 분리해 safety-critical execution과 latency를 맞춘다.
- action grounding은 caption 수준이 아니라 waypoint, trajectory, control까지 내려와야 강한 VLA로 볼 수 있다.
- textual action은 해석성이 높지만 controller와 직접 연결되기 어렵고, numerical action은 실행 가능성이 높지만 reasoning trace가 약해질 수 있다.
- open-loop metric만으로는 실제 driving safety를 충분히 판단할 수 없고, closed-loop evaluation과 instruction fidelity가 함께 봐야 한다.
- language는 설명, 입력 instruction, 중간 reasoning, action grounding의 네 역할로 구분할 수 있다.
- VLA 논문을 읽을 때는 dataset, metric, latency, fallback, safety monitor, failure case를 함께 확인해야 한다.
- long-tail scenario에서 설명이 가능하다는 것과 안전하게 행동할 수 있다는 것은 다르다.

## Key Quotes
> "차량이 무엇을 봤는가"를 "왜 그렇게 판단했는가"와 "어떤 trajectory/action으로 실행할 것인가"까지 연결하는 것

> "VA → End-to-End VLA → Dual-System VLA"

> "action grounding"

## Connections
- [[VisionLanguageActionForAutonomousDriving]] — 본 문서의 중심 연구 주제.
- [[ActionGrounding]] — 언어와 reasoning이 실행 가능한 행동으로 연결되는 핵심 축.
- [[ClosedLoopEvaluation]] — 자율주행 정책의 실제 안전성과 상호작용을 평가하는 관점.
- [[Safety]] — long-tail scene과 fallback, monitor를 읽는 기준.
- [[LongTailGeneralization]] — 희귀 상황에서의 일반화와 안전 대응을 다루는 축.
- [[Evaluation]] — open-loop, closed-loop, text metric를 비교하는 분석 프레임.
- [[MermaidDiagram]] — 이 노트의 시각적 taxonomy와 architecture map에 사용된 표현 형식.
- [[VisionAction]] — VLA 이전 단계의 직접적인 vision-to-action 계열.
- [[EndToEndVLA]] — perception, reasoning, planning을 한 모델로 통합하는 VLA 설계.
- [[DualSystemVLA]] — slow reasoning과 fast execution을 분리하는 VLA 설계.

## Contradictions
- 기존 [[VisionLanguageActionForAutonomousDriving]] 관련 위키 내용과 직접 충돌하지 않는다.
- 이 문서는 개별 모델의 SOTA 주장보다 taxonomy와 evaluation frame을 정리하는 데 초점이 있다.
