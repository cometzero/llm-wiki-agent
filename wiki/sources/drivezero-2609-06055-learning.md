---
title: "DriveZero 학습 노트"
type: source
tags: [autonomous-driving, learning-guide, trajectory-planning]
date: 2026-09-16
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W37/drivezero-end-to-end-driving-2609-06055/learning.md
source_hash: e14dc19abe135f0f
---

## Summary
학습 노트는 DriveZero를 log→mixed-agent simulator→privileged RL teacher→trajectory target→camera planner라는 데이터 흐름으로 설명한다. PPO, jerk/steering-rate action, WTA proposal supervision, PDM score와 deploy-time safety/latency 검증항목을 함께 정리한다.

## Key Claims
- DriveRL의 raw log 사용은 scene/goal initialization이며 사람 action imitation이 아니다.
- WTA trajectory loss는 여러 가능한 future를 평균내는 문제를 완화한다.
- simulator response model, perception gap, critic calibration을 배포 전 점검해야 한다.

## Connections
- [[DriveZero]] — study guide.
- [[ClosedLoopReinforcementLearning]] — prerequisite method.

## Contradictions
- 이 노트는 논문의 학습용 재구성이지 implementation recipe의 완전한 대체물이 아니다.
