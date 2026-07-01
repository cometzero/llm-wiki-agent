---
title: "Qwen-RobotNav"
type: entity
tags: [navigation-model, VLA, autonomous-driving]
sources: [qwen-robotnav-2606-18112, qwen-robotnav-2606-18112-learning]
last_updated: 2026-07-01
---

# Qwen-RobotNav

[[QwenRobotNav]] is a scalable navigation model based on [[Qwen3VL]] that achieves VLN-CE 76.5% and NAVSIM 91.4 PDMS using task-adaptive observation encoding.

## Key Characteristics
- Vision-language navigation model with 8-step waypoint trajectory output
- Task-adaptive token allocation based on task mode and context parameters (B, γ, w_c)
- Supports multi-view camera input with learnable camera weights
- Dual-system interface with upper-level planner for hierarchical control
- MLP action head for action grounding

## Architecture
- Vision encoder with natural-language viewpoint/time tags
- [[Qwen3VL]] LLM backbone
- MLP action head outputting waypoint trajectories
- Temporal decay mechanism for observation history

## Connections
- Part of [[AgenticNavigation]] dual-system framework
- Uses [[NAVSIM]] for closed-loop evaluation
- Related to [[ABot-N0]] for embodied navigation foundation models
