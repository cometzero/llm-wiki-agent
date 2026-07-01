---
title: "Agentic Navigation"
type: concept
tags: [navigation, agent, dual-system]
sources: [qwen-robotnav-2606-18112, qwen-robotnav-2606-18112-learning]
last_updated: 2026-07-01
---

# Agentic Navigation

[[AgenticNavigation]] is a dual-system interface approach where a high-level planner calls navigation models with different context strategies per sub-goal.

## Architecture
- **Upper-level planner**: Determines sub-goals, task modes, and context parameters
- **Navigation model (e.g., [[QwenRobotNav]])**: Executes navigation with task-adaptive observation encoding
- **Feedback loop**: Trajectory evidence and compressed summary returned to planner

## Key Features
- Task-adaptive context parameters (B, γ, w_c) per sub-goal
- Hierarchical control with upper planner coordination
- Supports diverse navigation tasks with single scalable model

## Related Concepts
- [[HierarchicalPlanning]]
- [[TaskAdaptiveObservationEncoding]]
- [[DualSystemArchitecture]]
