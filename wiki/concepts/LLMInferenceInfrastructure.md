---
title: "LLM Inference Infrastructure"
type: concept
tags: [LLM, inference, GPU, systems, infrastructure]
last_updated: 2026-05-10
sources: [ep-96-llm-추론-인프라와-토큰-경제학]
---

## 정의

[[LLM Inference Infrastructure]]는 학습된 모델이 실서비스에서 [[Token]]을 생성할 때의 하드웨어·메모리·스케줄링·캐시·요금 정책을 통합해 운영되는 시스템 전반을 말한다.

## 핵심 구성
- [[Transformer]] 추론 경로 (`[[Prefill]]`, `[[Decode]]`)
- [[GPU]]/[[HBM]]/[[NVLink]] 기반 가속 구조
- [[KVCache]] 저장·회수·계층화(온캐시 유지 vs 하강)
- 배치 스케줄러(동적 결합, 유휴 억제)
- [[TokenEconomy]]에 반영되는 비용 산출

## 핵심 원리
- 추론 지연은 `t_compute`와 `t_memory`의 최댓값으로 지배되는 경향이 있다.
- 동일 하드웨어에서 **동시 처리량**과 **지연 품질**은 배치 전략과 컨텍스트 편차 관리에 크게 좌우된다.
- 긴 컨텍스트에서는 메모리 적재량 증가로 token당 효율이 낮아질 수 있다.
- 따라서 최적 운영은 단순한 모델 우열 비교가 아니라 런타임 제약 내에서의 [[Throughput]]/[[Latency]] 균형이다.

## 실무적 의미
- 자원 절감은 모델 교체만으로 달성되지 않으며, 런타임, 캐시, 스케줄링 조합으로 달성된다.
- 비용 모델(가격 정책)과 직접 연결되어 [[가격 정책]]의 비대칭 요소(입력/출력 토큰 차이, 컨텍스트 구간별 tier)를 만든다.
