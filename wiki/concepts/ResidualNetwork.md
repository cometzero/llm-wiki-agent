---
title: "ResidualNetwork"
type: concept
tags: [cnn, deep-learning, resnet]
sources: [2026-05-10-day18-ai-ml-learning-review]
last_updated: 2026-05-10
---

# Residual Network (ResNet)

A **Residual Network (ResNet)** uses **skip connections** (also called residual connections) to allow very deep neural networks to train effectively. The core formula is:

```
output = x + F(x)
```

where `x` is the input and `F(x)` is a learned transformation (e.g., a few convolutional layers). The skip connection provides an **identity mapping** path, so the network only needs to learn the **residual** (the change from the input). If no change is needed, `F(x)` can approach zero, making the block act as identity. This stabilizes gradient flow because gradients can bypass the transformation layers via the skip path.

Key points:
- ResNet enabled very deep CNNs (e.g., ResNet-50, ResNet-101) that previously suffered from vanishing gradients.
- The idea is fundamental to [[Transformer]] architectures: attention and feed-forward outputs are added to the input via residual connections.
- In [[LLM]]s, the residual stream concept describes how each layer adds information to a shared hidden state.
- When shapes differ, a projection shortcut (e.g., 1×1 convolution) aligns dimensions.

See also: [[ChannelFeatureMapFilter]], [[PoolingDownsampling]], [[DeepLearning]], [[ConvolutionalNeuralNetworks]].