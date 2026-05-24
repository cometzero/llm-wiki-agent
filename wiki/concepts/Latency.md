---
title: "Latency"
type: concept
tags: [ai-ml, performance, inference]
sources: [2026-05-24-day30-ai-ml-learning-review]
last_updated: 2026-05-24
---

## Definition

[[Latency]]는 요청 하나가 들어와서 답이 나올 때까지 걸리는 시간이다. 사용자가 체감하는 "대기 시간"이며, "내 질문 하나가 얼마나 빨리 끝나는가"를 나타낸다.

## Key Concepts

### Latency vs Throughput
- **[[Latency]]**: 한 사용자의 체감 대기 시간 (예: 0.8초)
- **[[Throughput]]**: 서버 전체의 처리량 (예: 20 requests/sec)

두 개념은 다르다: 어떤 최적화는 [[Throughput]]은 높이지만 개별 [[Latency]]는 늘릴 수 있다.

### Key Metrics
- **p95 latency**: 요청의 95%가 완료되는 시간 (예: p95 latency 3초 = 요청 95%가 3초 내 완료)
- 평균 latency보다 분포 확인이 중요: 평균 1초여도 5%가 10초 대기하면 사용자 경험 저하

## Connections
- [[Throughput]] — 시스템 전체 처리량
- [[Serving]] — latency 관리의 대상
- [[InferenceOptimization]] — latency 최적화 기법

## Practical Notes

사용자는 답변을 30초 기다리고 싶어 하지 않는다. 평균 latency가 1초여도 p95가 높으면用户体验受损. LLM서빙에서는 특히 첫 token 생성 시간(TTFT)도 중요.
