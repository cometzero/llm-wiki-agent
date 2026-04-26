---
title: "Posterior"
type: concept
tags: [probability, bayes]
last_updated: 2026-04-26
sources: [2026-04-24-day02-ai-ml-learning-review]
---

## Summary
Posterior(사후확률)는 관측 데이터가 주어진 후, 어떤 가설/클래스가 더 타당한지의 갱신된 확률이다.

## Key Claims
- Posterior는 [[Prior]]와 [[Likelihood]]를 결합해 얻는다: \(P(y\mid x)\propto P(x\mid y)P(y)\).
- 베이즈 업데이트의 결과로, 데이터 반영 후의 최종 판단 근거가 된다.
- ML 분류에서는 최종 클래스 판단 확률로 해석하는 것이 일반적이다.

## Connections
- [[BayesTheorem]] — posterior가 최종 산물.
- [[Prior]], [[Likelihood]] — posterior를 만드는 입력 항.
- [[ConditionalProbability]] — 사전-사후의 조건부 확률 해석 틀.
- [[Classification]] — 클래스 예측 확률의 핵심 대상.

## AI Connections
- [[SpamFiltering]] 및 진단 분류에서 입력별 클래스 신뢰도로 직결되는 값.
- calibration과도 연동되어 예측 신뢰도를 점검한다.

## Contradictions
- No explicit contradiction identified.