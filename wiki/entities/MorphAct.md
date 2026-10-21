---
title: "MorphAct"
type: entity
tags: [VLA, robotics, contextual-parameterization]
sources: ["morphact-2610-20019-paper-ko", "morphact-2610-20019-analysis", "morphact-2610-20019-references", "morphact-2610-20019-learning"]
last_updated: 2026-10-21
---

# MorphAct

현재 observation·instruction·robot state에서 VLM과 action module의 low-rank update를 생성하는 numerical-action VLA framework. vision-side update 이후 representation이 action generator를 condition한다. native action objective로 generator를 공동 학습하고 update는 action chunk 안에서 재사용한다.

## Evidence and boundaries
- LIBERO·Meta-World·네 physical task의 closed-loop success를 보고한다. π0.5 LIBERO mean은 96.85→98.60%지만 Spatial은 소폭 하락한다.
- additional generator는 cost-free가 아니다. Appendix D.2의 π0.5 chunk latency 164 ms, measured control rate 21.20 Hz는 해당 실험 설정의 수치다.
- 차량 제어, NPU speedup, formal safety를 입증한 연구가 아니다. [[GroundingPI]]의 perception pretraining과 [[PerturBot]]의 data intervention과는 intervention layer가 다르다.

## Connections
- [[ContextualParameterGeneration]] — mechanism
- [[LoRA]] — factor representation
- [[morphact-2610-20019-paper-ko]] — source deliverable
- [[morphact-2610-20019-analysis]] — source deliverable
- [[morphact-2610-20019-references]] — source deliverable
- [[morphact-2610-20019-learning]] — source deliverable
