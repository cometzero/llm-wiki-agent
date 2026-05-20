---
title: "Hand Pose Estimation"
type: concept
tags: [hand-tracking, computer-vision, embodied-AI]
sources: [mobileego-anywhere-2605-05945-analysis]
last_updated: 2026-05-20
---

## Definition
이미지/비디오에서 손의 3D 관절 위치 및 자세(pose)를 추정하는 컴퓨터 비전 기술.

## In MobileEgo Anywhere Pipeline
1. **WiLoR 2D hand keypoints** — 2D 이미지에서 손的关键点 검출
2. **Depth unprojection** — 2D keypoints + depth map → 3D 좌표
3. **MANO model fitting** — 3D keypoints를 MANO 손 모델에 피팅
4. **Output**: world-frame 3D MANO hand trajectories

## Evaluation Metrics
| Metric | Value |
|---|---|
| Detection success | 86.2% |
| Mean confidence | 0.73 |
| Bone CV (left hand median) | 1.27% |
| Bone CV (right hand median) | 1.43% |
| Joint plausibility | >99.99% biomechanical bounds 내 |

## Related Concepts
- [[MANO]] — 3D 손 모델
- [[WiLoR]] — 2D keypoint detector
- [[StereoDepthEstimation]] — depth 기반 3D 복원
- [[ActionGrounding]] — 추정된 pose의 robot action 변환
