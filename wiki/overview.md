# Overview

This wiki synthesizes knowledge from multiple sources about AI, machine learning, hardware, and their societal impacts.

## Core AI/ML Foundations

The wiki covers a structured 30-day learning path. Key mathematical foundations include:

- **Linear Algebra** (2026-04-29-ai-ml-learning-review): [[VectorSpace]], [[Basis]], [[LinearMap]], [[Rank]], [[DotProduct]], [[Norm]], [[CosineSimilarity]] — underpinning [[Embedding]], [[Attention]], and basic [[Gradient]] operations.
- **Probability & Statistics** (2026-04-24-ai-ml-learning-review): [[RandomVariable]], [[ProbabilityDistribution]], [[Probability]], [[PMF]], [[PDF]], [[CDF]], and moment/stat dependence notions like [[Expectation]], [[Variance]], [[Covariance]], [[Correlation]]. Also covers [[ConditionalProbability]] and [[BayesTheorem]] through [[Prior]], [[Likelihood]], [[Posterior]] as a core update mechanism for model inference.
- **Machine Learning as Function Approximation** (2026-04-25-ai-ml-learning-review): [[FunctionApproximation]], [[HypothesisSpace]], [[LossFunction]], [[FeatureMatrix]], [[CurseOfDimensionality]].
- **Optimization via Calculus** (2026-04-26-ai-ml-learning-review, [[2026-04-27-day05-ai-ml-learning-review]], [[2026-04-28-day06-ai-ml-learning-review]]): [[Derivative]], [[PartialDerivative]], [[Gradient]], [[DirectionalDerivative]], [[ChainRule]], [[Jacobian]], [[ComputationalGraph]], [[ForwardPass]], [[BackwardPass]], [[Backpropagation]], [[Autograd]], [[GradientDescent]], [[LearningRate]], [[VanishingGradient]], [[ExplodingGradient]], [[MiniBatch]], [[Variance]], [[Momentum]], and [[Adam]], and the practical implications for [[Convergence]], [[Divergence]], and Oscillation.

## Core Learning Flow Added by Day 05

AI/ML 학습은 [[Objective]](목표함수) 설정에서 출발해 [[LossFunction]] 기반의 [[EmpiricalRisk]] 계산, [[GradientDescent]] 기반의 [[UpdateRule]] 반복으로 이어진다. 이때 [[StepSize]]/[[LearningRate]]는 수렴 안정성과 속도를 좌우하고, [[Constraint]] 및 [[Regularization]]은 과적합과 불안정성을 제어한다.

## Core Learning Flow Added by Day 06

[[MiniBatch]]는 실전 학습에서 계산/수렴 트레이드오프를 다루는 핵심 단위로, 전체 데이터의 완전 기울기 대신 표본 집합으로부터의 StochasticEstimate를 제공한다. 이는 학습 속도와 하드웨어 효율성 측면에서 유리하지만, [[Variance]]와 잡음으로 인해 Oscillation이 자연스러운 현상이 됨을 함께 고려한다.

학습의 안정성은 [[LearningRate]] 선택이 결정적이다. [[Convergence]], [[Divergence]], [[Divergence]] 위험을 줄이기 위해 보통 [[LearningRate]] schedule(Warmup, decay, cosine)와 함께 쓰이며, [[Optimizer]]의 진화 계열은 [[Momentum]]와 [[Adam]]으로 이어진다. 특히 [[Adam]]은 FirstMoment와 SecondMoment을 추적해 AdaptiveLearningRate 효과를 주므로 [[LLM]], [[Transformer]], [[Embedding]], [[Attention]] 기반 모델에서 성능/안정성 모두에 큰 영향을 준다.

## Core Learning Flow Added by Day 07

Day 07 introduces the structural perspective on model power and evaluation reliability.

1. [[HypothesisSpace]] defines what a model family can represent, while [[Capacity]] and [[Expressivity]] describe the breadth and complexity of that representable set.
2. Larger capacity expands the set of fit functions but increases [[Overfitting]] risk when data is limited, noisy, or biased.
3. [[InductiveBias]] is the model's built-in preference, which can stabilize learning when data is sparse and supports better [[Generalization]] if aligned with data structure.
4. Proper [[TrainValidationTestSplit]] is the control framework for deciding if the model learned actual structure rather than memorization.
5. [[TrainSet]] drives parameter fitting, [[ValidationSet]] supports tuning ([[Hyperparameter]], [[EarlyStopping]]), and [[TestSet]] estimates [[OutOfSample]] behavior; only last-stage use of test is considered reliable.
6. [[GeneralizationGap]] gives a practical diagnostic: small gap with high performance is preferable, while large gap requires investigation into overfitting, distribution mismatch, leakage, or preprocessing/data-split flaws.

## Core Learning Flow Added by Day 08

Day 08 closes the bridge from structural understanding to daily diagnostics.

- [[Overfitting]] and [[Underfitting]] are interpreted by comparing [[TrainingLoss]] and [[ValidationLoss]].
  - if training gets better but validation gets worse, the model is likely overfitting.
  - if both are poor, underfitting is likely.
