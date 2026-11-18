---
title: "Frontier VLM Feature Transfer"
type: "concept"
tags: ["VLA", "representation-transfer", "robotics"]
sources: ["scalevla-2611-21607-paper-ko", "scalevla-2611-21607-analysis", "scalevla-2611-21607-references", "scalevla-2611-21607-learning"]
last_updated: "2026-11-18"
---

# Frontier VLM Feature Transfer
대형 pretrained VLM의 text output이 아니라 중간 multimodal token representation을 task-specific numerical action head에 전달하는 접근이다. [[ScaleVLA]]는 backbone freeze, causal-encoder early readout, ordered modality tokens, demonstration-trained adapter/flow-matching DiT를 사용한다.

## 구분
- Explicit reasoning/tool invocation 또는 textual action generation과 다르다.
- Feature cache는 training 비용을 줄여도 online inference/storage 비용을 제거하지 않는다.
- Representation transfer는 teacher/student weight distillation과 같지 않다.
- [[GroundingPI]]의 precise perceptual foundation과 비교할 수 있지만 pure parameter count 효과는 backbone family/data/readout/hardware confound를 따로 통제해야 한다.
- [[ActionDynamicsPolicy]]의 physical-time integration과 flow generation time은 별개다.

## Deployment Boundary
Chunk latency와 actuator frequency, observation age를 분리한다. Stronger frozen features가 robot/vehicle dynamics limit, collision checking, independent safety fallback을 대신하지 않는다. NPU/edge 전이는 distillation/quantization 및 실제 hardware end-to-end measurement가 필요한 후속 가설이다.

## Sources
- [[scalevla-2611-21607-paper-ko]]
- [[scalevla-2611-21607-analysis]]
- [[scalevla-2611-21607-references]]
- [[scalevla-2611-21607-learning]]
