---
title: "DEFT-RLVR"
type: concept
tags: [autonomous-driving, vlm, rlvr, rubric, deferred-exposure]
sources: ["deft-rlvr-2608-01755-analysis"]
last_updated: 2026-08-12
---

## Definition
**DEFT-RLVR**은 [[DEFT]]의 후보 지연 노출 전략과 [[RLVR]](Reinforcement Learning from Verifiable Rewards) 최적화를 결합한 설계로, reasoning 결과와 선택 결정이 함께 정렬되도록 학습한다.

## 작동 방식
- 1단계: 장면 기반 근거 생성(후보 비노출)
- 2단계: 후보 노출 후 후보 선택
- 3단계: verifier와 structured rubric 신호를 통해 policy update

## 설계 이점
- 텍스트 추론이 즉시 결과 합리화로 흐르는 것을 억제
- selection 결과가 action grounding 관점에서 직접 검증됨
- 구조화된 rubric으로 탐색 품질을 제어

## 실험적 시사점
- AD-MCQ에서 severe hallucination 감소 경향
- OOD(nuScenes 500 scene)에서 기존 baseline 대비 성능 개선 가능성
- 일반 시각 능력 저하를 상대적으로 억제한 보고가 존재

## 위험 요소
- 후보 품질이 나쁘면 정답 후보 자체의 신뢰성이 하락
- CFS, rubric 점수는 full closed-loop 안전성(충돌, comfort, rule compliance) 보장을 대체하지 못함

## Related
- [[AD-MCQ]]
- [[TrajectoryAnchoringBias]]
- [[RLVR]]
- CFS
- [[AutonomousDrivingVLA]]
