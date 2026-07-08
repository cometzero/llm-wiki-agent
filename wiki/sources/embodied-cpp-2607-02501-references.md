---
title: "Embodied.cpp 참고 레퍼런스 요약"
type: source
tags: [VLA, WAM, embodied-ai, references]
date: 2026-07-08
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W28/embodied-cpp-portable-inference-runtime-2607-02501/references.md
source_hash: 2b9d49424697556e
---

## Summary
Semantic Scholar와 arXiv HTML 본문 citation을 기반으로 [[Embodied.cpp]]의 핵심 선행 연구 10개를 정리한 레퍼런스 요약이다. [[Execution-State Capsules]], [[MultiRate Execution]], [[WorldActionModel]], [[VLA]] inference, on-device deployment 관련 연구를 포괄하며, Embodied.cpp의 VLA+WAM first-class 지원과 heterogeneous hardware 타겟팅의 이론적·실천적 배경을 제공한다.

## Key Claims
- [[Execution-State Capsules]]는 KV cache뿐 아니라 recurrent/convolution/MTP state, metadata까지 포함한 complete restorable state를 graph-bound capsule로 저장/복원하며 sub-millisecond restore 달성
- [[MuseVLA]]는 RGB뿐 아니라 temperature, audio, radar 등의 sensor를 tool처럼 호출하는 adaptive multimodal sensing VLA의 사례
- [[LaWAM]]은 pixel-space video rollout 대신 compact latent visual subgoal을 예측하는 latent-space WAM으로 높은 success와 낮은 latency 보고
- [[DAM-VLA]]는 VLA의 synchronous clock 문제를 지적하고 modality별 latent buffer를 sensor rate에 맞게 refresh하는 asynchronous multi-rate execution 제안 (100Hz reactive control)
- [[WorldActionModel]] survey는 WAM을 future state modeling과 action generation을 결합하는 embodied foundation model paradigm으로 정의하고 taxonomy 정리
- [[Being-H0.7]]은 future observation embedding을 posterior branch로 사용하는 WAM/VLA hybrid로, training-only branch와 deployable prior branch 경계 관리 필요성 제시
- [[Stop Wandering]]은 embodied/navigation에서 3D semantic map, revisiting penalty, LLM reflective correction을 결합하며 spatial memory와 planner state도 runtime object가 됨을 보여줌
- [[H2O]]는 모델 weight가 KV cache보다 memory bottleneck이 되는 경우를 분석하고 hierarchical weight orchestration 제안
- [[vla.cpp]]은 Embodied.cpp의 직접적인 predecessor로 VLA를 portable C++ inference runtime으로 배포하나 WAM과 modular multi-component optimization은 제한적
- VLA foundation model family([[Pi0]], [[π0.5]], [[OpenVLA]], [[RT-2]])는 pretrained VLM semantics를 robot action generation으로 연결하나 action token/continuous action head/action chunk 형식 차이가 runtime complexity로 나타남

## Key Quotes
> "KV cache만 재사용하는 LLM serving과 달리, recurrent state, convolution state, MTP state, metadata까지 포함한 complete restorable state를 graph-bound capsule로 저장/복원한다" — [[Execution-State Capsules]] 요약

> "VLA가 모든 modality를 하나의 synchronous clock으로 처리하는 문제를 지적하고, modality별 latent buffer를 sensor rate에 맞게 refresh한다" — [[DAM-VLA]] 요약

> "VLA-centric이며 WAM과 modular multi-component optimization은 제한적이다. Embodied.cpp는 여기서 VLA+WAM, robot+simulator, heterogeneous hardware 지원으로 범위를 확장한다" — [[vla.cpp]] vs [[Embodied.cpp]] 비교

## Connections
- [[Embodied.cpp]] — 이 레퍼런스 요약의 대상 논문; VLA/WAM C++ runtime
- [[vla.cpp]] — Embodied.cpp의 직접적 predecessor
- [[Execution-State Capsules]] — latency-first batch-1 physical-AI serving 배경 연구
- [[DAM-VLA]] — multi-rate execution 필요성을 보여주는 asynchronous VLA
- [[WorldActionModel]] — WAM first-class 지원의 이론적 배경
- [[MuseVLA]] — extensible embodied I/O 필요성 시연
- [[LaWAM]] — latent-space WAM 사례
- [[Being-H0.7]] — WAM/VLA hybrid deployable architecture 사례
- [[Stop Wandering]] — spatial memory/planner state가 runtime object가 되는 사례
- [[H2O]] — on-device memory orchestration 관련 연구
- [[Pi0]], [[π0.5]], [[OpenVLA]], [[RT-2]] — Embodied.cpp가 target으로 삼는 VLA 모델 family

## Contradictions
- 없음. 기존 wiki의 [[Embodied.cpp]] 소스와 동일한 paper(2607.02501)에서 직접 파생된 레퍼런스 정리로矛盾 없음.
