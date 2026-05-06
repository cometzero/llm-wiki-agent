# Wiki Overview

This wiki synthesizes knowledge from ingested sources. It is a living document that evolves as new sources are added.

## Core Themes

### AI/ML Learning Journey
A structured 30-day learning path covering AI/ML fundamentals. Key milestones include:
- **Days 1-4**: Basic concepts, derivatives, gradients, backpropagation
- **Days 5-11**: Classical ML (Random Forest, Boosting, PCA), neural network foundations
- **Day 12**: Random Forest, Boosting, PCA
- **Day 13**: [[Perceptron]], [[MultiLayerPerceptron]], [[ActivationFunction]] — core neural network building blocks
- **Day 14**: [[ForwardPass]], [[Backpropagation]], and [[Parameters]] — the training loop that computes predictions, propagates gradients, and updates [[Weights]] and [[Biases]].

The learning emphasizes intuition, mathematical foundations, and connections to modern AI systems like [[LLM]]s and [[Transformer]]s.

### Neural Network Fundamentals
- [[Perceptron]]: Basic unit performing linear combination (weighted sum + bias) with threshold output.
- [[MultiLayerPerceptron]]: Stacked layers with nonlinearities enabling complex pattern learning.
- [[ActivationFunction]]: Essential for nonlinearity; [[ReLU]], [[Sigmoid]], [[Tanh]] are common.
- [[ForwardPass]]: Input-to-output computation that produces predictions and enables loss calculation.
- [[Backpropagation]]: Training algorithm that propagates gradients; activation function choice affects [[GradientFlow]].
- [[Parameters]]: Trainable values inside a model; [[Weights]] control feature influence and [[Biases]] shift output baselines.

### Hardware & Systems
- [[NVIDIA]] GPU architectures (Hopper, Blackwell, Vera Rubin)
- [[Groq]] LPX inference accelerators
- [[LinuxKernel]] topics (scheduling, isolation, safety)
- [[NPU]] design and programming

### Industry & Trends
- AI inference scaling, memory bandwidth, tokenomics
- Software-defined vehicles, embedded systems
- Robotics (Figure, Helix)

## Key Connections
- [[Perceptron]] → [[MultiLayerPerceptron]] → [[Transformer]] → [[LLM]]
- [[ActivationFunction]] → [[ForwardPass]] → [[Backpropagation]] → [[GradientFlow]]
- [[LinearCombination]] → [[AffineTransform]] → [[HiddenLayer]] → [[UniversalApproximation]]
- [[Parameters]] → [[Weights]] / [[Biases]] → [[Optimizer]] updates via gradients
