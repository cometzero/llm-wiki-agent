---
title: "RoboCasa365"
type: entity
tags: [benchmark, robotics, simulation, manipulation]
sources: [xiaomi-robotics-1-2607-15330]
last_updated: 2026-07-22
---

# RoboCasa365

RoboCasa365는 RoboCasa를 대규모로 확장한 로봇 조작 simulation benchmark로, 다양한 kitchen scene, object instance, short/long-horizon manipulation task를 통해 general-purpose robot policy의 일반화를 평가한다. Xiaomi-Robotics-1은 이 benchmark에서 57.6% success rate를 보고해 기존 최고치 46.6%를 넘어섰다고 정리된다.

## Connections
- [[RoboCasa]] — 원 benchmark 계열.
- [[RoboDojo]] — Xiaomi-Robotics-1이 함께 보고한 simulation benchmark.
- [[ClosedLoopEvaluation]] — policy를 환경에서 실행해 success를 측정하는 평가 축.
