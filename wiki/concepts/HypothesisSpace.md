---
title: "Hypothesis Space"
type: concept
tags: [machine-learning, model-selection]
sources: [2026-04-25-day03-ai-ml-learning-review]
last_updated: 2026-04-25
---

# Hypothesis Space

[[HypothesisSpace]]는 머신러닝 모델이 탐색할 수 있는 후보 함수들의 집합이다.

## Core Idea
- 선형모델, tree, neural network, transformer는 서로 다른 hypothesis space를 이룬다.
- 학습은 이 공간 안에서 loss를 가장 잘 줄이는 함수를 찾는 과정이다.

## Connections
- [[FunctionApproximation]] — 함수 근사 문제의 탐색 공간
- [[LossFunction]] — 후보를 비교하는 기준