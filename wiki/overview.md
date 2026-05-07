# Wiki Overview

This wiki synthesizes knowledge from ingested sources. It is a living document that evolves as new sources are added.

## Core Themes

### AI/ML Learning Journey
A structured 30-day learning path covering AI/ML fundamentals. Key milestones include:
- **Days 1-4**: Basic concepts, derivatives, gradients, backpropagation
- **Days 5-11**: Classical ML, ensemble methods, and early neural foundations
- **Day 12**: [[RandomForest]], [[Boosting]], [[PCA]]
- **Day 13**: [[Perceptron]], [[MultiLayerPerceptron]], [[ActivationFunction]]
- **Day 14**: [[ForwardPass]], [[Backpropagation]], and [[Parameters]] / [[Weights]] / [[Biases]]
- **Day 15**: [[RepresentationLearning]], [[Initialization]], [[VanishingGradient]], [[ExplodingGradient]], and stable training mechanics

The learning sequence progressively links intuitive understanding with mathematical grounding and modern AI systems such as [[LLM]]s and [[Transformer]]s.

### Neural Network Fundamentals
- [[RepresentationLearning]]: 학습 가능한 내부 특징 공간을 통해 원본 입력이 문제 해결에 유리한 표현으로 변환됨.
- [[LatentRepresentation]]: 관찰되지 않는 의미/구조를 캡처하는 내부 공간 내 벡터 표현.
- [[Embedding]] / [[HiddenState]] / [[LatentSpace]]: 텍스트·시각 신호에서 문맥적 유사도와 의미군집을 만드는데 핵심적인 벡터 공간 메커니즘.
- [[Initialization]]: 학습 시작 시점의 [[Weights]] 분포가 forward/backward 신호의 scale을 결정.
- [[SymmetryBreaking]]: 같은 초기값을 피하고 뉴런이 서로 다른 표현을 배우게 만듦.
- [[XavierInitialization]] / [[HeInitialization]]: fan-in/fan-out 기반 스케일링 규칙으로 안정적 시작값 제어.
- [[VanishingGradient]] / [[ExplodingGradient]]: 다층 미분 연쇄에서 작은/큰 local gradient의 누적로 발생.
- [[GradientClipping]], [[ResidualConnection]], [[LayerNorm]]: 깊은 네트워크에서 [[TrainingStability]] 확보를 위한 주요 완화장치.

### Practical Training Signals
- [[ForwardPass]] → [[BackwardPass]] 흐름에서 [[GradientFlow]]가 균형을 잃으면 학습이 정체되거나 발산한다.
- [[Optimizer]], [[LearningRate]], [[Initialization]], [[Normalization]], [[GradientClipping]]은 상호 의존적이다.
- 이론은 특히 [[Transformer]], [[CNN]], [[RNN]]의 실제 학습 튜닝에서 재현되는 핵심 체크리스트로 수렴한다.

## Key Connections
- [[Perceptron]] → [[MultiLayerPerceptron]] → [[Transformer]] → [[LLM]]
- [[ForwardPass]] → [[Backpropagation]] → [[GradientFlow]] → [[Optimizer]]
- [[RepresentationLearning]] → [[LatentSpace]] / [[Embedding]] / [[HiddenState]] → [[Transformer]] / [[LLM]]
- [[Initialization]] → [[GradientFlow]] 안정화 → [[TrainingStability]] 향상
- [[SymmetryBreaking]] + [[XavierInitialization]] / [[HeInitialization]] → 뉴런 특이성 + 안정적 학습
- [[ResidualConnection]] + [[LayerNorm]] + [[GradientClipping]] → [[VanishingGradient]]/[[ExplodingGradient]] 완화

## Hardware & Systems
- [[NVIDIA]] GPU architectures (Hopper, Blackwell, Vera Rubin)
- [[Groq]] LPX inference accelerators
- [[LinuxKernel]] topics (scheduling, isolation, safety)
- [[NPU]] design and deployment

### AI Education and Concept Graph
- This repo now includes a deeper chain linking representation learning to optimization mechanics, useful as a bridge from intuition to implementation in [[NeuralNetwork]] training.
