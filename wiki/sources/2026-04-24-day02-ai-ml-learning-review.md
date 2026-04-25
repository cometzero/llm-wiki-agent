---
title: "2026-04-24 AI/ML Learning Day 02"
type: source
tags: [diary, ai-ml-learning, probability, statistics]
date: 2026-04-24
source_file: raw/2026-04-24-day02-ai-ml-learning-review.md
last_updated: 2026-04-25
sources: [2026-04-24-day02-ai-ml-learning-review]
---

## Summary
Day 02는 LLM/AI 학습을 위해 [[Probability]]와 [[Statistics]] 기초를 정리한 기록이다.
확률표현의 핵심 단위는 [[RandomVariable]]이고, 분포는 [[PMF]], [[PDF]], [[CDF]]로 구분해 쓰며, 이 관계가 이산/연속 모델링의 선택과 계산 방식에 직접 연결됨을 정리한다.
또한 [[Expectation]], [[Variance]], [[Covariance]], [[Correlation]]을 통해 분포의 중심, 산포, 공동변동을 구조적으로 요약하고, [[ConditionalProbability]]와 [[BayesTheorem]]을 통해 새 정보 반영 시 [[Prior]], [[Likelihood]], [[Posterior]]가 어떻게 바뀌는지 정리한다.

## Key Claims
- [[RandomVariable]]는 불확실한 실험 결과를 수치로 대응시키는 함수이며, [[ProbabilityDistribution]]는 그 결과값의 확률 구조를 기술한다.
- [[PMF]]는 [[Discrete]] 변수에서 값별 확률 질량을, [[PDF]]는 [[Continuous]] 변수에서 밀도를, [[CDF]]는 누적확률을 제공하며, 누적-미분 관계로 연결된다.
- [[Expectation]]은 분포의 평균적 위치, [[Variance]]는 중심 주변 퍼짐, [[Covariance]]는 두 변수의 공동 변화, [[Correlation]]은 단위 무관 관계 강도 지표를 제공한다.
- [[ConditionalProbability]]는 추가 정보가 주어졌을 때 확률을 재평가하는 방법이며, [[BayesTheorem]]은 이를 [[Prior]], [[Likelihood]], [[Posterior]]의 곱셈/정규화 형태로 명시화한다.
- [[BayesTheorem]] 기반은 [[Classification]], [[Calibration]], [[SpamFiltering]] 같은 ML 태스크에서 직관적으로 사후판단을 구성한다.

## Key Quotes
i) "PMF: 이산(discrete) 확률변수에서 각 값의 확률을 나타낼 때 사용"  — 분포 표기 방식의 범주화

ii) "CDF: 이산/연속 모두에서 어떤 값 이하일 누적확률" — 누적 관점의 통일성

iii) "Bayes theorem은 posterior를 P(x|y)P(y)에 비례하는 값으로 표현" — 추론 갱신의 핵심 형태

## Connections
- [[MachineLearning]] — 확률 변수 모델링을 통해 추론 기준을 정량화하는 기반 축.
- [[RandomVariable]]와 [[ProbabilityDistribution]] — Day 01의 [[VectorSpace]]/[[Embedding]] 계열 기하학적 관점이 확률적 불확실성 모델로 확장됨.
- [[PMF]], [[PDF]], [[CDF]] — 데이터/모델의 출력 분포를 기술하는 3형태 표현.
- [[Expectation]], [[Variance]], [[Covariance]], [[Correlation]] — 분포의 중심, 퍼짐, 공동변동, 스케일 독립 관계 강도 지표군.
- [[ConditionalProbability]]와 [[BayesTheorem]] — 사후추론 프레임워크의 핵심.
- [[Prior]], [[Likelihood]], [[Posterior]] — [[Classification]]·진단·분류기의 판단 업데이트 구조.
- [[GaussianModeling]], [[Sampling]], [[GenerativeModeling]], [[PCA]], [[FeatureAnalysis]] — 분포 기반 정규화와 생성, 분석 태스크와 직접 연결.

## Contradictions
- No explicit contradiction with existing wiki pages was identified during this ingest pass.