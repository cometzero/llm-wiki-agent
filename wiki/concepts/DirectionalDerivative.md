---
title: "DirectionalDerivative"
type: concept
tags: [optimization, calculus, gradient]
last_updated: 2026-04-26
sources: [2026-04-26-day04-ai-ml-learning-review]
---

## Summary
[[DirectionalDerivative]]는 다변수 함수에서 특정 단위 방향 벡터 \(v\)로 미소하게 이동했을 때 함수값 변화율을 측정하는 값이다. 1차 근사의 형태로 보면 \(D_v f(x)\)는 해당 방향에서의 즉시 변화 속도를 알려준다.

## Key Claims
- [[DirectionalDerivative]]는 점 \(x\)에서 방향 \(v\)로의 변화율을 나타낸다.
- \(\nabla f(x)^T v\) 형태로 표현되며, 여기서 [[Gradient]]는 방향 변화율을 모든 방향에서 동시에 계산할 수 있게 한다.
- 단위 방향 \(\|v\|=1\)에서 최대 변화율은 [[Gradient]]의 크기와 연결되며, [[Optimization]]에서 급경사 방향 판단에 사용된다.

## Relation
- [[Gradient]] — [[DirectionalDerivative]]의 핵심 내부 표현으로, \(\nabla f\)와 \(v\)의 내적으로 나타난다.
- [[ChainRule]] — 여러 층으로 구성된 [[ComputationalGraph]]에서 국소 변화율을 연결할 때 방향 기반 해석에 쓰인다.
- [[GradientDescent]] — 역방향 이동으로 최소화 방향을 찾는다.