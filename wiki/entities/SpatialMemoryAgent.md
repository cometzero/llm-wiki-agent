---
title: "Spatial Memory Agent"
type: entity
tags: [memory, spatial-intelligence, embodied-ai]
sources: [spatial-memory-agent-2608-12743-paper-ko]
last_updated: 2026-08-19
---

[[SpatialMemoryAgent]]는 검증된 공간 경험을 짧은 절차 교훈으로 압축해 다시 쓰는 memory-based adaptation framework다. 동결된 [[VisionLanguageModel|VLM]]을 바꾸지 않고, verifier-guided reflection과 retrieval을 이용해 "어떤 공간 확인 절차가 도움이 되는가"를 학습한다.

## Key Properties
- frozen VLM 위에서 동작한다.
- raw answer 대신 transferable lesson을 저장한다.
- retrieval 시 semantic similarity와 [[TransferReliabilityScore|TRS]]를 함께 쓴다.
- read-only deployment에서도 메모리 bank를 그대로 사용할 수 있다.

## Connections
- [[TransferReliabilityScore]]
- [[PersistentMemory]]
- [[ReflectiveReasoning]]
- [[RetrievalAugmentedPolicy]]
- [[EmbodiedIntelligence]]
