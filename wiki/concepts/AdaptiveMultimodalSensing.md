---
title: "Adaptive Multimodal Sensing"
type: concept
tags: [multimodal, sensor, VLA, RGB, temperature, audio, radar]
sources: [embodied-cpp-2607-02501-references]
last_updated: 2026-07-08
---

## Overview
RGB 카메라만 사용하는 기존 VLA의 한계를 넘어 temperature, audio, radar 등 다양한 sensor를 tool처럼 호출하고, sensor measurement를 grounded sensor image로 변환해 VLA backbone과 결합하는 기법. [[MuseVLA]]가 대표적 사례로, runtime에서는 새로운 sensor modality와 grounded intermediate representation 지원이 필요하다.

## Key Claims
- RGB-only limitation: thermal, audio, radar sensor 미활용
- Tool-like sensor invocation: temperature, audio, radar를 sensor tool로 호출
- Grounded sensor image: sensor measurement를 이미지 형식으로 변환
- Runtime implication: 새로운 sensor modality와 intermediate representation 지원 필요
- Extensible embodied I/O: Embodied.cpp에서 지원해야 하는 설계 원칙

## Related Concepts
- [[SensorFusion]] — sensor 통합 관련
- [[VLA]] — 적용 모델
- [[MuseVLA]] — 대표 사례
- [[ExtensibleIO]] — 설계 방향

## Connections
- [[Embodied.cpp]] — extensible embodied I/O 지원
- [[MuseVLA]] — adaptive multimodal sensing 사례
- [[EmbodiedAI]] — 적용 도메인
