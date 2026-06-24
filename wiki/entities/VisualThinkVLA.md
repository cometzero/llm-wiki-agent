---
title: "VisualThink-VLA"
type: entity
tags: [vla, visual-reasoning, robotics, latency]
sources: [visualthink-vla-2605-30011-ko-analysis, visualthink-vla-2605-30011, world-action-models-survey-2606-20781-analysis]
last_updated: 2026-06-24
---

## Overview

VisualThink-VLA는 [[VLA]](Vision-Language-Action) 정책의 reasoning latency를 줄이기 위해 textual Chain-of-Thought 대신 visual intermediate reasoning을 사용하는 접근법이다. Compact visual evidence states를 action policy에 주입하여 sub-second 수준의 closed-loop latency를 달성한다.

## Key Components

- **Evidence Bank**: 후보 visual evidence states 저장소.
- **Selective Router**: instruction에 따라 적절한 evidence 선택.
- **Visual State Composer**: 선택된 evidence들을 통합해 VLA 입력 구성.

## Technical Details

- Training: FullSoft teacher distillation, route supervision, counterfactual utility dynamic loss.
- Inference: hard routing으로 비용 절감.
- Results: textual CoT latency 8.377s → visual reasoning 0.367s (22.8× speedup).

## WAM Connection

World Action Models survey 관점에서는 VisualThink-VLA가 video rendering 없이 compact visual evidence를 action path에 넣는 video-generation-free/action-facing reasoning 계열과 연결된다. 다만 논문 자체는 WAM taxonomy 논문이 아니라 VLA policy latency와 grounding을 직접 다룬다.

## Related Entities

- [[ECoT]] — textual CoT의 대안.
- [[SemanticGrounding]] — 해결하려는 문제 영역.
- [[RoboSemanticBench]] — 관련 benchmark.
- [[WorldActionModel]] — action-facing predictive/reasoning substrate 관점에서 비교 가능.
