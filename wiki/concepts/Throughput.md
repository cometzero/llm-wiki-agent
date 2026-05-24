---
title: "Throughput"
type: concept
tags: [ai-ml, performance, inference]
sources: [2026-05-24-day30-ai-ml-learning-review]
last_updated: 2026-05-24
---

## Definition

[[Throughput]]은 일정 시간 동안 시스템이 처리할 수 있는 요청 수나 token 수이다. "서버가 전체적으로 얼마나 많이 처리하는가"를 나타내며, 단위로 requests/sec 또는 tokens/sec를 사용한다.

## Key Concepts

### Throughput vs Latency
- **[[Latency]]**: 한 사용자의 체감 대기 시간
- **[[Throughput]]**: 시스템 전체의 처리량

[[Batching]]처럼 여러 요청을 묶는 방식은 [[Throughput]]은 높일 수 있지만, 어떤 사용자는 요청이 batch에 묶일 때까지 기다려야 하므로 개별 [[Latency]]는 늘어날 수 있다.

## Connections
- [[Latency]] — 개별 요청 응답 시간
- [[Batching]] — throughput 향상 기법
- [[Serving]] — throughput 관리의 대상

## Practical Notes

예: 1초에 20개 요청 처리 = throughput 20 req/s. LLM에서는 1초에 생성한 token 수(tokens/sec)도 자주 확인.
