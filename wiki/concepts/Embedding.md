---
title: "Embedding"
type: concept
tags: [ml, representation, llm]
sources: [2026-04-23-day01-ai-ml-learning-review]
last_updated: 2026-04-25
---

[[Embedding]]은 토큰·문서·개체를 연속 벡터로 매핑한 표현이다. [[VectorSpace]] 위에서 유사도와 변환을 다루기 때문에 [[DotProduct]], [[Norm]], [[CosineSimilarity]]가 모두 직접 연결된다.

## Connections
- [[VectorSpace]] — embedding이 놓이는 기하학적 공간
- [[CosineSimilarity]] — 의미 유사도 비교에 자주 사용되는 척도
- [[Attention]] — token embedding이 attention의 입력 표현이 됨
- [[LLM]] — 언어 모델이 학습하는 대표적인 표현 형식
