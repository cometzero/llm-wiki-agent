---
title: "Teacher-Student Distillation"
type: concept
tags: [VLA, Distillation, Latency]
sources: [visualthink-vla-2605-30011, visualthink-vla-2605-30011-ko-analysis, visualthink-vla-2605-30011-learning]
last_updated: 2026-06-03
---

## Definition
Teacher-student distillation은大型 teacher 모델의 knowledge를 경량 student 모델로 전달하는 기법으로, VLA에서는 teacher action-token distribution p_T^τ와 student distribution p_S^τ 사이의 divergence를 최소화한다.

## Purpose in VisualThink-VLA
Sparse routed interface가 dense evidence teacher의 성능을 보존하도록 함.
- **Teacher**: FullSoft teacher — 전체 teacher distribution p_T^τ 제공
- **Student**: sparse routed interface — 경량화된 selective routing 기반
- **Objective**: KL divergence 최소화하여 경량 모델의 [[ActionGrounding]] 능력 확보

## Key Benefit
Textual CoT 없이도 teacher의 semantic reasoning 능력을 student에게 전이하여:
- Latency 감소 (22.8× speedup)
- 실시간 실행 가능
- Action quality 보존

## Connections
- [[VisualThink-VLA]] — 메인 연구
- [[VisualReasoning]] — student가 활용하는 reasoning 방식
- [[SelectiveRouting]] — student의 핵심 메커니즘