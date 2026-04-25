---
title: "Matrix"
type: concept
tags: [linear-algebra, neural-networks]
sources: [2026-04-23-day01-ai-ml-learning-review]
last_updated: 2026-04-25
---

## 핵심 개념
[[Matrix]]는 벡터 집합의 연산을 요약해 표현한 구조이자 [[LinearMap]]의 유한차원 구현이다.

## 핵심 주장
- 행렬을 단순 숫자표로 보지 말고 입력 공간을 출력 공간으로 보내는 변환으로 이해해야 한다.
- [[Rank]]는 변환이 정보 보존을 어느 정도 허용하는지 보여주는 지표다.

## AI/ML 연결
- [[DenseLayer]], [[Projection]], [[Transformer]]의 [[Q]], [[K]], [[V]] 연산은 선형 변환으로 모두 행렬 곱을 사용한다.
- low-rank 근사, [[LoRA]]는 [[Matrix]]의 표현을 제한해 파라미터 효율을 얻는 기법이다.

## 연결 개념
- [[LinearMap]], [[Rank]], [[DotProduct]], [[DenseLayer]], [[Projection]], [[LoRA]]
