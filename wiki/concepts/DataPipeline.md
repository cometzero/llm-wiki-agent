---
title: "Data Pipeline"
type: concept
tags: [ai-ml, data, mlops, system-design]
sources: [2026-05-22-day30-ai-ml-learning-review]
last_updated: 2026-05-22
---

## Definition

The [[DataPipeline]] is the flow that transforms raw data into forms usable by models—encompassing collection, cleaning, transformation, and storage.

## Components

1. **Collection**: Gathering data from various sources
2. **Cleaning**: Handling duplicates, errors, PII, outliers
3. **Transformation**: Converting to embeddings, tokenization, chunking
4. **Storage**: Vector databases, data lakes, feature stores
5. **Quality assurance**: Validating data integrity and freshness

## Why It Matters

"Garbage in, garbage out"—even the best models fail with poor data. For RAG systems:
- Missing documents mean wrong answers
- Outdated documents cause hallucination
- PII exposure creates compliance risk

## Example: RAG Data Pipeline

1. Collect documents from Google Drive, Notion, PDFs
2. Split into chunks (text chunking)
3. Generate embeddings via [[EmbeddingModel]]
4. Store in vector database for similarity search
5. Implement access control and refresh cycles

## Connections
- [[TrainingStack]] — feeds data into model training
- [[FeedbackLoop]] — user feedback can trigger pipeline updates
- [[RAG]] — data pipeline is fundamental to RAG systems
- [[Serving]] — data pipeline quality affects serving quality
- [[Evaluation]] — eval data must also follow pipeline quality standards
