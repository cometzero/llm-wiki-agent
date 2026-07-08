---
title: "Adaptive Action Horizon"
type: concept
tags: [vla, control]
sources: [vla-corrector-2607-01804]
last_updated: 2026-07-08
---

# Adaptive Action Horizon

Adaptive action horizon은 fixed action horizon을 고정하지 않고, drift가 감지될 때 remaining actions를 truncation해 event-triggered로 짧아지는 execution horizon이다.

## Connections
- [[VLA]] — embodied action generation의 공통 기반.
- [[ClosedLoopRobot]] — 실행 중 feedback과 recovery가 중요한 deployment setting.
