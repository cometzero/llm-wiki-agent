---
title: "DEFT-RLVR"
type: concept
tags: [rlvr, autonomous-driving, verifiability, vlm]
sources:
  - deft-rlvr-2608-01755-paper-ko
last_updated: 2026-08-12
---

## Definition
[[DEFT-RLVR]]는 [[DEFT]]의 delayed exposure 설계를 [[RLVR]](verifiable reward learning) 보상으로 통합한 자율주행 VLM 학습/추론 방법이다. model을 먼저 후보를 보지 못한 상태에서 reasoning하게 만들고, 후보를 본 뒤 선택하도록 제약한다.

## Core design
1. Candidate-blind reasoning 단계
2. Candidate-grounded decision/verification 단계
3. 정답/선택 적합도 reward + structured rubric reward(장면 증거, 위험/규칙, decision logic) 결합

## Reported strengths
- AD-specific reasoning accuracy 개선
- shortcut-driven policy drift 완화
- 후보 노출 지연으로 explanation과 선택이 분리된 검증 신호 확보

## Connections
- [[DeferredExposure]]
- [[AD-MCQ]]
- [[RLVR]]
- [[TrajectoryAnchoringBias]]
- [[AutonomousDrivingVLA]]

## Notes
실험에서 training-free DEFT 대비, mixed-target distillation 대비, and DEFT-RLVR 조합의 trade-off를 분석해 성능-검증 균형을 보여준다.