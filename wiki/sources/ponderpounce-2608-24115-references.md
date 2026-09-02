---
title: "PonderPounce 참고 문헌: VLA memory·demonstration conditioning·slow-fast control"
type: source
tags: [vision-language-action, robotics, references, memory, dual-system, control]
date: 2026-09-02
source_url: https://arxiv.org/html/2608.24115
hf_url: https://huggingface.co/papers/2608.24115
arxiv_id: "2608.24115"
arxiv_url: https://arxiv.org/abs/2608.24115
pdf_url: https://arxiv.org/pdf/2608.24115
week: "2026-W36"
ingested_at_kst: "2026-09-02 09:40:54 KST"
selected_reason: "PonderPounce의 contextual memory와 action-interface design을 이해하는 핵심 reference를 정리한다."
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W36/ponderpounce-episode-context-2608-24115/references.md
source_hash: eba425e19cccded7
---

## Summary
이 문서는 [[PonderPounce]]를 읽을 때 함께 봐야 할 참고문헌 10개를 묶은 reference map이다. 축은 크게 [[RoboMME]] 계열의 memory benchmark, [[RoboTTT]]/[[MEM]]/[[MemoryVLA]]의 memory representation 설계, 그리고 [[SeeTraceAct]], [[Latent Bridge]], [[Libra-VLA]], [[StreamVLA]], [[Asynchronous Fast-Slow Vision-Language-Action Policies for Whole-Body Robotic Manipulation]], [[Running VLAs at Real-time Speed]]로 이어지는 slow-fast control 및 latency 관점이다.

핵심 메시지는 [[PonderPounce]]가 "memory를 넣는다"는 일반론이 아니라, episode context를 어떻게 유지하고 언제 최신 cognition을 제어 경로에 주입할지라는 문제를 다룬다는 점이다. 따라서 비교군도 단순 VLA baseline이 아니라 memory 압축, retrieval, demonstration grounding, async scheduling, serving latency까지 포함해야 한다.

## Key Claims
- [[RoboMME]]는 robot policy memory를 Counting, Permanence, Reference, Imitation으로 분해하는 주요 benchmark다.
- [[RoboTTT]]는 history를 fast weight로 압축하는 test-time-training 계열로, context를 parameter update로 보존하는 대안이다.
- [[MEM]]은 short video와 recursive language memory를 결합하는 multi-scale embodied memory 방법이다.
- [[MemoryVLA]]는 external memory bank에서 retrieve/fuse하는 perceptual-cognitive memory 접근이다.
- [[SeeTraceAct]]는 cross-embodiment demonstration video를 latent plan/visual trace로 grounding한다.
- [[Latent Bridge]]는 slow reasoning과 fast action policy 사이의 latent interface 효율을 다룬다.
- [[Libra-VLA]]는 asynchronous coarse-to-fine dual-system learning으로 slow-fast 분리를 다룬다.
- [[StreamVLA]]는 completion-state gating으로 reasoning-action cycle을 조절한다.
- [[Asynchronous Fast-Slow Vision-Language-Action Policies for Whole-Body Robotic Manipulation]]은 whole-body robot에서 slow semantic policy와 fast motor policy를 분리한다.
- [[Running VLAs at Real-time Speed]]는 VLA deployment latency를 시스템 관점에서 해석해야 함을 상기시킨다.

## Key Quotes
> Semantic Scholar `ARXIV:2608.24115/references` endpoint와 원문 reference를 바탕으로, memory representation·context-to-control·benchmark 축에서 10개를 골랐다.

> PonderPounce의 contextual memory와 action-interface design을 이해하는 핵심 reference를 정리한다.

## Connections
- [[PonderPounce]] — 이 reference map의 중심 대상.
- [[RoboMME]] — memory benchmark 축.
- [[RoboTTT]] — context scaling / test-time adaptation 축.
- [[MEM]] — multi-scale embodied memory 축.
- [[MemoryVLA]] — external memory bank 기반 대조군.
- [[SeeTraceAct]] — demonstration grounding 축.
- [[Latent Bridge]] — slow-fast interface efficiency 축.
- [[Libra-VLA]] — asynchronous coarse-to-fine learning 축.
- [[StreamVLA]] — reasoning/action gating 축.
- [[Running VLAs at Real-time Speed]] — serving latency 해석 축.
- [[DualSystemArchitecture]] — slow reasoning과 fast control 분리의 공통 배경.
- [[PersistentMemory]] — append-only episode memory와 연결.
- [[InferencePlanning]] — cognition refresh와 action invocation 스케줄링과 연결.
- [[TemporalDecay]] — context age가 제어 성능에 미치는 영향과 연결.

## Contradictions
- 기존 [[MemoryVLA]]류는 external bank와 retrieval을 전제하는 경우가 많은데, [[PonderPounce]]는 pretrained [[MultimodalModel|MLLM]]의 native context를 memory substrate로 쓰는 쪽에 더 가깝다.
- context 길이 확대만으로 memory 문제가 해결된다는 낙관과 달리, 이 reference map은 latency와 refresh scheduling이 함께 설계되어야 한다는 점을 강조한다.
- [[Running VLAs at Real-time Speed]]류 latency 관점은 PonderPounce의 p50 수치를 실제 closed-loop deadline과 동일시하지 말아야 한다는 보정점을 제공한다.