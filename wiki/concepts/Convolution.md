---
title: "Convolution"
type: concept
tags: [deep-learning, computer-vision, cnn]
sources: [2026-05-09-day17-ai-ml-learning-review]
last_updated: 2026-05-09
---

## Definition
Convolution is the core operation in [[ConvolutionalNeuralNetworks]]. A small weight matrix (kernel) slides over the input, computing dot products at each position to produce a feature map.

## Key Parameters
- **Kernel (Filter)** — small weight matrix (e.g., 3×3) that learns to detect specific patterns (edges, textures).
- **Stride** — step size for kernel movement. Larger stride reduces output resolution and computation.
- **Padding** — zeros added around input border to control output size and preserve edge information.

## Mathematical Intuition
Each output value is a dot product between the kernel and a local input patch. High values indicate strong pattern match.

## Practical Considerations
- In deep learning frameworks (PyTorch, TensorFlow), convolution is implemented as cross-correlation (no kernel flip).
- Tensor shapes: input `[batch, channels, height, width]` → output `[batch, num_kernels, new_h, new_w]`.
- Stride > 1 reduces spatial dimensions; padding='same' preserves dimensions.

## Related Concepts
- [[ConvolutionalNeuralNetworks]]
- [[FeatureMap]]
- [[ReceptiveField]]
- [[Backpropagation]]