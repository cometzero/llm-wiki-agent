---
title: "Convolutional Neural Networks"
type: concept
tags: [deep-learning, computer-vision, cnn]
sources: [2026-05-09-day17-ai-ml-learning-review]
last_updated: 2026-05-09
---

## Definition
CNNs are neural network architectures designed for spatially structured data (especially images). They exploit local connectivity, parameter sharing, and hierarchical feature learning.

## Core Ideas
1. **Local Receptive Field** — each neuron sees only a small region of the input (e.g., 3×3 pixels), exploiting [[SpatialLocality]].
2. **Parameter Sharing** — the same kernel (filter) is applied across all spatial positions, drastically reducing parameters vs. fully connected layers.
3. **Hierarchical Feature Learning** — lower layers detect edges/corners, middle layers detect parts (eyes, wheels), higher layers detect whole objects.

## Advantages
- Far fewer parameters than fully connected layers for image inputs.
- Translation invariance via shared kernels.
- Natural fit for spatial locality.

## Modern Context
- Still foundational for image classification, object detection, segmentation, medical imaging.
- [[VisionTransformer]] (ViT) uses attention but still divides images into patches (local processing).
- The inductive bias of locality is a key design principle: build data structure assumptions into the model.

## Related Concepts
- [[Convolution]]
- [[Backpropagation]]
- [[Pooling]]
- [[VisionTransformer]]