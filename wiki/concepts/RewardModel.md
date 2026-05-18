---
title: "Reward Model"
type: concept
tags: [rlhf, alignment, training]
sources: [2026-05-18-day26-ai-ml-learning-review]
last_updated: 2026-05-18
---

## Definition
A machine learning model trained to predict how a human would rate a given response to a prompt. It outputs a scalar "reward" score indicating the quality of the response from a human preference perspective.

## Training Process
1. Collect [[PreferenceData]]: pairs of responses with human rankings
2. Train model to predict which response humans prefer
3. Output: scalar reward score for any (prompt, response) pair

## Role in RLHF
- Serves as a proxy for human judgment
- Enables scalable feedback without requiring humans for every training step
- Guides [[PolicyOptimization]] to generate higher-quality responses

## Challenges
- Can learn biases present in human preference data
- May have blind spots exploitable by models ("reward hacking")
- Quality depends heavily on preference data quality

## Example
- Response A (short, vague): reward = 0.2
- Response B (detailed, helpful): reward = 0.9

The policy will learn to generate more B-like responses.

## Connections
- Central to [[RLHF]] pipeline
- Trained from [[PreferenceData]]
- Used in [[PolicyOptimization]]
- Related to [[DPO]] which eliminates the need for a separate reward model
