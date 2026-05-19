---
title: "Calibration"
type: concept
tags: [llm, reliability, uncertainty, evaluation]
sources: [2026-05-19-day27-ai-ml-learning-review]
last_updated: 2026-05-19
---

## Definition
Calibration measures how well a model's confidence estimates match its actual accuracy. A well-calibrated model says "90% confident" and is correct ~90% of the time. Poor calibration means confidence and accuracy diverge.

## Key Metrics
- **Expected Calibration Error (ECE)**: Weighted average of confidence-accuracy gap
- **Overconfidence**: Model says 80% but only correct 50% of the time
- **Underconfidence**: Model says 50% but correct 80% of the time

## Why Calibration Matters
- **Risk assessment**: In high-stakes domains, knowing model uncertainty enables appropriate responses
- **Human-AI collaboration**: Calibrated confidence helps humans decide when to trust model outputs
- **Reliability**: Users can set thresholds based on confidence levels

## Calibration vs Hallucination
- [[Hallucination]] deals with whether outputs are factually correct
- Calibration deals with whether the model knows WHAT IT DOESN'T KNOW
- Well-calibrated models can still hallucinate, but they should express uncertainty

## Improving Calibration
- Temperature scaling: Post-hoc adjustment of confidence
- Teaching models to say "I don't know"
- Constitutional AI / RLHF focused on uncertainty expression
- Ensemble methods for more robust confidence estimation

## Related Concepts
- [[Hallucination]] — what calibration helps mitigate
- [[Grounding]] — external evidence for factual grounding
- [[Uncertainty]] — expressing what the model doesn't know
- Temperature scaling — calibration technique
