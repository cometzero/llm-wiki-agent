---
title: "Waypoint"
type: concept
tags: [navigation, motion-planning, continuous-control]
sources: [abot-n1-2607-10383, qwen-robotnav-2606-18112]
last_updated: 2026-07-15
---

## Definition
Waypoint는 continuous navigation을 위한 연속 좌표 포인트로, [[Fast Action Expert]]가 [[PixelGoal]]과 text cue를 변환하여 생성한다.

## Role in ABot-N1
Pixel goal (image-space) → Waypoint (continuous 2D/3D coordinate) → Robot navigation controller

## Connection to Autonomous Driving
- Route planning의 상위 수준 intent를 BEV coordinate의 waypoints로 변환
- Trajectory planning의下游 output
- Safety envelope와 calibration 필요

## Related Concepts
- [[PixelGoal]] — upstream input
- [[SlowFastArchitecture]] — generation architecture
- [[ActionGrounding]] — coordinate transformation mechanism
- [[ClosedLoopNavigation]] — waypoint tracking and correction
