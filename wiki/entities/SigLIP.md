---
title: "SigLIP"
type: entity
tags: [vision-encoder, VLM, contrastive-learning]
sources: [qwen-robotnav-2606-18112]
last_updated: 2026-07-01
---

## Summary
SigLIP is a vision encoder family (including SigLIP-2 ViT) used as the visual backbone in Qwen3-VL. Provides native dynamic-resolution and 2D-RoPE positional encoding for the vision pipeline.

## Key Properties
- SigLIP-2 ViT: used in Qwen3-VL's vision encoder
- Supports native dynamic-resolution input
- 2D-RoPE (Rotary Position Embedding) for spatial awareness

## Connections
- [[Qwen3-VL]] — integrated as vision encoder
- [[Qwen-RobotNav]] — inherits via Qwen3-VL backbone
