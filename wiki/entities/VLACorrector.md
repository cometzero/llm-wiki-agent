---
title: "VLA-Corrector"
type: entity
tags: [vla, robotics]
sources: [vla-corrector-2607-01804, vla-corrector-2607-01804-paper-ko, vla-corrector-2607-01804-learning]
last_updated: 2026-07-08
---

# VLA-Corrector

VLA-Corrector는 action-chunked VLA policy에 Latent-space Vision Monitor, event-triggered truncation, Online Gradient Guidance를 붙여 adaptive action horizon을 구현하는 framework다.

## Connections
- [[VLA]] — embodied action generation의 공통 기반.
- [[ClosedLoopRobot]] — 실행 중 feedback과 recovery가 중요한 deployment setting.
