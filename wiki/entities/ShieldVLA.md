---
title: "ShieldVLA"
type: entity
tags: [vla, safety-alignment, hamilton-jacobi, robotics]
sources: [shieldvla-2609-13231-paper-ko, shieldvla-2609-13231-analysis, shieldvla-2609-13231-references, shieldvla-2609-13231-learning]
last_updated: 2026-09-23
---

# ShieldVLA

ShieldVLA는 visual VLA policy를 HJ reachability-inspired safety critic으로 fine-tune하는 safety alignment framework다. Frozen VLM rubric scorer가 만든 safety margin으로 critic을 학습하고, critic의 feasibility score가 task-reward update와 safety recovery update를 gate한다.

## Importance
- VLM semantic score를 action execution과 분리해 deployment latency를 늘리지 않는다.
- navigation·manipulation safety score를 closed-loop CSC/SR로 같이 평가한다.
- [[VLA]]를 안전 policy로 만드는 한 방법이나, learned critic은 physical guarantee가 아니다.

## See also
- [[VLA]]
