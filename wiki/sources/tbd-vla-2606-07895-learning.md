---
title: "TBD-VLA: 시간 블록 Diffusion 기반 Vision-Language-Action 모델 — learning"
type: source
tags: [vla, diffusion, temporal-modeling, robotics, learning]
date: 2026-06-10
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W24/tbd-vla-2606-07895/learning.md
source_hash: bc962acd104315db
---

## Summary
TBD-VLA(Temporal Block Diffusion Vision-Language-Action) 학습을 위한 종합 가이드로, [[BlockDiffusion]] 기반 VLA policy의 동작 원리와 구현 포인트를 다룬다. [[TemporalAR]] 구조로 병렬 디노이징과 순차 블록 처리을 결합하여 [[ClosedLoopLatency]]와 temporal coherence를 동시에 달성한다.

## 선수 지식

- Transformer autoregressive decoding과 KV cache
- VLM prompt/tokenizer 구조
- Imitation learning과 action chunking
- [[DiscreteDiffusion]] / masked token denoising
- [[VLAPolicy]], action grounding, [[ClosedLoopLatency]]

## 핵심 용어

| 용어 | 설명 |
|---|---|
| VLA | vision + language + action을 하나의 policy로 연결하는 모델 |
| action tokenization | continuous action feature를 discrete token으로 변환하는 절차 |
| temporal block | action sequence를 시간 축으로 나눈 작은 chunk |
| block diffusion | block 내부 token을 mask하고 병렬 복원하는 diffusion 방식 |
| temporal AR | block k가 이전 block 0..k-1에 조건화되는 autoregression |
| RTC | Real-Time Chunking; 실행 중인 action chunk 이후 미래 chunk를 갱신하는 방식 |

## 단계별 이해

1. action trajectory를 timestep-level token으로 바꾼다.
2. 전체 sequence를 block으로 나눈다.
3. 각 block 내부 일부 token을 mask한다.
4. VLM은 이전 block과 현재 corrupted block을 보고 clean token distribution을 예측한다.
5. inference에서는 block 내부를 병렬 denoise하고 다음 block으로 넘어간다.
6. control loop에서는 필요한 action prefix만 실행하고 나머지는 계속 갱신한다.

## 핵심 수식 직관

```text
p(a_1:H | o,g) = Π_k pθ(block_k | o,g, block_<k)
```

이 수식은 "block 내부는 병렬, block 사이 관계는 순차"라는 논문의 핵심을 담는다. [[TemporalAR]]의 조건부 분해로 각 블록이 이전 블록들에 의해 결정되고, 각 블록 내부는 병렬로 복원된다.

## 구현 메모

- action dimension이 커질수록 token length가 길어지므로 block size `m`이 latency와 quality의 주요 hyperparameter가 된다.
- `m=1`은 temporal modeling은 강하지만 느리다.
- `m=H`는 빠르지만 temporal dependency가 약하다.
- expectation sampling이 argmax보다 performance가 좋다고 보고된다.
- prefix KV cache는 control loop에서 반복 prompt/context 계산을 줄이는 데 중요하다.

## Study Questions

### 1. 왜 continuous action expert 대신 discrete token을 쓰는가?
VLM이 action generation에 직접 관여하므로 language/vision representation과 action grounding 사이를 더 직접적으로 분석할 수 있다.

### 2. 왜 pure parallel decoding만으로 충분하지 않은가?
action trajectory에는 시간 의존성이 있으므로 모든 token을 독립적으로 병렬 생성하면 coherence가 깨질 수 있다.

### 3. TBD-VLA가 자율주행에 주는 힌트는?
waypoint/trajectory token을 block diffusion으로 생성하면 closed-loop latency와 temporal consistency를 함께 다룰 수 있다. [[ReflectDrive-2]]의 trajectory planning과 유사한 접근.

## Reading Roadmap

- **1차**: Abstract, Figure 1, Method 4.1~4.3
- **2차**: Table 1, Table 5, Table 6 latency/ablation
- **3차**: LIBERO/SimplerEnv/real-world 결과 비교
- **4차**: [[DiscreteDiffusionVLA]], [[FastDVLA]], [[ReflectDrive-2]]와 비교

## Connections

- [[TBDVLA]] — 메인 소스 페이지
- [[TBDVLAAnalysis]] — 분석 페이지
- [[DiscreteDiffusionVLA]] — discrete VLA 관련 연구
- [[FastDVLA]] — 저지연 VLA 관련 연구
- [[ReflectDrive-2]] — 자율주행을 위한 discrete diffusion 연구
- [[BlockDiffusion]] — 블록 단위 디노이징 기법
- [[TemporalAR]] — 시간적 자기회귀 구조
- [[RTC]] — Real-Time Chunking 메커니즘

## Contradictions

- 없음
