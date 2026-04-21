---
title: "Attention FFN Disaggregation"
type: concept
tags: [inference-architecture, token-flow, moes]
last_updated: 2026-04-20
sources: [gtc-2026-the-inference-kingdom-expands]
---

## Definition
[[Attention FFN Disaggregation|AFD]]는 LLM 추론에서 [[Attention]] 연산과 [[FFN]] 연산의 성격을 분리해 각기 다른 하드웨어에 할당하는 방법이다.

## Why
- 디코드에서 어텐션은 KV 캐시 상태 의존성이 크고 배치 확장 효과가 제한적일 수 있다.
- FFN은 비교적 상태 비의존적 특성이 있어 정적 스케줄링이 가능한 장치로의 오프로딩에 유리하다.

## How in this source
- [[GPU]]는 어텐션 처리와 동적 KV 캐시 로딩을 담당한다.
- [[LPU]]는 FFN 경로를 처리해 토큰당 반복 계산의 지연을 낮춘다.
- MoE 환경에서 토큰 분산이 낮아졌을 때 전체 토큰 분포 효율을 높이는 데 도움이 된다.

## Related Systems
- [[Speculative Decoding]]: LPU 기반 디코드 경로에서 추가 가속을 기대.
- [[AFD]] + [[Token Routing]]: dispatch/combine 단계의 네트워크 병목을 관리해야 함.
- [[CPO]] 및 랙 네트워크 설계: 분업 가속의 이점을 실제로 살리기 위해 인터커넥트 대역폭 최적화가 선행되어야 함.
