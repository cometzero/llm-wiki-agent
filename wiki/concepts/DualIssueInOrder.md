---
title: "Dual-Issue In-Order"
type: concept
tags:
  - microarchitecture
  - execution
  - energy
sources:
  - npu-v0-1-hw-architecture
last_updated: 2026-05-03
---

## 정의
[[Dual-Issue In-Order]]는 한 사이클에 두 개 slot을 통해 병렬 발행하되, 명령 순서를 유지하는 실행 모델이다.

## v0.1에서의 적용
- slot 0: scalar/branch/CSR
- slot 1: vector/IME/VLSU
- 결과적으로 out-of-order 대비 검증 난이도/전력 비용이 낮고, compiler-scheduled kernel 성격에 맞는다.

## 성능 vs 예측성
v0.1은 throughput absolute 최적화보다 edge latency와 deterministic execution을 우선하여 이 모델을 채택한다.

## 연관 링크
- [[DeterministicExecution]], [[Vector]], [[RVV]], [[NPUv01]], [[ILEDecode]
