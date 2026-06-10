---
title: "Qwen2.5-VL-7B"
type: entity
tags: [VLM, captioning, Alibaba]
sources: [nvidia-omnidreams-2606-03159]
last_updated: 2026-06-10
---

# Qwen2.5-VL-7B

Alibaba의 Vision-Language Model로, OmniDreams의 학습 데이터 caption 생성에 사용된다.

## Usage in OmniDreams
10초 window마다 weather, lighting, time-of-day, traffic, driving behavior를 설명하는 caption을 생성. Short/medium/long caption을 혼합하여 학습.

## Connections
- [[OmniDreams]] — caption 생성 도구
- [[VLM]] — 상위 개념
