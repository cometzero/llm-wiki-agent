---
title: "Embodiment-Aware Prompt Design"
type: concept
tags: [prompt, embodiment, VLA, cross-embodiment]
sources: [qwen-robotnav-2606-18112]
last_updated: 2026-07-01
---

## Summary
Embodiment-aware prompt design is Qwen-RobotNav's approach to representing different robot embodiments (indoor mobile robot, quadruped, autonomous vehicle) via system prompt preamble rather than learned embeddings or separate action heads. Examples: "Imagine you are a robot programmed for navigation tasks" for general robot, or autonomous driving-specific preambles.

## Key Design Choices
- **No learned embeddings**: Uses natural language preamble instead
- **No separate action heads**: Single waypoint head works across embodiments
- **Cross-embodiment transfer**: Same model + different prompts

## Rationale
Different embodiments have different dynamics and safety constraints, but the same waypoint output format (x, y, θ) can be mapped to each embodiment's motor control. The prompt tells the model which embodiment context to assume.

## Connections
- [[Qwen-RobotNav]] — implements via system prompt preamble
- [[VLA]] — general VLA prompt design
- [[AgenticNavigation]] — planner may specify embodiment in prompt
