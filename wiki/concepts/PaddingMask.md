---
title: "Padding Mask"
type: concept
tags: [transformer, attention, masking, batch-processing]
sources: [2026-05-16-day24-ai-ml-learning-review.md]
last_updated: 2026-05-16
---

## Definition
A **padding mask** prevents attention to `<pad>` tokens that are added to equalize sequence lengths in batch processing. These tokens contain no semantic information and would corrupt token representations if attended to.

## Key Properties
- Required for all batch-processed Transformers ([[BERT]], [[GPT]], T5)
- Blocks attention to all `<pad>` positions regardless of query position
- Enables stable training across variable-length sequences
- Applied alongside causal mask in decoder models

## Example
In a batch with sequences of lengths [3, 5, 7] padded to length 7:
- All queries attend to actual tokens but not `<pad>` tokens at indices 3, 5-6
- Attention weights sum to 1 only over non-padded positions

## Related Concepts
- [[CausalMask]] — Often used together in decoder models
- [[AttentionMasking]] — General framework
- Batch processing — Context where padding is needed
- [[Transformer]] — Architecture this applies to
