---
title: "ECoT (Explicit Chain of Thought)"
type: concept
tags: [reasoning, chain-of-thought, vla]
sources: [visualthink-vla-2605-30011-ko-analysis]
last_updated: 2026-06-03
---

## Overview
ECoT(Explicit Chain of Thought)는 VLA(Vision-Language-Action) 정책에서 textual reasoning trace를 생성하여 decision-making의 설명 가능성을 높이는 접근법이다. 그러나 visual grounding 약함과 높은 closed-loop latency 문제가 있다.

## Problems with ECoT for VLA
1. **Visual Grounding 약함**: Text representation이 실제 시각적 환경과 연결 부족
2. **Closed-Loop Latency 높음**: ~8.377s로 실시간 robot control에 부적합

## Solution: Visual Intermediate Reasoning
- [[VisualThinkVLA]]에서 ECoT 대신 visual evidence states 사용 제안
- 22.8× latency reduction (8.377s → 0.367s)
- Visual grounding 강화

## Related Concepts
- [[VisualIntermediateReasoning]] — 대안 접근법
- [[ClosedLoopLatency]] — 해결하려는 문제
- [[SemanticGrounding]] — 관련 문제 영역
