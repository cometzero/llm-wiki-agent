---
title: "Object-Centric Residual RL for Zero-Shot Sim-to-Real VLA Enhancement — references"
type: source
tags: [VLA, residual-RL, sim-to-real, robotics, references]
date: 2026-07-01
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W27/object-centric-residual-rl-2606-18953/references.md
source_hash: 40eab246d59de3c0
---

## Summary
이 문서는 arxiv 2606.18953 논문의 참고 레퍼런스를 정리한 것으로, [[VLA]] backbone, [[ResidualRL]], sim-to-real transfer, pose/segmentation 기반 deployment 관련 핵심论文들을 Semantic Scholar와 본문에서 확인하여 정리한다.

## Key References

### VLA & Foundation Models
- **[[Pi06]]** (2025) — Physical Intelligence, A. Amin et al. RL with Experience and Corrections via Advantage-conditioned Policies (RECAP) 제시, heterogeneous data를 self-improvement에 통합하는 [[VLA]] 백본
- **[[π0.5]]** (2025) — Physical Intelligence, Kevin Black et al. [[Pi0]] 기반 co-training으로 open-world generalization 달성하는 [[VLA]] 모델
- **[[Pi0]]** (2024) — Kevin Black et al. Vision-Language-Action flow model for general robot control; [[VLA]] 연구의 foundational work
- **[[GR00T-N1]]** (2025) — Nvidia, Johan Bjorck et al. Humanoid robot를 위한 open foundation model; versatile body + intelligent mind 통합

### Residual RL & Policy Refinement
- **Self-Improving VLA with PLD** (2025) — Wenli Xiao et al. Probe, Learn, Distill (PLD) 3단계 framework; residual RL과 distribution-aware data collection으로 [[VLA]] 개선
- **[[Residual-Off-Policy-RL]]** (2025) — Lars Ankile et al. Behavior Cloning policy fine-tuning을 위한 residual off-policy RL 연구
- **[[Residual-RL-Precise-Assembly]]** (2024) — Lars Ankile et al. Imitation에서 refinement로의 전환, precision assembly를 위한 residual RL; distribution shift와 closed-loop corrective control 문제 해결
- **[[Refined-Policy-Distillation]]** (2025) — T. Jülg et al. VLA generalist에서 RL expert로의 bridge; refined policy distillation method 제시

### Spatial & Perception
- **[[SpatialVLA]]** (2025) — Delin Qu et al. 3D spatial representation을 위한 visual-language-action model; Ego3D Position Encoding과 Adaptive Action Grids 도입
- **[[SAM2]]** (2024) — Nikhila Ravi et al. Images and videos용 Segment Anything Model 2; promptable visual segmentation을 위한 foundation model

## Key Claims
- [[VLA]] backbone과 [[ResidualRL]]의 조합이 sim-to-real transfer의 핵심임을 강조
- Pose/segmentation 기반 deployment를 위해 [[SAM2]]와 같은 perception stack 필요
- VLA family([[Pi0]]/[[π0.5]]/[[Pi06]]/[[GR00T-N1]]) 이해가 선행되어야 residual RL 적용 가능

## Reading Roadmap
1. **Base VLA Family**: OpenVLA / [[Pi0]] / [[π0.5]] / [[GR00T-N1]] — VLA 아키텍처와 학습 패러다임 이해
2. **Residual RL**: [[Residual-Off-Policy-RL]] / [[Residual-RL-Precise-Assembly]] / PLD — imitation policy refinement 방식 이해
3. **Perception Stack**: [[SAM2]] / FoundationPose — object-centric observation을 현실에서 얻는 방법 이해

## Connections
- [[VLA]] — 논문의 메인 태스크
- [[ResidualRL]] — 핵심 방법론
- [[Sim-to-Real-Transfer]] — 적용 대상 도메인
- [[PhysicalIntelligence]] — [[Pi0]]/[[π0.5]]/[[Pi06]] 개발 기관
- [[Nvidia]] — [[GR00T-N1]] 개발 기관
- [[SAM2]] — Object segmentation을 위한 perception foundation model

## Contradictions
- 없음
