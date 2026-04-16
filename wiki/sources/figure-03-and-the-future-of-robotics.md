---
title: "Figure 03 and the Future of Robotics"
type: source
tags: [robotics, humanoids, hardware, developer-tools]
date: 2026-04-16
source_file: raw/Robotics/Figure 03 and the Future of Robotics.md
---

## Summary
This source analyzes [[Figure03]] as a marker of recent progress in humanoid robotics, emphasizing quieter electric actuators, hybrid control, richer sensing, better thermal design, and the [[Helix02]] behavior model. It also interprets Figure's public technical breadcrumbs as evidence of a modular stack built with simulation, low-level real-time control, and GPU-accelerated perception. A secondary theme is that developer-facing tools such as Isaac Lab and 3D mapping libraries make "physical intelligence" more accessible beyond elite robotics labs.

## Key Claims
- [[Figure03]] improves on older humanoids through electric actuators, quasi-direct drive, and hybrid physics-plus-ML control.
- Stereo cameras, palm cameras, and fingertip sensors reduce latency and improve precise manipulation.
- Figure's stack likely combines simulation training, hard real-time motor control, and GPU-based perception / 3D reconstruction.
- [[Nvidia]] Isaac Lab and related simulators make it practical for developers to train robot policies without full hardware access.
- [[PhysicalIntelligence]] is framed as the next major software frontier, with robots as an emerging computing platform.

## Key Quotes
> "Figure 03은 전기 액추에이터, 하이브리드 제어 스택, 스테레오 카메라 및 촉각 센서, 능동 냉각 배터리, 그리고 대규모 행동 모델 Helix를 통해 로봇 공학의 발전을 이끌고 있습니다." — source summary of the main hardware/software stack.

> "다음 소프트웨어의 프론티어는 앱이나 AI 모델이 아니라 물리적 지능(physical intelligence)에 있다." — the source's broader thesis.

> "Figure의 독점적인 두뇌인 Helix는 매우 모듈화된 스택 위에 자리 잡고 있음을 알 수 있다." — interpretation of the architecture from public repositories and tooling.

## Connections
- [[FigureAI]] — company discussed throughout the source.
- [[Figure03]] — focal robot platform.
- [[Helix02]] — behavior model linked to the robot's capabilities.
- [[Nvidia]] — Isaac Lab / Isaac Sim are named as major training tools.
- [[HumanoidRobotics]] — field-level context.
- [[TactileSensing]] — precision handling depends on tactile and in-hand visual sensors.
- [[PhysicalIntelligence]] — the source explicitly names this as the next frontier.
- [[VisuomotorControl]] — implied by the discussion of perception, control, and 3D world modeling.

## Contradictions
- The source complements the Helix 02 autonomy source by focusing more on hardware and developer tooling than on the detailed System 0 / 1 / 2 decomposition.
- Some implementation details are inferred from public repositories rather than directly confirmed by Figure, so specific stack details may be less certain than the claims summarized in the Helix 02 source page.