- [[BiasVarianceTradeoff]] explains why this happens:
  - [[Bias]] dominant states miss the true rule and underfit.
  - [[Variance]] dominant states overreact to sample-specific details and overfit.
- [[Generalization]] remains the real goal: low error on unseen data,
  not perfect memorization of training points.
- [[Regularization]] is the standard control layer for model complexity:
  - objective augmentation with penalty: [[L1Penalty]], [[L2Penalty]], [[WeightDecay]],
  - learning-control: [[EarlyStopping]], [[Dropout]], [[DataAugmentation]], noise-based robustness techniques,
  - parameter/data choice (more data, feature revision, better split hygiene).
- Practical interpretation from learning curves:
  - if training loss decreases continuously while validation loss turns up, reduce complexity or regularization strength and stop too-early fitting.
  - too strong regularization can cause [[Underfitting]], so [[Lambda]] tuning is always a tradeoff.

## Core Learning Flow Added by Day 09

Day 09 extends the flow into robust evaluation and alignment of objectives.

1. [[CrossValidation]] and specifically [[KFoldCrossValidation]] make performance estimation less dependent on one lucky or unlucky split by averaging validation outcomes across multiple folds.
2. Proper [[EvaluationMetric]] design is now framed as a model-choice tool, not a cosmetic score. In particular:
   - [[Accuracy]] can be misleading under [[ImbalancedData]],
   - [[Precision]]/[[Recall]] and [[F1Score]] expose different failure costs,
   - [[AUROC]] is useful for threshold-agnostic ranking behavior.
3. [[Threshold]] tuning is tied to business utility: lowering threshold usually raises recall while reducing precision, and vice versa.
4. [[Loss]] is separated from metric: learning signal ([[RegressionLoss]] vs [[ClassificationLoss]]) should match the task type.

## Core Learning Flow Added by Day 10

Day 10 adds the bridge from early ML foundations to how classical models realize "prediction as optimization + probabilistic decision + geometric separation."

1. [[LinearRegression]] is the baseline for regression: define a linear function and optimize parameters by minimizing [[LeastSquares]]/[[MSE]] risk.
2. [[LogisticRegression]] turns linear score into class probability via sigmoid/logit, then applies [[Threshold]] for binary classification.
3. [[DecisionBoundary]] is the geometric object induced by scoring functions; in linear models it is [[Hyperplane]], and [[Margin]] quantifies confidence-like robustness to perturbations.
4. [[LinearSeparability]] is a model-capacity condition: if not separable by one linear boundary, richer representations may be required.
5. [[FeatureSpace]] transformation is therefore central, and nonlinear models reshape feature spaces to make classes separable.

## Core Learning Flow Added by Day 11

Day 11 revisits classical ML from the lens of classification robustness:

1. [[SupportVectorMachine]] emphasizes robust geometric separation via [[MaximumMargin]], where support vectors define the boundary-relevant subset and [[KernelTrick]] enables nonlinear separability.
2. [[KNN]] highlights case-based reasoning: prediction comes from the nearest instances under a chosen [[DistanceMetric]], making the choice of metric and feature scaling central.
3. [[DecisionTree]] reframes learning as sequential questioning; splitting is evaluated by uncertainty reduction through [[InformationGain]], [[Entropy]], or [[GiniImpurity]].
4. Together, these models provide three complementary inductive biases:
   - margin-maximizing boundary construction,
   - local neighborhood voting,
   - recursive partitioning by pure splits.
5. Their practical limits are clear: [[SVM]] needs kernel/regularization choices, [[KNN]] struggles with scale and high dimension ([[CurseOfDimensionality]]), and [[DecisionTree]] needs pruning or depth constraints to avoid [[Overfitting]].
6. Modern AI systems still reuse these ideas: [[Embedding]] retrieval resembles KNN-style nearest-neighbor search, and distance/partition thinking appears inside feature-space engineering and tree-based models for tabular tasks.

## AI Hardware & Inference

Sources cover the hardware landscape for AI inference and training:
- [[NVIDIA]]'s Blackwell and [[VeraRubinPlatform]] with [[Groq]] LPU integration (GTC 2026)
- RISC-V extensions for AI ([[VectorBatchProduct]], MatrixExtensions)
- Memory dynamics: [[HBM]], [[HBF]], [[DRAM]] supercycle (MemoryMania)
- Inference acceleration: [[EAGLE3]], [[KVCache]], ONNX/[[ONNXRuntime]]

## AI Agents & Software

- Claude Code as an inflection point for agentic coding.
- [[VibeCoding]] in production with [[ClaudeCode]]
- [[MCP]] and [[Skills]] for extending AI capabilities
- [[ProjectGlasswing]] for security

## Societal & Economic Impacts

- [[Polycrisis]], [[ConnectedIntelligence]], [[UniversalBasicIncome]] in AI governance.
- [[SpaceX]] and [[Terafab]] for space-based computing.
- GDP 7% era with AI, robotics, space, biotech convergence.
- Korean semiconductor and currency analysis.

## Knowledge Graph

The wiki maintains a knowledge graph of interconnected concepts, entities, and sources. See graph/graph.html for visualization.
