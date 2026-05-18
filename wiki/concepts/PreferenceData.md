---
title: "Preference Data"
type: concept
tags: [rlhf, alignment, data]
sources: [2026-05-18-day26-ai-ml-learning-review]
last_updated: 2026-05-18
---

## Definition
A dataset containing comparisons between multiple responses to the same prompt, indicating which response a human prefers. This is the foundation for training reward models and preference optimization methods.

## Data Format
```
{
  prompt: "Explain quantum entanglement to a 10-year-old.",
  chosen: "Response B (uses analogy, clear language, age-appropriate)",
  rejected: "Response A (too technical, assumes background knowledge)"
}
```

## Collection Methods
- Human annotators ranking or pairwise comparison
- Automated evaluation for clear metrics (code execution, math grading)
- Crowdsourced preference judgments

## What Gets Ranked
- Accuracy and correctness
- Helpfulness and relevance
- Clarity and readability
- Politeness and tone
- Safety and appropriateness
- Format compliance (lists, code blocks, etc.)

## Importance
- Captures nuanced judgment that single-answer data cannot
- Reflects actual human values and preferences
- Enables scalable learning from human feedback

## Connections
- Foundation for [[RLHF]] and [[RewardModel]] training
- Used in [[PreferenceOptimization]] methods
- Quality directly affects model alignment quality
- Related to [[InstructionTuning]] data but focuses on comparison rather than single correct answer
