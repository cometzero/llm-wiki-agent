---
title: "Mode Collapse"
type: concept
tags: [generative-model, training-stability]
sources: [flow-erd-2607-06957]
last_updated: 2026-07-15
---

## Overview
Mode collapse는 generative model이 학습 과정에서 일부 high-probability mode에만 집중하고 다른 valid modes를 잃어버리는 현상입니다. Traffic simulation에서는 단일 dominant behavior(직진 등)만 생성하게 됩니다.

## Flow-ERD에서의 관련성
- Vanilla reverse-KL objective (β=1)는 mode-seeking으로 dominant mode로 쉽게 붕괴
- Flow-ERD의 ERD는 β<1로 entropy regularization을 적용하여 plausible modes 보존

## Connections
- [[FlowERD]] — 해결책 적용
- [[CovariateShift]] — 관련 문제
- [[MultiAgentSimulation]] — 발생하는 domain
