---
title: "Sigmoid"
type: concept
tags:
  - activation
  - probability
  - classification
sources:
  - 2026-05-02-day10-ai-ml-learning-review
last_updated: 2026-05-02
---

## Summary
Sigmoid는 실수 전영역 값을 `0`에서 `1` 사이 값으로 압축하는 S자 활성화 함수이다.

로지스틱 회귀와 이진 분류에서 raw score를 확률적 점수로 바꾸는 표준 변환이다.

## Formula
`\sigma(z)=1/(1+e^{-z})`

## Key Claims
- 입력이 큰 음수면 0에 가깝고, 큰 양수면 1에 가깝다.
- `z=0`에서는 0.5가 된다.
- 경계 판단은 종종 `\sigma(z) >= 0.5` 규칙으로 수행된다.

## Connections
- [[Logit]]: sigmoid 이전 점수.
- [[LogisticRegression]]: 핵심 확률 변환 단계.
- [[BinaryClassification]]: 분류 확률 산출.
- [[CrossEntropy]]: 확률형 손실과 결합.
