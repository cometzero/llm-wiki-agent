---
title: "Inference Stack"
type: concept
tags: [ai-ml, inference, mlops, system-design]
sources: [2026-05-24-day30-ai-ml-learning-review]
last_updated: 2026-05-24
---

## Definition

[[InferenceStack]]은 학습된 모델을 실제 요청에 대해 실행하고 응답을 돌려주는 서빙 구조이다. [[TrainingStack]]과 달리 weight 업데이트 없이 현재 파라미터로 예측만 수행하며, latency, throughput, 비용, 안정성이 핵심이다.

## Key Components
1. **Tokenizer**: 텍스트를 token으로 변환
2. **Model server**: 모델 실행 (GPU/CPU forward pass)
3. **Batching**: 요청 묶음 처리
4. **KV cache**: attention 결과 재사용
5. **Quantization**: 메모리/비용 최적화
6. **Safety filter**: 출력 후처리
7. **Monitoring**: latency, throughput, error rate 추적

## Training vs Inference Stack
|Aspect|Training Stack|Inference Stack|
|---|---|---|
|Focus|loss, gradient, optimizer|latency, throughput, stability|
|Updates|Weight 변경|Weight 불변|
|Memory|Gradient 저장 필요|상대적으로 적음|
|Parallelism|데이터/모델 병렬화|요청 batching|

## Connections
- [[TrainingStack]] — 학습된 모델 공급
- [[Serving]] — inference stack을 사용한 모델 운영
- [[Latency]] — 핵심 성능 지표
- [[Throughput]] — 핵심 성능 지표

## Practical Notes

사용자가 질문을 보내면 tokenizer → model server → 결과를 다시 문장으로 변환 → 응답. 학습처럼 weight를 바꾸지 않으며, 빠르게 계산하고 많은 요청을 처리하는 것이 목표.
