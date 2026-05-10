---
title: "KV Cache"
type: concept
tags: [LLM, Transformer, memory, attention]
last_updated: 2026-05-10
sources: [ep-96-llm-추론-인프라와-토큰-경제학]
---

## 정의

[[KVCache]]는 [[Transformer]] self-attention에서 각 토큰 처리 시 계산된 [[Key]]/[[Value]] 상태를 누적 저장해 다음 토큰 생성에서 재연산을 줄이는 캐시이다.

## 추론에서의 역할
- prefill에서 키·밸류를 생성/저장하고 decode에서 재사용한다.
- 긴 입력과 다수 동시 사용자 상황에서 메모리 사용량이 크게 커질 수 있다.
- 캐시 상태는 캐시 계층(예: HBM→DRAM→flash→삭제) 이탈 시 지연/비용 특성이 달라진다.

## 최적화 이슈
- 블록 단위 관리(PagedAttention), 압축(Mixed/ sparse 전략), TTL 기반 유지 정책은 고밀도 서비스에서 유효하다.
- 컨텍스트 폭발형 워크로드에서 캐시 효율이 곧 직접 비용으로 전이된다.
