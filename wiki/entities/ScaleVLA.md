---
title: "ScaleVLA"
type: "entity"
tags: ["VLA", "representation-transfer", "robotics"]
sources: ["scalevla-2611-21607-paper-ko", "scalevla-2611-21607-analysis", "scalevla-2611-21607-references", "scalevla-2611-21607-learning"]
last_updated: "2026-11-18"
---

# ScaleVLA
Ruixi Yu 외 12인의 arXiv:2611.21607v1(2026-11-16) 연구. [[FrontierVLMFeatureTransfer]]로 frozen 552B DeepSeek-V4.1-Flash-1017의 causal-encoder token을 trainable action DiT에 전달한다. VLM decoder 및 autoregressive reasoning은 실행하지 않는다.

## Architecture
5120-dimensional ordered image/non-image token → layer norm/linear projection/4-layer adapter → 32-layer action DiT → 4 flow steps → numerical action chunk. Backbone을 freeze하고 action-side component를 scratch train한다.

## Evidence Boundary
LIBERO/PRO/RoboCasa/DexJoCo 및 실물 charger insertion의 manipulation 결과다. LIBERO-PRO 평균 45.1%와 실물 9/10·8/15, 4×H200 RoboCasa median 215.8ms를 보고한다. Full-data normalization, single training seed, successful-trial time, timing/backend equivalence 미검증을 함께 보존한다. 차량 closed-loop·NPU·formal safety 실험은 없다.

## Connections
[[GroundingPI]]는 precise perception foundation의 action transfer를 다루고, [[ODEPolicy]]는 physical-time action dynamics를 바꾼다. ScaleVLA는 backbone representation scale/interface를 바꾼다.

## Sources
- [[scalevla-2611-21607-paper-ko]]
- [[scalevla-2611-21607-analysis]]
- [[scalevla-2611-21607-references]]
- [[scalevla-2611-21607-learning]]
