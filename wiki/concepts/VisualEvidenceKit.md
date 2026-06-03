---
title: "VisualEvidence-Kit"
type: concept
tags: [vla, dataset, supervision, audit]
sources: [visualthink-vla-2605-30011]
last_updated: 2026-06-03
---

## Definition
VisualEvidence-Kit은 VLA control을 위한 route-grounded supervision/audit resource로, VisualEvidence-Agent가 생성한 754.7k规模的 VLA instruction supervision/audit set이다.

## Components
1. **VisualEvidence-Agent**: raw frames와 trajectory metadata → evidence extraction 수행
2. **VisualEvidence-Set**: 754.7k instruction supervision/audit set

## Dataset Structure
VisualEvidence-Set은 다음을 포함:
- **Observation**: RGB observation
- **Instruction Context**: language instruction
- **Feature Manifest**: evidence feature description
- **Supervised Route Target**: 학습용 evidence channel selection target
- **Counterfactual Channel Utilities**: alternative channel utility
- **Channel-Grounded Trace**: evidence channel별 trajectory trace

## Subsets
- **Full-Clean**: 전체 정제 데이터
- **HQ-Trace**:高质量 trace subset
- **Gold-Faithfulness**: 정답 faithfulness 기준 데이터

## Purpose
- VLA의 visual intermediate reasoning 학습 위한 supervision 제공
- Evidence channel routing 학습용 ground truth 제공
- Counterfactual analysis 통한 channel utility 평가

## Related Concepts
- [[VisualThink-VLA]]: VisualEvidence-Kit을 활용하는 VLA 시스템
- [[VisualEvidenceAgent]]: VisualEvidence-Kit 생성 agent
- [[VLA]]: Vision-Language-Action policy framework
