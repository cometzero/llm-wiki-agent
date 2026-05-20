---
title: "Robot Foundation Model"
type: concept
tags: [robotics, foundation-model, AI]
sources: [humannet-2605-06747-references, nvidia-gr00t-vs-gemini-robotics-vs-pi-로봇의-뇌는-어떻게-다르게-설계됐을까-vla-모델-3대장-비교-분석, ashok-elluswamy-building-foundational-models-for-robots-at-tesla]
last_updated: 2026-05-13
---

## Definition
Robot Foundation Model(로봇 파운데이션 모델)은 대규모 데이터로 사전 학습되어 다양한 로봇 태스크에 전이 가능한 범용 로봇 정책을 학습하는 접근으로, [[VLA]]가 핵심 구현체가 된다.

## Key Approaches
- **Heterogeneous Robot Data**: [[Open X-Embodiment]], [[DROID]] — 다양한 로봇 플랫폼 데이터 통합
- **Human-Robot Data Mixture**: [[GR00T-N1]], [[LingBot-VLA]] — 인간 데이터 혼합
- **Human Video Scaling**: [[HumanNet]] — 100만 시간 인간 중심 비디오로 스케일링

## Data Bottleneck Problem
로봇 데이터 수집의 높은 비용([[DROID]] 인용)이 핵심 병목으로, [[HumanNet]]은 인간 중심 비디오로 이 문제를 우회한다.

## Connections
- [[HumanNet]] — 인간 비디오 기반 로봇 파운데이션 모델 학습
- [[VLA]] — 로봇 파운데이션 모델의 핵심 구현
- [[Open X-Embodiment]] — 이종 로봇 데이터 기반 범용 모델
- [[GR00T-N1]] — 인간/로봇 혼합 데이터 활용 VLA 모델

## Summary
로봇 파운데이션 모델은 [[HumanNet]]의 핵심 목표이며, 인간 중심 비디오의 대규모 확보를 통해 로봇 데이터 병목을 우회하는 방향이 제시된다.
