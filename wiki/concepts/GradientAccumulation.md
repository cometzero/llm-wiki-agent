---
title: "GradientAccumulation"
type: concept
tags: [training, deep-learning]
sources: [2026-05-08-day16-ai-ml-learning-review]
last_updated: 2026-05-08
---

**Gradient Accumulation** is a technique to simulate a larger [[BatchSize]] when GPU memory is limited. Instead of updating weights after every micro-batch, gradients are accumulated over several micro-batches and then a single optimizer step is performed. This allows effective batch sizes larger than what fits in memory. Related: [[BatchSize]], [[Iteration]].