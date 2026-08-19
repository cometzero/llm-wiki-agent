---
title: "Spatial Memory Agent 참고 레퍼런스"
type: source
tags:
  - spatial-memory
  - vision-language-model
  - retrieval
  - procedural-memory
  - embodied-ai
  - references
date: 2026-08-19
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W33/spatial-memory-agent-2608-12743/references.md
source_hash: 4272c592235e1419
---

## Summary
이 참고문헌 정리는 [[SpatialMemoryAgent]](SMA)가 어떤 계보 위에 서 있는지 보여 준다. 핵심 비교축은 공간 표현 학습 계열([[SpatialVLM]], [[SpatialRGPT]], [[EmbSpatial-Bench]])과 메모리/에이전트 계열([[RAG]], [[Mem0]], [[MemP]]), 그리고 도구/자기진화 계열([[SpaceTools]], [[S-Agent]], [[SpatialEvo]])이다.

논문의 메시지는 단순한 의미 유사도 검색보다, 실제로 새 과제에 전이되었는지를 반영하는 절차 메모리와 신뢰도 보정이 더 중요하다는 점이다. 읽기 순서는 retrieval-memory 기본기에서 공간 grounding, procedural memory, tool use/self-evolution 비교로 이어진다.

## Key Claims
- [[SpatialVLM]]과 [[SpatialRGPT]]는 공간 관계를 학습된 표현에 담는 반면, [[SpatialMemoryAgent]]는 runtime retrieval로 절차를 보강한다.
- [[EmbSpatial-Bench]]는 left/right/above/under/near/far 같은 언어-공간 관계를 embodied task 관점에서 평가하는 대표 벤치마크다.
- [[RAG]]는 semantic similarity retrieval의 기본선이며, SMA는 여기에 실제 전이 성과를 반영하는 [[TransferReliabilityScore]](TRS)를 추가한다.
- [[Mem0]]는 production-oriented long-term memory 관리 축을 보여 주고, SMA는 generic memory보다 verifier-grounded spatial procedure를 중심 상태로 삼는다.
- [[MemP]]는 procedural memory baseline으로서 가장 직접적인 비교 대상이며, SMA는 semantic retrieval에 TRS 보정을 더해 더 신뢰도 높은 경험 선택을 지향한다.
- [[SpaceTools]]와 [[S-Agent]]는 tool-augmented spatial reasoning 계열로, SMA가 제안하는 tool-free inference와 대비되는 대안이다.
- [[SpatialEvo]]는 deterministic geometric environment 기반 self-evolution 축으로, training-based route와 external memory route의 차이를 비교하게 해 준다.

## Key Quotes
> "Semantic similarity만으로는 실제로 transfer된 절차를 고르기 어렵다." — SMA가 강조하는 retrieval 한계

> "읽기 순서는 memory/retrieval의 기본 가정부터 공간 grounding, procedural memory, tool use/self-evolution 비교로 간다." — 이 참고문헌 정리의 핵심 안내

## Connections
- [[SpatialMemoryAgent]] — 중심 방법론
- [[SpatialVLM]] — 공간 표현을 학습하는 비교 축
- [[SpatialRGPT]] — grounded spatial reasoning 비교 축
- [[EmbSpatial-Bench]] — 핵심 평가 벤치마크
- [[RAG]] — semantic retrieval baseline
- [[Mem0]] — production memory 관리 계열
- [[MemP]] — procedural memory baseline
- [[SpaceTools]] — tool-augmented spatial reasoning
- [[S-Agent]] — spatial tool use 대안
- [[SpatialEvo]] — training-based self-evolution 비교 대상
- [[PersistentMemory]] — 장기 메모리 설계 축
- [[RetrievalAugmentedPolicy]] — retrieval-based policy 보정 상위 개념
- [[EmbodiedIntelligence]] — 적용 문제 영역

## Contradictions
- 단순 의미 유사도 중심 retrieval가 충분하다는 관점과 다르게, 이 소스는 [[TransferReliabilityScore]]로 실제 전이 신뢰도를 별도로 추적해야 한다고 본다.
- tool-based spatial reasoning이나 training-based self-evolution이 유일한 해법이라는 주장과 달리, 이 소스는 read-only memory 보정만으로도 유효한 대안을 제시한다.
