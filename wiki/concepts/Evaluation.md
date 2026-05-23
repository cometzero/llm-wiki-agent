---
title: "Evaluation"
type: concept
tags: [ai-ml, evaluation, benchmarking]
sources: [2026-05-23-day30-ai-ml-learning-review, 2026-05-22-day30-ai-ml-learning-review]
last_updated: 2026-05-23
---

## Definition
평가(evaluation)는 모델의 답이 얼마나 좋은지 측정하는 과정이다. 번역, 분류, 질의응답, 코딩, 수학 문제 풀이 등 다양한 task에서 모델 출력을 정답이나 기준과 비교하여 성능을 정량화한다.

## Key Points
- **Task Metric**: accuracy, F1, BLEU, ROUGE, pass@k, win rate 등 task별 측정 지표
- **Human Evaluation**: 사람이 직접 모델 출력을 평가하는 방식
- **LLM-as-a-Judge**: LLM을 평가자로 활용하지만 편향이 있을 수 있음
- **Evaluation Structure**: task 정의 → 데이터 준비 → 기준 설정 → 출력 수집 → 자동/사람 평가 → 오류 분석

## Evaluation vs Benchmark
- **Eval**: 모델 성능을 측정하는 과정
- **Benchmark**: 여러 모델을 같은 조건에서 비교하기 위한 공통 시험 세트

## Common Metrics
| Metric | Description |
|--------|-------------|
| Accuracy | 전체 중 맞힌 비율 |
| Precision | 모델이 맞다고 한 것 중 실제 맞은 비율 |
| Recall | 실제 정답 중 모델이 찾아낸 비율 |
| F1 | Precision과 Recall의调和平均 |
| BLEU | 번역 품질 측정 (n-gram overlap) |
| ROUGE | 요약 품질 측정 (n-gram recall) |
| pass@k | k개 샘플 중 하나라도 정답이면 성공 |
| Win Rate | 두 모델 비교 시 한쪽이 더 낫다고 선택된 비율 |

## Connections
- [[Benchmark]] — 평가에 사용하는 공통 시험 프레임워크
- [[HumanEvaluation]] — 사람 기반 평가 방식
- [[LLMasJudge]] — LLM 평가자 활용
- [[DataPipeline]] — 평가 데이터의 출처
- [[FeedbackLoop]] — 평가 결과가 개선에 반영되는 구조
