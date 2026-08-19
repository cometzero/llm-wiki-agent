---
title: "POMDP"
type: concept
tags:
  - planning
  - decision-making
  - decision-theory
date: 2026-08-19
sources:
  - 360cityarena-2608-08814-learning
last_updated: 2026-08-19
---

## Partially Observable Markov Decision Process (POMDP)

[[POMDP]]는 상태를 직접 볼 수 없는 환경에서 관측($o_t$), 믿음/메모리($M_t$), 행동($a_t$)으로 다음 상태를 추정하고 정책을 결정하는 decision model이다.

### In this source
`360CityArena`에서 `s_t\xrightarrow{render}o_t`, `a_t=\pi(o_t,M_t,g)` 식은 [[ObservationToActionLoop]]와 함께 부분 관측 기반의 route reasoning을 정식화한 예시이다.

### Why it matters for [[EmbodiedNavigation]]
모든 상태가 보이지 않는 AD/VLA 환경에서 one-shot 정답 생성보다 history 유지와 plan update가 중요해진다.