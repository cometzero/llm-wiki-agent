---
title: "WaveGroup Tensor Execution"
type: concept
tags:
  - Warp
  - WarpGroup
  - Tensor Core
  - Synchronization
  - Asynchronous Pipeline
sources:
  - 1-tmem-vs-registers-how-nvidia-and-amd-feed-tensor-compute-linkedin
last_updated: 2026-05-03
---

## Definition
WaveGroup Tensor Execution은 여러 [[Warp]]가 협업해 하나의 텐서 행렬 곱셈 단위를 처리하는 실행 패턴을 의미한다. 본 소스에서는 [[NVIDIA]]의 [[Blackwell]]에서 [[Warp]] 4개가 결합한 128-thread 워프그룹이 핵심 예시로 등장한다.

## Operating Characteristics
- [[WGMMA]]는 데이터 준비·연산의 동기화가 묵시적으로 구성된 단위로 이해된다.
- 워프그룹 단위는 주소 계산/동기화 분담을 단순화하고, 주소 지정이 규칙화되는 편이다.
- 파이프라인이 비동기 발행될 수 있어, 대기 지연이 코드 전체 점유율로 전이되기 쉬운 문제를 줄인다.

## Contrast with AMD Wave Approach
[[AMD]]는 동일한 목표를 [[Wavefront]]/레지스터 기반 접근으로 달성하려 했으나, 본 소스에서 지적되듯 생산자-소비자 분리가 [[NVIDIA]]만큼 매끄럽게 이식되지 않을 수 있다.

## Relevance
이 실행 패턴은 단일 하드웨어 성능 수치가 아닌 '코드 구조 수명주기' 관점에서 중요하다. 즉, 아키텍처별로 동일한 목표를 두고도 스케줄러/메모리 배치/동기화 패턴이 달라진다.