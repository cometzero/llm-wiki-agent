---
title: "ChannelFeatureMapFilter"
type: concept
tags: [cnn, deep-learning, computer-vision]
sources: [2026-05-10-day18-ai-ml-learning-review]
last_updated: 2026-05-10
---

# Channel, Feature Map, Filter

In [[ConvolutionalNeuralNetworks|CNNs]], images are represented as tensors with multiple **channels** (e.g., RGB has 3 channels). A **filter** (or kernel) is a small learned weight matrix that slides over the input, computing dot products to detect local patterns. The output of applying one filter across the entire input is a **feature map** — a spatial map of where that pattern appears. A set of filters is called a **filter bank**; N filters produce N output channels.

Key points:
- Filters are learned via gradient descent, not hand-designed.
- Early layers detect simple features (edges, colors); deeper layers detect more abstract features (parts, objects).
- The convolution operation: output[i,j] = sum over input patch × filter + bias.
- This concept is analogous to hidden representations in [[Transformer]] models and [[LLM]] residual streams.

See also: [[PoolingDownsampling]], [[ResidualNetwork]], [[DeepLearning]].