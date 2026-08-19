---
title: "Spatial Memory Agent: 경험 기반 절차 메모리로 공간 추론을 보정하기"
type: source
tags: [spatial-intelligence, vision-language-model, memory, retrieval, verifier, embodied-ai, korean-technical-translation]
date: 2026-08-19
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W33/spatial-memory-agent-2608-12743/paper-ko.md
source_hash: 733f186cc13fc0c8
---

## Summary
[[SpatialMemoryAgent]](SMA)는 동결된 [[VisionLanguageModel|VLM]]이 파라미터 재학습이나 추론 시 외부 3D 도구 없이도, 검증된 공간 경험을 재사용하는 [[PersistentMemory|절차 메모리]]로 공간 추론을 개선할 수 있는지 묻는다. 이 방법은 verifier가 확인한 rollout을 reflection으로 짧은 transferable lesson으로 압축하고, 이후 retrieval에서는 semantic filtering과 [[TransferReliabilityScore|TRS]]를 결합해 실제로 도움이 된 경험을 우선적으로 선택한다.

논문은 다섯 개 대표 공간 벤치마크와 네 개 VLM에서 SMA가 다수 설정의 최고 성능을 기록했다고 보고한다. 핵심 메시지는 단순 유사도 검색이 아니라, "이 절차가 새 문제에서도 실제로 transfer 되었는가"를 반영하는 신뢰도 보정 메모리가 공간 지능의 병목을 완화할 수 있다는 점이다.

## Key Claims
- [[SpatialMemoryAgent]]는 frozen [[VLM]]을 유지한 채, verifier reward를 transferable spatial procedure로 바꾸는 training-free memory framework다.
- memory card에는 source task, rollout summary, transferable lesson, retrieval count, cumulative reward, and [[TransferReliabilityScore|TRS]]가 저장되며, raw prediction이나 정답 자체는 넣지 않아 leakage를 줄인다.
- one-pass memory writing은 중복 card 폭증을 줄이고, bank를 고정한 채 선택된 카드의 신뢰도만 갱신한다.
- two-stage retrieval은 semantic similarity threshold filtering 뒤, normalized similarity와 normalized TRS를 결합한 score로 카드를 고른다.
- TRS는 uniform prior에서 시작해 visit evidence와 reward를 반영하는 shrinkage estimator로 업데이트된다.
- 실험에서 SMA는 [[RoboSpatial]], [[ERQA]], [[Omni3D]], [[SAT]], [[EmbSpatial]] 등에서 plain RAG와 memory baseline보다 더 안정적인 개선을 보였다.
- ablation은 summary, transferable lesson, semantic filter 각각이 성능에 실질적으로 기여함을 보여 준다.

## Key Quotes
> "동결된 VLM이 파라미터 업데이트와 외부 전문가 도구 없이도, 검증된 경험으로 공간 추론을 스스로 개선할 수 있는가?" — 논문의 중심 질문

> "실패한 예시를 쌓는 것보다, 실제로 transfer된 절차를 보정해 저장하는 편이 더 중요하다." — TRS 기반 memory selection의 요지

## Connections
- [[SpatialMemoryAgent]] — 이 소스의 중심 방법론
- [[PersistentMemory]] — retrieval 가능한 장기 메모리라는 설계 축
- [[ReflectiveReasoning]] — verifier-guided reflection으로 lesson을 추출하는 과정
- [[RetrievalAugmentedPolicy]] — 메모리 기반 실행 보정의 상위 개념
- [[EmbeddingModel]] — task embedding similarity를 이용한 후보 필터링과 연결
- [[CosineSimilarity]] — similarity ranking의 기본 연산과 연결
- [[EmbodiedIntelligence]] — 공간 지능 및 embodied reasoning 문제 영역
- [[VLM]] — frozen backbone으로 사용되는 base model family
- [[Verification]] — memory card 생성의 품질 보증 축
- [[RAG]] — 단순 semantic retrieval과 대비되는 메모리 보정형 접근

## Contradictions
- 기존 [[RetrievalAugmentedPolicy]] 계열이 유사성 중심 retrieval을 주로 쓰는 반면, 이 소스는 TRS로 "실제로 transfer된 절차"를 별도로 반영해야 한다고 주장한다.
- 기존 공간 reasoning 방법이 외부 3D 도구 호출이나 파라미터 post-training에 치우친다면, 이 소스는 read-only deployment 메모리만으로도 성능을 개선할 수 있다고 본다.
