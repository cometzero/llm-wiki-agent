---
title: "Throughput"
type: concept
tags: [ai-ml, serving, performance]
sources: [2026-05-23-day30-ai-ml-learning-review, 2026-05-22-day30-ai-ml-learning-review]
last_updated: 2026-05-23
---

## Definition
Throughput은 단위 시간에 처리할 수 있는 요청 수 또는 token 수이다. 시스템 전체의 처리 능력을 나타내며, 대규모 서비스에서 GPU 비용과 직결된다.

## Restaurant Analogy
- 식당이 한 시간에 처리할 수 있는 전체 손님 수
- throughput이 높으면 더 많은 고객을 서비스할 수 있음

## Latency vs Throughput
| 구분 | Latency | Throughput |
|------|---------|------------|
| 의미 | 한 요청의 대기 시간 | 전체 처리량 |
| 관점 | 개별 사용자 체감 | 시스템 능력 |
| 최적화 | 속도 향상 | 병렬 처리, batching |

## Why It Matters
- 대규모 API 서비스에서 throughput이 낮으면 GPU 비용이 폭발함
- 대량 문서 요약, 배치 번역, 로그 분석처럼 많은 작업을 한꺼번에 처리하는 경우에 중요
- 1초에 몇 개의 요청 또는 token을 처리할 수 있느냐가 비용을 좌우

## Optimization
- Batching으로 GPU 효율 향상
- [[Quantization]]으로 메모리/계산 효율화
- [[KVCache]]로 반복 계산 제거
- Model parallelism

## Connections
- [[Latency]] — throughput과 함께 균형 잡아야 함
- [[Serving]] — throughput이 측정되는 영역
- [[InferenceOptimization]] — throughput 향상 기법
