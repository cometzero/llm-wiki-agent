---
title: "PerturBot"
type: entity
tags: [robotics, vla, huggingface-weekly]
sources: [perturbot-2610-04616-paper-ko, perturbot-2610-04616-analysis, perturbot-2610-04616-references, perturbot-2610-04616-learning]
last_updated: 2026-10-07
---

# PerturBot

successful demonstration의 visual·lexical·motor cue가 task evidence를 대체하는 modality shortcut을 다룬다. label-valid V/C/R training data intervention과 null/causal paired action response의 GroundFscore를 결합하며 inference architecture는 유지한다.

## Method and Evidence
Task-preserving wrist perturbation V, behavior-supported caption C, screened/relabelled random/failed segment R로 standard π0.5 flow matching을 학습한다. [[GroundFscore]]는 null-edit stability와 causal-edit responsiveness를 함께 측정한다. General PnP와 RoboTwin 2.0 closed-loop 결과를 offline response 진단과 분리한다.

## Limits
R relabeling은 unrecorded recovery를 생성하지 않는다. GF는 paired expert delta와 valid edits에 의존하는 diagnostic이며 formal safety certificate가 아니다. abstract/full-text metric 명칭 차이를 보존했다.

## Connections
- [[VisionLanguageModel]] — 범용 multimodal reasoning과 action interface.
- [[MotorMind]] — runtime evidence checking 대 training evidence-use 개선.
- [[LatentInterfaceTraining]] — representation/interface 수준의 대안.

## Sources
- [[perturbot-2610-04616-paper-ko]] — 한국어 기술 번역
- [[perturbot-2610-04616-analysis]] — 방법·평가 분석
- [[perturbot-2610-04616-references]] — 핵심 참고문헌
- [[perturbot-2610-04616-learning]] — 핵심 기술 학습
