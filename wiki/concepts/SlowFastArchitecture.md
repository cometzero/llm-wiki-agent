---
title: "Slow-Fast Architecture"
type: concept
tags: [architecture, dual-system, reasoning, action]
sources: [abot-n1-2607-10383-learning]
last_updated: 2026-07-15
---

## Definition
느린 reasoning system과 빠른 action/control system을 분리하는 구조. Slow system이 고수준 목표/추론을 담당하고, Fast system이 저수준 제어를 담당한다.

## Key Characteristics
- **Interpretability**: reasoning과 action 분리로 모델 해석 향상
- **Latency Control**: fast system이 높은 주기로 실행 가능
- **Modularity**: 각 모듈 독립적 최적화 가능

## Applications
- [[ABot-N1]]: pixel goal reasoning → waypoint execution
- [[DriveVLM]]: slow reasoning → fast driving control
- [[DualAD]]: dual-system autonomous driving
- [[Qwen-RobotNav]]: agentic navigation dual-system interface

## Related Concepts
- [[ActionGrounding]]: slow-fast bridge 역할
- [[WaypointNavigation]]: fast system output
- [[PixelGoal]]: intermediate representation 예시
