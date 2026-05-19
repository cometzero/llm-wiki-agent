---
title: "Grounding"
type: concept
tags: [llm, reliability, RAG, citations]
sources: [2026-05-19-day27-ai-ml-learning-review]
last_updated: 2026-05-19
---

## Definition
Grounding connects LLM outputs to external evidence — documents, databases, search results, tool outputs, or citations — ensuring that generated content is anchored to verifiable sources rather than pure model memory.

## Why Grounding Is Essential
LLMs can generate fluent, confident, but factually incorrect text ([[Hallucination]]). Grounding mitigates this by:
1. Providing factual context the model can reference
2. Enabling verification by users/external systems
3. Reducing reliance on potentially outdated training data

## Grounding Techniques
- **RAG (Retrieval-Augmented Generation)**: Fetch relevant documents, include in context
- **Citations**: Include source references in responses
- **Tool use**: Query databases, APIs, calculators before answering
- **Chain-of-thought with verification**: Include validation steps
- **Policy grounding**: For chatbots, restrict outputs to approved content

## Examples
| Task | Ungrounded | Grounded |
|------|------------|----------|
| Q&A | "Revenue is 120B won" | "Per Q3 report, revenue is 118B won" |
| Code | Generate without checking docs | Retrieve API docs, generate compliant code |
| Medical | Answer without checking guidelines | Retrieve latest guidelines first |

## Related Concepts
- [[RAG]] — retrieval-augmented generation framework
- [[Hallucination]] — problem grounding addresses
- [[Calibration]] — expressing uncertainty about ungrounded knowledge
- [[Grounding]] in agent systems — tool use for evidence gathering

## Grounding in Production
- Customer support bots: Must ground in current policy documents
- Legal/medical AI: Grounding in authoritative sources is critical
- Research assistants: Citation and source verification
