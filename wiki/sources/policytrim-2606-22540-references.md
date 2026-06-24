---
title: "PolicyTrim: VLA의 intrinsic policy efficiency를 높이는 RL post-training — references"
type: source
tags: [references, VLA, RL, post-training, policy-efficiency]
date: 2026-06-24
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W26/policytrim-2606-22540/references.md
source_hash: 4be92111121b302d
---

## Summary
PolicyTrim 논문(arxiv 2606.22540)의 참고 레퍼런스를 8개 축으로 정리한 가이드다. [[VLA]] foundation model 계열(π0, OpenVLA, GR00T)과 평가 benchmark(LIBERO, ManiSkill, Meta-World)를 포함하며, [[RLPostTraining]] 기반 deployment-oriented reward 설계와 efficient VLA 연구 맥락을 제공한다.

## Key Claims
- [[VLA]] foundation model은 action chunk reliability와 execution efficiency 측면에서 intrinsic inefficiency를 가질 수 있음
- [[Pi05|π0/π0.5]]/π0.5 계열은 대표적 vision-language-action policy foundation model이며 PolicyTrim의 주요 평가 대상임
- [[OpenVLA]]와 OpenVLA-OFT는 open-source VLA policy 계열로 PolicyTrim의 cross-architecture 적용 가능성을 뒷받침함
- [[GR00T]]류 generalist robot policy도 foundation-scale에서 intrinsic policy inefficiency를 보일 수 있음

## Key Quotes
> "PolicyTrim은 RL을 task success만이 아니라 reliable horizon과 redundancy reduction에 맞춘다. 이는 sparse success reward를 넘어서 deployment-oriented reward를 설계하는 사례다."

> "PolicyTrim은 per-step 속도가 같아도 policy가 더 긴 chunk를 안정적으로 실행하고 step 수를 줄이면 전체 deployment가 빨라질 수 있음을 보여준다."

## References by Category

### 1. π0 / π0.5 계열 VLA policy
[[VLA]] vision-language-action policy의 대표적 foundation model 계열. PolicyTrim은 π0.5를 포함한 VLA backbone에서 action chunk reliability와 execution efficiency를 평가한다.

### 2. OpenVLA / OpenVLA-OFT
Open-source VLA policy 계열로, fine-tuning/robot action adaptation 맥락에서 자주 비교된다. PolicyTrim의 cross-architecture 결과는 특정 closed model이 아니라 open VLA에도 적용 가능함을 보여준다.

### 3. GR00T / generalist robot policy
다양한 embodiment/task로 일반화를 목표로 하는 generalist robot policy 계열. PolicyTrim은 이런 foundation-scale policy도 intrinsic policy inefficiency를 가질 수 있음을 보여준다.

### 4. LIBERO Benchmark
Language-conditioned robotic manipulation benchmark로, long-horizon/generalization setting에서 [[VLA]] policy를 평가하는 데 널리 쓰인다. PolicyTrim은 success rate뿐 아니라 step 수와 chunk horizon을 함께 보고한다.

### 5. ManiSkill
Simulation manipulation benchmark로 다양한 robot task를 제공한다. PolicyTrim은 LIBERO 외부 benchmark에서도 speedup과 SR 유지 여부를 검증한다.

### 6. Meta-World
Multi-task robot manipulation benchmark다. PolicyTrim이 여러 benchmark에서 동작한다는 주장을 뒷받침한다.

### 7. Reinforcement Learning for post-training
PolicyTrim은 [[ReinforcementLearning|RL]]을 task success만이 아니라 reliable horizon과 redundancy reduction에 맞춘다. 이는 sparse success reward를 넘어서 deployment-oriented reward를 설계하는 사례다.

### 8. Efficient VLA / Token pruning / Quantization 연구
기존 효율화는 per-step compute를 줄이는 방향이 많다. PolicyTrim은 per-step 속도가 같아도 policy가 더 긴 [[ActionChunk]]를 안정적으로 실행하고 step 수를 줄이면 전체 deployment가 빨라질 수 있음을 보여준다.

## Reading Order Suggestion
1. [[VLA]] action chunk 개념 이해
2. LIBERO/ManiSkill/Meta-World metric 확인
3. PolicyTrim Figure 1로 inefficiency 현상 파악
4. Figure 2와 Method로 두 단계 RL objective 학습
5. Table 1–5로 SR/steps/speedup trade-off 확인

## Connections
- [[PolicyTrim]] — 메인 논문의 references
- [[VLA]] — 핵심 기술領域
- [[Pi05|π0/π0.5]] — 평가 대상 VLA backbone
- [[OpenVLA]] — 비교 모델
- [[GR00T]] — 비교 모델
- [[LIBERO]] — benchmark
- [[ManiSkill]] — benchmark
- [[Meta-World]] — benchmark
- [[RLPostTraining]] — 핵심 방법론
- [[ActionChunk]] — 핵심 개념

## Contradictions
- 없음 (references 페이지는 기존 wiki 내용과 충돌 없음)
