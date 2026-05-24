---
title: "Benchmark"
type: concept
tags: [ai-ml, evaluation, benchmarking]
sources: [2026-05-24-day30-ai-ml-learning-review]
last_updated: 2026-05-24
---

## Definition

[[Benchmark]]는 미리 정해진 데이터셋, 문제 형식, 채점 기준을 묶어 놓은 평가 세트이다. 여러 모델을 같은 조건에서 비교하기 위한 "공통 시험장" 역할을 한다.

## Key Concepts

### Why Benchmarks Matter
- 수능처럼 모두가 같은 문제를 풀어야 점수 비교 가능
- "모델 A가 모델 B보다 어떤 작업에서 더 낫다"를 정량적으로 판단

### Benchmark Limitations
- [[Benchmark]] 점수가 높으면 실제 업무 능력이 좋은 것은 아님
- 시험 성적 vs 실제 업무 수행 능력 비유와 동일
- Data contamination: 평가 문제가 학습 데이터에 섞여 점수 부풀림
- [[Benchmark]] 데이터가 오래되어 모델이 이미 유사 문제 학습 가능

### Best Practices
- 공개 [[Benchmark]] + private eval + [[HumanEvaluation]] 조합
- "답이 정확한가", "근거 문서 따르는가", "hallucination 줄었는가" 동시 평가
- 사용자 만족도, 안전성, 응답 속도, 비용도 함께考量

## Connections
- [[Evaluation]] — 벤치마크를 포함하는 평가 절차
- [[HumanEvaluation]] — 벤치마크alone으로는 부족한 품질 판단
- [[DataPipeline]] — 평가 데이터 준비

## Practical Notes

LLM 시대에는 답이 하나의 정답으로 딱 떨어지지 않는 경우가 많다. "좋은 요약", "친절한 답변", "근거 있는 답변"은 자동 metric만으로 판단 어려워 [[HumanEvaluation]] 필수.
