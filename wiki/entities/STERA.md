---
title: "STERA"
type: entity
tags: [data-processing, pipeline, VLA, hand-tracking]
sources: [mobileego-anywhere-2605-05945-analysis]
last_updated: 2026-05-20
---

## Overview
MobileEgo Anywhere의 오프라인 처리 파이프라인. 2D hand keypoints(WiLoR)에서 3D world-frame MANO hand trajectory를 생성하고, atomic action labeling 및 hierarchical task instruction tree를 동시에 생성하여 VLA-ready dataset을 출력한다.

## Processing Stages
1. **WiLoR 2D hand keypoints** 추출
2. **Depth unprojection**으로 3D 복원
3. **MANO model** 피팅으로 world-frame 3D hand trajectory 생성
4. **Atomic action labeling** — 개별 동작 세그먼트 태깅
5. **Hierarchical task instruction labeling** — 상위 instruction/sub-goal 트리 구조

## Output
- VLA pretraining용 egocentric trajectory dataset
- hierarchical language labels (instruction following, sub-goal planning용)

## Related
- [[MobileEgoAnywhere]] — 파이프라인 소유 프로젝트
- [[WiLoR]] — 2D hand keypoints 소스
- [[MANO]] — 3D hand model
