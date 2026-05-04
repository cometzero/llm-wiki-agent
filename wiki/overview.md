# Wiki Overview

## Living Synthesis

This wiki synthesizes knowledge from diverse sources: AI hardware (NVIDIA GPUs, Groq, memory), software-defined vehicles, Linux kernel internals, AI/ML learning diaries, and more.

### AI/ML Foundations

A series of daily learning logs (Days 1–12) builds up core ML concepts from derivatives and backpropagation through neural networks to classical models. Day 12 introduces three foundational classical ML techniques:

- **[[RandomForest]]**: An [[Ensemble]] method that builds many [[DecisionTree|decision trees]] using [[Bootstrap]] sampling and FeatureSubsampling, then averages their predictions to reduce variance and combat [[Overfitting]].
- **[[Boosting]]**: A sequential ensemble approach ([[AdaBoost]], [[GradientBoosting]]) where weak learners are added one by one, each correcting the residuals of the previous ensemble. Forms an AdditiveModel.
- **[[PCA]] (Principal Component Analysis)**: An unsupervised [[DimensionalityReduction]] technique that finds the directions of maximum variance (principal components) via eigenvectors of the [[Covariance]] matrix. ExplainedVariance measures information retained.

These models remain important baselines, especially for tabular data (XGBoost, LightGBM, CatBoost). The ensemble philosophy also connects to modern LLM techniques like SelfConsistency.

### Hardware & Inference

... (existing content preserved) ...

### Software & Systems

... (existing content preserved) ...

### Other Domains

... (existing content preserved) ...