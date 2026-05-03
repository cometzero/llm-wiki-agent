---
title: "CUDA"
type: concept
tags:
  - GPU
  - ParallelProgramming
  - HeterogeneousComputing
date: 2026-05-03
sources:
  - cuda-refresher-the-cuda-programming-model-nvidia-technical-blog
---

## 개요
[[CUDA]]는 [[NVIDIA]]가 제공하는 이기종 병렬 계산 프레임워크로, [[Host]] 메모리에서 실행되던 제어 코드를 유지하면서, 대규모 연산을 [[Device]]([[GPU]])에서 [[CUDA Kernel]] 단위로 병렬 실행한다.

## 핵심 구성
- [[CUDA Programming Model]]: host-device 메모리 분리, kernel launch, thread hierarchy 기반 실행 모델.
- [[Kernel Launch]]: 디바이스 코드 진입점과 실행 파라미터(그리드/블록 구조)를 결정.
- [[Memory Hierarchy]]: 레지스터, 공유 메모리, 캐시, 전역 메모리의 계층별 사용이 성능을 좌우.

## 실행 흐름(요약)
1. 호스트에서 입력을 [[HostMemory]]에 준비
2. 필요 데이터의 [[Device]] 전송
3. [[CUDA Kernel]] 실행
4. 결과를 [[DeviceMemory]]에서 호스트로 회수

## 관련 개념
- [[Host]], [[Device]], [[GPU]], [[StreamingMultiprocessor]], [[ComputeCapability]], [[Thread Hierarchy]]

## 실무 시사점
개발자는 단순히 커널 함수만 작성하는 것이 아니라, 스레드 인덱싱 전략과 메모리 계층 접근 패턴을 통해 동시성/메모리 대역/동기화를 함께 설계해야 한다.