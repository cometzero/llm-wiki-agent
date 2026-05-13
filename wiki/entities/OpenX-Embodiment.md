---
title: "Open X-Embodiment"
type: entity
tags: [robotics, foundation-model, dataset, VLA]
sources: [humannet-2605-06747-references, nvidia-gr00t-vs-gemini-robotics-vs-pi-로봇의-뇌는-어떻게-다르게-설계됐을까-vla-모델-3대장-비교-분석, ashok-elluswamy-building-foundational-models-for-robots-at-tesla, a-peek-into-tesla-s-autonomous-future-core-tech-revealed-by-vp-ashok-elluswamy-at-iccv25-wdfm-ad]
last_updated: 2026-05-13
---

## Overview
Open X-Embodiment(통칭 RT-X)은 이종(heterogeneous) 로봇 로그를 통해 로봇 파운데이션 모델 스케일링의 대표 사례로, 다양한 로봇 플랫폼의 데이터를 통합하여 범용 로봇 정책 학습을 가능케 한다. [[HumanNet]]은 robot data 병목 문제를 인간 비디오 데이터로 우회하는 접근을 취하며, Open X-Embodiment와 상호 보완적 관계에 있다.

## Key Characteristics
- **Data Source**: 이종 로봇 플랫폼의 조작 데이터
- **Goal**: Robot foundation model scaling
- **Approach**: Heterogeneous robot logs 통합
- **Role in HumanNet**: "robot data는 비싸다"는 문제의식의 핵심 인용 대상

## Connections
- [[DROID]] — real-world robot manipulation dataset
- [[GR00T N1]] — heterogeneous data mixture를 사용하는 [[VLA]] 계열
- [[HumanNet]] — robot data 병목 우회方案的 비교 대상
- [[RobotFoundationModel]] — 범용 로봇 파운데이션 모델 구축 목표 공유

## References
- https://robotics-transformer-x.github.io/
