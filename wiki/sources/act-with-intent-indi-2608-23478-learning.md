---
title: "Act with Intent (INDI) 학습 노트: behavior cloning에서 intent distillation으로"
type: source
tags: [vision-language-action, learning, distillation, action-grounding]
date: 2026-09-09
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W36/act-with-intent-indi-2608-23478/learning.md
source_hash: 3faebb32c8a59af6
---

## Summary
이 학습 노트는 behavior cloning, behavior intent, future-based supervision, distillation, latent intervention을 정의하고 teacher–student pipeline 및 loss의 개념적 형태를 설명한다. Training-only evidence와 deployment safety boundary를 명확히 구분한다.

## Key Claims
- Intent target은 future outcome의 특정 realization보다 objective/progress representation을 목표로 한다.
- Teacher target cache의 split hygiene와 teacher-quality ablation이 필수다.
- Latent intervention은 representation usefulness를 inspect하는 구현 방법이다.

## Connections
- Latent action grounding과 privileged-information distillation의 실무적 점검표다.

## Contradictions
- Teacher가 future evidence를 본다는 사실만으로 student의 robust generalization이 성립하지는 않는다.
