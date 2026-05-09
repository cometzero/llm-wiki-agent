# Wiki Overview

This wiki synthesizes knowledge from ingested sources. It is updated after each ingest to reflect the current state of understanding.

## Core Themes

### AI/ML Learning Series
A structured 30-day AI/ML learning journey from fundamentals to advanced topics. The series covers classical ML (Random Forest, Boosting, PCA), neural network foundations (perceptron, MLP, activation functions, backpropagation), and deep learning training mechanics (epoch/batch, BatchNorm, Dropout).

**Day 17** introduces three key deep learning concepts:
- **Learning curves** — monitoring train/validation loss to detect overfitting and underfitting, and using early stopping.
- **CNN local connectivity** — how CNNs exploit spatial locality via local receptive fields, parameter sharing, and hierarchical feature learning.
- **Convolution operation** — the mechanics of kernel, stride, and padding for pattern detection.

### Hardware & Systems
Sources cover GPU architecture (NVIDIA Blackwell, Hopper, Vera Rubin), inference accelerators (Groq 3 LPX), memory technology (HBM, HBF), and Linux kernel topics (real-time, isolation, NPU subsystems, SDV).

### AI Industry & Research
Topics include speculative decoding, context rot, reasoning models (Cosmos-Reason1), robotics (Figure 03, Helix 02), and AI coding agents (Claude Code, Karpathy's views).

### Other Domains
Personal finance (Korean real estate tax), geopolitics (global intelligence crisis), and education (high school strategy).

## Key Entities
- [[NVIDIA]] — GPU architecture, inference platforms
- [[AMD]] — competitor in inference benchmarks
- [[Groq]] — LPU inference accelerator
- [[OpenAI]] — referenced in context of reasoning models
- [[Anthropic]] — Claude Code, MCP
- [[Google]] — Android boot security, TPU
- [[Samsung]] / [[SKHynix]] — HBM/HBF memory

## Key Concepts
- [[LearningCurves]] — train/validation loss analysis
- [[ConvolutionalNeuralNetworks]] — local connectivity, parameter sharing
- [[Convolution]] — kernel, stride, padding
- [[EarlyStopping]] — validation-based training termination
- [[Overfitting]] / [[Underfitting]] — diagnosis via learning curves
- [[Backpropagation]] — gradient-based weight updates
- [[BatchNormalization]] / [[Dropout]] — regularization techniques
- [[SpeculativeDecoding]] — LLM inference acceleration
- [[ContextRot]] — LLM performance degradation with long inputs
- [[Quantization]] — number formats for efficient inference
- [[RAG]] — retrieval-augmented generation
- [[VisionTransformer]] — attention-based alternative to CNNs

## Open Questions
- How do learning curve patterns differ for very large models (e.g., LLMs) where validation loss may not be available?
- What are the practical trade-offs between CNNs and Vision Transformers for modern computer vision tasks?