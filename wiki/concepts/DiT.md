---
title: "DiT"
type: concept
tags: [diffusion, transformer, robotics, vla]
sources: [xiaomi-robotics-1-2607-15330]
last_updated: 2026-07-22
---

# DiT

DiT(Diffusion Transformer)는 diffusion 또는 flow-matching 방식의 생성 모델에서 denoising/vector-field 예측기를 Transformer로 구현한 구조다. Xiaomi-Robotics-1에서는 [[Qwen3-VL]]이 만든 observation/language context와 robot state를 조건으로 받아 연속 [[ActionChunking|action chunk]]를 생성하는 action branch로 사용된다.

## Connections
- [[DiffusionTransformer]] — 확장 명칭과 같은 개념군.
- [[FlowMatching]] — Xiaomi-Robotics-1의 action generation objective.
- [[Xiaomi-Robotics-1]] — VLM context + DiT action generator를 결합한 VLA 모델.
