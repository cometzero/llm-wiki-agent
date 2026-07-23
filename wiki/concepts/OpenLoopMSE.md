---
title: "Open-loop MSE"
type: concept
tags: [evaluation, robotics, imitation-learning]
sources: [xiaomi-robotics-1-2607-15330]
last_updated: 2026-07-22
---

# Open-loop MSE

Open-loop MSE는 policy가 예측한 action과 dataset의 ground-truth action 사이 평균제곱오차를 측정하는 imitation-learning 평가 지표다. 환경 feedback이나 recovery behavior는 직접 반영하지 않으므로, 로보틱스와 자율주행에서는 [[ClosedLoopEvaluation]]과 함께 해석해야 한다.

## Connections
- [[ActionChunking]] — action chunk 예측 품질을 측정할 때 쓰일 수 있다.
- [[Xiaomi-Robotics-1]] — pre-training validation action error로 MSE를 보고한다.
