---
title: "RL Post-training"
type: concept
tags: [reinforcement-learning, VLA, fine-tuning]
sources: [policytrim-2606-22540-analysis]
last_updated: 2026-06-24
---

RL Post-training은 pretrained [[VLA]] 모델을 강화학습으로 추가 fine-tuning하여 특정 목표(성능, 효율성 등)를 최적화하는 방법론이다. PolicyTrim은 VLA의 [[PolicyEfficiency]]를 향상시키기 위해 RL post-training을 활용한다.

## PolicyTrim의 2-stage RL Curriculum

### Stage 1: Reliable Horizon Extension
- Chunk horizon을 점진적으로 늘려가며 성공적인 rollout을 reward
- 긴 action chunk도 안정적으로 실행 가능한 policy로 성장

### Stage 2: Redundancy-Aware Step Reduction
- Task success rate를 유지하면서 physical steps 감소
- 불필요한/redundant action을 penalty로 억제

## 특징
- 추가 demonstration 불필요: pretrained policy + benchmark rollout만으로 학습 가능
- Cross-architecture 적용 가능: [[π0.5]], [[OpenVLA-OFT]], [[GR00T]] 등 검증
- Offline action prediction이 아닌 closed-loop deployment 시나리오 최적화

## 연결
- [[VLA]] — 대상 모델
- [[PolicyTrim]] — 구체적 적용 사례
- [[PolicyEfficiency]] — 최적화 목표
- [[ActionChunk]] — 최적화 대상
- [[RobotManipulation]] — 적용 도메인
