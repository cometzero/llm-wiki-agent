---
title: "Kernel Launch"
type: concept
tags:
  - CUDA
  - ExecutionModel
  - GPU
  - Parallelism
date: 2026-05-03
sources:
  - cuda-refresher-the-cuda-programming-model-nvidia-technical-blog
---

## 개요
[[Kernel Launch]]는 [[CUDA Kernel]] 실행을 시작하는 구문/동작으로, 커널에서 사용할 [[Grid]] 크기와 [[Block]] 크기를 지정한다.

## 핵심 역할
- 한 번의 런치에서 여러 스레드가 동일 커널을 수행하게 만드는 시작점이다.
- [[Host]] 측에서 설정되어 [[Device]]에서 병렬 실행되며, 일반적으로 실행은 비동기적으로 동작한다.

## 관련 속성
- 커널 타입: [[CUDA Kernel]]이어야 함
- 실행 구성: [[Block]] 수, [[CUDA Thread]] 수, 1D/2D/3D 배치
- 동기화: 블록 단위 동기화는 [[__syncthreads]]로 보장

## 사용상 주의
커널 런치 구성은 계산량, 메모리 액세스 패턴, [[StreamingMultiprocessor]] 자원 점유율을 동시에 고려해 선택해야 한다.