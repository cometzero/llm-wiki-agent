---
title: "Context Modeling (Navigation)"
type: concept
tags: [context, observation, navigation, VLA]
sources: [qwen-robotnav-2606-18112]
last_updated: 2026-07-01
---

## Summary
Context modeling is Qwen-RobotNav's reframing of the multi-task navigation problem: diverse navigation tasks (instruction following, object search, target tracking, autonomous driving) share a perception-planning backbone but differ in how they consume the observation stream. Rather than task-specific architectures, the solution is a parameterized context interface controlling token allocation.

## The Problem
Traditional approaches use:
1. Task-specific architectures/heads, OR
2. Fixed observation context for all tasks

Both are suboptimal. Different tasks need different:
- Memory horizons (episode-level for instruction following, frame-level for tracking)
- Observation fidelity (high-res latest frames vs. compressed history)
- Camera importance (front-focused for driving, omnidirectional for search)

## The Solution
Keep the backbone constant; control task behavior via:
- Task mode parameter
- Token allocation parameters (budget, decay, camera weights, sampling)
- Prompt preamble (embodiment)
- Natural-language viewpoint/timestep tags

## Connections
- [[Qwen-RobotNav]] — proposes this reframing
- [[TaskAdaptiveObservationEncoding]] — implements context modeling
- [[AgenticNavigation]] — planner provides context parameters
