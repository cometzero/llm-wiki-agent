---
title: "Confidence Gating"
type: concept
tags: [robotics, safety, deployment]
sources: ["object-centric-residual-rl-vla-enhancement-2606-18953"]
last_updated: 2026-07-01
---

## Definition
Confidence gating은 [[PoseEstimation]]이나 [[VLA]] inference confidence가 낮을 때 residual correction을 비활성화하고 fallback하는 safety 기법이다. 특히 incorrect pose에 반응하는 residual이 위험한 상황을 방지한다.

## Importance in This Paper
Residual policy는 작고 빠르지만 pose estimation latency가 병목이 될 수 있고, 잘못된 pose에 반응하면 safety hazard가 된다. 따라서 confidence-based fallback이 필수적이다.

## Connections
- [[ObjectCentricResidualRL]] — applied in
- [[PoseEstimation]] — confidence source
- [[Safety]] — primary concern
- [[VLA]] — base policy
