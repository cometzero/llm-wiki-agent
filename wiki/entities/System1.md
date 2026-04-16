---
title: "System 1"
type: entity
tags: [control-layer, robotics]
sources: [introducing-helix-02-full-body-autonomy]
last_updated: 2026-04-16
---

## Summary
[[System1]] is the fast visuomotor layer in the Helix 02 stack. It consumes camera, tactile, and proprioceptive inputs and outputs full-body joint targets that translate semantic intent into coordinated motion.

## Key Points
- Expands earlier upper-body control into all-sensor, all-actuator full-body control.
- Depends on palm cameras and fingertip sensors for dexterous manipulation under occlusion.
- Feeds target motions to [[System0]] while being guided by higher-level latents from [[System2]].

## Connections
- [[Helix02]]
- [[System0]]
- [[System2]]
- [[TactileSensing]]
- [[VisuomotorControl]]
