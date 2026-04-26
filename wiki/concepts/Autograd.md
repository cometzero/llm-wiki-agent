---
title: "Autograd"
type: concept
tags: [machine-learning, software-engineering, optimization]
last_updated: 2026-04-26
sources: [2026-04-26-day04-ai-ml-learning-review]
---

## Summary
[[Autograd]]는 계산 그래프 위에서의 자동 미분 시스템으로, 사용자가 직접 도함수를 전개하지 않아도 [[Backpropagation]]에 필요한 기울기를 계산해 준다. 큰 모델 학습에서 실무 필수 인프라다.

## Key Claims
- 연산을 기록하고 역방향으로 미분을 전파해 [[Gradient]]를 계산한다.
- [[ForwardPass]]와 [[BackwardPass]]의 결합으로 구현되며, 복잡한 [[Transformer]] 블록도 구성 단위로 미분 가능하게 만든다.
- 학습자에게는 계산 효율성과 구현 단순화를 동시에 제공한다.

## Relation
- [[ComputationalGraph]] — [[Autograd]]가 추적하는 실행 구조.
- [[ChainRule]] — 내부 역전파 규칙.
- [[Backpropagation]] — 계산 그래프 기반 미분 전파의 구체적 동작.
- [[Optimization]] — [[GradientDescent]] 파이프라인의 기반 엔진.