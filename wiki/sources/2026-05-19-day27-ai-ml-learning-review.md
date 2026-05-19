---
title: "AI/ML Learning Review — Day 27 (2026-05-19): Decoding Strategies, Context Window, Hallucination/Calibration/Grounding"
type: source
tags: [ai-ml-learning, decoding, context-window, hallucination, calibration, grounding]
date: 2026-05-19
source_file: raw/ai_ml_learning/2026-05-19-day27-ai-ml-learning-review.md
source_hash: 53e0aabdaafbcaa6
---

## Summary
Day 27 covers three foundational inference-time concepts: (1) decoding strategies that control how LLM selects the next token, (2) context window and KV cache limitations that govern how much memory is available during generation, and (3) hallucination, calibration, and grounding — the trio of concepts that determine how trustworthy LLM outputs are.

## Key Claims
- Decoding strategies (greedy, beam search, temperature, top-k, top-p) control the balance between accuracy and creativity without changing the model's underlying knowledge
- Context window is the "workspace" size — maximum tokens LLM can process at once — and when exceeded, earlier information is dropped
- KV cache stores key/value activations to speed up generation but consumes GPU memory proportional to sequence length and model size
- Hallucination occurs because LLM optimizes for "natural-sounding next token" rather than "factual correctness"
- Grounding connects answers to external evidence (documents, search, tool outputs) to reduce hallucination
- Calibration measures whether model confidence matches actual accuracy — overconfidence is dangerous in high-stakes domains

## Key Quotes
> "LLM 추론은 '다음 token을 어떻게 고를지', '얼마나 많은 context를 볼 수 있는지', '답을 얼마나 믿을 수 있게 만들지'가 함께 결정하는 과정이다" — Day 27 one-liner summary

> "temperature는 '선택의 과감함'을 조절하는 손잡이라고 보면 된다" — intuitive explanation of temperature

## Connections
- [[GreedyDecoding]] — simplest decoding strategy, picks highest probability token
- [[BeamSearch]] — explores multiple candidate paths for better output quality
- [[Temperature]] — controls probability distribution sharpness for diverse vs conservative outputs
- [[TopK]] — restricts candidates to top k tokens by probability
- [[TopP]] — restricts candidates to those whose cumulative probability exceeds p (nucleus sampling)
- [[ContextWindow]] — maximum token range LLM can process in one forward pass
- [[KVCache]] — memory structure storing key/value activations to speed up autoregressive generation
- [[Hallucination]] — confident-sounding but factually incorrect model outputs
- [[Calibration]] — alignment between model confidence and actual accuracy
- [[Grounding]] — anchoring responses to external evidence (RAG, citations, tool outputs)
- Builds on [[2026-05-18-day26-ai-ml-learning-review]] — instruction tuning and RLHF alignment concepts
- Related to [[EP 96. LLM 추론 인프라와 토큰 경제학]] — prefill-decode structure and token economics

## Contradictions
- None identified. Content is consistent with established LLM inference fundamentals.

## Concepts Covered
1. **Decoding Strategies**: greedy decoding, beam search, temperature, top-k, top-p (nucleus sampling)
2. **Context & Memory**: context window, prompt length, KV cache, attention complexity O(n²)
3. **Trustworthiness**: hallucination, calibration, grounding, uncertainty expression
