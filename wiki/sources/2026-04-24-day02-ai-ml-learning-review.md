---
title: "2026-04-24 AI/ML Learning Day 02"
type: source
tags: [diary, ai-ml-learning, probability, statistics]
date: 2026-04-24
last_updated: 2026-04-26
source_file: raw/ai_ml_learning/2026-04-24-day02-ai-ml-learning-review.md
sources: [2026-04-24-day02-ai-ml-learning-review]
---

## Summary
Day 02는 AI/ML 학습 30일 플랜에서 확률의 기초를 정리한 복습 기록이다. 핵심은 불확실성을 숫자로 다루는 [[RandomVariable]]와 이를 표현하는 [[ProbabilityDistribution]]이며, 이산/연속 구분에 따라 [[PMF]], [[PDF]], [[CDF]]를 구분해 사용한다. 이어서 분포의 요약 통계로 [[Expectation]], [[Variance]], [[Covariance]], [[Correlation]]의 역할을 정리하고, 새로운 정보 반영 규칙인 [[ConditionalProbability]]와 [[BayesTheorem]]을 통해 [[Prior]], [[Likelihood]], [[Posterior]]의 업데이트 구조를 다룬다. 마지막으로 [[Classification]]과 [[SpamFiltering]] 같은 ML 문제에서 사후 확률 관점의 직관을 연결한다.

## Key Claims
- [[RandomVariable]]는 불확실한 실험 결과를 숫자화하는 수단이며, [[ProbabilityDistribution]]은 그 결과가 나타날 확률 구조를 기술한다.
- 이산 변수는 [[PMF]]로, 연속 변수는 [[PDF]]로 각 값(또는 구간)에 대한 확률 질량/밀도를 표현하고, 누적확률은 [[CDF]]로 계산한다.
- [[Discrete]]와 [[Continuous]]의 구분은 모델링 방식과 계산(합/적분) 선택을 바꾼다.
- [[Expectation]]은 분포 중심, [[Variance]]는 퍼짐, [[Covariance]]는 두 변수의 공동변화, [[Correlation]]은 단위 영향을 제거해 비교 가능한 관계 강도를 제공한다.
- [[ConditionalProbability]]는 추가 정보가 들어왔을 때 확률이 어떻게 재평가되는지 설명하며, [[BayesTheorem]]은 이를 [[Prior]], [[Likelihood]], [[Posterior]]의 조합으로 정식화한다.
- 분류 문제에서는 궁극적으로 입력 `x`가 주어졌을 때 클래스 `y`의 사후확률 [[Posterior]]를 잘 추정하는 것이 목표가 된다.

## Key Quotes
> "확률변수는 **불확실한 결과를 숫자로 표현하는 방법**이고, 확률분포는 **그 숫자들이 얼마나 자주 나오는지 설명하는 규칙**이다."

> "PMF: 이산(discrete) 확률변수에서 각 값의 확률을 나타낼 때 사용."

> "Bayes theorem은 prior와 likelihood의 곱을 정규화해 posterior를 계산한다."

## Connections
- [[RandomVariable]] — day02의 출발점이 되는 핵심 개념
- [[ProbabilityDistribution]] — 결과값 공간의 확률 구조
- [[PMF]] / [[PDF]] / [[CDF]] — 분포를 계산할 때 이산/연속 방식 구분
- [[Expectation]] — 모델 출력의 평균적 중심
- [[Variance]] — 평균 주변 퍼짐을 통한 안정성/변동성 요약
- [[Covariance]] — 두 변수의 동시변화량
- [[Correlation]] — 공분산의 스케일 정규화 버전
- [[ConditionalProbability]] — 정보 반영형 확률 추론의 출발점
- [[BayesTheorem]] — 추론 업데이트의 핵심 정체성
- [[Prior]], [[Likelihood]], [[Posterior]] — 분류기에서의 사전/가능도/사후 프레임
- [[Probability]] — 전체 확률적 사고의 상위 프레임
- [[Statistics]] — 분포 요약과 측도로 학습 안정성·모델 분석에 기여
- [[Classification]] — posterior 기반 결정 규칙으로 연결
- [[SpamFiltering]] — 조건부확률/Bayes 직관의 전형적 응용
- [[GaussianModeling]] — 분포 기반 가정이 가능한 경우의 모델링 축
- [[PCA]] — 분산 구조 해석의 선형 확장축으로 연결

## Contradictions
- No explicit contradiction with existing wiki pages was identified during this ingest pass.