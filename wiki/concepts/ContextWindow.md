---
title: "Context Window"
type: concept
tags: [llm, memory, inference, architecture]
sources: [2026-05-19-day27-ai-ml-learning-review, 2026-05-21-day29-ai-ml-learning-review]
last_updated: 2026-05-21
---

## Definition
The context window (context length) is the maximum number of tokens an LLM can process in a single forward pass. It includes the input prompt, previous conversation history, attached documents, and the output being generated.

## Key Properties
- **Model-specific**: Ranges from ~4K (early models) to 128K+ (modern models) to 1M+ (specialized models)
- **Shared budget**: Input + output must fit within the limit
- **Information loss**: Exceeding the window causes earlier content to be dropped (no automatic retrieval)
- **Cost/speed**: Longer context = more compute, memory, latency, and cost

## Why It Matters
- **Conversational memory**: Old messages may be forgotten when window fills
- **Document QA**: Long documents may not fit entirely
- **RAG necessity**: When documents exceed context window, retrieval/chunking is required

## Practical Implications
- **Prompt engineering**: Put most relevant information at the end (recency bias)
- **Memory management**: Summarize old conversation, use external storage
- **RAG integration**: Retrieve only relevant chunks to stay within limit

## Related Concepts
- [[KVCache]] — memory optimization for faster generation
- [[RAG]] — retrieval to handle longer contexts
- [[Attention]] — computational cost grows quadratically with context length
- [[Chunking]] — splitting long documents to fit within window

## Examples of Context Window Sizes
- GPT-3.5: 4K, 16K tokens
- GPT-4: 8K, 32K, 128K tokens
- Claude 3: 200K tokens
- Gemini 1.5: 1M tokens
