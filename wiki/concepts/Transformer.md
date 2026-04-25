---
title: "Transformer"
type: concept
tags: [ml, llm, architecture]
sources: [2026-04-23-day01-ai-ml-learning-review]
last_updated: 2026-04-25
---

[[Transformer]]는 self-attention과 feed-forward block을 쌓아 시퀀스를 처리하는 현대 LLM의 대표 구조다. Day 01의 [[Attention]], [[Embedding]], [[Matrix]] 해석이 이 구조를 이해하는 기반이 된다.

## Connections
- [[Attention]] — transformer의 핵심 연산
- [[Embedding]] — 입력 토큰의 초기 표현
- [[DenseLayer]] — attention 이후 표현을 비선형적으로 변환함
- [[LLM]] — transformer 계열이 현재 언어 모델의 표준 아키텍처
