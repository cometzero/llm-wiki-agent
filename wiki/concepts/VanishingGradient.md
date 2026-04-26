---
title: "VanishingGradient"
type: concept
tags: [optimization, neural-networks, training-stability]
last_updated: 2026-04-26
sources: [2026-04-26-day04-ai-ml-learning-review]
---

## Summary
[[VanishingGradient]]는 깊은 네트워크에서 기울기가 역전파 과정에서 매우 작아져 상위(초기) 계층까지 제대로 전달되지 않는 현상이다. 학습이 느려지거나 정체되는 대표적 문제다.

## Key Claims
- 반복적인 곱셈(또는 소수 값의 연쇄)에서 기울기 크기가 급격히 감소한다.
- 하부 파라미터 업데이트가 미약해져 수렴이 느려질 수 있다.
- 네트워크 구조/정규화/초기화/activation 선택과 [[LearningRate]] 스케줄링으로 완화할 수 있다.

## Relation
- [[ExplodingGradient]] — 반대 성격의 안정성 문제 쌍.
- [[Backpropagation]] — 역전파 시 발생할 수 있는 핵심 병목.
- [[Optimization]] 및 [[GradientDescent]] 성능 튜닝의 핵심 진단 항목.