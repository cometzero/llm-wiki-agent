---
title: "Parameters"
type: concept
tags: [neural-network, deep-learning, training]
sources: [2026-05-06-day14-ai-ml-learning-review]
last_updated: 2026-05-06
---

Parameters are the learnable values inside a model that are adjusted during training to minimize the loss. The two primary types are [[Weights]] and [[Biases]]. Weights determine the influence of input features on the output, while biases shift the output baseline. In neural networks, parameters are organized as matrices and vectors (e.g., embedding matrices, attention projection matrices). The set of all possible parameter values forms the parameter space. Parameters are distinct from [[Hyperparameter]]s, which are set by the user. Training involves using [[Backpropagation]] to compute gradients and an [[Optimizer]] to update parameters.