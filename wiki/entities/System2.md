---
title: "System 2"
type: entity
tags: [control-layer, reasoning]
sources: [introducing-helix-02-full-body-autonomy]
last_updated: 2026-04-16
---

## Summary
[[System2]] is the semantic reasoning layer in the Helix 02 architecture. It interprets scenes and language, then emits latent goals that let lower layers execute multi-step tasks without hand-coding each body movement.

## Key Points
- Handles scene understanding, language grounding, and action sequencing.
- Lets [[Helix02]] scale from simple pick actions to room-scale tasks such as loading and unloading a dishwasher.
- Delegates detailed motion realization to [[System1]] and [[System0]].

## Connections
- [[Helix02]]
- [[System1]]
- [[LocoManipulation]]
- [[VisuomotorControl]]
