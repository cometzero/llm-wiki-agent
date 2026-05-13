---
title: "LingBot"
type: entity
tags: [vla, robot, embodied-ai]
last_updated: 2026-05-13
---

# LingBot

[[LingBot]]은 HumanNet 논문에서 VLA 모델로 사용된 robot-specific VLA(Vision-Language-Action) 시스템이다. HumanNet egocentric video subset으로 continued training한 후, downstream robot post-training corpus에 투입하여 validation loss 비교에 활용되었다.

## Overview
로봇 태스크를 위한 Vision-Language-Action 모델로, 인간의 언어 명령을 기반으로 로봇 행동을 생성한다.

## Connections
- [[VLA]] — LingBot은 VLA 아키텍처의 구체적 구현체
- [[HumanNet]] — LingBot-VLA post-training ablation으로 egocentric human video의 transfer value 검증
- [[Qwen]] — VLM backbone으로 비교 기준 제공
- [[Embodied AI]] — LingBot의 주요 적용 도메인

## Key Characteristics
- Robot-specific action space and control interface
- Continued training capability with external data sources
- Used in HumanNet experiments as primary VLA model
- Compared against: generic Qwen VLM, 100h real-robot CoBot, 20,000h LingBot real-robot data
