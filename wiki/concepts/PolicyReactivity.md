---
title: "Policy Reactivity"
type: concept
tags: [autonomous-driving, simulation, evaluation]
sources: [nvidia-omnidreams-2606-03159-analysis]
last_updated: 2026-06-10
---

# Policy Reactivity

Policy action이 simulator state를 바꾸고, generated observation이 이를 반영하는 능력. Closed-loop simulation의 핵심 지표.

## Overview
Policy reactivity는 생성형 시뮬레이터가 policy action에 얼마나 빠르게且정확하게 반응하는지를 측정한다. 이 능력이 부재하면, simulator는 실제로 policy를 평가하지 못하고 pre-recorded scenario만 replay하게 됨.

## Why It Matters
OmniDreams는 "open-loop video quality가 아니라 closed-loop reactivity가 핵심"이라고 강조. Policy가 action을 바꾸면 simulator state가 바뀌어야 하고, generated observation이 이를 반영해야 한다. 이 조건을 만족해야 policy의 장기 roll-out failure를 평가할 수 있다.

## Measurement
- Policy action → state change detection latency
- Generated observation이 state change를 반영하는 정확도
- Long rollout에서 drift累积 정도

## Connections
- [[OmniDreams]] — policy reactivity 실현
- [[ClosedLoopSimulation]] — 요구되는 환경
- [[ExposureBias]] — reactivity 저하 원인
- [[RolloutDrift]] — 장기 reactivity 실패 현상
