---
title: "ForwardPass"
type: concept
tags: [optimization, neural-networks, training]
last_updated: 2026-04-26
sources: [2026-04-26-day04-ai-ml-learning-review]
---

## Summary
[[ForwardPass]]는 [[ComputationalGraph]]를 입력에서 출력 방향으로 한 번 순회하면서 각 연산의 값을 계산하는 단계이다. 신경망에서는 입력 텐서가 레이어를 통과해 예측값/로짓/출력까지 도달하는 과정이다.

## Key Claims
- [[ForwardPass]]는 추론값(예: [[LLM]]의 로짓, [[LossFunction]] 입력)을 먼저 만든다.
- 역전파 이전에 각 노드의 중간값과 국부 미분에 필요한 정보를 보존한다.
- [[Autograd]]는 [[ForwardPass]]에서 생성한 실행 기록을 바탕으로 [[BackwardPass]]를 자동 구성한다.

## Relation
- [[BackwardPass]] — 역방향으로 [[Gradient]]를 전달하는 대응 단계.
- [[ComputationalGraph]] — 순전파와 역전파 모두 수행되는 그래프 구조.
- [[LossFunction]] — 보통 forward 결과에서 계산된다.