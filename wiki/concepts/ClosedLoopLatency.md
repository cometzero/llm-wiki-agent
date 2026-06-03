---
title: "Closed-Loop Latency"
type: concept
tags: [robotics, latency, real-time-control]
sources: [visualthink-vla-2605-30011-ko-analysis]
last_updated: 2026-06-03
---

## Overview
Closed-loop latency는 VLA(Vision-Language-Action) 정책이 observation을 입력받아 action을 출력하는 데 걸리는时间来 정의된다. 실시간 robot control에서 critical한 지표이다.

## Problem
- Textual CoT(Chain-of-Thought) 기반 VLA: ~8.377s latency
- 이는 실시간 robot control에 부적합

## Solution: Visual Intermediate Reasoning
- VisualThink-VLA: ~0.367s latency
- 22.8× speedup 달성
- Sub-second 수준으로 실시간 control 가능

## Evaluation
- 단순 VQA/open-loop reasoning score가 아닌 simulation 또는 real-robot execution에서 action이 올바른 target/trajectory로 이어지는지 측정
- VLA의 deployment relevance 평가에 더 적합

## Related Concepts
- [[VLA]] — 적용 대상
- [[ECoT]] — latency 문제의 원인
- [[VisualIntermediateReasoning]] — 해결책
- [[RealTimeControl]] — 응용 분야
