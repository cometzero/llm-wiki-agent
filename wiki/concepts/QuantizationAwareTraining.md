---
title: "Quantization Aware Training"
type: concept
tags: [Quantization, Training, ModelAdaptation]
sources: [neural-network-quantization-number-formats-from-first-principles]
last_updated: 2026-05-03
---

[[QuantizationAwareTraining]] is the process of training or fine-tuning a model while simulating lower-precision arithmetic so the model adapts to quantized conditions before deployment. It is more expensive than [[PostTrainingQuantization]] but usually offers better accuracy retention.

The source frames QAT as the practical route when simple post-training conversion is not accurate enough for the target deployment.

## Connections
- [[NeuralNetworkQuantization]] — umbrella concept.
- [[PostTrainingQuantization]] — cheaper alternative.
- [[FP8]] — common training-time low-precision target.
