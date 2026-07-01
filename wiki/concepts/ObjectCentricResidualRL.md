---
title: "Object-Centric Residual RL"
type: concept
tags: [robotics, reinforcement-learning, sim-to-real, vla]
sources: ["object-centric-residual-rl-vla-enhancement-2606-18953"]
last_updated: 2026-07-01
---

## Definition
Object-centric residual RL은 frozen [[VLA]] policy 위에 simulation에서 학습한 residual correction policy를 더하는 hybrid architecture이다. Object 6-DoF pose + proprioception + base VLA action을 입력으로 받아 corrective action을 출력하며, zero-shot sim-to-real transfer를 가능하게 한다.

## Key Properties
- **Input**: object pose, proprioception, base VLA action
- **Output**: corrective residual action
- **Training**: simulation-only TD3 with pose noise/dropout
- **Deployment**: zero-shot, no real robot fine-tuning
- **Results**: 42% → 76% success rate (+34%)

## Architecture
```
Base VLA: RGB + Language → action chunk
Residual: [pose + proprio + base_action] → corrective action
Final: base_action + corrective_action → robot command
```

## Connections
- [[VLA]] — base policy
- [[TD3]] — residual policy algorithm
- [[SimToRealTransfer]] — zero-shot deployment mechanism
- [[ResidualRL]] — general methodology
- [[PoseEstimation]] — required for object 6-DoF pose input
- [[FR3]] — robot deployment target
- [[MuJoCo]] — simulation training environment
