---
title: "NVIDIA GR00T"
type: entity
tags: [VLM, VLA, EmbodiedAI, Robotics]
sources: [embodiedmidtrain-2604-20012-ko-analysis, embodiedmidtrain-2604-20012-references, embodiedmidtrain-2604-20012-study-guide, policytrim-2606-22540]
last_updated: 2026-06-24
---

# NVIDIA GR00T

## Summary

NVIDIA GR00T는 범용 로봇/휴머노이드용 foundation model 계열이며, VLA와 embodied policy 연구의 대표 비교 축이다. PolicyTrim 논문에서는 π0.5, OpenVLA-OFT와 함께 intrinsic policy efficiency 개선 대상 backbone으로 등장한다.

## Relevance to PolicyTrim

PolicyTrim은 GR00T 같은 generalist robot policy도 action chunk tail degradation과 redundant physical step 문제를 가질 수 있음을 보여준다. 따라서 deployment 효율성은 모델 크기나 per-step latency뿐 아니라 policy가 얼마나 긴 chunk를 안정적으로 실행하고 불필요한 step을 줄이는지로도 평가해야 한다.

## Connections

- [[EmbodiedMidtrain]] — GR00T/NVIDIA robotics foundation model 맥락의 기존 source.
- [[VLA]] — GR00T가 속한 model paradigm.
- [[VLM]] — vision-language backbone과 연결.
- [[PolicyTrim]] — GR00T의 intrinsic policy efficiency를 개선하는 framework.
- [[Pi05]] — PolicyTrim에서 함께 비교된 VLA backbone.
- [[OpenVLA-OFT]] — PolicyTrim에서 함께 비교된 open VLA backbone.
