---
title: "ChainRule"
type: concept
tags: [calculus, optimization, machine-learning]
sources: [2026-04-26-day04-ai-ml-learning-review]
last_updated: 2026-04-26
---

The chain rule is a formula for computing the derivative of a composition of functions. It states that the derivative of f(g(x)) is f'(g(x)) * g'(x). In the context of neural networks, it allows gradients to flow backward through multiple layers.

## Key Points
- Backpropagation is the systematic application of the chain rule on a [[ComputationalGraph]].
- Each node in the graph computes its local gradient; the chain rule multiplies upstream and local gradients.
- Enables training of deep networks by decomposing the overall gradient into manageable pieces.

## Connections
- [[Backpropagation]] — algorithm built on chain rule.
- [[ComputationalGraph]] — structure on which chain rule is applied.
- [[Derivative]] — the basic building block.
- [[Autograd]] — automates chain rule application.