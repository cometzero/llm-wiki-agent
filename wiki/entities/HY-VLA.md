---
title: "HY-VLA"
type: entity
tags: [VLA, robot-model]
sources: [embodied-cpp-2607-02501]
last_updated: 2026-07-08
---

## Overview
HY-VLA는 Embodied.cpp에서 평가된 VLA(Vision-Language-Action) 모델로, C++ deployment 환경에서 100.0% success rate를 달성했다. RoboTwin place_empty_cup 벤치마크에서 6850 MiB VRAM을 사용한다.

## Key Properties
- **Type**: Vision-Language-Action model (VLA)
- **Deployment**: C++ runtime via [[EmbodiedCpp]]
- **Success Rate**: 100.0% (RoboTwin place_empty_cup)
- **VRAM**: 6850 MiB

## Connections
- [[VLA]] — model category
- [[EmbodiedCpp]] — deployment runtime
- [[π0.5]] — comparative deployment target
