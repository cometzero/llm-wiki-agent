---
title: "Streaming Multiprocessor"
type: concept
tags:
  - CUDA
  - GPU
  - Scheduler
  - ParallelExecution
date: 2026-05-03
sources:
  - cuda-refresher-the-cuda-programming-model-nvidia-technical-blog
---

## 개요
[[Streaming Multiprocessor]]는 NVIDIA [[GPU]] 내부에서 여러 [[CUDA Block]]를 실행하는 병렬 처리 단위로, 블록 스케줄링과 동시 실행 자원 할당의 기준점이다.

## 동작 원리
- 한 블록이 하나의 SM에 배치되어 실행되며, 배치된 SM 간 블록 마이그레이션은 제한됨.
- 같은 블록 내 스레드는 공유 메모리, barrier 동기화, 캐시/레지스터 제약을 함께 공유.

## 성능 함의
블록당 스레드 수, 자원 사용량, 메모리 배치가 특정 SM의 병렬성 및 점유율을 결정하므로 블록 단위 튜닝이 곧바로 처리량과 지연으로 연결된다.