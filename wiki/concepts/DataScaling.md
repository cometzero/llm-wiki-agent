---
title: "Data Scaling"
type: concept
tags: [llm, training, data]
sources: [2026-05-18-day26-ai-ml-learning-review]
last_updated: 2026-05-18
---

## Definition
The practice of increasing the quantity and diversity of training data to improve model performance. In LLM training, this means more training tokens from more diverse sources.

## Key Aspects
- **Quantity**: More training tokens seen by the model
- **Diversity**: Coverage of different topics, languages, formats, and writing styles
- **Quality**: Clean, well-structured data vs. noisy web text

## Why It Matters
- LLMs learn by predicting next tokens from context
- More data = exposure to more contextual patterns
- Diverse data helps models generalize to new situations
- Data quality matters: garbage in, garbage out

## Scaling Dynamics
- [[ScalingLaw]] shows that data scaling and model size should be balanced
- Simply scaling data with a small model leads to wasted potential
- Large models need proportionally more data to be fully utilized

## Common Data Sources
- Web text (filtered and quality-assessed)
- Books and academic papers
- Code repositories
- Conversational data
- Specialized corpora for domain adaptation

## Connections
- Key dimension of [[ScalingLaw]]
- Related to [[ComputeBudget]]: more data = more training compute needed
- [[ParameterCount]] must be balanced with data scale
- Links to [[DataCurriculum]] and training curriculum design
