---
title: "VLAct"
type: concept
tags: [vision-language-action, robotics, pretraining]
sources: [vlact-2608-27550-paper-ko]
last_updated: 2026-09-02
---

[[VLAct]]는 pretrained [[VisionLanguageModel|VLM]]의 prior를 보존하면서 heterogeneous robot data로 continued pretraining을 수행해 [[VisionLanguageAction|VLA]] representation을 강화하는 recipe다. 핵심은 더 많은 data 자체보다 representation preservation, decoder diversity, and action-space alignment에 있다.

## Core Ideas
- shallow-layer protection
- caption mixing
- multi-head continuous action co-supervision
- partially unified action layout
- downstream task-specific head reinitialization

## Related Concepts
- [[VisionLanguageModel]]
- [[VisionLanguageAction]]
- [[CrossEmbodimentLearning]]
- [[ActionSpaceAlignment]]
- [[DataRecipe]]
- [[ActionHead]]
- [[RepresentationLearning]]
