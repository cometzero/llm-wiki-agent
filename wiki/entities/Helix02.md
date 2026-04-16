---
title: "Helix 02"
type: entity
tags: [model, robotics, autonomy]
sources: [introducing-helix-02-full-body-autonomy, figure-03-and-the-future-of-robotics]
last_updated: 2026-04-16
---

## Summary
[[Helix02]] is Figure's full-body autonomy model for humanoid robots. The corpus presents it as a learned architecture that ties together semantic reasoning, visuomotor policy generation, and high-frequency whole-body control so a robot can walk, manipulate objects, balance, and recover continuously.

## Key Points
- Targets integrated [[LocoManipulation]] rather than separate walking and manipulation pipelines.
- Uses [[System2]] for semantic task reasoning, [[System1]] for full-body action generation, and [[System0]] for physical stabilization and execution.
- Gains dexterity from tactile sensing and palm-camera feedback on [[Figure03]].

## Connections
- [[FigureAI]]
- [[Figure03]]
- [[System0]]
- [[System1]]
- [[System2]]
- [[LocoManipulation]]
- [[VisuomotorControl]]
