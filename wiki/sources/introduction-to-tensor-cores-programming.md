---
title: "Introduction to Tensor Cores Programming"
type: source
tags:
  - NVIDIA
  - TensorCores
  - CUDA
  - WMMA
  - MatrixMultiplication
  - Precision
  - GFLOPS
  - GPU
  - CUDACore
  - Warp
  - cuBLAS
date: 2026-05-03
source_file: raw/Nvidia/LilysAI/introduction-to-tensor-cores-programming.md
sources:
  - introduction-to-tensor-cores-programming
last_updated: 2026-05-03
---

## Summary
이 소스는 [[TensorCores]]의 동작 원리와 프로그래밍 실무를 중심으로, AI에서 가장 큰 비중을 차지하는 행렬 곱셈 연산을 가속하는 CUDA 기반 접근을 정리한다. 기본 개념은 [[NVIDIA]] GPU의 텐서 코어가 [[Tensor]] 연산에서 우위를 보이며, 특히 [[FP16|HalfPrecision]] 입력을 받아 [[FP32|SinglePrecision]] 누적으로 계산해 성능과 정확도를 균형 있게 맞춘다는 점이다.

또한 소스는 행렬 저장 방식(행우선/열우선), 메모리 정밀도 선택, 그리고 실제 구현에서의 타일링·워프 협업 구조를 상세히 보여 준다. 특히 16x16 기반 연산 제약을 넘기기 위한 패딩과 타일 분할 방법, 그리고 [[nvcuda::wmma]] API를 통한 프래그먼트 기반 구현이 핵심 실전 포인트로 제시된다.

마지막으로 성능 지표로 [[GFLOPS]] 기반 분석을 강조하며, CUDA 코어 대비 텐서 코어의 속도 이점이 존재하지만 구현이 단순히 바꾼다고 자동으로 좋아지는 것은 아니며, 타일 크기·메모리 레이아웃·루프 구조가 지표를 좌우한다고 정리한다.

## Key Claims
- [[TensorCores]]는 AI 연산 중 행렬 곱셈이 차지하는 비용을 줄이기 위해 특화된 연산 유닛으로, 주로 [[FP16|HalfPrecision]] 입력과 [[FP32|SinglePrecision]] 누적 출력으로 동작한다.
- [[Volta]] 마이크로아키텍처 이후 [[NVIDIA]] GPU에 본격 탑재된 텐서 코어는 기존 CUDA 코어 대비 [[MatrixMultiplication|행렬 곱셈]] 처리 최적화에 유리하다.
- 2차원 행렬은 실제로는 선형 주소공간에 저장되므로, 요소 접근은 행렬 인덱스를 선형 인덱스로 변환해 처리한다.
- 워프 단위 협업이 핵심이며, 텐서 코어 연산은 일반적으로 한 워프(32개 스레드)가 하나의 타일을 담당해 [[WMMA]] 파이프라인에서 협력한다.
- 텐서 코어는 특정 타일 크기에 제약이 있어 실제 구현에서는 16x16 타일 기반 분할과 16의 배수 정렬을 위해 패딩을 사용한다.
- [[WMMA]] 기반 구현은 [[fragment]](프래그먼트) 관리, `load_matrix_sync`, `mma_sync`, `store_matrix_sync` 형태의 API 사용 패턴으로 구성되며, 누산기(accumulator) 초기화가 필수다.
- 텐서 코어 성능은 [[GFLOPS]] 같은 연산량 지표로 보는 것이 실측 비교에서 더 유효하다.
- 타일링 기반 텐서 코어 구현은 CUDA 코어 타일링 버전 대비 큰 성능 이점을 보이지만, cuBLAS 최적화 코드와 비교하면 미세 구현 최적화의 차이로 격차가 존재한다.

## Key Quotes
> "NVIDIA GPU의 텐서 코어는 AI 알고리즘 연산 비용의 90% 이상을 차지하는 행렬 곱셈에 특화된 가속 장치이다." — source

> "텐서 코어는 일반적으로 하프 프리시전(FP16) 입력을 받아 싱글 프리시전(FP32) 출력을 생성하도록 설계되었다." — source

> "워크프 내의 모든 스레드(32개 스레드)가 협력하여 하나의 16x16 행렬 곱셈 및 누적 연산을 수행한다." — source

## Connections
- [[NVIDIA]] — 본 자료의 중심 하드웨어 공급자.
- [[TensorCores]] — AI 행렬 연산의 특화 가속 단위.
- [[CUDA]] — 텐서 코어를 프로그래밍하는 실행 환경.
- [[Volta]] — 텐서 코어 본격 탑재 시점으로 언급되는 아키텍처.
- [[WMMA]] — 텐서 코어용 고수준 CUDA API.
- [[FP16]] — 텐서 코어 입력 정밀도 흐름의 핵심.
- [[FP32]] — 누적/출력 정밀도로 언급되는 정밀도.
- [[Warp]] — 텐서 코어 연산의 워프 단위 동기 협업 단위.
- [[MatrixMultiplication]] — 연산의 핵심 수학 연산.
- [[GFLOPS]] — 성능 지표 비교의 핵심 단위.
- [[MemoryLayout]] — 행 우선/열 우선 저장 방식이 타일 로드 성능을 결정.
- [[cuBLAS]] — 성능 비교에서 자주 참조되는 고도로 최적화된 대조군.

## Contradictions
- 기존 위키의 [[AIInfrastructure]] 및 [[CUDA]] 관련 항목과 충돌하지 않는다. 다만 본 소스는 FP16-FP32 텐서 코어 경로를 성능 중심 관점에서 정면 강조하며, 이미 존재하던 일반 CUDA 성능 비교 프레임을 보완한다.
