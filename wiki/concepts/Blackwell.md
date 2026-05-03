---
title: "Blackwell"
type: concept
tags: [NVIDIA, GPUArchitecture, TensorCores, AIHardware]
sources: [nvidia-tensor-core-evolution-from-volta-to-blackwell]
last_updated: 2026-05-03
---

## Definition

[[Blackwell]]는 텐서 코어 계산 구조를 레지스터 중심에서 텐서 메모리 중심으로 이동시킨 차세대 NVIDIA 아키텍처로, 큰 MMA 형태, 협업 단위 세분화, 그리고 저정밀도 연산 도입이 동시에 진전된 세대이다.

## Key characteristics

- 텐서 연산의 스테이징 계층이 [[TMEM]] 중심으로 재구성
- [[tcgen05.mma]] 기반의 5세대 텐서 코어 경로와 [[MMA.2SM]] 같은 다중 SM 협업 방식
- [[StructuredSparsity]]의 2:4→4:8 패턴 및 NVFP 계열 정밀도 적용
- 데이터 로딩/저장 파이프라인의 비동기화를 강화해 처리량/지연 균형 개선

## Cross-links

- [[Hopper]]
- [[TMEM]]
- [[TensorCores]]
- [[MMA]]
- [[StructuredSparsity]]
- [[MXFP4]]