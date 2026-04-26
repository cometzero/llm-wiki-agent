---
title: "Likelihood"
type: concept
tags: [probability, bayes]
last_updated: 2026-04-26
sources: [2026-04-24-day02-ai-ml-learning-review]
---

## Summary
Likelihood(우도)는 특정 가설이 주어졌을 때 관측값이 나타날 가능성을 나타내는 값이다.

## Key Claims
- Likelihood는 보통 \(P(x\mid y)\) 형태로 쓰이며, 데이터가 실제로 관측될 생존 가능성에 초점을 둔다.
- [[BayesTheorem]]에서 분자의 핵심 항으로 [[Posterior]] 계산에 기여한다.
- 동일한 관측값이라도 가설별 likelihood 값 비교가 분류 경계와 판단을 바꾼다.

## Connections
- [[BayesTheorem]] — prior와 결합되어 posterior 계산.
- [[Prior]], [[Posterior]] — 베이즈 추론 삼각구조.
- [[ConditionalProbability]] — 조건부 확률 해석의 실무적 변환.
- [[Classification]] — 클래스별 우도 비교의 핵심.

## AI Connections
- 분류 모델에서 클래스별 점수(logits/확률) 해석에 대응.
- [[GenerativeModeling]]에서 데이터-가설 결합 판단에 사용.

## Contradictions
- No explicit contradiction identified.