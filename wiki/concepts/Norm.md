---
title: "Norm"
type: concept
tags: [linear-algebra, optimization]
last_updated: 2026-04-26
sources: [2026-04-23-day01-ai-ml-learning-review]
---

## 핵심 정의
[[Norm]]은 벡터의 크기(길이)를 측정하는 함수로, 0벡터와의 거리 개념을 일반화한다.

## AI/ML 연결
- [[L2Norm]]은 가장 흔히 쓰이는 길이 척도이며 `sqrt(Σx_i^2)`로 계산된다.
- [[Gradient]]의 크기 제어(예: [[GradientNormClipping]])에 직접 쓰인다.
- [[Regularization]]에서 파라미터 크기 제약을 통해 과적합을 억제한다.
- distance(거리) 계산의 기본 요소로도 사용된다.

## 관련 개념
- [[L2Norm]]
- [[GradientNormClipping]]
- [[Regularization]]
- [[Embedding]]
