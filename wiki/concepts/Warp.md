---
title: "Warp"
type: concept
tags:
  - CUDA
  - GPU
  - Parallelism
  - TensorCore
sources:
  - introduction-to-tensor-cores-programming
last_updated: 2026-05-03
---

## Summary
[[Warp]]는 [[CUDA]]에서 스케줄링되는 32개 스레드 단위의 병렬 실행 그룹이다. 텐서 코어 연산에서는 워프 단위 협업이 핵심 실행 단위로 작동한다.

## Key Claims
- 텐서 코어는 보통 한 워프가 하나의 타일 연산 단위를 맡아 처리한다.
- 워프 단위 협업이 프래그먼트 로딩과 곱셈/누산 루프의 성능을 좌우한다.
- 커널 내 워프 식별과 바인딩이 성능 안정성의 핵심이다.

## Connections
- [[TensorCores]] — 하드웨어 실행 동작을 워프 단위로 묶어 효율화.
- [[WMMA]] — 워프 기반 API 사용 패턴이 정형화됨.
- [[CUDA]] — 워프 스케줄링 구조를 제공하는 실행 모델.

## Notes
워크로드가 워프 협업 성질과 맞지 않으면 텐서 코어의 잠재 성능이 거의 사라질 수 있다.