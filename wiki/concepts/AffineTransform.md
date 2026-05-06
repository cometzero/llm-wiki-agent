---
title: "Affine Transform"
type: concept
tags: [neural-network, linear-algebra, deep-learning]
sources: [2026-05-06-day14-ai-ml-learning-review]
last_updated: 2026-05-06
---

An affine transform is the `Wx + b` calculation used inside many neural-network layers: inputs are mixed by [[Weights]] and shifted by [[Biases]]. During the [[ForwardPass]], this transform produces a pre-activation value, often called `z`, which may then pass through an [[ActivationFunction]] to become the layer output. It is the basic linear-plus-offset computation behind dense layers, transformer projections, and classifier heads.
