---
title: "Bootstrap"
type: concept
tags: [resampling, statistics, bagging]
sources: [2026-05-04-day12-ai-ml-learning-review]
last_updated: 2026-05-04
---

**Bootstrap** is a resampling technique where multiple datasets are created by drawing samples with replacement from the original dataset. Each bootstrap sample has the same size as the original but contains duplicates and omits some observations (out-of-bag samples).

## Key Points
- Used in [[Bagging]] to create diverse training sets for ensemble models.
- Out-of-bag samples can be used for validation without a separate holdout set.
- Not a data augmentation method; it reuses existing data.

## Connections
- [[Bagging]] — bootstrap aggregating.
- [[RandomForest]] — uses bootstrap for each tree.
- [[Ensemble]] — bootstrap enables diversity.