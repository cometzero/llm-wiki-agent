---
title: "AI/ML Learning Review — Day 30 (2026-05-22): Evaluation, Serving, and AI System Design"
type: source
tags: [diary, ai-ml-learning, evaluation, serving, system-design]
date: 2026-05-22
source_file: raw/ai_ml_learning/2026-05-22-day30-ai-ml-learning-review.md
source_hash: 84720ce3739065ce
---

## Summary
Day 30 of the AI/ML learning curriculum covers three foundational concepts for production AI systems: model evaluation and benchmarks, serving and inference optimization, and the full picture of AI system design. The lesson emphasizes that good AI products require more than just good models—they need robust evaluation pipelines, efficient serving infrastructure, and continuous feedback loops.

## Key Claims
- Model evaluation measures whether a model is actually useful, distinct from training loss which only reflects next-token prediction accuracy
- Benchmark scores don't guarantee real-world service quality because benchmarks may not reflect actual user queries or may have been seen by the model during training
- Serving is the process of making trained models respond to real user requests; inference optimization makes this faster and cheaper
- AI systems should be understood as a cycle: data collection → model training → service deployment → user feedback → improvement
- Latency measures individual wait time while throughput measures total processing capacity; both matter but are often in tension

## Key Quotes
> "좋은 AI 제품은 좋은 모델 하나가 아니라, 평가로 품질을 확인하고, serving으로 안정적으로 제공하며, 데이터와 피드백으로 계속 개선되는 전체 시스템입니다."

> "latency는 한 사람의 대기 시간이고, throughput은 전체 처리량입니다. 고속도로로 비유하면 latency는 내 차가 목적지까지 가는 시간이고, throughput은 1시간 동안 도로가 처리할 수 있는 차량 수입니다."

> "benchmark 점수는 모델의 전체 능력이 아닙니다. 특정 시험을 잘 본 것일 뿐입니다."

## Connections
- [[Evaluation]] — core concept for measuring model quality
- [[Benchmark]] — standardized comparison framework
- [[Serving]] — operationalizing trained models
- [[Inference]] — computing outputs from trained models
- [[Latency]] — individual request response time metric
- [[Throughput]] — aggregate processing capacity metric
- [[Quantization]] — reducing model size for efficient serving
- [[KVCache]] — memory optimization for autoregressive generation
- [[Batching]] — grouping requests for parallel processing
- [[Streaming]] — token-by-token response delivery
- [[DataPipeline]] — data collection and preparation flow
- [[TrainingStack]] — model training infrastructure
- [[InferenceStack]] — model serving infrastructure
- [[FeedbackLoop]] — continuous improvement cycle
- [[RAG]] — retrieval-augmented generation system design
- [[RLHF]] — reinforcement learning from human feedback for alignment
- [[HumanEvaluation]] — manual quality assessment

## Evaluation and Benchmarks

### One-line Intuition
Model evaluation is the "exam" that verifies "is this model actually usable?" and a benchmark is a standardized test for comparing multiple models fairly.

### Definition
[[Evaluation]] (eval) measures how well a model performs a given task. [[Benchmark]] is a predefined dataset and problem set for comparing models under identical conditions. In LLM development, "running evals" is a constant activity to verify mathematical ability, code generation, instruction following, and honesty.

### Why It Matters
AI models are trained to minimize loss, but low loss doesn't guarantee user satisfaction. A translation model may have low training loss but produce awkward translations for long user inputs. Similarly, LLMs trained for next-token prediction don't always provide accurate, safe responses. Thus, "training metrics" and "actual user performance" must be evaluated separately.

### Evaluation Workflow
1. Define the task (translation, summarization, math, code generation, QA)
2. Prepare evaluation data (must be unseen during training for fairness)
3. Choose metrics (task-specific measurement criteria)
4. Generate model outputs (same inputs across models)
5. Compare via numbers or human evaluation

### LLM-Specific Considerations
LLMs often require multiple evaluation dimensions:
- Accuracy: Are facts correct?
- Completeness: Was essential content included?
- Instruction compliance: Did the model follow the requested format?
- Safety: Did it avoid harmful or inappropriate responses?
- Helpfulness: Can the user actually benefit?

## Serving and Inference Optimization

### One-line Intuition
[[Serving]] is making a trained model respond to real user requests; inference optimization makes this faster, cheaper, and more scalable.

### Definition
[[Inference]] is computing outputs from a trained model for new inputs. [[Serving]] is providing this inference as an actual service—users input questions via an app, the server calls the model, the model generates answers, and results are returned. [[Inference]] optimization techniques include reducing [[Latency]], increasing [[Throughput]], [[Quantization]], and [[KVCache]] usage.

### Why Speed Matters
Even smart models fail as services if too slow. If a chatbot's first response takes 30 seconds, most users find it frustrating. LLM cost is significant because large matrix operations run for each user query. A service serving 100 users daily vs. 1 million users daily requires completely different serving strategies.

### Key Techniques
- [[Quantization]]: Reducing precision (e.g., 32-bit to 8-bit) cuts memory by ~4x with acceptable accuracy loss
- [[KVCache]]: Stores previous token keys/values to avoid recomputation during autoregressive generation
- [[Batching]]: Groups multiple requests for parallel processing
- [[Streaming]]: Sends tokens as generated rather than waiting for complete response

## AI System Design

### One-line Intuition
AI systems are a cycle: collect data → train models → serve users → incorporate feedback → improve.

### Four Pillars
- [[DataPipeline]]: Collecting, cleaning, and transforming raw data into usable form
- [[TrainingStack]]: Training code, hardware, optimizer, distributed training
- [[InferenceStack]]: Serving configuration for fast, stable execution
- [[FeedbackLoop]]: Collecting user reactions and errors for improvement

### Full System Pipeline
1. Problem definition (what user problem to solve)
2. Data collection (gather necessary data)
3. Data cleaning (handle duplicates, errors, PII, outliers)
4. Training or prompt/RAG design
5. Evaluation (benchmark, eval, human evaluation)
6. Deployment and serving
7. Monitoring (Latency, error rate, cost, user satisfaction)
8. Feedback loop (failure cases and reactions inform next iteration)

## Contradictions
- No contradictions detected with existing wiki content. This lesson builds on concepts from previous days (Days 25-29) and provides synthesis rather than conflicting information.
