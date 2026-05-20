---
title: "DriveFine"
type: entity
tags: [autonomous-driving, diffusion, VLA]
sources: [reflectdrive-2-2605-04647-references]
last_updated: 2026-05-13
---

## Overview
DriveFine (arXiv 2602.14577)은 masked diffusion driving VLA에 refinement를 추가한 연구로, ReflectDrive-2의 가장 가까운 선행 연구이다. drafter/editor 구조를 제안하지만 joint RL coupling이 약하다는 한계가 있다.

## Key Claims
- Refinement-augmented masked diffusion VLA 제시
- Drafter/editor 기반 trajectory generation
- Joint RL coupling이 충분히 강력하지 않은 한계

## Connections
- [[ReflectDrive2]] — inherits refinement architecture, strengthens RL alignment
- [[MaskedDiffusion]] — core diffusion paradigm
- [[VLA]] — model category

## Contradictions
- ReflectDrive-2는 DriveFine의 약한 joint RL coupling을 극복하기 위해 stronger RL-aligned draft-edit rollout을 도입함
