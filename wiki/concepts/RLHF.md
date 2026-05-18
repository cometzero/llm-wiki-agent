---
title: "RLHF (Reinforcement Learning from Human Feedback)"
type: concept
tags: [llm, alignment, reinforcement-learning]
sources: [2026-05-18-day26-ai-ml-learning-review]
last_updated: 2026-05-18
---

## Definition
A method that uses human feedback to improve a model\'s response policy. Unlike SFT (which follows a single "correct" answer), RLHF learns from preferences between multiple responses.

## The Problem SFT Can\'t Fully Solve
- Good answers are rarely unique
- Human judgment involves multiple factors: accuracy, helpfulness, politeness, conciseness, safety
- SFT teaches "what a good answer looks like" but not "which of several good answers is better"

## RLHF Pipeline

### Step 1: Prepare SFT Model
- Start with an instruction-following model

### Step 2: Collect Preference Data
- Generate multiple responses for the same prompt
- Have humans rank/binary-choose the better response
- Format: {prompt, chosen, rejected}

### Step 3: Train Reward Model
- Learns to predict "human preference score" for any response
- Input: prompt + response → scalar reward

### Step 4: Policy Optimization
- Adjust LLM to generate responses with higher reward
- Typically uses PPO (Proximal Policy Optimization)
- Includes KL penalty to prevent drifting too far from original SFT model

## Preference Optimization Variants

### PPO-based RLHF
- Full pipeline: SFT → preference data → reward model → RL training
- Computationally intensive

### [[DPO]] (Direct Preference Optimization)
- No separate reward model needed
- Directly increases probability of chosen answers and decreases rejected answers
- Simpler implementation

## Key Considerations
- Reward hacking: models may exploit reward model weaknesses (e.g., producing overly long responses)
- Preference data can contain human biases
- Safety and honesty are part of the preference criteria

## Connections
- Builds on [[SupervisedFineTuning]] (typically starts with SFT model)
- Related to [[RewardModel]] and [[PreferenceData]]
- [[PolicyOptimization]] adjusts the model\'s response selection strategy
- Leads to more helpful, safer, and more preferred AI assistants
- See also [[PreferenceOptimization]] for broader methods
