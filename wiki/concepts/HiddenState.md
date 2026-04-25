---
title: "HiddenState"
type: concept
tags: [ml, llm, sequence-modeling]
sources: [2026-04-23-day01-ai-ml-learning-review]
last_updated: 2026-04-25
---

[[HiddenState]]는 모델이 입력을 처리하며 내부적으로 유지하는 중간 표현 벡터다. [[LLM]]에서는 문맥 정보가 누적된 token-level representation으로 이해할 수 있다.

## Connections
- [[Vector]] — hidden state도 벡터 표현이다
- [[Embedding]] — 초기 입력 표현이 hidden state로 변환됨
- [[Attention]] — hidden state 간 상호작용을 조절함
- [[LLM]] — 문맥을 유지하는 핵심 내부 상태
