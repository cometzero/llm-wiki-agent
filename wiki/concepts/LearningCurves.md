---
title: "Learning Curves"
type: concept
tags: [deep-learning, training, diagnostics]
sources: [2026-05-09-day17-ai-ml-learning-review]
last_updated: 2026-05-09
---

## Definition
Learning curves plot training loss and validation loss (or accuracy) over epochs or training steps. They are the primary diagnostic tool for monitoring model training dynamics.

## Key Patterns
1. **Both losses high** → [[Underfitting]] (model hasn't learned enough). Solutions: more epochs, larger model, better features, adjust learning rate.
2. **Low train loss, high validation loss** → [[Overfitting]] (model memorizes training data). Solutions: more data, [[Regularization]], [[Dropout]], [[BatchNormalization]], data augmentation, [[EarlyStopping]].
3. **Both decrease then validation plateaus/rises** → classic overfitting onset. Save model at best validation point.

## Importance
- Train loss alone is misleading; validation loss measures generalization.
- Used in all model training: image classification, LLM fine-tuning, embedding models, hyperparameter tuning.
- Tools: TensorBoard, Weights & Biases, MLflow.

## Related Concepts
- [[EarlyStopping]]
- [[Overfitting]]
- [[Underfitting]]
- [[Generalization]]