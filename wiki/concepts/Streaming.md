---
title: "Streaming"
type: concept
tags: [ai-ml, serving, user-experience, latency]
sources: [2026-05-22-day30-ai-ml-learning-review]
last_updated: 2026-05-22
---

## Definition

[[Streaming]] in LLM serving means sending tokens to the user as they are generated, rather than waiting for the complete response before transmitting anything. Users see text appear progressively.

## Why It Matters

Users perceive responses as "fast" when first tokens appear quickly, even if total generation time is unchanged. Streaming:
- Reduces perceived latency dramatically
- Creates a sense of "AI is thinking"
- Prevents timeout issues for long responses

## Time to First Token (TTFT)

The most important streaming metric—how quickly the first token appears after the user submits their query. This is the primary driver of perceived speed.

## Implementation

Streaming requires:
- Server-sent events (SSE) or WebSockets
- Token-by-token response as model generates
- Client-side rendering of streaming output

## Connections
- [[Serving]] — key UX feature for production chatbots
- [[Latency]] — streaming primarily improves perceived latency
- [[Inference]] — continuous token generation enables streaming
- [[TrainingStack]] — doesn't directly affect training
