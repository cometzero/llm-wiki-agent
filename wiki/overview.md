# Overview

This wiki synthesizes knowledge from multiple sources about AI, machine learning, hardware, and their societal impacts.

## Core AI/ML Foundations

The wiki covers a structured 30-day learning path. Key mathematical foundations include:

- **Linear Algebra** (2026-04-23-ai-ml-learning-review): [[VectorSpace]], [[Basis]], [[LinearMap]], [[Rank]], [[DotProduct]], [[Norm]], [[CosineSimilarity]] — underpinning [[Embedding]], [[Attention]], and basic [[Gradient]] operations.
- **Probability & Statistics** (2026-04-24-ai-ml-learning-review): [[RandomVariable]], [[ProbabilityDistribution]], [[Probability]], [[PMF]], [[PDF]], [[CDF]], and moment/stat dependence notions like [[Expectation]], [[Variance]], [[Covariance]], [[Correlation]]. Also covers [[ConditionalProbability]] and [[BayesTheorem]] through [[Prior]], [[Likelihood]], [[Posterior]] as a core update mechanism for model inference.
- **Machine Learning as Function Approximation** (2026-04-25-ai-ml-learning-review): [[FunctionApproximation]], [[HypothesisSpace]], [[LossFunction]], [[FeatureMatrix]], [[CurseOfDimensionality]].
- **Optimization via Calculus** (2026-04-26-ai-ml-learning-review, [[2026-04-27-day05-ai-ml-learning-review]], [[2026-04-28-day06-ai-ml-learning-review]]): [[Derivative]], [[PartialDerivative]], [[Gradient]], [[DirectionalDerivative]], [[ChainRule]], [[Jacobian]], [[ComputationalGraph]], [[ForwardPass]], [[BackwardPass]], [[Backpropagation]], [[Autograd]], [[GradientDescent]], [[LearningRate]], [[VanishingGradient]], [[ExplodingGradient]], [[MiniBatch]], [[Variance]], [[Momentum]], and [[Adam]], and the practical implications for [[Convergence]], [[Divergence]], and Oscillation.

## Core Learning Flow Added by Day 05

AI/ML 학습은 [[Objective]](목표함수) 설정에서 출발해 [[LossFunction]] 기반의 [[EmpiricalRisk]] 계산, [[GradientDescent]] 기반의 [[UpdateRule]] 반복으로 이어진다. 이때 [[StepSize]]/[[LearningRate]]는 수렴 안정성과 속도를 좌우하고, [[Constraint]] 및 [[Regularization]]은 과적합과 불안정성을 제어한다.

## Core Learning Flow Added by Day 06

[[MiniBatch]]는 실전 학습에서 계산/수렴 트레이드오프를 다루는 핵심 단위로, 전체 데이터의 완전 기울기 대신 표본 집합으로부터의 StochasticEstimate를 제공한다. 이는 학습 속도와 하드웨어 효율성 측면에서 유리하지만, [[Variance]]와 잡음으로 인해 Oscillation이 자연스러운 현상이 됨을 함께 고려한다.

학습의 안정성은 [[LearningRate]] 선택이 결정적이다. [[Convergence]], [[Divergence]], [[Divergence]] 위험을 줄이기 위해 보통 [[LearningRate]] schedule(Warmup, decay, cosine)와 함께 쓰며, [[Optimizer]]의 진화 계열은 [[Momentum]]와 [[Adam]]으로 이어진다. 특히 [[Adam]]은 FirstMoment와 SecondMoment을 추적해 AdaptiveLearningRate 효과를 주므로 [[LLM]], [[Transformer]], [[Embedding]], [[Attention]] 기반 모델에서 성능/안정성 모두에 큰 영향을 준다.

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