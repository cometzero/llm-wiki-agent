---
title: "LIT 학습 노트"
type: source
tags: [vla, learning-guide, flow-matching, latent-interface]
date: 2026-09-16
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W38/latent-interface-training-2609-12641/learning.md
source_hash: e6846cc9d283e1af
---

## Summary
학습 노트는 image-free action prior, 100-token latent interface, pose reconstruction, flow-matching action chunk를 단계별로 설명한다. counterfactual visual intervention, token-capacity sweep, driving goal representation 전환을 실험 과제로 제안한다.

## Key Claims
- Stage 1과 stage 2가 같은 terminal pose를 각각 action condition과 visual reconstruction target으로 쓴다.
- Inference에서는 pose encoder/decoder가 제거되며 image·language·robot state만 필요하다.
- Action loss와 pose loss, ID/OOD rollout, latency는 분리해 검증해야 한다.

## Connections
- [[LatentInterfaceTraining]] — study guide.
- [[VisionActionShortcut]] — diagnostic concept.

## Contradictions
- Latent bottleneck이 정보량과 generalization을 자동으로 동시에 개선하지는 않는다.
