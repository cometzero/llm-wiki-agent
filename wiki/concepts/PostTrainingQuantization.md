---
title: "Post Training Quantization"
type: concept
tags: [Quantization, Inference, ModelCompression]
sources: [neural-network-quantization-number-formats-from-first-principles]
last_updated: 2026-05-03
---

[[PostTrainingQuantization]] is the family of methods that convert a trained model to lower precision without running a full new training cycle. It often uses calibration data, rounding rules, or layer-wise heuristics to reduce cost while trying to preserve accuracy.

The source notes that PTQ methods range from simple rounding to more advanced techniques like [[GPTQ]], [[Smoothquant]], [[AWQ]], and [[AdaRound]].

## Connections
- [[NeuralNetworkQuantization]] — umbrella concept.
- [[GPTQ]] — second-order PTQ method.
- [[Smoothquant]] — activation-outlier mitigation method.
- [[AWQ]] — activation-aware weight quantization.
- [[AdaRound]] — layer-wise rounding optimization.
