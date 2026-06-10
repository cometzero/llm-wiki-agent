---
title: "Reconstruction Simulator"
type: concept
tags: [autonomous-driving, simulation]
sources: [nvidia-omnidreams-2606-03159-analysis]
last_updated: 2026-06-10
---

# Reconstruction Simulator

기존 장면을 reconstruction하여 sensor prediction을 수행하는 시뮬레이터. OmniDreams가 극복하려는 이전 패러다임.

## Overview
Reconstruction-based simulator는 기록된 scene의 geometry와 appearance를 기반으로 novel view synthesis나 sensor prediction을 수행한다. Photorealistic하지만 기록된 데이터의 범위를 벗어난 novel event와 dynamic interaction을 생성하기 어렵다는 한계가 있다.

## Limitations
1. **Novel event generation 한계**: Pre-recorded scenario 내에서만 동작
2. **Dynamic interaction 부재**: Actor 간의 상호작용이나 policy action에 따른 reaction 미반영
3. **Closed-loop evaluation 불가**: Policy action이 scene에 영향을 주지 않음

## OmniDreams의 대안
OmniDreams는 reconstruction 대신 generation 패러다임을 채택하여:
- Policy action에 조건화된 novel scene generation
- Dynamic interaction simulation
- Closed-loop policy evaluation 가능

## Connections
- [[OmniDreams]] — 대안 제시
- [[ClosedLoopSimulation]] — reconstructed data의 한계
- [[NovelEventGeneration]] — reconstruction의 병목
