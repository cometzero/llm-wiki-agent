---
title: "Cross-Entropy"
type: concept
tags: [loss, classification, llm]
sources: [2026-04-27-day05-ai-ml-learning-review]
last_updated: 2026-04-27
---

## Summary
Cross-Entropy는 정답 분포와 모델이 예측한 확률 분포 사이의 차이를 재는 대표적인 분류 손실이다. [[LLM]]의 다음 토큰 예측 학습에서도 핵심 손실로 쓰인다.

## Key Claims
- [[Classification]]과 언어모델 학습에서 가장 흔한 [[LossFunction]] 중 하나다.
- 정답에 높은 확률을 줄수록 손실이 작아진다.
- softmax 출력과 함께 쓰이며 [[SurrogateLoss]]의 대표적 예시다.

## Connections
- [[LossFunction]], [[Classification]], [[LLM]], [[SurrogateLoss]], [[EmpiricalRisk]]
