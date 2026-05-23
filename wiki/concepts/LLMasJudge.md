---
title: "LLM-as-a-Judge"
type: concept
tags: [ai-ml, evaluation, llm]
sources: [2026-05-23-day30-ai-ml-learning-review, 2026-05-22-day30-ai-ml-learning-review]
last_updated: 2026-05-23
---

## Definition
LLM-as-a-judge는 LLM을 평가자로 활용하여 모델 출력을 평가하는 방법이다. 사람 대신 LLM에게 두 모델의 답변을 비교하게 하거나 답변의 품질을 점수화하게 한다.

## Advantages
- 사람 평가보다 빠름
- 비용이 적음
- 대규모 평가 가능

## Limitations
- LLM 평가자도 편향과 오류가 있음
- 자기 자신의 출력에 대해 유리하게 평가할 수 있음 (self-preference bias)
- 특정 스타일이나 형식을 선호하는 경향
- 중요한 제품에서는 사람 평가와 샘플 검토가 여전히 필요

## Best Practices
- 여러 judge 모델로 교차 검증
- 사람 평가로 judge의 편향 보정
- 평가 기준을 명확하고 구체적으로 지시
- 샘플링 기반 인간 검토 병행

## Connections
- [[Evaluation]] — 평가 방법의 하나
- [[HumanEvaluation]] — 사람 평가와의 비교
- [[Benchmark]] — 자동 평가 프레임워크
