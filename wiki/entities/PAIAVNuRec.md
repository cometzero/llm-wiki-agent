---
title: "PAI AV NuRec"
type: entity
tags: [dataset, autonomous-driving]
sources: [nvidia-omnidreams-2606-03159]
last_updated: 2026-06-10
---

# PAI AV NuRec

Physical AI Autonomous Vehicles NuRec dataset으로, OmniDreams의 [[WorldActionModel]] 평가에 사용된다.

## WAM Evaluation Results
- Collision: 6.9% → 4.2% (WAM post-training 후)
- Collision_front: 1.0% → 0.9%
- Collision_lateral: 0.6% → 0.4%
- Collision_rear: 5.3% → 3.0%

## Connections
- [[OmniDreams]] — 평가 데이터셋
- [[WorldActionModel]] — 평가 대상
