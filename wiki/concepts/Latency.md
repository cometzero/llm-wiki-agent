---
title: "Latency"
type: concept
tags: [ai-ml, serving, performance]
sources: [2026-05-23-day30-ai-ml-learning-review, 2026-05-22-day30-ai-ml-learning-review]
last_updated: 2026-05-23
---

## Definition
Latency는 요청 하나가 들어와서 응답이 나올 때까지 걸리는 시간이다. 사용자가 질문을 입력한 뒤 답변을 받기까지의 대기 시간으로, 사용자 경험에 직접적인 영향을 미친다.

## Restaurant Analogy
- 식당에서 손님이 주문을 하고 음식을 받을 때까지 걸리는 시간
- latency가 낮으면 손님 한 명의 체감 대기 시간이 짧음

## Latency vs Throughput
- **Latency**: 한 요청의 대기 시간 (개별 체감)
- **Throughput**: 단위 시간당 전체 처리량 (시스템 능력)

Batch를 크게 하면 throughput은 좋아질 수 있지만, batch가 모일 때까지 기다려야 하므로 개별 latency는 늘어날 수 있다.

## Why It Matters
- 챗봇, 음성 비서, 실시간 번역처럼 사용자가 바로 응답을 기대하는 서비스에서 중요
- 사용자가 20초를 기다리면 답답함을 느낌
- LLM은 token을 하나씩 생성하므로 긴 답변일수록 latency가 누적됨

## Optimization
- [[Quantization]] — 계산 비용 감소
- [[KVCache]] — 반복 계산 제거
- Batching 전략 조정
- GPU 성능 활용

## Connections
- [[Throughput]] — latency와 함께 관리해야 할 지표
- [[Serving]] — latency가 발생하는 영역
- [[InferenceOptimization]] — latency 감소 기법
