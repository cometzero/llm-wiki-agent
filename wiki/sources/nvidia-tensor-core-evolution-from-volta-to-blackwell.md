---
title: "NVIDIA Tensor Core Evolution: From Volta To Blackwell"
type: source
tags:
  - NVIDIA
  - TensorCores
  - Volta
  - Turing
  - Ampere
  - Hopper
  - Blackwell
  - TMEM
  - MMA
  - HMMA
  - WGMMA
  - StructuredSparsity
  - FP16
  - BF16
  - FP8
  - MXFP4
  - TensorMemoryAccelerator
date: 2026-05-03
source_file: raw/Nvidia/LilysAI/nvidia-tensor-core-evolution-from-volta-to-blackwell.md
sources:
  - nvidia-tensor-core-evolution-from-volta-to-blackwell
last_updated: 2026-05-03
---

## Summary
이 글은 [[NVIDIA]] 텐서 코어가 [[Volta]]에서 [[Blackwell]]로 진화한 과정을 정리한다. 핵심은 동일한 [[TensorCores|텐서 코어]]의 개수를 늘리는 방식보다, 코어 크기와 메모리 계층을 키우며 계산/데이터 이동 불균형을 줄이는 방향으로 이동한 점이다.

[[AIInfrastructure]] 관점에서 텐서 코어 진화는 단일 기능 개선보다 **성능 밀도**, **데이터 이동 병목 완화**, **저정밀도 타입 도입**이 결합된 결과이며, 대규모 AI 추론/학습 워크로드에서 비용과 지연 개선을 함께 추구한다.

또한 전처리·파이프라인 제약을 줄이기 위해 [[MMA]] 명령 실행 방식이 워프(1 warp) 단위에서 [[Warpgroup]] 단위, 나아가 [[Blackwell]]의 [[TMEM]] 중심 데이터 이동으로 진화했다는 점이 핵심 통찰이다.

## Key Claims
- [[Volta]]는 텐서 코어 시대의 시작으로, 주로 [[FP16]] 입력·[[FP32]] 누적 경로를 강화한 [[HMMA]]로 ML 연산의 전력 효율을 개선했다.
- [[Turing]]은 INT8/INT4 정밀도 지원을 추가해 [[TensorCores]] 유연성과 적용 범위를 넓혔다.
- [[Ampere]]는 비동기 데이터 복사(cp.async)와 [[ldmatrix]] 최적화를 통해 레지스터 압력과 동기화 부담을 줄였고, [[BF16]] 표준화로 범용 AI 정밀도 선택을 넓혔다.
- [[Hopper]]는 [[ThreadBlockCluster]]와 [[TensorMemoryAccelerator]]를 도입해 SM 간 협업 범위를 확장하고 데이터 이동 단계를 더 큰 단위로 최적화했다.
- [[WGMMA]](Warp-group MMA)로 워프 협업 단위를 4개 워프로 확장해 더 큰 연산 형태와 더 넓은 형태 조합을 처리했다.
- [[Blackwell]]는 [[TMEM]]를 도입해 텐서 연산 데이터 경로를 레지스터 중심에서 공유 메모리·텐서 메모리 중심으로 이동시켰고, [[tcgen05.mma]] 기반 MMA.2SM까지 확장되었다.
- 텐서 코어는 세대가 지날수록 코어 수보다 코어 크기(예: MMA 형태 확장)와 메모리 계층 최적화에 비중이 이동했다.
- 데이터 이동은 계산보다 본질적으로 느리고 비싸므로, 높은 산술 강도(arithmetic intensity) 확보가 텐서 코어 확장 동력의 핵심이었다.
- 정밀도는 16비트에서 4비트로 내려오며 연산 처리량과 전력 효율을 높였고, 대규모 추론에서는 추론 정확도와 비용의 균형을 조정하는 주요 레버가 되었다.
- 구조적 희소성은 [[StructuredSparsity]](2:4, 4:8 형태)로 이론적 처리량 두 배 가능성을 제공하지만, 실제 엔드투엔드 추론에서 항상 이론치에 못 미치며 모델 압축 제약/커널 성숙도 제약이 남는다.
- 본 소스의 결론은 텐서 코어 성능 향상은 “더 큰 코어 + 더 많은 저정밀도 + 더 적은 데이터 이동 경로”의 조합으로 설명된다.

## Key Quotes
> "NVIDIA 텐서 코어는 AI 및 머신러닝의 기반이다."

> "MMA 명령은 겉보기에는 동기식에서 비동기식으로 갑자기 전환된 것처럼 보이지만, 실제로는 LDSM/레지스터 상호작용 제약을 완화하기 위한 점진적 비동기화 경로였다."

> "Blackwell은 레지스터를 사용해 행렬을 보유하는 방식에서 완전히 벗어나, 공유 메모리와 텐서 메모리를 결합한 경로로 이동했다."

## Connections
- [[NVIDIA]] — 텐서 코어 아키텍처 진화의 주체이며, Blackwell까지 성능 구조를 연속적으로 확장한 공급자.
- [[TensorCores]] — 본 문서의 중심 가속기 개념.
- [[Volta]] — 텐서 코어 도입 첫 상용 아키텍처.
- [[Turing]] — 2세대 텐서 코어의 정밀도 확장 전환.
- [[Ampere]] — 비동기 복사(cp.async), ldmatrix, BF16 확장 중심의 가속 경로.
- [[Hopper]] — [[ThreadBlockCluster]], [[TensorMemoryAccelerator]], [[WGMMA]] 기반으로 워프/SM 협업 구조를 재설계.
- [[Blackwell]] — [[TMEM]], tcgen05.mma, MMA.2SM 및 MXFP 계열 확장.
- [[CUDA]], [[PTX]], [[SASS]] — 텐서 코어 프로그래밍과 ISA 계층의 실무 기반.
- [[H100]], [[A100]], [[Tesla V100]] — 세대 비교의 대표 모델 문맥.
- [[StructuredSparsity]] — 텐서 코어 처리량 이슈 대응을 위한 가지치기 스킴.
- [[MxFP4]], [[FP8]], [[BF16]], [[FP16]], [[FP32]] — 정밀도 진화 경로.
- [[ArithmeticIntensity]] — 데이터 이동 병목 해소의 성능 해석 핵심 축.
- [[TCM]] — 데이터 이동과 연산 오버랩 설계를 설명하기 위한 개념적 배경.
- [[MemoryWall]] — DRAM/트랜지스터 속도 격차에서 파생된 병목 프레임.

## Contradictions
- 기존 위키의 [[Hopper]] 정밀도/FP8 관련 서술과 충돌하지 않지만, 본 소스는 Blackwell에서 [[INT4]]의 역할이 약화되고 [[INT8]] 처리량이 실제 운영 요구에 따라 상대적으로 조정될 수 있다는 점을 강조한다. 이는 일부 외부 서술의 “세대별 정밀도 단조 증가” 가정과 부분적으로 다른 뉘앙스를 가진다.
