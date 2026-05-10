---
title: "Closed-Loop Simulation Evaluation"
type: concept
tags: [simulation, autonomy, verification, testing, reinforcement-learning]
last_updated: 2026-05-10
sources:
  - a-peek-into-tesla-s-autonomous-future-core-tech-revealed-by-vp-ashok-elluswamy-at-iccv25-wdfm-ad
---

## Definition
[[ClosedLoopSimulationEvaluation]]은 과거 상태-행동 쌍에서 시작해 동적 환경을 반복적으로 생성하고 정책 신경망과 함께 동작시켜, 시스템 전체 안정성을 장기적으로 평가하는 절차다.

## Core Elements
- State-action 기반 시뮬레이터 역추론
- 과거 실패 사례의 재생성
- 새 코너 케이스 시나리오의 인위적 합성
- 정책 신경망과의 폐쇄루프 상호작용을 통한 충돌/정합성/회복성 측정

## Why It Matters
- 오픈루프 지표가 높더라도 실차 동작에서 좋은 성능을 보장하지 않는 경우가 많다.
- 폐쇄루프는 policy drift와 compounding error를 드러낸다.
- 소량의 edge case 개선이 전체 주행 품질에 미치는 영향을 정량화할 수 있다.

## Links to Existing Concepts
- [[Simulation]]
- [[Reinforcement Learning]]
- [[ValidationSet]]
- [[Evaluation]
- [[AutonomousVehicle]]
- [[Safety]]
