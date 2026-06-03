---
title: "Visual Reasoning"
type: concept
tags: [VLA, Reasoning, Latency]
sources: [visualthink-vla-2605-30011, visualthink-vla-2605-30011-ko-analysis, visualthink-vla-2605-30011-learning]
last_updated: 2026-06-03
---

## Definition
Visual reasoning는 textual Chain-of-Thought(CoT) 대신 시각적 evidence states를 활용하여 reasoning을 수행하는 접근법이다.

## Problem with Textual CoT
- Latency过大: textual CoT decode가 8.377초 소요
- 실시간 시스템 부적합: 환경 변화 후 실행되어 [[UnsafeAction]] 발생 가능
- Language reasoning 결과를 action head가 소비 가능한 structured state로 보존 어려움

## VisualThink-VLA Solution
1. **Candidate Visual Evidence Bank**: RGB 입력을 후보 시각적 evidence로 변환
2. **Selective Router**: instruction 기반으로 relevant evidence 선택
3. **Visual State Composer**: 선택된 evidence를 compact visual/BEV evidence로 구성
4. **Latency Result**: 8.377s → 0.367s (22.8× speedup)

## Key Insight
실시간 시스템에서는 textual CoT보다 compact visual/BEV evidence 또는 verified symbolic state가 안전하고 효율적.

## Applications
- 자율주행: lane/object/route/trajectory candidate로 block target 대체
- Robot control: visual state가 action decoder 직접 소비
- Closed-loop systems: 환경 변화에 신속한 반응 가능

## Connections
- [[VisualThink-VLA]] — 메인 연구
- [[ActionGrounding]] — reasoning 결과의 action 변환
- [[ClosedLoop]] — 실시간 제어 시스템
- [[SelectiveRouting]] — evidence 선택 메커니즘