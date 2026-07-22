---
title: "Qwen3.5-27B"
type: entity
tags: [vlm, auto-labeling, robotics]
sources: [xiaomi-robotics-1-2607-15330]
last_updated: 2026-07-22
---

# Qwen3.5-27B

Qwen3.5-27B는 Xiaomi-Robotics-1 논문에서 UMI trajectory segment의 state transition을 자동 captioning하는 데 사용된 VLM 계열 모델로 언급된다. 이 모델은 gripper와 object의 변화 과정을 자연어로 설명해 [[StateTransitionCaptioning]] supervision을 만든다.

## Connections
- [[Qwen]] — Qwen 모델 계열.
- [[Qwen3-VL]] — Xiaomi-Robotics-1의 observation/language encoder backbone으로 사용된 VLM 계열.
- [[StateTransitionCaptioning]] — trajectory를 language-conditioned action data로 변환하는 절차.
