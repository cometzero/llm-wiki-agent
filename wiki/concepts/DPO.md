---
title: "DPO (Direct Preference Optimization)"
type: concept
tags: [rlhf, alignment, training]
sources: [2026-05-18-day26-ai-ml-learning-review]
last_updated: 2026-05-18
---

## Definition
A preference optimization method that directly adjusts model probabilities without training a separate reward model. It increases the probability of generating "chosen" responses and decreases probability of "rejected" responses.

## How It Differs from PPO-based RLHF
| Aspect | PPO-based RLHF | DPO |
|--------|---------------|-----|
| Reward Model | Required | Not needed |
| Complexity | Higher (RL loop) | Lower (classification-style loss) |
| Stability | More complex | Generally more stable |
| Compute | Higher | Lower |

## Loss Function Intuition
- Maximize: P(chosen response)
- Minimize: P(rejected response)
- Equivalent to pairwise classification where chosen should score higher

## Advantages
- Eliminates reward model training step
- Simpler implementation
- Avoids some RL complexities
- Good empirical results on alignment tasks

## Considerations
- Still benefits from quality [[PreferenceData]]
- May have different failure modes than PPO
- Research ongoing on comparative effectiveness

## Connections
- One method of [[PreferenceOptimization]]
- Alternative to PPO-based [[RLHF]]
- Uses [[PreferenceData]] directly
- Part of the broader alignment toolkit with [[SupervisedFineTuning]]
