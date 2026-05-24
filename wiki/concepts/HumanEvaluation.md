---
title: "Human Evaluation"
type: concept
tags: [ai-ml, evaluation, human-in-the-loop]
sources: [2026-05-24-day30-ai-ml-learning-review]
last_updated: 2026-05-24
---

## Definition

[[HumanEvaluation]]은 사람이 직접 모델 출력을 보고 품질을 평가하는 방식이다. 자동 metric으로 측정하기 어려운 품질 차원(공손함, 과장 여부, 창작 여부 등)을 판단하는 데 필수적이다.

## Key Concepts

### When Human Evaluation is Needed
- "좋은 요약", "친절한 답변", "근거 있는 답변" 등 정답이 하나로 定하지 않는 경우
- LLM의 창의성, 일관성, 안전성 평가
- 자동 metric이 포착하지 못하는 뉘앙스 평가

### Challenges
- 평가자 간 기준 불일치 (inter-rater reliability 문제)
- 비용이 많이 듬
- 명확한 rubric, 다수 평가자, 자동 metric 조합 필요

## Connections
- [[Evaluation]] — 전체 평가 절차의 일부
- [[Benchmark]] — 표준화된 평가의 일부
- [[FeedbackLoop]] — 사용자 피드백이 곧 일종의 human evaluation

## Practical Notes

LLM 고객상담 봇 예시: 공손한지, 과장하지 않았는지, 정책 밖 말을 지어내지 않았는지는 자동 metric만으로 판단 어려워 사람이 직접 평가해야 함.
