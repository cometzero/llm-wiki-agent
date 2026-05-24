---
title: "Serving"
type: concept
tags: [ai-ml, inference, deployment, mlops]
sources: [2026-05-24-day30-ai-ml-learning-review]
last_updated: 2026-05-24
---

## Definition

[[Serving]]은 학습된 모델을 API, 앱, 검색 시스템, 챗봇 등 실제 환경에서 안정적으로 제공하는 것이다. 모델 품질만큼 빠르고 안정적인 serving이 중요하며, "연구 노트북에서 잘 돌아간다"와 "실제 사용자를 처리한다"는 완전히 다른 문제이다.

## Key Concepts

### Serving Architecture
1. **입력 처리**: 텍스트를 token으로 변환, 이미지라면 tensor 형태로 변환
2. **모델 실행**: GPU/CPU에서 forward pass, gradient 계산 없음
3. **출력 처리**: 생성된 token을 문장으로 변환, safety filter 적용
4. **모니터링**: latency, throughput, error rate, GPU memory, queue length 관찰

### LLM-Specific Serving
- [[KVCache]]로 attention 계산 재사용
- [[Batching]]으로 throughput 향상
- [[Quantization]]으로 메모리/비용 절감
- Router로 쉬운 질문은 작은 모델, 어려운 질문은 큰 모델로 분기

### Trade-offs
- 모델을 작게 → 빠르고 싸지만 성능 하락 가능
- 큰 모델 → 답 좋지만 느리고 비쌈
- [[Quantization]] → 메모리 줄지만 정밀도 손실 가능
- [[Batching]] → throughput 향상 but 개별 latency 증가 가능

## Connections
- [[InferenceStack]] — serving의 기술적 구성
- [[Latency]] — serving 성능 핵심 지표
- [[Throughput]] — serving 성능 핵심 지표
- [[KVCache]] — LLM serving 핵심 최적화
- [[Quantization]] — memory/cost optimization
- [[Evaluation]] — 배포 전 안전성 검증

## Practical Notes

LLM은 답변을 한 토큰씩 생성하기 때문에 KV cache를 잘 쓰지 않으면 이미 계산한 attention 정보를 계속 다시 계산하게 되어 매우 비효율적이다.
