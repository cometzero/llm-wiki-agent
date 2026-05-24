---
title: "Evaluation"
type: concept
tags: [ai-ml, evaluation, benchmarking]
sources: [2026-05-24-day30-ai-ml-learning-review]
last_updated: 2026-05-24
---

## Definition

[[Evaluation]]은 AI 모델의 출력이 원하는 기준에 얼마나 맞는지 측정하는 절차이다. 분류, 번역, 요약, 검색, 코딩, 추론, 안전성 등 특정 [[TaskMetric]]을 통해 모델 성능을 정량화한다.

## Key Concepts

### What to Evaluate
- Task type이 평가 기준을 결정한다: 분류, 번역, 요약, 검색, 코딩, 추론, 안전성
- Task metric 예: accuracy, F1, ROUGE, pass@k, win rate

### Data for Evaluation
- 학습 데이터와 분리된 validation set, test set 사용
- 실제 사용자 로그에서 분리한 평가셋 활용
- Data contamination 주의: 평가 데이터가 학습 데이터에 섞이면 점수 부풀림 발생

### Metrics
- **Classification**: accuracy, precision, recall, F1
- **Generation**: exact match, BLEU, ROUGE, pass@k, win rate, human preference
- **LLM-specific**: 자동 metric + [[HumanEvaluation]] 조합 필요

### Interpretation
- [[Benchmark]] 점수가 높다고 실제 제품 성능이 좋은 것은 아님
- 공통 benchmark + private eval + 실제 사용자 feedback loop 조합 권장

## Connections
- [[Benchmark]] — 표준화된 평가 세트
- [[HumanEvaluation]] — 사람이 직접 품질 평가
- [[TaskMetric]] — 특정 작업별 점수 기준
- [[Serving]] — 배포 전 안전성 검증에 활용

## Practical Notes

평가 없이는 "더 큰 모델? fine-tuning? RAG? prompt 변경?" 중 선택이 감에 의존하게 된다. "정확도 3% 상승, latency 2배" 같은 구체적 비교가 가능하려면 체계적 [[Evaluation]]이 필수다.
