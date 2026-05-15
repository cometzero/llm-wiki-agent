---
title: "Skip Path"
type: concept
tags: [deep-learning, optimization]
sources: [2026-05-15-day23-ai-ml-learning-review.md]
last_updated: 2026-05-15
---

## Definition

The direct connection from input to output in a [[ResidualConnection]] that bypasses the transformation block `F(x)`.

Also called: shortcut connection, identity shortcut, residual path.

## Purpose

- Creates shortest possible path for gradient propagation
- Preserves input information even if transformation block is poorly trained
- Enables training of very deep networks

## In Context

Part of [[ResidualConnection]]: `y = x + F(x)`

The `x` term represents the skip path; the `F(x)` term represents the main transformation path.

## Related Concepts

- [[ResidualConnection]] — skip path is a component
- [[Gradient]] — benefits from short propagation path
- [[GradientFlow|OptimizationPath]] — gradient's learning route through the network
