---
title: "System 0"
type: entity
tags: [control-layer, robotics]
sources: [introducing-helix-02-full-body-autonomy]
last_updated: 2026-04-16
---

## Summary
[[System0]] is the lowest-level layer in the Helix 02 stack. It is described as a learned whole-body controller running at 1 kHz that stabilizes contact, posture, balance, and execution using human-motion data and sim-to-real reinforcement learning.

## Key Points
- Replaces large amounts of hand-written control code with a learned neural prior for movement.
- Tracks whole-body commands from [[System1]] while keeping execution smooth and stable.
- Anchors the physical side of [[VisuomotorControl]] in the Helix architecture.

## Connections
- [[Helix02]]
- [[System1]]
- [[LocoManipulation]]
- [[HumanoidRobotics]]
