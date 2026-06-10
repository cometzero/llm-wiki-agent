---
title: "TBD-VLA: 시간 블록 Diffusion 기반 Vision-Language-Action 모델 — references"
type: source
tags: [vla, vision-language-action, discrete-diffusion, references]
date: 2026-06-10
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W24/tbd-vla-2606-07895/references.md
source_hash: 5af1f7284416f1ac
---

## Summary
TBD-VLA 관련 참고 문헌 정리. Discrete diffusion VLA 계열의 직접적 기술 배경을 포함하며, 읽기 우선순위에 따라 구성됨.

## Key References

### 1. Fast-dVLA ([arXiv:2603.25661](https://arxiv.org/abs/2603.25661))
- 가장 가까운 speed-oriented discrete diffusion VLA 계열
- TBD-VLA는 단순 speedup을 넘어 [[TemporalBlock]] 구조를 명시화

### 2. Discrete Diffusion VLA ([arXiv:2511.01718](https://arxiv.org/abs/2511.01718))
- [[ActionDecoding]]을 discrete diffusion으로 바꾼 직접 선행연구
- TBD-VLA는 여기에 block-level [[TemporalAutoregression]] 추가

### 3. Qwen3-VL ([arXiv:2511.21631](https://arxiv.org/abs/2511.21631))
- TBD-VLA의 [[VLM]] backbone
- Action token decoding 능력은 이 backbone의 multimodal representation에 의존

### 4. LIBERO-Plus ([arXiv:2510.13626](https://arxiv.org/abs/2510.13626))
- TBD-VLA robustness 평가에 사용되는 perturbation benchmark
- [[SimplerEnv]]과 함께 sim-to-real 평가 기반

### 5. InternVLA-M1 ([arXiv:2510.13778](https://arxiv.org/abs/2510.13778))
- Spatial grounding을 VLA action으로 연결하는 관련 연구
- TBD-VLA의 [[TemporalActionGrounding]]과 보완적 관계

### 6. VLA-0 ([arXiv:2510.13054](https://arxiv.org/abs/2510.13054))
- [[VLM]] 자체를 거의 수정하지 않고 VLA policy로 쓰려는 흐름
- TBD-VLA도 VLM-native [[ActionDecoding]] 지향

### 7. LLaDA-VLA ([arXiv:2509.06932](https://arxiv.org/abs/2509.06932))
- [[LanguageDiffusionModel]]을 VLA action generation에 적용하는 계열

### 8. OpenVLA ([OpenVLA](https://github.com/openvla/openvla))
- 대표적인 [[Autoregressive]] discrete VLA baseline
- TBD-VLA는 token generation의 [[Latency]] 한계를 겨냥

### 9. π0.5
- [[ContinuousAction]] expert 기반 강력 baseline
- TBD-VLA의 real-world 비교 대상

### 10. FAST
- [[ActionToken]] 수 자체를 줄이는 approach
- TBD-VLA는 token compression 대신 [[BlockDiffusionDecoding]] 선택

## 읽기 우선순위

| 우선순위 | 레퍼런스 | 이유 |
|---------|---------|------|
| 1 | [[Fast-dVLA]], [[DiscreteDiffusionVLA]] | TBD-VLA 직접 기술 배경 |
| 2 | [[Qwen3-VL]] | VLM backbone과 multimodal representation 이해 |
| 3 | [[OpenVLA]], [[VLA-0]], [[π0.5]] | discrete-token VLA vs continuous-action-expert VLA 대비 |
| 4 | [[LIBERO-Plus]], [[SimplerEnv]] | robustness와 sim-to-real 평가 방식 |

## Connections
- [[TBD-VLA]] — 메인 소스; 이 레퍼런스 페이지는 관련 연구 정리
- [[DiscreteDiffusion]] — VLA action decoding 핵심 기법
- [[VLA]] — Vision-Language-Action 모델링 패러다임
- [[Qwen]] — VLA backbone으로 활용
- [[OpenVLA]] — baseline comparison 대상

## Contradictions
- 없음
