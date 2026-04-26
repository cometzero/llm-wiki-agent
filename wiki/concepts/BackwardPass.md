---
title: "BackwardPass"
type: concept
tags: [optimization, neural-networks, training]
last_updated: 2026-04-26
sources: [2026-04-26-day04-ai-ml-learning-review]
---

## Summary
[[BackwardPass]]는 [[ComputationalGraph]]에서 출력에서 입력 방향으로 기울기를 전달하는 단계로, 각 연산의 기여도를 [[ChainRule]]로 연결해 입력/파라미터 민감도를 계산한다. 실전에서는 [[Backpropagation]]의 핵심 엔진이다.

## Key Claims
- [[BackwardPass]]는 출력 쪽부터 시작해 각 노드의 \(\frac{\partial L}{\partial x}\)를 누적한다.
- 각 단계에서 upstream gradient와 local gradient를 곱해 이전 노드로 전달한다.
- 계산 그래프가 깊어져도 각 노드 분할 덕분에 전체 미분 계산이 선형 복잡도로 관리된다.

## Relation
- [[Backpropagation]] — [[BackwardPass]]를 네트워크 전체에 반복 적용한 알고리즘.
- [[GradientDescent]] — [[BackwardPass]] 산출값으로 [[LearningRate]]를 곱해 parameters를 갱신한다.
- [[Autograd]] — [[BackwardPass]] 자동화의 소프트웨어 실무 구현.