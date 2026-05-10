---
title: "Roofline Analysis"
type: concept
tags: [performance, latency, compute-vs-memory, inference]
last_updated: 2026-05-10
sources: [ep-96-llm-추론-인프라와-토큰-경제학]
---

## 정의

[[Roofline Analysis]]는 특정 워크로드에서 계산량(연산)과 메모리 대역폭의 상대적 제약이 성능을 어떻게 제한하는지 분석하는 도식적 프레임이다. [[LLM]] 추론에서는 [[Latency]]와 [[Throughput]]를 설명하기 위한 실무 도구로 쓰인다.

## LLM 추론에서의 적용
- `t_compute`는 배치 크기와 활성 파라미터 수(또는 활성화 연산량)에 비례해 증가할 수 있다.
- `t_memory`는 모델 가중치 로딩과 [[KVCache]] 로딩을 포함하고, 배치/시퀀스 길이 증가와 함께 증가한다.
- 배치가 작을 때는 메모리 바운드, 클수록 연산 바운드로 이동하는 경향이 있어 `토큰당 비용` 곡선에 비선형성이 생긴다.

## 실무 적용
- `토큰당 비용`을 최소화하려면 `t_compute`와 `t_memory`가 교차하는 지점을 중심으로 배치 크기, 스케줄링, 캐시 정책을 설정한다.
- 최적점은 고정값이 아니라 스파시티, 하드웨어 세대, 런타임 정책에 따라 변한다.
