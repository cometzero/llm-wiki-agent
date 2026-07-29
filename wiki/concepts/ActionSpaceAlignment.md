---
title: "ActionSpaceAlignment"
type: concept
tags: [robotics, alignment, vision-language-action, embodiment]
sources: ["data-pyramid-for-embodied-manipulation-2607-24744", "data-pyramid-for-embodied-manipulation"]
last_updated: 2026-07-29
---

## Definition

**ActionSpaceAlignment**은 언어/비전 표현에서 계산된 제어 신호가 각 robot embodiment의 실제 action space와 일치하도록 정렬되는 정도를 뜻한다. 동일한 정책이 다른 로봇 morphology에 적용될 때 action 파라미터화, 제약 조건, 타이밍 스케일이 맞아야 한다.

## Why it matters

- [[VisionLanguageAction]] 시스템은 semantic 정확도만으로는 충분하지 않다.
- [[RealRobotData]]를 확장해도 embodiment 간 actuator/pose 제약이 어긋나면 폐루프 성능은 크게 하락할 수 있다.
- [[DataPyramidForEmbodiedManipulation]]의 핵심 난제 중 하나로, cross-embodiment 전이 시 정책 성능 보존에 직접 영향한다.

## Relations

- Related to [[GeometricAlignment]]
- Enables robust [[CrossEmbodimentLearning]]
- A prerequisite for safe [[ClosedLoop]] deployment

## Open issues

- action-space mismatch로 인한 데이터 레시피 오류
- reward가 task-level은 좋아도 실행-level에서 실패율이 급증하는 현상
- failure/recovery trajectory를 통한 보정 필요
