---
title: "Modular: Matrix Multiplication on Blackwell: Part 2 - Using Hardware Features to Optimize Matmul"
type: source
tags:
  - NVIDIA
  - Blackwell
  - TensorCores
  - MatrixMultiplication
  - TensorMemoryAccelerator
  - Tcgen05MMA
  - TMEM
  - SharedMemory
  - Stmatrix
  - Swizzling
  - BankConflict
date: 2026-05-03
source_file: raw/Nvidia/LilysAI/modular-matrix-multiplication-on-blackwell-part-2-using-hardware-features-to-optimize-matmul.md
sources:
  - modular-matrix-multiplication-on-blackwell-part-2-using-hardware-features-to-optimize-matmul
last_updated: 2026-05-03
---

## Summary
Blackwell에서 행렬 곱셈([[MatrixMultiplication]]) 성능을 높이기 위한 실전 커널 최적화 흐름을 다룬다. 기본 타일 기반 접근에서 시작해 [[TensorMemoryAccelerator|TMA]]를 통한 비동기 타일 로드/저장, [[Tcgen05MMA]]의 하드웨어 명령 활용, 그리고 [[TMEM]] 기반 중간 저장 구조로 계산 경로를 재설계한다. 여기에 더해 공유 메모리 뱅크 충돌을 [[Swizzling]]으로 완화하고, 마지막으로 출력 데이터의 공유 메모리 패킹과 [[Stmatrix|stmatrix]]를 결합해 TMA store로 전송한다. 나이브 커널 대비 최대 58배 성능을 달성했지만, cuBLAS 대비 여전히 격차가 남아 파이프라인/오버랩이 다음 단계로 제시된다.

## Key Claims
- [[Blackwell]]에서의 고효율 [[MatrixMultiplication]]은 단일 최적화가 아니라 [[SharedMemory]], [[TensorMemoryAccelerator]], [[Tcgen05MMA]], [[Stmatrix]], 그리고 [[Swizzling]]의 결합 설계가 핵심이다.
- 루프 타일링을 통해 전역 메모리 접근 횟수를 줄이면 반복 계산 당 GMEM I/O를 줄일 수 있어 성능 병목의 큰 부분을 완화한다.
- [[TensorMemoryAccelerator]]는 입력 타일을 GMEM→SMEM로 비동기 복사하고, [[Tmbar]]/barrier 동기(문맥상 `tma_phase` 갱신)로 단계별 정합을 맞춘다.
- [[Tcgen05MMA]]는 [[Blackwell]] 세대 텐서 코어의 확장된 형태로, 최대 128x256x16 형태 및 256x256x16 2SM 경로 사용이 가능해 처리량이 증가한다.
- 텐서 연산은 [[TMEM]]에 결과를 누적·중간 저장해 레지스터 압력을 줄이고 ALU/텐서 코어 간 레지스터 경합을 완화한다.
- [[TMEM]]은 고정 열 단위(예: 16KB 단위)로 할당되고, 256KB 크기의 온칩 영역으로 대형 연산 블록([[C_tile]])을 운반하는 데 쓰인다.
- [[SharedMemory]] 뱅크 충돌은 코어 행렬 배치에서 큰 직렬화를 만들 수 있으므로, [[Swizzling|스위즐링]]으로 동시 접근 충돌을 줄이면 속도가 크게 향상된다.
- 본문 커널 3(스위즐링 적용)은 커널 2 대비 B200에서 288.3 TFLOPS까지 달성했고, 이는 동일 커널군 대비 약 87% 개선이다.
- [[Stmatrix]]를 사용해 레지스터에서 나온 FP32 출력을 SMEM에 BF16 패킹 방식으로 저장해야 TMA store 파이프라인이 자연스럽게 동작한다.
- TMA save/store는 커밋/대기 그룹(wait_group) 설계로 파이프라인 격리를 만들고, 향후 데이터 전송과 계산을 오버랩해 더 높은 성능 여지가 남는다.
- 전체 실험에서 나이브 커널 대비 최종적으로 58배 성능 향상을 보였으며, 최대 성능은 글로벌 메모리 대역폭이 지배하는 현재 구조에서 cuBLAS까지는 미치지 못했다.

## Key Quotes
> "Blackwell GPU에서 행렬 곱셈 성능을 최적화하는 방법은 TMA, tcgen05.mma, stmatrix 등을 활용해 공유 메모리 접근을 최적화하는 것" — source

> "이 커널은 288.3 TFLOPs를 달성" — source

> "이 게시물에서는 나이브 커널 대비 58배 성능 향상" — source

> "TMA의 진정한 힘은 비동기성에 있으며, 이는 파이프라이닝 및 작업 오버랩을 가능하게 한다" — source

## Connections
- [[Blackwell]] — 본 소스의 아키텍처 대상.
- [[NVIDIA]] — 하드웨어 및 생태계를 제공하는 주체.
- [[TensorMemoryAccelerator]] — 타일 로드/스토어를 비동기화하는 핵심 기능.
- [[Tcgen05MMA]] — Blackwell 텐서 코어 MMA 명령 집합의 핵심 수행 경로.
- [[TMEM]] — 텐서 메모리 저장소로 레지스터 압력과 동작 병렬성 간 경합을 분리.
- [[SharedMemory]] — 타일 데이터 공유와 bank conflict 해결의 핵심 영역.
- [[Swizzling]] — [[SharedMemory]] 뱅크 충돌 완화 기법.
- [[Stmatrix]] — 레지스터 결과를 SMEM로 패킹해 TMA store로 이전하기 위한 저장 명령.
- [[BankConflict]] — 스미스 매트릭스 배치에서 성능 저하를 일으키는 원인 축 중 하나.
- [[MemoryBoundKernel]] — 본문 성능 상한이 전역 메모리 대역폭으로 제한됨을 보여 주는 맥락.
- [[KernelOptimization]] — 타일링, 배리어, 명령 재배치, 파이프라이닝을 결합한 실전 최적화 사례.

## Contradictions
- 기존 위키의 [[TensorCores]] 및 [[CUDA]] 기본 구현 가이드와 충돌하지 않으며, 이를 Blackwell 세대의 하드웨어 기능으로 구체화한다.
- 기존 [[cuBLAS]] 중심 벤치마크 대비 본문은 "구현-마이크로아키텍처 정렬"의 여지가 남았음을 제시하므로, 상호 배제적이기보다 보완적이다.
