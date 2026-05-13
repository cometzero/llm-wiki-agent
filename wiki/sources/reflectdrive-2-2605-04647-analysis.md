---
title: "ReflectDrive-2: 이산 Diffusion Driving을 위한 강화학습 정렬 Self-Editing — analysis"
type: source
tags: [autonomous-driving, VLA, diffusion, reinforcement-learning, trajectory-planning]
date: 2026-05-13
sources: []
last_updated: 2026-05-13
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W19/reflectdrive-2-2605-04647/analysis.md
source_hash: 0a68ff1154fbeffe
---

## Summary
ReflectDrive-2는 자율주행 VLA planner에서 trajectory를 discrete token으로 표현하고, masked diffusion draft와 AutoEdit rewrite를 RL terminal reward로 함께 정렬해 "고칠 수 있는 계획"을 실시간에 가깝게 생성하는 Decision-Draft-Reflect 아키텍처를 제안한다. NAVSIM benchmark에서 camera-only 설정으로 91.0 PDMS, best-of-6으로 94.8 PDMS를 달성하며, NVIDIA Thor에서 ~30ms latency를 보인다.

## Key Claims
- 기존 end-to-end planner는 trajectory를 한 번 생성한 뒤 구조적으로 수정하기 어렵고, autoregressive VLA planner는 correction latency가 크다
- 자율주행 error는 longitudinal/lateral 축으로 구조화되어 나타나므로, token-space in-place editing이 가능한 planner가 필요하다
- Goal posterior + masked discrete diffusion + AutoEdit로 구성된 decision–draft–reflect pipeline이 효과적이다
- Longitudinal/lateral perturbation을 이용한 structure-aware AutoEdit supervision이 safety-critical correction에 중요하다
- Draft/edit composed rollout 전체에 closed-loop reward를 주는 RL fine-tuning이 핵심이다
- Shared-prefix KV reuse, ASD, fused CUDA unmasking으로 deployment latency 최적화가 가능하다

## Architecture / Pipeline

| 단계 | 내용 | Action grounding 의미 |
|---|---|---|
| Input | 3-view camera × 2 frames, route instruction, ego state | scene + intent + kinematics |
| Decision | goal-point posterior | behavior hypothesis 선택 |
| Draft | masked discrete diffusion over BEV trajectory tokens | full 4s trajectory 생성 |
| Reflect | AutoEdit token-to-token rewrite | drivable/safe/reward-aligned correction |
| Output | waypoint trajectory | executable driving plan |

## Training Recipe
1. Supervised masked trajectory generation
2. AutoEdit supervised recovery from structured perturbations
3. Drivable-area field regularization
4. RL fine-tuning with closed-loop PDMS reward over full draft-and-edit rollout

## Benchmark / Metric
- **Benchmark**: NAVSIM / nuPlan 기반 closed-loop planning
- **Input**: camera-only setting 중심
- **Metric**: PDMS = collision, drivable area, TTC, comfort, ego progress aggregation
- **Output horizon**: 4초, 2Hz waypoint trajectory

## Strengths
- 자율주행 failure mode에 맞는 editable action representation
- VLA에서 language token을 route intent conditioning으로 명확히 사용
- model-side idea와 serving-side latency 최적화를 함께 제시
- AutoEdit gain이 RL 후 커지는 ablation이 설득력 있음

## Limitations / Safety / Latency
- proprietary pretrained weights를 사용해 재현성 제한 가능
- fixed coordinate binning으로 trajectory precision 제한
- reward가 PDMS proxy라 real-world safety까지 보장하지 않음
- multi-agent negotiation failure(yield timing, cut-in response)는 추가 perturbation/reward 필요
- NVIDIA Thor latency는 특정 hardware/kernel 최적화 의존

## Connections
- [[VLA]] — Vision Language Action 모델링 프레임워크
- [[NAVSIM]] — benchmark evaluation environment
- [[NVIDIAThor]] — deployment hardware target
- [[DiscreteDiffusion]] — trajectory generation methodology
- [[AutoEdit]] — self-correcting rewriting mechanism
- [[ClosedLoopReward]] — RL alignment approach
- [[BEVTrajectory]] — output representation

## Contradictions
- 없음 (신규 분석 문서)
