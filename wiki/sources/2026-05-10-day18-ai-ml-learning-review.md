---
title: "AI/ML Learning Review — Day 18 (2026-05-10)"
type: source
tags: [ai-ml-learning, cnn, deep-learning, resnet]
date: 2026-05-10
source_file: raw/ai_ml_learning/2026-05-10-day18-ai-ml-learning-review.md
source_hash: a07d613b5817339d
---

## Summary

Day 18 of the AI/ML learning journey covers three core CNN concepts: (1) channels, feature maps, and filters — how CNNs represent images as tensors and use learned filters to produce feature maps; (2) pooling and downsampling — how max pooling reduces spatial size and provides slight translation invariance; (3) Residual Networks (ResNet) — how skip connections enable very deep networks by learning residuals instead of full transformations. The follow-up review answers reinforce these ideas with concrete examples and connections to [[Transformer]] architectures and [[LLM]] residual streams.

## Key Claims

- **Channels, Feature Maps, Filters**: A CNN treats an image as a tensor with multiple channels (e.g., RGB). Learned filters (small weight matrices) slide over the input, computing dot products to produce feature maps. A filter bank of N filters produces N output channels. Deeper layers learn more abstract features (edges → parts → objects). Filters are learned via gradient descent, not hand-designed.
- **Pooling and Downsampling**: Max pooling selects the maximum value in each local window, reducing spatial dimensions (e.g., 2×2 pooling halves height and width). This reduces computation and provides mild translation invariance — small shifts in input produce similar outputs. Average pooling preserves overall activation strength. Downsampling can also be done via strided convolution.
- **Residual Networks**: The core idea is the skip connection: output = x + F(x), where F(x) is a learned transformation. This makes it easy for layers to learn identity mapping (F(x) ≈ 0) when no change is needed, stabilizing training of very deep networks. Gradients flow more easily through the skip path. This concept is fundamental to [[Transformer]] architectures and [[LLM]] residual streams.

## Key Quotes

> "CNN은 이미지를 한 장의 납작한 그림으로 보지 않고, 여러 겹의 숫자판(channel)을 쌓아 둔 tensor로 본 뒤, 작은 탐지기(filter)를 여기저기 밀어 보면서 새로운 특징 지도(feature map)를 만든다." — One-line intuition on CNN view of images.

> "Pooling은 큰 그림에서 중요한 정보만 남기고 해상도를 줄이는 방법이고, downsampling은 데이터의 크기를 줄이는 전체 아이디어다." — One-line intuition on pooling vs downsampling.

> "Residual Network, 즉 ResNet은 깊은 neural network가 '전부 새로 배우기'보다 '기존 입력에 필요한 변화만 더하기'를 배우게 해서 학습을 훨씬 쉽게 만든 구조다." — One-line intuition on ResNet.

## Connections

- [[ConvolutionalNeuralNetworks]] — This source provides foundational CNN concepts (channels, filters, feature maps, pooling).
- [[DeepLearning]] — The training mechanics (gradient flow, loss minimization) are central to understanding how filters are learned.
- [[Transformer]] — Residual connections in Transformers are directly analogous to ResNet skip connections; feature maps relate to hidden representations.
- [[LLM]] — The residual stream concept in LLMs mirrors ResNet's identity mapping.
- [[BatchNormalization]] and [[Dropout]] — Previously covered training stabilization techniques (Day 16) complement ResNet's approach.
- [[ChannelFeatureMapFilter]] — Concept page created from this source.
- [[PoolingDownsampling]] — Concept page created from this source.
- [[ResidualNetwork]] — Concept page created from this source.
- [[2026-05-09-day17-ai-ml-learning-review]] — Previous day introduced CNN local connectivity and convolution; this source deepens those ideas.

## Contradictions

None identified. The content is consistent with existing wiki pages on [[DeepLearning]] and [[ConvolutionalNeuralNetworks]].