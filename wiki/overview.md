# Wiki Overview

*Living synthesis of all ingested sources.*

## Current State

This wiki documents a broad range of topics including AI/ML learning (from fundamentals to deep learning), semiconductor hardware (NVIDIA, AMD, memory), Linux kernel development, automotive software, and emerging AI technologies.

### AI/ML Learning Path

The learning journey has progressed from basic ML concepts (Day 1–12) through neural network fundamentals (Day 13–14) and training mechanics (Day 15–16) to CNN architecture (Day 17–18). Day 18 introduces three core CNN concepts: channels/feature maps/filters, pooling/downsampling, and Residual Networks (ResNet) with skip connections. These concepts are foundational for understanding modern deep learning architectures including [[Transformer]] models and [[LLM]] residual streams.

### Key Themes

- **Deep Learning Training Stability**: Initialization, normalization, dropout, and now skip connections all address the challenge of training deep networks.
- **Representation Learning**: From raw pixels to abstract features — CNNs build hierarchical representations; this mirrors the hidden state evolution in [[Transformer]] models.
- **Computation vs. Information Trade-off**: Pooling reduces computation but loses spatial precision; skip connections preserve gradient flow at the cost of extra parameters.

### Open Questions

- How do modern architectures (e.g., Vision Transformers) compare to CNNs on the same tasks?
- What are the practical limits of depth with ResNet-style skip connections?

### Sources Ingested

See [Index](index.md) for full list.