---
title: "ODE Policy"
type: "entity"
tags: ["VLA", "robotics", "continuous-control"]
sources: ["ode-policy-2611-01729-paper-ko", "ode-policy-2611-01729-analysis", "ode-policy-2611-01729-learning", "ode-policy-2611-01729-references"]
last_updated: "2026-11-11"
---

# ODE Policy
Jindou Jia 외의 arXiv:2611.01729v1 연구. [[ActionDynamicsPolicy]]로 action interface를 parameterize하고 visuomotor policy, VLA/WAM action head와 model-based RL actor를 비교한다.

## 핵심
- Desired action을 physical time에 적분하며 measured state는 field condition이다.
- Short-path supervision, contractive perturbation, seamless chunking, detached diversity head가 주요 구성이다.
- [[OSWAM]]의 few/one-step generation과 달리 시간 변수와 command parameterization을 바꾼다.

## Evidence Boundary
LIBERO/LIBERO-plus와 14개 실물 robot task를 보고한다. Closed-loop vehicle driving·NPU benchmark·formal safety proof는 없다. 초기 학습 우위와 최종 우위, pretrained FM과 random-init FM 비교를 구분한다.

## Sources
- [[ode-policy-2611-01729-paper-ko]]
- [[ode-policy-2611-01729-analysis]]
- [[ode-policy-2611-01729-learning]]
- [[ode-policy-2611-01729-references]]
