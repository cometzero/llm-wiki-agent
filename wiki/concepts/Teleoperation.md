---
title: "Teleoperation"
type: concept
tags: [robotics, data-collection, imitation-learning]
sources: [xiaomi-robotics-1-2607-15330]
last_updated: 2026-07-22
---

# Teleoperation

Teleoperation은 사람이 원격 또는 직접 조작 인터페이스로 로봇을 움직여 demonstration trajectory를 수집하는 방식이다. 고품질 robot data를 얻는 표준 방법이지만, 비용과 속도, hardware deployment 제약 때문에 대규모 VLA pre-training corpus를 만들 때 병목이 된다.

## Connections
- [[UMI]] — in-the-wild trajectory 수집 비용을 낮추는 대안적 interface.
- [[CrossEmbodimentLearning]] — 서로 다른 embodiment data를 정렬하는 후속 학습 문제.
