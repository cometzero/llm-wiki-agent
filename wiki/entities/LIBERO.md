---
title: "LIBERO"
type: entity
tags: [robotics, benchmark, simulation, task-suite, VLA-evaluation]
sources: [tbd-vla-2606-07895-analysis, physbrain-1-0-2605-15298, policytrim-2606-22540, apt-action-expert-pretraining-2606-12366]
last_updated: 2026-06-24
---

## Overview

LIBERO는 language-conditioned robotic manipulation 평가를 위한 benchmark/task suite다. SimplerEnv와 함께 TBD-VLA의 주요 평가 환경으로 사용되었고, PolicyTrim에서는 action chunk utilization, physical steps, success rate를 측정하는 주요 benchmark 중 하나로 쓰인다.

## Variants / Evaluation Role

- **LIBERO / LIBERO-Plus**: multi-task suite와 perturbation을 포함한 robot manipulation 평가 환경.
- **LIBERO-Spatial / Object 등 하위 세트**: spatial reasoning, object manipulation, long-horizon instruction following을 나누어 측정한다.
- **PolicyTrim metric**: success rate, average physical steps, action chunk execution length, end-to-end speedup.

## Related Concepts

- [[SimplerEnv]] — 또 다른 VLA 평가 환경.
- [[BlockDiscreteDiffusion]] — TBD-VLA 기술.
- [[VisionLanguageAction]] — 평가 대상 VLA 모델.
- [[PolicyTrim]] — LIBERO에서 RL post-training 효율성 개선을 검증.
- [[ActionChunk]] — PolicyTrim이 최적화하는 action representation.
