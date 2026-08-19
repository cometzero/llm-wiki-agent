---
title: "ReflectionMemory"
type: concept
tags:
  - memory
  - uncertainty
  - route-planning
  - calibration

date: 2026-08-19
sources:
  - 360cityarena-2608-08814-learning
last_updated: 2026-08-19
---

## ReflectionMemory

## Definition
[[ReflectionMemory]]는 기존 관측/가설/근거를 기록해 다음 판단의 근거가 되도록 정리한 메모리 뷰이다.

### In this source
`360CityArena` 학습 노트에서 `M_t`는 place recognition, heading 가설, evidence 정합, 실패 사유를 누적하는 용도로 등장한다.

### Practical use
- 같은 위치/목표 재방문 시 오인식 누적을 줄이기 위한 evidence 기반 gate 역할
- planner가 중복 루프/정체를 감지하는 보조 상태로 활용