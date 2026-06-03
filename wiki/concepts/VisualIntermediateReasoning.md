---
title: "Visual Intermediate Reasoning"
type: concept
tags: [vla, reasoning, visual-grounding]
sources: [visualthink-vla-2605-30011-ko-analysis]
last_updated: 2026-06-03
---

## Overview
Visual Intermediate Reasoning은 [[VLA]] 정책에서 textual Chain-of-Thought 대신 visual evidence states를 intermediate reasoning 단계로 사용하는 패러다임이다. Visual grounding을 강화하면서 동시에 closed-loop latency를 줄이는 것이 목표이다.

## Problem with Textual CoT
- [[ECoT]](Explicit Chain of Thought)는 설명 가능성을 제공하지만:
  - Visual grounding이 약함
  - Closed-loop latency가 너무 커 실시간 robot control에 부적합

## Solution: Visual Evidence States
- Compact visual evidence를 action policy에 직접 주입
- Text representation 없이 visual grounding 강화
- Sub-second latency 달성 가능

## Architecture
```
current/previous RGB + instruction
  → evidence bank
  → selective router
  → visual state composer
  → frozen/base VLA action decoder
  → action token/robot action
```

## Related Concepts
- [[ECoT]] — 대안 접근법
- [[SemanticGrounding]] — 해결하려는 문제
- [[ClosedLoopLatency]] — 개선 목표
- [[VisualThinkVLA]] — 구체적 구현
