---
title: "Qwen3-VL"
type: entity
tags: [VLM, vision-language-model, backbone]
sources: [qwen-robotnav-2606-18112, tbd-vla-2606-07895]
last_updated: 2026-07-01
---

## Overview
[[Qwen3VL]]는 Qwen-RobotNav의 백본으로 사용된 Vision-Language Model이다. SigLIP-2 vision encoder와 LLM을 결합하여 multi-view RGB 입력과 자연어 명령을 처리한다.

## Role in Navigation
- Vision encoder: multi-view camera input processing
- LLM backbone: instruction understanding, scene reasoning
- Action hidden state extraction: trajectory regression을 위한 hidden state 제공

## Connections
- [[QwenRobotNav]] — navigation model built on Qwen3-VL
- [[VisionLanguageAction]] — model family
