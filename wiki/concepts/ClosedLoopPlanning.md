---
title: "Closed-Loop Planning"
type: concept
tags: [autonomous-driving, planning, simulation, reinforcement-learning]
sources: [reflectdrive-2-2605-04647-references]
last_updated: 2026-05-13
---

## Overview
Closed-Loop Planning은 시뮬레이션 환경에서 planned trajectory를 실행하고 feedback을 받아 재계획하는 iterative planning 패러다임이다. [[NAVSIM]] 벤치마크를 통해 평가되며, [[ReflectDrive-2]]의 RL alignment와 밀접한 관련이 있다.

## Key Properties
- Environmental feedback 기반 planning refinement
- Safety-critical scenario evaluation
- RL reward signal과 결합 가능

## Connections
- [[ReflectDrive-2]] — RL-aligned closed-loop evaluation
- [[NAVSIM]] — benchmark platform
- [[E2EAutonomousDriving]] — planning domain

## Contradictions
- None identified.
