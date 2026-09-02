---
title: "PonderPounce"
type: entity
tags: [vision-language-action, robotics, memory, dual-system, control]
sources: [ponderpounce-2608-24115-learning, ponderpounce-2608-24115-analysis, ponderpounce-2608-24115-paper-ko]
last_updated: 2026-09-02
---

[[PonderPounce]] is a dual-system [[VisionLanguageAction|VLA]] framework that reuses a pretrained [[MultimodalModel|MLLM]]'s native causal context as episode memory. [[Ponder]] acts as the slow [[System 2]] context accumulator and reasoner, while [[Pounce]] serves as the fast [[System 1]] action generator that consumes the latest ready continuous cognition state plus freshness information.

The main design point is not adding an external memory bank, but turning the model's own context into a reusable control substrate. The approach makes temporal freshness, async scheduling, and stale-context fallback part of the interface, not an afterthought.

## Related Concepts
- [[DualSystemArchitecture]]
- [[PersistentMemory]]
- [[InferencePlanning]]
- [[TemporalDecay]]
- [[ActionGrounding]]
- [[ActionChunking]]
