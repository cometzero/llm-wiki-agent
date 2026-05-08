---
title: "Iteration"
type: concept
tags: [training, deep-learning]
sources: [2026-05-08-day16-ai-ml-learning-review]
last_updated: 2026-05-08
---

An **iteration** is one optimizer update step, processing one mini-batch of data. It consists of a forward pass, loss calculation, backward pass (gradient computation), and optimizer step. The number of iterations per [[Epoch]] is determined by the dataset size and [[BatchSize]]. Related: [[Epoch]], [[BatchSize]], [[GradientAccumulation]].