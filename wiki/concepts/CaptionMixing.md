---
title: "Caption Mixing"
type: concept
tags: [caption, representation-learning, training-recipe, vision-language]
last_updated: 2026-09-02
---

[[CaptionMixing]]는 robot action supervision 외의 dense caption 신호를 함께 넣어 [[VisionLanguageModel|VLM]] semantic 축을 유지시키는 학습 기법이다.

VLAct 맥락에서는 action 학습이 VLM prior를 완전히 덮어쓰는 것을 완화하는 보조 손실 역할을 하며, 표현 보존과 일반화 성능의 안정성에 기여한다.

관련 연결: [[VLAct]], [[VisionLanguageModel]], [[RepresentationLearning]], [[DataRecipe]].