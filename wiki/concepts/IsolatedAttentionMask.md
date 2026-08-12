---
title: "Isolated Attention Mask"
type: concept
tags:
  - autonomous-driving
  - attention
  - leakage-control
sources:
  - simwam-2608-07468
last_updated: 2026-08-12
---

# Isolated Attention Mask

[[IsolatedAttentionMask]]는 action token이 future frame token을 직접 참조하지 못하게 제한하는 attention 제약이다. [[SimWAM]] 같은 학습-배포 분리형 [[WorldActionModel]]에서, training-time privileged future information이 action branch로 shortcut 형태로 새어 들어가는 것을 막기 위해 사용된다.

## Why it matters
- leakage를 줄여 train-test mismatch를 완화한다.
- action branch가 future video reconstruction에 과의존하지 않도록 만든다.
- inference-time에 video branch를 제거해도 학습된 action representation이 유지되도록 돕는다.

## Connections
- [[SimWAM]]
- [[FlowMatching]]
- [[InferenceTimeActionOnlyDeployment]]
- [[WorldActionModel]]

## Notes
- 이 개념은 일반적인 causal mask보다 더 구체적으로, action/future-video 사이의 정보 흐름만 차단하는 목적에 가깝다.
- 실제 구현에서는 mask unit test로 action token -> future latent 경로가 0인지 확인하는 식으로 검증할 수 있다.
