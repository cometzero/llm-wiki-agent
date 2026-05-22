---
title: "Feedback Loop"
type: concept
tags: [ai-ml, continuous-improvement, system-design, mlops]
sources: [2026-05-22-day30-ai-ml-learning-review]
last_updated: 2026-05-22
---

## Definition

The [[FeedbackLoop]] is the cyclical process of collecting user reactions and errors, then incorporating that data into future model improvements.

## Why It Matters

Without feedback loops, AI systems stagnate. User needs change, new edge cases emerge, and models that were accurate become outdated. The feedback loop ensures continuous improvement.

## The Feedback Cycle

1. **Collect**: Gather user reactions (likes, dislikes, corrections)
2. **Analyze**: Identify patterns in failures
3. **Prioritize**: Determine which issues to address
4. **Improve**: Update [[DataPipeline]], [[Evaluation]], or model
5. **Deploy**: Release improved system
6. **Repeat**

## Quality Control

Not all feedback is good feedback:
- Malicious inputs may be designed to corrupt models
- Unintentional user mistakes shouldn't be reinforced
- Feedback must be curated and [[Evaluation|evaluated]] before incorporation

## Example

Customer service chatbot:
- User flags "This answer is wrong"
- Collect flagged cases
- Add to eval set
- Verify improvement before deployment
- Next version scores higher on this edge case

## Connections
- [[Evaluation]] — feedback informs what to evaluate
- [[DataPipeline]] — feedback data enters the pipeline
- [[TrainingStack]] — may use feedback for fine-tuning
- [[Serving]] — monitoring captures feedback signals
- [[RLHF]] — human feedback is a key feedback source
