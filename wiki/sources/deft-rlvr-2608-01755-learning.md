---
title: "DEFT-RLVR 학습 노트: candidate-grounded AD reasoning"
type: source
tags: [autonomous-driving, vlm, deft, rlvr, ad-mcq, verifiable-reasoning, learning]
date: 2026-08-12
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W32/deft-rlvr-verifiable-ad-vlms-2608-01755/learning.md
source_hash: eba3e43b0b95e283
---

## Summary
이 학습 노트는 [[DEFT-RLVR]] 논문의 핵심을 자율주행 [[VisionLanguageAction|VLA]] 관점에서 다시 정리한다. 중심 메시지는 candidate trajectory를 먼저 보여 주지 않고 [[TrajectoryAnchoringBias]]를 줄인 뒤, [[DEFT]]식 candidate-blind reasoning과 [[AD-MCQ]] 기반 선택을 결합해 검증 가능한 decision을 학습해야 한다는 점이다. 또한 [[RLVR]] 보상과 구조화된 rubric을 통해 단순 정답률뿐 아니라 근거 정합성, 규칙 준수, 환각 억제를 함께 다룬다.

## Key Claims
- [[DEFT-RLVR]]는 reasoning 전에 candidate trajectory를 숨겨, 결과를 먼저 본 뒤 설명을 맞추는 사후 합리화 경향을 줄이려는 설계다.
- [[AD-MCQ]]는 자유 형식 trajectory 회귀보다 후보 선택 문제로 바꿔, 결정 정답성을 명확히 검증할 수 있게 한다.
- [[RLVR]]와 rubric reward를 결합하면 exact match만 보는 것보다 장면 근거, 위험 판단, 규칙 준수까지 함께 최적화할 수 있다.
- candidate visibility를 reasoning 이후로 미루는 exposure ordering 자체가 supervision constraint가 된다.
- AD 도메인에 맞춘 fine-tuning만으로는 일반 시각 추론 능력이 무너질 수 있으므로 general visual evaluation을 같이 봐야 한다.

## Key Quotes
> "candidate가 먼저 노출되는 추론은 정답 유추보다 정답 정합 편향으로 흘러가기 쉽다."

> "DEFT는 reasoning을 먼저 만들고 candidate를 나중에 노출하는 순서를 통해 causal scene grounding을 훼손하지 않은 상태로 후보 선택을 검증 가능하게 만든다."

## Connections
- [[DEFT-RLVR]] — 이 노트의 주제인 candidate-grounded AD reasoning의 중심 대상
- [[DEFT]] — reasoning과 candidate exposure를 분리하는 핵심 설계
- [[AD-MCQ]] — scene별 후보 trajectory 선택을 위한 benchmark 형식
- [[RLVR]] — 검증 가능한 reward 기반 후학습 프레임
- [[TrajectoryAnchoringBias]] — GT future 노출이 reasoning을 왜곡하는 편향
- [[AutonomousDrivingVLA]] — 적용 도메인
- [[ClosedLoopPlanning]] — trajectory 선택과 closed-loop 평가가 만나는 지점
- [[Hallucination]] — GT-conditioned reasoning에서 악화될 수 있는 실패 모드

## Contradictions
- 없음. 기존 [[DEFT-RLVR]] 관련 위키 항목들의 논지를 보강하며, reasoning-first / candidate-later 순서를 분명히 설명한다.
