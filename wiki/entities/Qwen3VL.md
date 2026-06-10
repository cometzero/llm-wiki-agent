---
title: "Qwen3-VL"
type: entity
tags: [vlm, vision-language-model, backbone]
sources: [tbd-vla-2606-07895-analysis]
last_updated: 2026-06-10
---

## Overview
Qwen3-VL은 Alibaba Cloud에서 개발한 vision-language 모델 시리즈의 최신 버전으로, TBD-VLA의 backbone으로 채택된 2B规模的 VLM이다. Visual observation과 language instruction을 처리하는 multimodal capability를 갖추고 있어 VLA(Vision-Language-Action) policy의 foundation model로 활용된다.

## Key Properties
- **Parameters**: 2B规模 (TBD-VLA 사용 기준)
- **Architecture**: Vision encoder + Language model decoder
- **Role in TBD-VLA**: Visual observation, proprioceptive state, language instruction을 통합 처리하는 prompt generator 및 action token decoder

## Related Concepts
- [[VisionLanguageAction]] — VLA policy의 foundation model로 활용
- [[TBDVLA]] — Qwen3-VL을 backbone으로 사용하는 VLA framework
- [[VisualThinkVLA]] — 또 다른 VLA reasoning approach

## References
- TBD-VLA paper: https://huggingface.co/papers/2606.07895
- Qwen3-VL: Alibaba Cloud multimodal model
