---
title: "THAW-VLA"
type: entity
tags: [vla, world-model, representation-distillation, robotics]
sources: [thaw-vla-2609-24682-paper-ko, thaw-vla-2609-24682-analysis, thaw-vla-2609-24682-references, thaw-vla-2609-24682-learning]
last_updated: 2026-09-23
---

# THAW-VLA

THAW-VLA는 frozen world model의 cached hidden representation을 VLA student에 align해 physical/dynamics prior를 증류하고, deployed policy에서는 teacher와 projector를 제거하는 compact robot-policy method다.

## Importance
- future generation을 control loop에서 제거해 base VLA latency를 유지한다.
- [[WorldActionModel]]의 predictive representation과 VLA action policy 사이의 transfer 설계다.
- representation gain은 long-horizon planning 또는 safety guarantee를 의미하지 않는다.

## See also
- [[WorldActionModel]]
