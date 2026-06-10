---
title: "Closed-loop Simulation"
type: concept
tags: [simulation, autonomous-driving, evaluation]
sources: [nvidia-omnidreams-2606-03159-references, tbd-vla-2606-07895]
last_updated: 2026-06-10
---

## Overview
자율주행 policy 검증에서 open-loop metric 한계를 보완하는 평가 패러다임. Agent의 action이 environment에 영향을 주고, 그 결과가 다시 agent 입력에 반영되는 반복적 루프.

## Key Claims
- Open-loop metric의 한계 극복 (static evaluation)
- Agent-environment interaction을 통한 realistic 평가
- [[Waymo]], [[CARLA]], [[nuPlan]] 등이 활용하는 표준 평가 방식

## Connections
- [[VLA]] — closed-loop로 평가되는 policy
- [[OmniDreams]] — real-time closed-loop simulation 제공
- [[AlpaSim]] — closed-loop orchestrator
