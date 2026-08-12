---
title: "AD-MCQ"
type: concept
tags: [autonomous-driving, benchmark, multiple-choice, trajectory, verifiable-evaluation]
sources:
  - deft-rlvr-2608-01755-paper-ko
last_updated: 2026-08-12
---

## Definition
[[AD-MCQ]]는 자율주행 장면에서의 미래 trajectory 후보 집합을 기반으로 한 다중 선택 benchmark이다. 모델은 scene별로 제시된 후보 중 정답을 골라내고, 각 후보에 대한 reasoning trace(사유 설명)도 함께 출력해야 한다.

## Construction
- scene별로 소수의 후보 trajectory를 clustering/코드북으로 구성
- 후보는 validity, deduplication, oracle fidelity, candidate separation 점검을 거쳐 평가용으로 사용
- reconstruction error trade-off를 위해 코드북 크기를 균형 조정(논문은 K=8192를 제시)

## Why this matters
- GT trajectory를 직접 정답으로 주고 정답/비정답 reasoning을 비교하는 방식보다, 선택 정합성 검증이 가능
- 근사한 scene grounding vs 미래 trajectory 정당성 구분이 쉬워져 shortcut을 더 잘 적발

## Metrics / role
- 추론 정확도, candidate-grounding 정합, and CFS 같은 평가 지표와 결합되어 사용 가능

## Connections
- [[DEFT-RLVR]]
- [[DeferredExposure]]
- [[AutonomousDrivingVLA]]
- [[ActionGrounding]]

## Notes
벤치 설계가 [[ClosedLoopPlanning]] 및 closed-loop rollout 평가로 확장될 때, 안전성 기반 검증 신호를 강화하는 데 유리한 형태이다.