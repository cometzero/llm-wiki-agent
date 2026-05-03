---
title: "MFMA"
type: concept
tags:
  - Matrix Instructions
  - AMD
  - Registers
  - Tensor Compute
  - SIMD
sources:
  - 1-tmem-vs-registers-how-nvidia-and-amd-feed-tensor-compute-linkedin
last_updated: 2026-05-03
---

## Definition
[[MFMA]]는 [[AMD]] 워크로드에서 사용되는 Matrix Fused Multiply-Add 연산 형태군으로, 16x16/32x32 등 다양한 형태를 갖는다.

## Core Claim from Source
- 텐서 연산 수행의 핵심 기반으로, [[AGPR]](누산 전용)와 [[VGPR]](범용) 간 데이터 이동을 동반한다.
- 형태별로 레지스터 매핑/요구사항이 다르기 때문에, 커널 중간에 형태를 전환할 경우 추가 재포맷 비용이 발생한다.

## Tradeoff
[[MFMA]] 기반은 [[AMD]]의 대규모 레지스터 전략과 결합되며, 고유 형태 유연성은 높지만 SW 측에서는 높은 규칙 설계 비용을 만든다.

## Connections
- [[AGPR]]
- [[VGPR]]
- [[RegisterFile]]
- [[AMD]]
- [[Wavefront]]
- [[MatrixInstruction]]

## Practical Impact
텍스트의 핵심은 이념이 아니라 비용이다. [[MFMA]]의 형태 다양성은 이론적 표현력을 제공하지만, 실제 최적화에서 코드 경로 수 증가와 레이아웃 관리 복잡도를 유발한다.