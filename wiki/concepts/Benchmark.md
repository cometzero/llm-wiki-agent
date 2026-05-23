---
title: "Benchmark"
type: concept
tags: [ai-ml, evaluation, benchmarking]
sources: [2026-05-23-day30-ai-ml-learning-review, 2026-05-22-day30-ai-ml-learning-review]
last_updated: 2026-05-23
---

## Definition
벤치마크(benchmark)는 여러 모델을 같은 조건에서 비교하기 위해 만든 데이터셋과 평가 방식의 묶음이다. "공통 시험 문제 + 채점 기준"으로, 한 학생이 학교마다 다른 시험을 보면 실력을 비교하기 어려운 것처럼, AI 모델도 benchmark로 공정하게 비교할 수 있다.

## Key Points
- **Benchmark ≠ 전체 능력**: 평가 점수는 특정 문제 묶음에서의 성능만 보여줌
- **대표성 중요**: benchmark가 실제 사용 상황과 다르면 점수가 높아도 서비스에서는 부적합할 수 있음
- **내부 Eval Set**: 회사들은 공개 benchmark뿐 아니라 자기 서비스에 맞는 내부 eval set을 따로 만듦

## Limitations
1. 실제 사용자의 질문 방식이 benchmark와 다를 수 있음
2. 속도, 비용, 안전성, 환각 등은 점수로 잘 포착되지 않음
3. LLM에서는 정답이 하나로 고정되지 않아 평가가 어려움
4. "벤치마크 점수 1등"보다 "우리 사용자의 실제 문제를 해결하는가"가更重要

## Connections
- [[Evaluation]] — benchmark를 사용하는 평가 과정
- [[HumanEvaluation]] — benchmark 점수 외의 보완 평가
- [[DataDrift]] — 학습 데이터와 실제 서비스 데이터의 분포 차이
