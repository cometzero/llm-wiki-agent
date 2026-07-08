---
title: "Open Loop Blind Spot"
type: concept
tags: [vla, control]
sources: [vla-corrector-2607-01804-paper-ko]
last_updated: 2026-07-08
---

# Open Loop Blind Spot

Open-loop blind spot은 action chunk를 실행하는 동안 fresh observation이 들어와도 policy가 horizon 종료까지 이를 사용하지 못하는 구간이다.

## Connections
- [[VLA]] — embodied action generation의 공통 기반.
- [[ClosedLoopRobot]] — 실행 중 feedback과 recovery가 중요한 deployment setting.
