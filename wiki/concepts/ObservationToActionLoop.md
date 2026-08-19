---
title: "ObservationToActionLoop"
type: concept
tags:
  - embodied-loop
  - perception
  - memory
  - planning
  - action

date: 2026-08-19
sources:
  - 360cityarena-2608-08814-learning
last_updated: 2026-08-19
---

## Observation → Action Loop

## Definition
`ObservationToActionLoop`은 observation과 메모리 상태가 다음 행동 선택에 반영되고, 그 결과가 다음 관측을 바꾸는 반복 구조이다.

### In this source
`360CityArena` 학습 노트에서 핵심 루프는 다음으로 정리된다.

$$o_t, M_t \rightarrow a_t \rightarrow s_{t+1}, o_{t+1} \rightarrow ...$$

### Components
- Perception 입력 (`o_t`)
- Memory 통합 (`M_t`)
- Planner/Policy (`\pi`)
- Actuation (`a_t`)
- State transition / 다음 관측

### Why this matters
VLA/AD에서 route reasoning 실패는 보통 single-shot reasoning이 아니라 loop 단계에서 반복되는 state estimation과 uncertainty accumulation에서 기인한다.