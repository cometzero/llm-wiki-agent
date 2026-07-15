---
title: "ABot-N1"
type: entity
tags: [visual-language-navigation, vla, embodied-robotics]
sources: [abot-n1-2607-10383, abot-n1-2607-10383-references]
last_updated: 2026-07-15
---

## Overview
ABot-N1(arXiv:2607.10383)은 slow-fast VLM 아키텍처, pixel goal intermediate representation, continuous waypoint prediction을 통해 VLN(Vision-Language Navigation)을 통합하는 범용 foundation model이다. Point navigation, object navigation, POI arrival, instruction following, person-following을 단일 모델로 지원한다.

## Key Papers
- **Main paper**: [[ABot-N1]] (2607.10383)
- **前身**: [[ABot-N0]]

## Architecture
- **Slow-fast VLM**: Dual-stream vision-language processing
- **Pixel Goal**: Intermediate representation for goal specification
- **Continuous Waypoint**: Direct waypoint prediction for navigation

## Performance
- POI arrival: 77.3%
- Indoor success rate: 95.4%
- Outdoor success rate: 92.9%

## Connections
- [[VLN]] — 연구 분야
- [[VLA]] — foundation model category
- [[Qwen-RobotNav]] — related navigation research
- [[ABot-N0]] — predecessor version
