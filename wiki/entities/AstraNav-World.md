---
title: "AstraNav-World"
type: entity
tags: [world-model, autonomous-driving, diffusion]
sources: [qwen-robotnav-2606-18112-references]
last_updated: 2026-07-01
---

## Overview
AstraNav-World (2025)는 end-to-end world model로, future visual states와 action sequences를 unified probabilistic framework에서 jointly reason한다. Diffusion-based video generator와 vision-language policy를 통합한다.

## Key Claims
- Diffusion-based video generation + vision-language policy 통합
- Foresight of world evolution과 action unfolding 동시 추론
- Open, dynamic environments에서의 embodied navigation 지원

## Connections
- [[QwenRobotNav]] — world model 계열로 참조
- [[WorldModel]] — unified probabilistic framework
- [[DiffusionModel]] — video generation backbone
