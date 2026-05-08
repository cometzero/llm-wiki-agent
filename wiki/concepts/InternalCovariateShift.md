---
title: "InternalCovariateShift"
type: concept
tags: [normalization, training, deep-learning]
sources: [2026-05-08-day16-ai-ml-learning-review]
last_updated: 2026-05-08
---

**Internal Covariate Shift** is the phenomenon where the distribution of network activations changes during training as earlier layer weights are updated. This makes training deeper networks difficult because later layers must continuously adapt to shifting input distributions. [[BatchNormalization]] was originally proposed to reduce internal covariate shift by normalizing activations, though modern understanding suggests its benefits may also stem from smoothing the optimization landscape. Related: [[BatchNormalization]], [[LayerNormalization]].