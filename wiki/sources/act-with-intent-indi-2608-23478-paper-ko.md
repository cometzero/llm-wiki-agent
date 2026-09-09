---
title: "Act with Intent (INDI) 한국어 기술 번역"
type: source
tags: [vision-language-action, robotics, intent-distillation, action-grounding]
date: 2026-09-09
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W36/act-with-intent-indi-2608-23478/paper-ko.md
source_hash: 93adb93c2ddd23fa
---

## Summary
INDI는 frozen teacher VLM이 executed behavior의 video와 instruction에서 만든 behavior-level intent를 student VLA decoder의 intermediate latent에 증류한다. Student는 deployment input만으로 intent를 recover하고 continuous action, visual outcome, textual purpose grounding을 함께 예측한다.

## Key Claims
- Behavior cloning은 action realization을 지도하지만 behavior objective와 progress는 암묵적일 수 있다.
- Teacher/target generator는 training-only이며 deployment runtime graph에서 제거된다.
- SimplerEnv-Bridge, RoboCasa, real-robot success와 intent intervention을 보고한다.

## Connections
- VLM teacher supervision을 continuous action decoder의 latent interface로 연결한다.

## Contradictions
- Teacher intent가 human/true task intent이거나 safety constraint를 자동 보장하지는 않는다.
