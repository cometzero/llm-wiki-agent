---
title: "A Peek into Tesla’s Autonomous Future: Core Tech Revealed by VP Ashok Elluswamy at ICCV25 WDFM-AD"
type: source
tags: [Tesla, EndToEnd, AutonomousVehicle, Robotics, Simulation, GaussianModeling, Cybercab, Optimus, VLA]
date: 2026-05-10
sources:
  - a-peek-into-tesla-s-autonomous-future-core-tech-revealed-by-vp-ashok-elluswamy-at-iccv25-wdfm-ad
last_updated: 2026-05-10
source_file: raw/Robotics/LilysAI/a-peek-into-tesla-s-autonomous-future-core-tech-revealed-by-vp-ashok-elluswamy-at-iccv25-wdfm-ad.md
source_hash: 1512b30027316d75
---

## Summary
This source explains Tesla’s move to a single large-scale [[EndToEndAutonomy]] model for self-driving, presented by [[AshokElluswamy]] at [[ICCV25 WDFM-AD]].
The core thesis is that explicit modular stacks (perception → prediction → planning → control) lose critical behavioral context, while a unified model better captures long-horizon intent from raw multi-camera data.
The source argues this architecture enables smoother and safer planning in edge cases, plus a broader path toward robotics applications such as [[Cybercab]] and [[Optimus]].

## Key Claims
- [[Tesla]] has shifted production-oriented autonomy toward a single large-scale [[NeuralNetwork]] that maps raw camera/video input directly to control outputs.
- The shift aims to resolve limitations of modular stacks where explicit interface boundaries hide uncertainty and can drop information needed for safety-critical decisions.
- Tesla frames this as better aligned with real human preference encoding: explicit reward or rule design for all driving scenarios is difficult for rules-based stacks.
- The [[EndToEndAutonomy]] stack supports smooth behavior in dynamic scenes (예: 물웅덩이 우회 시 반대 차선 진입, 보행자/동물 대기/후진 회피).
- Tesla cites large-scale data as foundational; vehicles generate multiple high-resolution camera streams and long-horizon context can be reduced to control tokens (steer/throttle)
  from enormous state representations.
- Rare-event and extreme cases are addressed by massive data collection from the fleet, not only synthetic edge-case curation.
- The model can predict future hazards and take preemptive action before a crash trajectory completes, not only react at the moment of failure.
- Debugging is argued to be practical via multi-task probing: the same model can be queried for occupancy, traffic state, signs, lane boundaries, and explanatory signals.
- [[GaussianModeling]]-style 3D scene reconstruction is used to improve observability for verification and inspection during model analysis.
- Closed-loop robustness is emphasized by a simulator built from state-action inversion: given past states and actions, the simulator can synthesize future states.
- The simulator supports evaluating past failures, generating corner-case variants, and running reinforcement-style iterative testing.
- Tesla extends this technical direction to robots: the same core learning stack is presented as adaptable to a broader robot platform, including autonomous fleets and [[Optimus]].

## Key Quotes
> "모듈식 파이프라인은 인터페이스에서 정보가 손실될 수 있다; 단일 네트워크는 장면을 통합적으로 보고 판단한다."

> "규칙 기반으로 사람의 선호를 정확히 코딩하는 것은 너무 어렵다. 위험한 상황에서 언제 얼마나 브레이크를 밟을지 같은 판단은 분포적이다."

> "우리는 단순히 사고가 나기 전에 멈추는 것이 아니라, 사고가 날 가능성이 높은 순간을 사전에 이해하고 대응하려고 한다."

## Connections
- [[AshokElluswamy]] — source speaker and Tesla autonomy executive describing the architecture.
- [[Tesla]] — organization implementing fleet-scale autonomy and data loop.
- [[EndToEndAutonomy]] — central model architecture pattern described.
- [[AutonomousVehicle]] — target application domain for the stack.
- [[NeuralNetwork]] — model family used for end-to-end action output.
- [[ComputerVision]] — camera stream perception input for control inference.
- [[Cybercab]] — Tesla’s autonomous mobility rollout framing tied to the same core stack.
- [[Optimus]] — robotics extension case built from shared autonomy core ideas.
- [[Simulation]] — core evaluation and scenario generation mechanism.
- [[GaussianModeling]] — visualization/debugging technique for scene reconstruction.
- [[Safety]] — intended outcome from predictive and preemptive control behavior.
- [[Robotics]] — broader extension target beyond driving.

## Contradictions
- The source does not present direct factual contradictions to prior sources, but it contrasts with traditional modular AV pipelines and argues they create hidden information bottlenecks. Existing sources that emphasize decomposition remain valid for some engineering contexts, but this source elevates a data-and-model-centric design with broader implicit information flow.
