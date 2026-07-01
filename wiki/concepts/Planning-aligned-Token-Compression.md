---
title: "Planning-aligned Token Compression"
type: concept
tags: [token-compression, autonomous-driving, efficiency]
sources: [qwen-robotnav-2606-18112-references]
last_updated: 2026-07-01
---

## Definition
Planning-aligned Token Compression은 monolithic vision-action models에서 extended temporal context를 encoding할 때 발생하는 real-time computational budget 문제를 해결한다. Token compression이 architecture와 가장 compatible한 해결책이다.

## Key Insight
Linear transformers나 external memory가 context를 lightweight하게 만들지만, token compression이 architecture compatibility 측면에서 가장 우수하다.

## Connections
- [[QwenRobotNav]] — VLA deployment efficiency 관련
- [[VLA Inference Efficiency]] — long-context problem
- [[Autonomous Driving]] — trajectory planning의 computational constraint
