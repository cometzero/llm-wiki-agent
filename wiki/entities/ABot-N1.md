---
title: "ABot-N1"
type: entity
tags: [visual-navigation, VLA, VLN, foundation-model]
sources: [abot-n1-2607-10383]
last_updated: 2026-07-15
---

## Overview
ABot-N1은 [[VLM]] 기반 slow-fast Visual Language Navigation foundation model로, 다섯 navigation task(point/object/POI/instruction/person-following)를 하나의 goal-conditioned visual-control framework로 통합한다.

## Architecture
- **Slow VLM Reasoner**: CoT reasoning + Pixel goal generation으로 cognition/control decoupling 실현
- **Fast Action Expert**: pixel guidance + text cue를 continuous waypoint로 변환
- **Pixel Goal**: image-space anchor로 semantic reasoning과 executable action 사이의 bridging representation

## Performance
- POI arrival: 77.3%
- Indoor navigation: 95.4% SR
- Outdoor navigation: 92.9% SR

## Related Entities
- [[Qwen-RobotNav]] — similar scalable navigation approach
- [[ABot-N0]] — predecessor
- [[VLA-Corrector]] — adaptive closed-loop control related

## Connections
- Slow planner/route planning ↔ [[VLA]] taxonomy position
- Pixel anchor ↔ [[ActionGrounding]] mechanism
- Fast action expert ↔ [[Waypoint]] generation
