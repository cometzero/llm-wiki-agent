---
title: "Attention"
type: concept
tags: [ml, transformer, representation]
sources: [2026-04-23-day01-ai-ml-learning-review]
last_updated: 2026-04-25
---

[[Attention]]은 query와 key의 관련도를 계산해 value를 가중합하는 메커니즘이다. Day 01의 [[DotProduct]]와 [[Matrix]] 관점이 실제 [[LLM]] 연산으로 이어지는 대표 사례다.

## Connections
- [[DotProduct]] — query-key score 계산의 핵심 연산
- [[Matrix]] — Q/K/V projection과 output projection이 모두 행렬곱으로 구현됨
- [[Embedding]] — token representation이 attention 입력으로 사용됨
- [[LLM]] — transformer 계열 모델의 중심 연산 블록
