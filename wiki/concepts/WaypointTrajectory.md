---
title: "Waypoint Trajectory"
type: concept
tags: [action-representation, trajectory, navigation]
sources: [qwen-robotnav-2606-18112]
last_updated: 2026-07-01
---

## Overview
[[WaypointTrajectory]]는 VLA navigation 모델의 action representation 방식이다. K=8개의 waypoint 시퀀스를 출력하며, 각 waypoint는 (x, y, θ) 좌표로 표현된다.

## Properties
- **K=8**: 8개의 waypoint 시퀀스
- **Coordinates**: (x, y, θ) — planar position + heading
- **Controller dependency**: low-level control보다 planner/controller dependency가 남음

## Connections
- [[QwenRobotNav]] — 8-waypoint trajectory regression
- [[VisionLanguageAction]] — action head design
