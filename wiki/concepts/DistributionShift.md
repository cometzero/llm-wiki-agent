---
title: "DistributionShift"
type: concept
tags: [ai-ml-learning]
sources:
  - 2026-04-29-day07-ai-ml-learning-review
last_updated: 2026-04-29
---

## Summary
[[DistributionShift]]는 학습 데이터 분포와 실제 운영 데이터 분포가 달라지는 상황을 말한다. 성능 추정이 실제와 엇갈릴 수 있다.

## Key Points
- 조명, 사용자군, 시간 구간, 문서 스타일 변화가 shift 원인이 된다.
- train/test split만으로는 커버하지 못하는 환경 차이가 있을 수 있다.
- [[Generalization]]이 낮거나 불안정한 시스템은 분포 이동에 취약하다.

## Connections
- [[Generalization]]
- [[TestSet]]
- [[GeneralizationGap]]
- [[DataLeakage]]
- [[LLM]]
