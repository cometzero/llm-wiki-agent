---
title: "OSWAM"
type: entity
tags: [autonomous-driving, WAM, robotics, one-step]
sources: [oswam-2610-35850-paper-ko, oswam-2610-35850-analysis, oswam-2610-35850-references, oswam-2610-35850-learning]
last_updated: 2026-11-04
---

# OSWAM

OSWAM (arXiv:2610.35850v1) 은 pretrained video prior를 활용하면서 test-time future rollout 없이 한 번의 Action DiT denoising으로 numerical action chunk를 생성하는 direct-policy [[WorldActionModel]]이다. [[StructuredActionInitialization]]으로 pure-noise 시작점을 학습된 action prior로 대체한다.

## 설계

- Wan2.2-5B Video DiT/T5/VAE와 reduced Action DiT를 MoT shared attention으로 연결한다.
- Action Imagination Tokens(AIT)는 current visual context에서 action prior를 만들고 Scene Imagination Tokens(SIT)가 context를 보완한다.
- Prior는 stop-gradient 후 같은 action noise로 re-noise하고 residual velocity를 한 번 예측해 refine한다. Role-aware RoPE가 token 역할과 latent time을 정렬한다.
- Full-future frozen teacher의 multi-depth AIT feature를 student에 distill하며 teacher와 미래 frame은 추론에서 제거한다.

## 근거와 한계

저자 보고 NAVSIM PDMS 90.3/H20 136ms는 [[SimWAM]]의 90.3/410ms에 비해 빠르다. RoboTwin 평균 90.00%는 multi-step Fast-WAM 91.83%보다 1.83 pp 낮다. RTX 5090 compiled latency 40.81ms는 robot 설정이고 driving은 52.64ms다. NAVSIM non-reactive simulation과 nuScenes open-loop는 실차 reactive closed-loop가 아니며, NPU 측정이나 formal safety는 제공하지 않는다. 실물 2 task의 trial은 method당 각 20회다.

## 연결

- [[oswam-2610-35850-paper-ko]] — CC BY 4.0 절별 번역·수식·선별 부록
- [[oswam-2610-35850-analysis]] — taxonomy·trade-off·deployment boundary
- [[oswam-2610-35850-references]] — 핵심 문헌 9편
- [[oswam-2610-35850-learning]] — 실행 검증한 교육 예제
- [[FlowMatching]] — action velocity와 time convention
- [[Echo]] — action/status coupling과 initialization 개입의 차이
