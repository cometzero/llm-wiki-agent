---
title: "TMEM"
type: concept
tags: [NVIDIA, TensorMemory, GPUArchitecture]
sources: [nvidia-tensor-core-evolution-from-volta-to-blackwell]
last_updated: 2026-05-03
---

## Definition

[[TMEM]](Tensor Memory)은 [[Blackwell]]에서 텐서 코어 전용으로 추가된 메모리 계층으로, 피연산자/출력 저장 경로를 공유 메모리 밖의 중간 단계로 분리해 레지스터 압력과 메모리 대역폭 병목을 줄이는 데 사용된다.

## Role in architecture

- [[TensorCores]] 연산에서 피연산자 체류 위치를 재배치
- 워프그룹 및 [[MMA]] 협업 단위에서 연산-이동 간 오버랩을 더 쉽게 구성
- D-tile 및 반복 접근이 잦은 출력 행렬의 재사용 효율 향상에 기여

## Cross-links

- [[Blackwell]]
- [[SharedMemory]]
- [[Registers]]
- [[TensorCores]]
- [[MMA]]