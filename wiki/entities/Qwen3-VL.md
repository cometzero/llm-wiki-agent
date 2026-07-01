---
title: "Qwen3-VL"
type: entity
tags: [VLM, LLM, backbone, Alibaba]
sources: [qwen-robotnav-2606-18112, tbd-vla-2606-07895]
last_updated: 2026-07-01
---

## Summary
Qwen3-VL is Alibaba's multimodal LLM backbone that natively supports visual-language reasoning across vision encoder and LLM layers. Used as the base for Qwen-RobotNav's navigation model, inheriting SigLIP-2 ViT vision encoder with native dynamic-resolution and 2D-RoPE support.

## Key Properties
- Vision encoder: SigLIP-2 ViT (native dynamic-resolution, 2D-RoPE)
- LLM backbone processes visual tokens + text prompts together for spatial-language reasoning
- Final hidden state `E^A` feeds into task-specific action heads (e.g., 4-layer MLP for Qwen-RobotNav waypoints)
- Supports natural-language viewpoint and timestep tags inserted among visual tokens
- Language reasoning capabilities reused for camera/time identity tagging

## In This Wiki
- Qwen-RobotNav built on Qwen3-VL — adds lightweight action head for waypoint prediction
- TBD-VLA uses Qwen3-VL as backbone for block discrete diffusion VLA

## Connections
- [[Qwen-RobotNav]] — uses as backbone
- [[TBD-VLA]] — uses as backbone
- [[SigLIP]] — vision encoder foundation
