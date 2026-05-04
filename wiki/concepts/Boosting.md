---
title: "Boosting"
type: concept
tags: [ensemble, additive-model, weak-learner]
sources: [2026-05-04-day12-ai-ml-learning-review]
last_updated: 2026-05-04
---

**Boosting** is an [[Ensemble]] method that sequentially adds weak learners (e.g., shallow [[DecisionTree|decision trees]]), each trained to correct the errors of the previous ensemble. The final model is an AdditiveModel: a weighted sum of all weak learners.

## Key Variants
- **[[AdaBoost]]**: Increases weights on misclassified samples so subsequent learners focus on them.
- **[[GradientBoosting]]**: Fits new learners to the gradient of the loss function (residuals). Modern implementations: XGBoost, LightGBM, CatBoost.

## Key Points
- Weak learners are intentionally simple; strength comes from combining many.
- [[LearningRate]] controls how much each new learner contributes; smaller rates reduce overfitting.
- Often outperforms deep learning on tabular data.
- Prone to overfitting if too many learners or deep trees are used.

## Connections
- [[RandomForest]] — parallel ensemble vs. sequential.
- AdditiveModel — mathematical form.
- [[GradientDescent]] — conceptual parallel in neural networks.
- [[Residual]] — what each new learner fits.