---
title: "EP 96. LLM 추론 인프라와 토큰 경제학"
type: source
tags: [LLM, Inference, TokenEconomy, GPU, HBM, NVIDIA, Transformer, KVCache, Prefill, Decode, BatchInference]
date: 2026-05-10
last_updated: 2026-05-10
sources: [ep-96-llm-추론-인프라와-토큰-경제학]
source_file: raw/AI/LilysAI/ep-96.-llm-추론-인프라와-토큰-경제학.md
source_hash: dfc1a5f5468e7c2d
---

## Summary
[[LLM]] 추론은 모델 크기 자체보다 하드웨어-메모리 병목, 배치 처리 전략, 캐시 관리로 성능과 비용이 결정되며, [[GPU]]와 [[HBM]]의 이용 효율이 서비스 경제성의 핵심이 된다. 핵심은 추론 지연 시간의 두 성분인 [[t_compute]]와 [[t_memory]]를 균형화해 GPU 활용률을 높이는 것이다.

[[Transformer]] 계열은 `prefill`과 `decode` 단계로 토큰을 처리하고, 이 과정에서 [[KVCache]]가 계산 비용과 메모리 비용의 중심이 된다. 긴 컨텍스트와 고빈도 추론 환경에서는 캐시 계층, 배치 스케줄링, 메모리 계층 정책이 품질·비용·처리량을 좌우한다. 즉, 모델 자체 혁신만큼이나 [[LLM 인프라]]의 운영 설계가 토큰당 비용과 가격 정책([[TokenEconomy]])에 직접 반영된다.

## 주요 주장
- 추론은 `t_compute`와 `t_memory` 중 더 큰 쪽으로 지연이 좌우되며, 
  [[MFU]](모델 FLOPs 활용률)와 실제 [[GPU]] utilization의 간극은 비용 구조의 핵심 원천이다.
- 현대 [[LLM]] 추론의 중요한 최적화 축은 [[Transformer]]의 [[Prefill]]/[[Decode]] 분리, [[KVCache]] 길이 관리, 배치 정규화가 아닌 **배치 정책(동적 통합, 패딩 제어)**이다.
- `prefill` 단계는 긴 입력을 병렬 처리하는 구간으로 토큰 처리량을 늘리고, `decode` 단계는 토큰을 하나씩 자기회귀로 생성한다.
- `cache`를 유지할 수 있는 구간이 길어질수록 같은 사용자의 연속 대화에서 비용 효율이 좋아지며, 시간이 지나면 DRAM/flash/HDD로 내릴수록 접근 비용이 달라진다.
- [[NVIDIA]]의 [[Blackwell]] 계열(특히 NVL72)과 같이 랙 단위 자원 통합이 가능해질수록 스루풋이 개선되지만, [[GPU]] 간 통신과 메모리 이동 비용은 여전히 제약으로 남아 있다.
- [[Roofline Analysis]] 관점에서 [[BatchSize]]가 작으면 메모리 바운드, 커지면 연산 바운드가 되어 토큰당 비용 곡선이 달라진다.
- 최적 배치 크기는 `t_compute ≈ t_memory`를 만족하도록 잡을 때 성능/비용 관점에서 안정적인 운영점을 만든다.
- 스파시티(`활성화된 파라미터 / 전체 파라미터`)가 높아질수록 스케일러블한 배치 운영이 쉬워져 동일 하드웨어로 더 많은 사용자를 수용할 수 있다.
- [[vLLM]]·[[SGLang]] 같은 런타임 최적화 계층은 긴 prefill 분할(`chunked prefill`), [[PagedAttention]], 대규모 요청 합성 스케줄링으로 GPU 자원 유휴를 줄인다.

## Key Claims
- LLM 추론 시간은 `t_compute`와 `t_memory` 중 더 큰 값에 의해 좌우된다.
- `t_compute`는 활성화된 파라미터 수와 배치 크기, `FLOPs`에 따라 증가하고, `t_memory`는 총 가중치 적재 및 KV 캐시 적재량(컨텍스트 길이, 배치 크기, 토큰 크기)과 메모리 대역폭에 의해 결정된다.
- 추론 배치에서 패딩을 줄이고 동적 배치 결합을 사용하면 GPU 자원 손실을 줄여 처리량과 비용 효율을 높일 수 있다.
- 긴 prefill 요청이 decode 흐름을 막지 않도록 chunked prefill 같은 분할 기법이 필요하다.
- 입력 토큰과 출력 토큰의 가격 정책은 하드웨어/캐시 상태 및 컨텍스트 길이 전략과 밀접히 연결된다.

## Key Quotes
> "LLM 추론 시간은 연산 시간 `t_compute`와 메모리 접근 시간 `t_memory` 중 더 오래 걸리는 쪽이 결정한다."

> "최적 배치 크기는 보통 `t_compute`와 `t_memory`가 맞물리는 지점에서 결정된다."

> "컨텍스트 길이가 길어지면 더 적은 동시 사용자 처리량으로 떨어져 비용이 급격히 올라갈 수 있다."

## Connections
- [[LLM]] — 추론 지연, 품질, 비용, 캐시 정책의 운영 단위를 연결한다.
- [[Transformer]] — prefill/decode와 KV cache의 구조적 출발점.
- [[KVCache]] — 토큰 생성 반복 시 재활용되는 핵심 메모리 자산.
- [[GPU]] / [[HBM]] / [[Blackwell]] / [[NVIDIA]] — 하드웨어 계층의 성능·비용 제약을 제공한다.
- [[InferenceOptimization]], [[TokenEconomy]], [[BatchInference]] — 비용 효율 설계와 직접 연동.
- [[vLLM]], [[SGLang]], [[PagedAttention]], [[Chunked Prefill]], [[Roofline Analysis]] — 실무 실행 최적화 기술군.
- [[Dwarkesh]] — 본문에서 반복 학습/요약형 정리법을 강조한 지식 전달자로 연결.

## Contradictions
- 기존의 일부 자료에서 모델 경쟁을 가격·성능의 일차적 전부로 보는 해석이 있다면, 본 소스는 같은 맥락을 유지하되 **운영 인프라와 토큰 처리 전략이 수익성의 병목/완충 장치**가 된다는 점을 구체적으로 보강한다. 본질적 상충이라기보다 분석 단위의 보완적 확장으로 해석된다.