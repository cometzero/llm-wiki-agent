---
title: "2026-05-06 AI/ML Learning Review Day 14"
type: source
tags: [ai-ml-learning, review, diary]
date: 2026-05-06
source_file: raw/ai_ml_learning/2026-05-06-day14-ai-ml-learning-review.md
source_hash: 9fd093e99ad5e883
---

## Event Summary

Today's lesson covered three core concepts of neural network training: [[ForwardPass]] (순전파), [[Backpropagation]] (역전파), and [[Parameters]]/[[Weights]]/[[Biases]] (파라미터, 가중치, 편향).

- **Forward Pass**: The computation flow from input to output. Each layer applies an [[AffineTransform]] ($z = Wx + b$) followed by an [[ActivationFunction]] to produce a layer output, which becomes the next layer's input. The forward pass is the starting point for training, enabling loss calculation.
- **Backpropagation**: Efficiently computes gradients of the loss with respect to each parameter using the [[ChainRule]], solving the [[CreditAssignment]] problem. It propagates error signals backward from the loss through the network. Backpropagation does not update parameters directly; it computes gradients for the [[Optimizer]] (e.g., SGD, Adam) to use.
- **Parameters**: Learnable values adjusted during training. [[Weights]] determine the influence of input features on output; [[Biases]] shift the output baseline. In neural networks, parameters are organized as matrices and vectors (e.g., embedding matrices, attention projection matrices). The parameter space is the set of all possible parameter combinations. Parameters are distinct from [[Hyperparameter]]s.

The follow-up review answers reinforced these concepts with examples and clarified common confusions (e.g., backpropagation vs. optimizer, weight vs. bias effects).

## Key Claims

- Forward pass is the computation from input to prediction; without it, no loss can be calculated.
- Backpropagation computes gradients via the chain rule; it does not update parameters — the optimizer does.
- Weights control the strength of input influence; biases control the output baseline.
- Parameters are the model's "memory" — the same architecture with different parameters can produce entirely different behaviors.

## Key Quotes

> "딥러닝 학습은 forward pass로 예측과 loss를 만들고, backpropagation으로 각 parameter의 책임을 계산한 뒤, optimizer가 weight와 bias를 조금씩 조정해 더 좋은 표현을 만드는 과정이다." — Daily summary

> "gradient가 있어야 optimizer가 parameter를 어느 방향으로 수정할지 안다." — On the necessity of backpropagation

## Connections

- [[ForwardPass]] — core concept explained
- [[Backpropagation]] — core concept explained
- [[Parameters]] — core concept explained
- [[Weights]] — sub-concept of parameters
- [[Biases]] — sub-concept of parameters
- [[AffineTransform]] — the $Wx + b$ computation
- [[ActivationFunction]] — applied after affine transform
- [[Gradient]] — the signal computed by backpropagation
- [[ChainRule]] — mathematical foundation of backpropagation
- [[CreditAssignment]] — problem solved by backpropagation
- [[Optimizer]] — uses gradients to update parameters
- [[Hyperparameter]] — distinct from parameters (e.g., learning rate)
- [[NeuralNetwork]] — the broader context
- [[DeepLearning]] — the field
- [[LossFunction]] — used to measure prediction error
- [[GradientFlow]] — the propagation of gradients through layers
- [[Transformer]] — architecture that uses these concepts
- [[LLM]] — application of these concepts

## Shifts & Contradictions

None identified.