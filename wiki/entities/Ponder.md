---
title: "Ponder"
type: entity
tags: [MLLM, System2, episode-memory]
sources: [ponderpounce-2608-24115-paper-ko]
last_updated: 2026-09-02
---

# Ponder

[[Ponder]]는 [[PonderPounce]]의 slow System 2 MLLM이다. Instruction, demonstration, observation history와 prior cognition을 append-only causal context에 누적하고, carrier hidden state를 continuous cognition으로 [[Pounce]]에 전달한다.
