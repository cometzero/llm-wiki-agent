---
title: "MotorMind"
type: entity
tags: [robotics, vla, huggingface-weekly]
sources: [motormind-2609-38078-paper-ko, motormind-2609-38078-analysis, motormind-2609-38078-references, motormind-2609-38078-learning]
last_updated: 2026-10-07
---

# MotorMind

범용 frozen VLM의 semantic decision을 parameterized mid-level action과 deterministic Controller에 연결한다. sequential execution에 asynchronous monitoring·background memory·explicit outcome verification을 결합하며 LIBERO-PRO와 xArm6에서 zero-shot 조작을 평가한다.

## Method and Evidence
Frozen generic VLM의 Planner·Executor·Monitor·Verifier·Memory와 deterministic Controller를 구분한다. base-frame translation/rotation/gripper action은 structured proposal이며 measured outcome으로 advance/retry/replan을 결정한다. LIBERO-PRO base/perturbation 및 xArm6 placement를 평가한다.

## Limits
action-boundary stop은 immediate emergency stop이 아니며 local QA·single-seed sensitivity·tabletop SR을 real-road safety로 일반화할 수 없다. 원문 D.1의 task-family count 불일치를 번역에 기록했다.

## Connections
- [[VisionLanguageModel]] — 범용 multimodal reasoning과 action interface.
- [[PerturBot]] — runtime evidence checking 대 training evidence-use 개선.
- [[LatentInterfaceTraining]] — representation/interface 수준의 대안.

## Sources
- [[motormind-2609-38078-paper-ko]] — 한국어 기술 번역
- [[motormind-2609-38078-analysis]] — 방법·평가 분석
- [[motormind-2609-38078-references]] — 핵심 참고문헌
- [[motormind-2609-38078-learning]] — 핵심 기술 학습
