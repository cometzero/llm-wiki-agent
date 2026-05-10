---
title: "PoolingDownsampling"
type: concept
tags: [cnn, deep-learning, computer-vision]
sources: [2026-05-10-day18-ai-ml-learning-review]
last_updated: 2026-05-10
---

# Pooling and Downsampling

**Downsampling** reduces the spatial dimensions (height and width) of a feature map. **Pooling** is a common downsampling method. **Max pooling** selects the maximum value in each local window (e.g., 2×2), preserving the strongest activation. **Average pooling** takes the mean. Pooling reduces computation (e.g., 2×2 pooling reduces spatial size by 4×) and provides mild **translation invariance** — small shifts in input produce similar outputs because the exact position of a feature within the window is lost.

Key points:
- Pooling is not the only way to downsample; strided convolution also works.
- Too much downsampling can lose fine spatial information needed for tasks like segmentation.
- In [[Transformer]] models, patch merging or sequence length reduction serves a similar purpose.

See also: [[ChannelFeatureMapFilter]], [[ResidualNetwork]], [[ConvolutionalNeuralNetworks]].