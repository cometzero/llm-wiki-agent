---
title: "Structured Action Initialization"
type: concept
tags: [WAM, action-generation, flow-matching, distillation]
sources: [oswam-2610-35850-paper-ko, oswam-2610-35850-analysis, oswam-2610-35850-learning]
last_updated: 2026-11-04
---

# Structured Action Initialization

Action diffusion/[[FlowMatching]]을 unstructured Gaussian noise 대신 observation-conditioned numerical action prior에서 시작하여 적은 refinement step으로 coherent action을 생성하는 방법이다. [[OSWAM]]은 이 원리를 AIT/SIT와 privileged feature distillation로 구체화한다.

## OSWAM에서의 계약

1. Video DiT의 AIT auxiliary decoder가 velocity를 예측해 prior `a_bar = epsilon - v_A`를 만든다.
2. Prior를 detach하고 같은 epsilon으로 `a_init = (1-sigma) * a_bar + sigma * epsilon`을 만든다.
3. Action DiT는 target `(a_init - a_gt) / sigma`를 학습한다.
4. One-step output은 `a_hat = a_init - sigma * v_act`다. Default sigma는 0.5다.

Prior는 auxiliary action loss와 frozen full-future teacher의 multi-depth feature supervision으로 학습된다. SIT는 current-scene context slot이고 AIT와의 attention path로 간접 감독된다. Student는 future frame을 attend하지 않고 teacher는 deployment에서 제거된다.

## 의미와 경계

단순 sampler step 감소나 training-free shortcut이 아니다. One-step은 Action DiT denoising 횟수이며 Video DiT/VAE 비용은 남는다. Scalar algebra가 맞아도 learned velocity의 OOD error와 action feasibility는 보장되지 않는다. Stop-gradient/noise sharing, teacher future-access boundary, coordinate/time/latency contract를 검증해야 한다.

## 연결

- [[oswam-2610-35850-learning]] — residual target과 RoPE timeline의 두 실행 예제
- [[oswam-2610-35850-analysis]] — NAVSIM/RoboTwin trade-off 및 safety 해석
- [[WorldActionModel]] — video-generative prior와 policy learning
- [[SimWAM]] — online future rollout을 제거한 직접 선행
