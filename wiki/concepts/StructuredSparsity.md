---
title: "Structured Sparsity"
type: concept
tags: [AI, Optimization, TensorCores]
sources: [nvidia-tensor-core-evolution-from-volta-to-blackwell]
last_updated: 2026-05-03
---

## Definition

[[StructuredSparsity]]는 가중치/연산 구조를 제약(patterned sparsity)해 계산량을 줄이고 메모리 사용량을 낮추는 희소성 최적화 기법이다.

## Examples in this source

- [[Ampere]]: 2:4 희소성 패턴
- [[Blackwell]]: NVFP4 기반 4:8 페어별 희소성 패턴

## Practical caveats

- 압축/메타데이터 오버헤드가 존재
- 모델 정확도 유지 및 정규화 최적화 난이도
- 실제 엔드투엔드 커널(특히 밀집 커널 대비)에서 이론치 2배 성능을 항상 달성하지 못함

## Cross-links

- [[TensorCores]]
- [[Ampere]]
- [[Blackwell]]
- [[FFN]]
- [[MoE]]