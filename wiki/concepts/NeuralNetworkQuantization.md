---
title: "Neural Network Quantization"
type: concept
tags: [Quantization, LowPrecision, HardwareEfficiency]
sources: [neural-network-quantization-number-formats-from-first-principles]
last_updated: 2026-05-03
---

[[NeuralNetworkQuantization]] is the process of reducing numeric precision in model parameters, activations, and accumulators to improve memory usage, bandwidth, energy efficiency, and throughput. The central tradeoff is that fewer bits usually reduce cost but can increase rounding error and accuracy loss.

In practice, quantization is not just about shrinking weights. It also depends on the value distribution, scaling strategy, accumulation precision, and whether the model is adapted through [[PostTrainingQuantization]] or [[QuantizationAwareTraining]].

## Connections
- [[INT8]] — common low-bit inference target.
- [[FP8]] — important low-bit training/inference format.
- [[FP16]] — common reduced-precision baseline.
- [[BF16]] — reduced-precision format with wide exponent range.
- [[PostTrainingQuantization]] — inference-side adaptation path.
- [[QuantizationAwareTraining]] — training-side adaptation path.
- [[BlockNumberFormats]] — shared-scale approach to reducing redundancy.
- [[NVIDIA]] — major vendor pushing low-precision hardware.
