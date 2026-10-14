---
title: "Precise Grounding Transfer"
type: concept
tags: [perception, action-grounding, vla, representation-transfer]
sources: [groundingpi-2609-39601]
last_updated: 2026-10-14
---

# Precise Grounding Transfer

[[GroundingPI]]가 탐색하는 perception-native foundation 접근이다. Language query를 spatial target(point/box)에 정밀히 연결하는 representation을 먼저 학습하고, downstream action learner가 그 feature를 활용하도록 adapt한다. 희소 action demonstration이 perception과 control을 동시에 가르쳐야 하는 부담을 줄일 수 있다는 동기다.

## 두 Action Interface

1. Driving: [[AutonomousDrivingVLA]]의 numerical-action path. 기존 atomic coordinate vocabulary를 metric range에 대응시켜 six cumulative waypoint를 생성한다.
2. Manipulation: [[VisionLanguageModel]]의 hidden feature를 normalized depth·shared projector·resampler로 고정 condition budget에 전달하고 [[FlowMatching]] Action DiT가 continuous control chunk를 만든다.

Base grounding output과 executable controller는 다른 layer다. Image coordinate, ego-frame metric position, embodiment-specific actuator control을 혼동하지 않는다.

## 근거와 경계

- Dense grounding group 제거는 driving/manipulation transfer를 악화시킨다. OCR/Layout/GUI auxiliary group은 다른 grounding group과 상보적으로 작동한다.
- Pretraining exposure와 OOD gain의 동반 증가가 모든 ID metric의 monotonic law나 OCR-only causality를 입증하지 않는다.
- Precision capability·serialized token efficiency는 closed-loop safety·observation-to-action deadline와 다르다. Metric calibration, dynamics/contact, feedback control은 downstream 과제다.
- [[PerturBot]]의 evidence-valid supervision과 [[MotorMind]]의 measured-feedback harness는 각각 training/runtime에서 같은 grounding 문제를 다른 방식으로 다룬다.

## 학습 자료

[[groundingpi-2609-39601-analysis]], [[groundingpi-2609-39601-learning]], [[groundingpi-2609-39601-paper-ko]].
