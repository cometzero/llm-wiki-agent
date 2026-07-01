---
title: "Waypoint Action Head"
type: concept
tags: [action, trajectory, navigation, MLP]
sources: [qwen-robotnav-2606-18112]
last_updated: 2026-07-01
---

## Summary
The waypoint action head is a lightweight 4-layer MLP that maps Qwen3-VL's final hidden state E^A to a sequence of K=8 waypoints, each expressed as (x_k, y_k, θ_k) in 3-DoF format, yielding a 24-dimensional trajectory output.

## Technical Details
- Input: Final LLM hidden state E^A from [[Qwen3-VL]]
- Architecture: 4-layer MLP (lightweight, task-specific head)
- Output: K=8 waypoints × 3 DoF = 24-dimensional trajectory
- Per-dataset scale factor normalizes output to [-1, 1] range
- Training: L = L_traj + λ L_VL where L_traj = ||Ŵ - W*||²₂

## Connections
- [[Qwen-RobotNav]] — the model using this head
- [[Qwen3-VL]] — backbone providing E^A
- [[VLA]] — general VLA action output paradigm
