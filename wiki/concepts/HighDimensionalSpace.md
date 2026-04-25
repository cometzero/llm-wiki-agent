---
title: "HighDimensionalSpace"
type: concept
tags: [machine-learning, geometry, representation]
sources: [2026-04-25-day03-ai-ml-learning-review]
last_updated: 2026-04-25
---

# HighDimensionalSpace

[[HighDimensionalSpace]] refers to the setting where data lives in many dimensions and becomes sparse as dimensionality grows.

## Core Idea
- As dimensions increase, the volume of the space grows faster than the amount of available data.
- Distances become less informative because points spread out and nearest-neighbor gaps shrink in relative significance.
- Many intuitive low-dimensional methods degrade in this regime.

## Connections
- [[CurseOfDimensionality]] — the classic failure mode of high-dimensional data.
- [[RepresentationLearning]] — a response that tries to find a better, lower-dimensional structure.
- [[DimensionalityReduction]] — a direct strategy for reducing dimensional burden.
