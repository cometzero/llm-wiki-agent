---
title: "Efficient Inference for Driving Models"
type: concept
tags: [inference-optimization, deployment, latency, KV-cache]
sources: ["reflectdrive-2-2605-04647"]
last_updated: 2026-05-13
---

# Efficient Inference for Driving Models

ReflectDrive-2는 modeling과 serving을 함께 설계하여 NVIDIA Thor에서 약 30ms latency를 달성한다.

## 주요 최적화 기법

### Shared-prefix KV Reuse
- Visual/route/ego-state prefix는 decision, draft, reflect phase에서 공통이므로 재사용

### Mutable Action-cache Rewinding
- Action token block은 draft/edit 중 바뀌므로 prefix boundary까지 cache pointer를 rewind
- Mutable block만 재계산

### Action-expert FFN
- Action branch에는 compact FFN을 사용하여 latency 감소

### Fused On-device Unmasking
- Confidence ranking, token selection, state update를 CUDA kernel으로 fuse
- CPU synchronization 감소

### Alternating Step Decode (ASD)
- **Full-step frame**: 전체 decision-draft-reflect 수행
- **Lite-step frame**: 이전 plan을 현재 ego frame으로 transform한 뒤 짧은 AutoEdit만 수행

## 결과
NVIDIA Thor에서 평균 약 30ms (세부 최적화 표 기준 약 30.2ms) latency 달성

## Implications
VLA/LLM-style reasoning planner가 real-time constraint를 만족하려면 model architecture뿐 아니라 cache와 token update path까지 같이 설계해야 함을 시사.

## Connections
- [[ReflectDrive-2]] — 적용 대상
- [[NVIDIA]] — 타겟 하드웨어 Thor
- [[KVCache]] — Shared prefix reuse 기법
