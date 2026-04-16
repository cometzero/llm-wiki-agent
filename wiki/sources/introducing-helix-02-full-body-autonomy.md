---
title: "Introducing Helix 02: Full-Body Autonomy"
type: source
tags: [robotics, humanoids, autonomy]
date: 2026-04-16
source_file: raw/Robotics/Introducing Helix 02_ Full-Body Autonomy.md
---

## Summary
This source describes Figure's Helix 02 as a full-body humanoid control stack that unifies locomotion, manipulation, and balance instead of treating them as separate subsystems. It frames the main breakthrough as long-horizon autonomous loco-manipulation, where a robot can move across a room, handle objects, recover from small errors, and continue a task without resets or teleoperation. The writeup also emphasizes new dexterity enabled by palm cameras, tactile sensing, and a three-layer System 0 / System 1 / System 2 architecture.

## Key Claims
- [[Helix02]] integrates walking, balance, and object manipulation into one learned full-body control system.
- [[System0]] is a learned whole-body controller trained on 1,000+ hours of human motion data and sim-to-real reinforcement learning.
- [[Figure03]] hardware adds palm cameras and fingertip tactile sensing that enable fine manipulation such as picking up pills or controlling a syringe.
- The source presents a 4-minute autonomous dishwasher task with 61 continuous actions as evidence of unusually long-horizon [[LocoManipulation]].
- The architecture separates semantic reasoning ([[System2]]), visuomotor policy generation ([[System1]]), and high-frequency physical control ([[System0]]).

## Key Quotes
> "로봇이 걷는 동시에 물건을 다루고, 균형을 잡는 모든 행동을 하나의 신경망(Helix 02)으로 처리" — source summary of the central technical claim.

> "진정한 자율성은 근본적으로 다른 것을 요구하며, 이는 전신을 한 번에 추론하는 단일 학습 시스템이다." — rationale for replacing handoff-heavy classical pipelines.

> "61개의 이동-조작 동작이 암묵적인 오류 복구와 함께 올바르게 순서가 지정되었으며" — evidence cited for long-horizon autonomy.

## Connections
- [[FigureAI]] — company building the Helix stack and the Figure humanoid platform.
- [[Figure03]] — hardware platform whose tactile sensors and palm cameras are highlighted.
- [[Helix02]] — main model described in the source.
- [[LocoManipulation]] — the source treats integrated movement-plus-manipulation as the key robotics bottleneck.
- [[TactileSensing]] — fine manipulation is tied to fingertip force sensing and in-hand perception.
- [[VisuomotorControl]] — the system is described as an end-to-end pixel-to-action policy.
- [[HumanoidRobotics]] — broader field context for the claimed breakthrough.

## Contradictions
- No direct contradictions identified yet; this page is broadly consistent with the Figure 03 source on the importance of learned control, sensing, and simulation-backed training.
