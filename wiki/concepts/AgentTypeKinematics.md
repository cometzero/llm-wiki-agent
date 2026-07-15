---
title: "Agent-Type Kinematics"
type: concept
tags: [kinematics, traffic-agent, physics-constraints]
sources: [flow-erd-2607-06957]
last_updated: 2026-07-15
---

# Agent-Type Kinematics

## Overview
Agent-type kinematics는 traffic simulation에서 vehicle, cyclist, pedestrian 각 유형의 물리적 운동 역학을 구분하여 적용하는 방법. Flow-ERD의 AFM(Agent-Type Aware Flow Matching)에서 핵심 역할을 하며, 생성된 action을 각 agent 유형에 맞는 kinematic constraints로 변환한다.

## Agent Types
1. **Vehicle**: 4轮 운동학,steering angle constraints, 차선 따라가기
2. **Cyclist**: 2轮 운동학,バランス 유지, 더 작은 회전 반경
3. **Pedestrian**: 보행 운동학, 보행 패턴,قف동작 포함

## Purpose
- **Physical plausibility**: 생성된 trajectory가 물리적으로 실행 가능
- **Type-specific constraints**: 각 agent의 고유한 운동학 반영
- **Transition consistency**: flow action → kinematic transition → rollout 파이프라인 일관성

## Connections
- [[FlowERD]] — AFM의 핵심 구성요소
- [[WorldModel]] — 물리 시뮬레이션 레이어
