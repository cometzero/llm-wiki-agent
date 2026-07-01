---
title: "Object-Centric Observation"
type: concept
tags: [robotics, observation-design, sim-to-real]
sources: [object-centric-residual-rl-vla-enhancement-2606-18953]
last_updated: 2026-07-01
---

## Definition
Visual observation(图像) 대신 task-relevant object의 6-DoF pose, robot proprioception, base action으로 구성된 compact geometric observation space이다.

## Composition
```
s_t = [s_t^obj, s_t^prop, a_t^base]
```

- **s_t^obj**: Object 6-DoF pose (position + orientation) — [[FoundationPose]] + [[SAM2]]로 추정
- **s_t^prop**: Robot proprioception (joint positions, velocities, forces)
- **a_t^base**: Base VLA action (현재 action chunk)

## Key Property
**Simulation-Reality Consistency**: object pose는 rendering gap 없이 sim/reality 모두에서 비교적 동일하게 획득 가능

## Ablation Results
Table 2 (Figure 7参照)에서 observation space 비교:
- Image-based observation: visual domain gap으로 transfer 실패
- Object-centric poses: 가장 효과적으로 transfer

## Connections
- [[ObjectCentricResidualRL]] — 적용 framework
- [[ZeroShotSimToReal]] — 가능한 이유
- [[FoundationPose]] — pose estimation
- [[SAM2]] — segmentation support
