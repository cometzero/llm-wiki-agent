---
title: "Prior"
type: concept
tags: [probability, bayes]
last_updated: 2026-04-26
sources: [2026-04-24-day02-ai-ml-learning-review]
---

## Summary
Prior(사전 확률)는 새로운 관측 전, 어떤 가설/클래스가 얼마나 그럴듯한지에 대한 사전 믿음이다.

## Key Claims
- [[Prior]]는 사건/클래스의 초기 확률로, 관측 데이터 이전의 기준값이다.
- [[BayesTheorem]]에서는 관측 가능성인 [[Likelihood]]과 곱해져 [[Posterior]]의 분자에 반영된다.
- 데이터가 많아질수록 사전의 영향은 점차 약해질 수 있으나, 소표본에서는 중요하게 작동한다.

## Connections
- [[BayesTheorem]] — prior-likelihood-posterior의 한 축.
- [[Likelihood]], [[Posterior]] — 사전-우도-사후의 연쇄 구조.
- [[Classification]] — 클래스 사전 빈도/클래스 불균형을 반영.
- [[ConditionalProbability]] — 사전에서 조건부로 이동하는 추론 흐름.

## AI Connections
- [[SpamFiltering]], diagnosis(진단), [[Classification]]에서 클래스 편향/불균형을 반영해 과적합 위험을 줄이는 데 유용한 기준점이다.

## Contradictions
- No explicit contradiction identified.