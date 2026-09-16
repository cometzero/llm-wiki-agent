---
title: "Vision–Action Shortcut"
type: concept
tags: [vla, robustness, causal-representation, generalization]
sources: [latent-interface-training-2609-12641-paper-ko, latent-interface-training-2609-12641-analysis]
last_updated: 2026-09-16
---

## Overview
Vision–action shortcut은 VLA/robot policy가 action을 정할 때 goal-relevant spatial relation 대신 training distribution에서 action과 우연히 공존한 background, camera viewpoint, lighting, texture 같은 visual cue를 사용하는 failure mode다. 이 shortcut은 in-distribution success를 유지하면서 visual distribution shift에서 action trajectory를 불안정하게 만들 수 있다.

## Mitigation Patterns
- Image-free action prior로 action generation을 visual correlation에서 먼저 분리한다.
- Goal/pose/waypoint reconstruction을 받는 bottleneck으로 visual signal을 action-relevant geometry에 정렬한다.
- camera, noise, lighting, layout, distractor의 task-preserving intervention에서 ID/OOD trajectory와 success를 함께 검사한다.

## Constraints
Bottleneck이나 attention map만으로 causal grounding을 증명할 수 없다. Counterfactual goal change, real rollout, latency·safety failure analysis가 필요하다.

## Connections
- [[LatentInterfaceTraining]] — terminal-pose-supervised mitigation.
- [[VLA]] — applicable policy family.
