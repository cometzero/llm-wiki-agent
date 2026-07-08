---
title: "Online Gradient Guidance"
type: concept
tags: [vla, inference]
sources: [vla-corrector-2607-01804]
last_updated: 2026-07-08
---

# Online Gradient Guidance

Online Gradient Guidance(OGG)는 interrupt 직후 flow-matching velocity를 corrective latent direction으로 guide해 recovery replan을 유도하는 inference-time 방법이다.

## Connections
- [[VLA]] — embodied action generation의 공통 기반.
- [[ClosedLoopRobot]] — 실행 중 feedback과 recovery가 중요한 deployment setting.
