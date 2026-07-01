---
title: "Parameterized Navigation Interface"
type: concept
tags: [navigation, interface, inference-configurable]
sources: [qwen-robotnav-2606-18112]
last_updated: 2026-07-01
---

## Overview
[[ParameterizedNavigationInterface]]는 inference time에 조절 가능한 navigation model의 입력 구조이다. Task mode, token budget, temporal decay, camera weights, frame sampling을 동적으로 설정하여 다양한 navigation task를 단일 모델로 처리한다.

## Parameters
- **Task mode**: instruction following, object search, target tracking, autonomous driving
- **Token budget**: computation budget allocation
- **Temporal decay**: historical frame weighting
- **Camera weights**: multi-view camera importance
- **Frame sampling**: temporal sampling rate

## Connections
- [[QwenRobotNav]] — 핵심 설계
- [[AgenticNavigation]] — upper planner가 parameters 동적 조절
