---
title: "Vision-Language Co-Training"
type: concept
tags: [training, VLA, reasoning]
sources: [qwen-robotnav-2606-18112]
last_updated: 2026-07-01
---

## Overview
[[VisionLanguageCoTraining]]은 trajectory-only training으로 인한 collapse를 방지하고 language reasoning ability를 유지하기 위한 training 전략이다. Composite loss L = L_traj + λ L_VL을 사용한다.

## Properties
- **Trajectory loss**: waypoint MSE regression
- **Vision-language loss**: language reasoning preservation
- **Effect**: scene understanding과 reasoning ability 동시 유지

## Connections
- [[QwenRobotNav]] — training recipe 핵심
- [[VisionLanguageAction]] — training methodology
