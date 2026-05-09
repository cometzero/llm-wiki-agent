---
title: "Early Stopping"
type: concept
tags: [deep-learning, training, regularization]
sources: [2026-05-09-day17-ai-ml-learning-review]
last_updated: 2026-05-09
---

## Definition
Early stopping is a regularization technique that halts training when validation performance stops improving, preventing [[Overfitting]].

## How It Works
- Monitor validation loss (or another metric) after each epoch.
- If validation loss has not improved for a set number of epochs (patience), stop training.
- Restore model weights from the best validation epoch.

## Key Insight
- It is not "giving up early" but selecting the model that generalizes best.
- Works because after a certain point, further training reduces train loss but increases validation loss.

## Related Concepts
- [[LearningCurves]]
- [[Overfitting]]
- [[ValidationSet]]
- [[Regularization]]