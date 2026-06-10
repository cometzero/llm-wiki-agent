---
title: "Multi-View Generation"
type: concept
tags: [generation, multi-camera, optimization]
sources: [nvidia-omnidreams-2606-03159]
last_updated: 2026-06-10
---

# Multi-View Generation

여러 카메라视角의 이미지를 동시에 생성하는 기술.

## Challenge
Naive full attention: `O(N²T²)` complexity로expensive

## OmniDreams Solution: Factorized Attention
1. **Temporal attention**: 각 view 내에서 causal KV cache 사용
2. **Cross-view attention**: 동일 time step에서 view 간 correspondence

Result: `O(NT²) + O(N²)` complexity

## Camera Configuration
- 7 cameras: front-wide, front-telescope, front-left/right, rear-left/right, rear-tele
- 학습: 4 camera view 사용
- Resolution: 704×1280

## Performance
- Single-camera: GB300 1대에서 720p 68 FPS
- 4-camera: GB300 16대에서 720p 105 FPS

## Connections
- [[OmniDreams]] — 구현체
- [[KVCache]] — temporal attention 최적화
- [[Flex-Attention]] — 구현 기술
