---
title: "Simulation"
type: concept
tags: [systems, validation, autonomy, robotics]
last_updated: 2026-05-10
sources:
  - a-peek-into-tesla-s-autonomous-future-core-tech-revealed-by-vp-ashok-elluswamy-at-iccv25-wdfm-ad
---

## Definition
[[Simulation]]은 실제 주행/로봇 정책을 대규모로 반복 점검하기 위해 사용되는 가상 환경 생성 시스템이다.
이 소스에서 핵심은 저비용으로 다양한 주행 동역학/행동 상황을 합성해 정책의 실차 전이 전 성능을 점검하는 점이다.

## Practices Noted
- State-action 기반 world model로 다음 상태를 합성
- 과거 사고의 재현(replay)
- 기존 데이터 기반·인위적 케이스 생성(hypothetical conflict scenario)
- 실시간 조향/제동 상호작용 기반 장기 안정성 측정

## Connections
- [[ClosedLoopSimulationEvaluation]]
- [[AutonomousVehicle]]
- [[Reinforcement Learning]]
- [[DataAugmentation]]
- [[Safety]]
