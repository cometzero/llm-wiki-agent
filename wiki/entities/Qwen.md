---
title: "Qwen"
type: entity
tags: [vlm, foundation-model, open-source]
last_updated: 2026-05-13
---

# Qwen

[[Qwen]]는 Alibaba Cloud가 개발한 대규모 Vision-Language Model(VLM) 시리즈이다. HumanNet 분석에서는 VLM backbone으로 사용되어, human-centric video 데이터로 continued training后的 transfer value 검증에 활용되었다.

## Overview
开源多模态基础模型，支持图像、视频、音频等多种模态的理解和生成。

## Connections
- [[HumanNet]] — VLM backbone으로 사용되어 egocentric video transfer 실험에 활용
- [[VLA]] — VLM backbone으로서 VLA 시스템의 시각-언어 이해 담당
- [[LingBot-VLA]] — HumanNet 논문에서 함께 비교된 VLA 모델

## Key Characteristics
- Large-scale pretraining on diverse web data
- Strong zero-shot and few-shot capabilities
- Vision-language alignment for downstream tasks
- Used as baseline in HumanNet experiments
