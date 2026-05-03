---
title: "Maximum Margin"
type: concept
tags:
  - decision-boundary
  - robustness
  - svm
sources:
  - 2026-05-03-day11-ai-ml-learning-review
last_updated: 2026-05-03
---

## Definition
[[MaximumMargin]]는 분류 경계와 각 클래스의 가장 가까운 데이터 간 최소 거리를 가능한 한 크게 만드는 원칙이다.

## Why it matters
- 경계 주변에 여유가 생겨 작은 노이즈나 입력 흔들림에 덜 민감
- [[SupportVectorMachine]]에서 성능의 핵심 안정성 직관 중 하나

## Notes
- 마진이 클수록 분류 강건성(stability)과 generalization 직관이 좋아 보이지만, 실제 적용에서는 허용오차/soft margin가 필요할 수 있다.