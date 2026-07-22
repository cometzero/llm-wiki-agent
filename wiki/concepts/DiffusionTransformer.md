---
title: "Diffusion Transformer"
type: concept
tags: [diffusion, transformer, action-generation, vla]
sources: [xiaomi-robotics-1-2607-15330]
last_updated: 2026-07-22
---

# Diffusion Transformer

Diffusion Transformer는 diffusion/flow-matching 기반 생성 과정을 Transformer backbone으로 모델링하는 구조다. 로보틱스 VLA에서는 이미지나 텍스트를 생성하는 대신, noisy action sequence에서 실행 가능한 연속 action chunk로 가는 방향을 학습하는 데 쓰일 수 있다.

## Connections
- [[DiT]] — 약칭.
- [[DiffusionPolicy]] — action distribution을 generative model로 다루는 선행 흐름.
- [[FlowMatching]] — Xiaomi-Robotics-1의 action chunk 학습 손실.
- [[ActionChunking]] — 생성 대상이 되는 연속 action block 표현.
