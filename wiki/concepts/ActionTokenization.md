---
title: "Action Tokenization"
type: concept
tags: [tokenization, vla, discrete-representation]
sources: [tbd-vla-2606-07895, tbd-vla-2606-07895-learning]
last_updated: 2026-06-10
---

## Definition

Action Tokenization은 [[VLA]]에서 continuous action feature를 discrete token sequence로 변환하는 절차이다. 이 변환으로 [[VLM]]이 action generation에 직접 관여할 수 있게 된다.

## Purpose

1. **Language/Vision 통합**: discrete token으로 unified representation 달성
2. **Direct Action Grounding**: VLM representation과 action space 직접 연결
3. **Analysis 지원**: language model과 action generation 사이 직접 분석 가능

## Process

1. Continuous action vector를 discretize
2. Vocabulary에 매핑하여 token ID 생성
3. [[BlockDiffusion]]으로 순차/병렬 생성
4. Token을 다시 continuous action으로 복원

## Why Discrete Over Continuous?

| Aspect | Continuous Expert | Discrete Tokenization |
|--------|-------------------|----------------------|
| VLM Integration | Indirect | Direct |
| Analysis | Difficult | Straightforward |
| Latency | Higher | Lower |
| Temporal Modeling | Implicit | Explicit via [[TemporalAR]] |

## Related Concepts

- [[BlockDiffusion]] — token의 병렬 디노이징
- [[VLAPolicy]] — action token 사용 policy
- [[DiscreteDiffusion]] — discrete token 기반 diffusion
- [[ActionGrounding]] — language-vision-action 연결

## Connections

- [[TBDVLA]] — discrete action tokenization 사용
- [[FastDVLA]] — low-latency action generation
- [[VisualThinkVLA]] — visual reasoning과 action grounding
- [[RoboSemanticBench]] — semantic grounding 진단 benchmark

## Applications

- [[RoboticManipulation]] — 로봇 조작 정책
- [[AutonomousNavigation]] — 자율주행 planning
