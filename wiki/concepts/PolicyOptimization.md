---
title: "Policy Optimization"
type: concept
tags: [rlhf, reinforcement-learning, training]
sources: [2026-05-18-day26-ai-ml-learning-review]
last_updated: 2026-05-18
---

## Definition
The process of adjusting a model\'s response generation policy to increase the probability of generating high-reward (human-preferred) responses. In LLMs, this means adjusting token selection probabilities.

## Context: LLM as Policy
- LLM = policy that selects next token given previous tokens
- Same prompt → multiple possible next tokens with different probabilities
- Policy optimization = adjust these probabilities to favor better responses

## Methods

### PPO-based (Classical RLHF)
1. Start with SFT model
2. Use reward model to score responses
3. Apply Proximal Policy Optimization
4. Include KL penalty to prevent divergence from SFT model

### DPO (Direct Preference Optimization)
- No separate reward model
- Directly increase P(chosen) and decrease P(rejected)
- Simpler, increasingly popular

## KL Penalty / Constraint
- Prevents model from "gaming" the reward model
- Maintains original language capabilities
- Balances improvement with stability
- "Safety belt" that keeps model behavior grounded

## Goal
- Not "new knowledge injection" but "preference alignment"
- More helpful, safer, better-formatted responses
- Responses that users actually prefer

## Connections
- Core step in [[RLHF]] pipeline
- Uses [[RewardModel]] to guide optimization
- Works on [[PolicyOptimization]] in the LLM\'s token selection
- Related to [[DPO]] as an alternative approach
- Follows [[SupervisedFineTuning]] in typical pipeline
