---
title: "PolicyTrim: VLA의 intrinsic policy efficiency를 높이는 RL post-training"
type: source
tags: [VLA, RL-post-training, robotics, efficiency]
date: 2026-06-24
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W26/policytrim-2606-22540/paper-ko.md
source_hash: a619256bbe0d6f95
---

## Summary
PolicyTrim은 Vision-Language-Action(VLA) 모델의 intrinsic policy efficiency를 강화학습 기반 post-training으로 향상시키는 framework다. 두 단계(신뢰할 수 있는 action chunk 확장 + 중복 단계 감축)로 구성되며, 성공률을 유지하면서 end-to-end deployment 속도를 최대 5.83배 향상시킨다.

## Key Claims
- VLA deployment 병목은 compute-centric efficiency가 아닌 intrinsic policy efficiency 문제
- Action chunk의 신뢰할 수 있는 실행 길이(reliable executable length)와 총 물리 단계(total physical steps)가 전체 inference 호출 수를 결정
- 현재 VLA policy는 planning unreliability와 action redundancy에 취약
- PolicyTrim은 architecture 변경 없이도 여러 VLA backbone에 적용 가능

## Key Quotes
> "Intrinsic policy efficiency: 같은 success rate를 유지하면서 더 긴 action chunk를 믿고 실행하고, 더 적은 physical step으로 task를 완료함"

> "PolicyTrim은 success rate와 함께 실행 호출 수 / physical step 수 / reliable horizon을 직접 최적화"

## Method Overview

### Stage 1: Reliable Action Chunk Extension
- Dynamic exploration strategy로 더 긴 executable length를 성공적으로 완료하도록 reward 부여
- Empirical limit까지 trustworthy prediction horizon을 점진적으로 확장
- 실패하지 않는 긴 action chunk 실행 경로를 발견하면 보상

### Stage 2: Redundancy-Aware Step Reduction
- Task success를 유지하면서 전체 physical step을 줄이는 reward 설계
- 재현 불가능한 shortcut은 penalize
- "무작정 빠르게"가 아닌 "성공 가능한 최소한의 불필요 동작 제거"

## Key Results
| Metric | Result |
|--------|--------|
| Action chunk utilization | ~3배 개선 |
| Physical execution steps | 51.4% 감소 |
| End-to-end speedup | 최대 5.83배 |
| Success rate | 유지 |

## Benchmarks & Models
- **Benchmarks**: LIBERO, ManiSkill, Meta-World
- **VLA Models**: [[π0.5]], [[OpenVLA-OFT]], [[GR00T]]

## Connections
- [[VLA]] — PolicyTrim이 최적화하는 모델 paradigm
- [[π0.5]] — 실험 대상 VLA backbone
- [[GR00T]] — 실험 대상 VLA backbone
- [[OpenVLA-OFT]] — 실험 대상 VLA backbone
- [[RLPostTraining]] — PolicyTrim의 학습 방법론
- [[ActionChunk]] — PolicyTrim이 최적화하는 핵심 개념
- [[IntrinsicPolicyEfficiency]] — PolicyTrim이 정의하는 새로운 효율성 지표

## Contradictions
- 없음 — 이전 wiki에 PolicyTrim 관련 내용 없음
