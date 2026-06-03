---
title: "Selective Routing"
type: concept
tags: [vla, routing, architecture]
sources: [visualthink-vla-2605-30011-ko-analysis]
last_updated: 2026-06-03
---

## Overview
Selective routing은 VisualThink-VLA 아키텍처에서 instruction과 context에 따라 evidence bank에서 적절한 visual evidence states를 선택하는 메커니즘이다. Route supervision을 통해 학습되고, inference에서는 hard routing으로 효율을 높인다.

## Role in Pipeline
```
evidence bank → **selective router** → visual state composer
```

## Training vs Inference
- Training: route supervision으로 올바른 routing 학습
- Inference: hard routing으로 latency 최소화

## Related Concepts
- [[VisualThinkVLA]] — 상위 architecture
- [[EvidenceBank]] — 입력 source
- [[VisualStateComposer]] — 출력 destination
- [[RouteSupervision]] — 학습 메커니즘
