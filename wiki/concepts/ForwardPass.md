---
title: "ForwardPass"
type: concept
tags: [optimization, neural-networks, training, deep-learning]
last_updated: 2026-05-06
sources: [2026-04-26-day04-ai-ml-learning-review, 2026-05-06-day14-ai-ml-learning-review]
---

## Summary
[[ForwardPass]]는 [[ComputationalGraph]]를 입력에서 출력 방향으로 한 번 순회하면서 각 연산의 값을 계산하는 단계이다. 신경망에서는 입력 텐서가 레이어를 통과해 예측값/로짓/출력까지 도달하는 과정이다.

Day 14 reframes the same idea in neural-network layer terms: each layer often applies an [[AffineTransform]] (`z = Wx + b`) and then an [[ActivationFunction]] to produce a layer output. That output becomes the next layer's input, and the final output is used to compute a [[LossFunction]].

## Key Claims
- [[ForwardPass]]는 추론값(예: [[LLM]]의 로짓, [[LossFunction]] 입력)을 먼저 만든다.
- 역전파 이전에 각 노드의 중간값과 국부 미분에 필요한 정보를 보존한다.
- [[Autograd]]는 [[ForwardPass]]에서 생성한 실행 기록을 바탕으로 [[BackwardPass]]를 자동 구성한다.
- Forward pass is the prerequisite for [[Backpropagation]] because gradients are computed from the loss and intermediate values produced during the forward computation.

## Relation
- [[BackwardPass]] — 역방향으로 [[Gradient]]를 전달하는 대응 단계.
- [[Backpropagation]] — uses forward-pass values to compute gradients.
- [[ComputationalGraph]] — 순전파와 역전파 모두 수행되는 그래프 구조.
- [[AffineTransform]] — common per-layer calculation (`Wx + b`).
- [[ActivationFunction]] — often applied after the affine transform.
- [[LossFunction]] — 보통 forward 결과에서 계산된다.
