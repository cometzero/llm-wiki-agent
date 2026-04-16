---
title: "NVIDIA Groq 3 LPX 소개[](#introducing_nvidia_groq_3_lpx )"
type: source
tags: [nvidia, inference]
date: 2026-04-16
source_file: raw/Nvidia/Inside_NVIDIA_Groq_3_LPX_The_Low-Latency_Inference_Accelerator_for_the_NVIDIA_Vera_Rubin_Platform.md
---

## Summary
NVIDIA Groq 3 LPX는 NVIDIA Vera Rubin platform을 위한 새로운 rack-scale inference accelerator로, agentic 시스템이 요구하는 low-latency와 large-context 워크로드를 겨냥해 설계되었습니다. NVIDIA Vera Rubin NVL72와 함께 co-design된 LPX는 빠르고 예측 가능한 token generation에 최적화된 엔진으로 AI factory를 보강합니다. 반면 Vera Rubin NVL72는 여전히 유연하고 범용적인 워크호스 역할을 유지하면서 학습과 inference에서 높은 throughput을 제공하며, prefill과 decode 전반(장문 맥락 처리, decode attention, 대규모 동시성 serving 포함)에서 성능을 담당합니다. 이 조합이 중요한 이유는, agentic 미래에서는 더 높은 형태의 inference가 필요하기 때문입니다. 사용자당 초당 token 생성 속도가 1,000 tokens/sec 수준에 접근하면, 모델은 단순 대화형 상호작용을 넘어 thinking-speed 상호작용에 가까워집니다. 이 속도에서는 AI가 reasoning, simulation, response를 연속적으로 수행할 수 있어, turn-based chat보다 실시간 협업에 가까운 사용자 경험이 가능해집니다.

## Key Claims
- Matrix execution modules (MXM): 텐서 연산용 dense multiply-accumulate를 제공하며, 고정된 데이터 타입으로 예측 가능한 throughput을 유지합니다.
- Vector execution modules (VXM): pointwise arithmetic, type conversion, activation function을 처리하며 lane당 여러 ALU로 구성된 mesh 방식으로 동작합니다.
- Switch execution modules (SXM): 순열, 회전, 분배, 전치(transposition) 등 구조화된 데이터 이동을 수행합니다.
- 가변 워크로드에서 줄어든 execution jitter

## Key Quotes
> "LPU chip-to-chip (C2C) 링크는 tray 내 직접 통신, tray 간 LPU C2C spine 통신, rack 간 통신을 지원합니다. interactive inference는 단순 계산량만이 아니라, 장치 간 데이터 이동 효율, 작업 협업 방식, 요청이 확산되며 생기는 지연 편차(가변 지연)를 얼마나 줄이느냐도 성능에 큰 영향을 주기 때문에 이 연결성이 중요합니다." — extracted from the source narrative.

## Connections
- [[NVIDIA]] — directly referenced in or strongly associated with this source.
- [[Groq3LPX]] — directly referenced in or strongly associated with this source.
- [[VeraRubinPlatform]] — directly referenced in or strongly associated with this source.
- [[Dynamo]] — directly referenced in or strongly associated with this source.
- [[InteractiveInference]] — one of the main technical themes discussed by this source.
- [[SpeculativeDecoding]] — one of the main technical themes discussed by this source.
- [[DeterministicExecution]] — one of the main technical themes discussed by this source.
- [[HeterogeneousInference]] — one of the main technical themes discussed by this source.

## Contradictions
- No explicit contradiction with existing wiki pages was identified during this first ingest pass.
