---
title: "CUDA Refresher: The CUDA Programming Model | NVIDIA Technical Blog"
type: source
tags:
  - CUDA
  - CUDAProgrammingModel
  - GPU
  - Kernel
  - MemoryHierarchy
  - ComputeCapability
  - ParallelProgramming
date: 2026-05-03
source_file: raw/Nvidia/LilysAI/cuda-refresher-the-cuda-programming-model-nvidia-technical-blog.md
last_updated: 2026-05-03
sources:
  - cuda-refresher-the-cuda-programming-model-nvidia-technical-blog
---

## Summary
이 문서는 [[CUDA]]가 [[Host]]와 [[Device]]의 이기종 환경에서 어떻게 동작하는지 정리한다. 핵심은 [[NVIDIA]] [[GPU]]에서 실행되는 병렬 커널을 정의·실행하기 위해, 개발자가 [[CUDA Kernel]]과 스레드/블록 계층을 명시하는 방식이다.

문서의 중심은 다음 두 단계다.
- [[CUDA Kernel Launch]]를 통해 병렬 실행 구조를 선언
- [[Thread Hierarchy]]와 [[Memory Hierarchy]]를 고려해 성능/자원 관리를 최적화

또한 [[Compute Capability]]가 하드웨어 기능 집합을 결정하며 런타임 동작 선택을 좌우한다는 점, 즉 아키텍처별 기능을 반영한 코드 작성의 필요성을 강조한다.

## Key Claims
- [[CUDA Programming Model]]은 [[Host]] 메모리와 [[Device]] 메모리가 분리된 모델에서 출발하며, 데이터 전송이 명시적으로 host→device 및 device→host 방향으로 수행된다.
- [[CUDA Kernel]]은 [[GPU]]에서 실행되는 함수로, 동일 커널이 다수의 스레드에서 병렬로 반복 수행된다.
- [[Grid]]는 여러 개의 [[CUDA Block]]으로 구성되며, 각 블록은 1개 이상 [[CUDA Thread]] 집합을 가진다.
- [[__global__]] 지정자는 CUDA 커널의 함수 선언에서 필수이며, 컴파일러와 런타임이 커널 런치 문맥을 인식할 수 있게 한다.
- 커널 내에서는 [[threadIdx]], [[blockIdx]], [[blockDim]] 같은 3D 내장 변수를 통해 스레드 인덱싱과 3차원 작업 분할을 수행한다.
- 스레드 동기화는 주로 [[__syncthreads]]로 블록 내부 동기점을 두어 처리 단계 간 정합을 맞춘다.
- 블록당 스레드 수는 하드웨어가 제한(일반적으로 1024)되며, 스레드/블록 크기 선택은 점유율 및 병렬성에 직접 영향을 준다.
- [[Streaming Multiprocessor|SM]]는 블록 단위 스케줄링 단위로, 블록은 마이그레이션되지 않고 동일 SM에서 실행된다.
- [[GPU]] 메모리 계층은 [[Register]], [[Shared Memory]], [[L1 cache]], [[Read-only Memory]], [[L2 cache]], [[Global Memory]]로 구성되며, 계층별 활용이 성능에 직접 반영된다.
- 숙련된 CUDA 개발자는 메모리 계층별 접근 패턴(온칩/오프칩 구분)을 조율해 성능 최적화를 수행한다.
- [[Compute Capability]]는 하드웨어 지원 기능과 명령어 사용 가능성을 결정하며, 런타임/컴파일 타임 선택을 구분하는 주요 기준이다.
- [[deviceQuery]]와 같은 CUDA 샘플은 디바이스의 compute capability 및 하드웨어 속성 탐지에 사용된다.

## Key Quotes
> "커널은 [[Kernel Launch|커널 런치]] 구문에서 블록 수와 블록당 스레드 수를 지정해 디바이스 코드로 비동기 실행된다." — [[CUDA]] 실행 모델의 실행 단위 구문을 설명하는 부분.

> "블록은 고정된 SM에 바인딩되어 스케줄링되며, 블록 내에서 스레드 동기화가 필요한 경우 [[__syncthreads]]를 사용한다." — [[Streaming Multiprocessor]] 단위 실행 특성과 동기화 원칙을 보여줌.

## Connections
- [[NVIDIA]] — 본 문서의 출처 및 CUDA 생태계의 중심 제조사.
- [[CUDA]] — host-device 이기종 병렬 처리 모델의 핵심 프레임워크.
- [[CUDA Programming Model]] — 병렬 커널, 스레드/블록, 메모리 계층을 아우르는 실행 규격.
- [[CUDA Kernel]] — [[Device]]에서 실행되는 계산 단위.
- [[Kernel Launch]] — 커널 실행 파라미터를 결정하는 핵심 구문.
- [[Thread Hierarchy]] — 블록-스레드 2-level 병렬 구조.
- [[Streaming Multiprocessor]] — SM 스케줄링 단위에서 실행 성능을 결정.
- [[Memory Hierarchy]] — 레지스터/공유메모리/캐시/전역메모리 계층으로 구성되는 성능 핵심.
- [[Compute Capability]] — 하드웨어-소프트웨어 기능 호환성의 버전 신호.
- [[deviceQuery]] — 디바이스 특성 탐지 및 capability 확인 루틴.

## Contradictions
- 기존 위키의 [[AI Infrastructure]] 및 추론 지향 문헌과 충돌하지 않는다. 오히려 CUDA 계층(스레드-블록-메모리 최적화)의 실행 원리를 구체화해 [[NVIDIA]]/GPU 가속기 성능 이해를 기초적으로 보강한다.
