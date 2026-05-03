---
title: "Hopper"
type: concept
tags: [NVIDIA, GPUArchitecture, TensorCores]
sources: [nvidia-tensor-core-evolution-from-volta-to-blackwell]
last_updated: 2026-05-03
---

## Definition

[[Hopper]]는 NVIDIA 데이터센터 텐서 아키텍처의 중간 전환점으로, 워프 협업 단위를 재구성하고 전용 메모리 전송 경로를 도입해 추론·학습 워크로드의 데이터/연산 동시성을 높인 세대이다.

## Key characteristics

- [[ThreadBlockCluster]] 개념 도입으로 CTA-클러스터 레벨 협업 구조 강화
- [[TensorMemoryAccelerator]]를 통해 비동기 데이터 이동 단위를 확대
- [[WGMMA]](Warp-group MMA) 도입으로 더 큰 형태의 텐서 연산과 확장성 확보
- [[Hopper]]의 메모리·메시지 설계는 [[Blackwell]]의 [[TMEM]] 흐름으로 연결됨

## Cross-links

- [[Volta]], [[Ampere]], [[Blackwell]]
- [[ThreadBlockCluster]]
- [[TensorMemoryAccelerator]]
- [[WGMMA]]
- [[TensorCores]]