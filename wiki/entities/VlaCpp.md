---
title: "vla.cpp"
type: entity
tags: [VLA, C++, inference-runtime, predecessor]
sources: [embodied-cpp-2607-02501-references]
last_updated: 2026-07-08
---

## Overview
Portable C++ inference runtime for Vision-Language-Action (VLA) models. [[Embodied.cpp]]의 직접적인 predecessor로, 여러 VLA architecture를 하나의 runtime으로 가져오지만 VLA-centric 접근으로 WAM과 modular multi-component optimization이 제한적이다.

## Key Papers
- Embodied.cpp의 선행 시스템으로 citation됨 (arXiv:2607.02501)

## Architecture
- Single-runtime approach: 여러 VLA architecture 통합 지원
- C++ inference runtime: portability 및 on-device deployment 타겟
- Limitations: WAM(Wrapped Action Model) 미지원, modular multi-component optimization 제한적

## Connections
- [[Embodied.cpp]] — 직접적 successor; VLA+WAM, robot+simulator, heterogeneous hardware 지원으로 확장
- [[VLA]] — 핵심 타겟 모델 유형
- [[WorldActionModel]] — vla.cpp에서는 미지원, Embodied.cpp에서 first-class 지원
- [[OnDeviceInference]] — 공통 타겟 도메인
