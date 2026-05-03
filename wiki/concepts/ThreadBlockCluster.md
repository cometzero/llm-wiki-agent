---
title: "Thread Block Cluster"
type: concept
tags:
  - CUDA
  - Hopper
  - SM
  - GPU Programming
sources:
  - nvidia-hopper-아키텍처-심층-분석하기-nvidia-technical-blog
last_updated: 2026-05-03
---

## Definition
[[ThreadBlockCluster]]는 단일 [[SM]] 단위 블록 모델을 넘어 여러 블록을 협력 단위로 묶어 스케줄링·동기화를 확장하는 계층이다.

## 핵심 아이디어
- 기존 CUDA 스레드 블록의 지역성 한계를 완화한다.
- 더 많은 스레드 협업을 통해 공유 메모리 재사용과 스레드간 동기/데이터 교환 범위를 넓힌다.
- [[DistributedSharedMemory|분산 공유 메모리]]와 결합해 블록 간 데이터 교환 비용을 낮춘다.

## 성능효과
- 병목 완화: 단일 블록 크기 한계를 넘어선 협업 동작.
- 데이터 병렬성 강화: 특정 AI/HPC 커널에서 더 높은 로컬리티 및 메모리 효율을 만든다.
- 동기 제어 효율화: [[AsynchronousTransactionBarrier|비동기 트랜잭션 장벽]]과 함께 동작.
