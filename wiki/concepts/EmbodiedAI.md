---
title: "Embodied AI"
type: concept
tags: [robotics, ai, physical-learning]
last_updated: 2026-05-13
---

# Embodied AI

[[Embodied AI]]는 물리적 환경과 상호작용하면서 학습하는 AI 패러다임이다. 단순히 정적인 데이터를 처리하는 것이 아니라, 에이전트가 환경에서 행동하고 그 결과를 관찰하며 학습한다. [[VLA]] 모델이 대표적인 Embodied AI 구현체이며, HumanNet은 이 분야의 데이터 scaling 문제를 해결하기 위한 접근을 제시한다.

## Overview
물리적 환경에서知觉-행동 피드백 루프를 통해 학습하는 AI 시스템. 로봇, 자율주행车辆, 실시간 대화 에이전트 등이 포함된다.

## Connections
- [[HumanNet]] — 100만 시간 human-centric video로 Embodied AI 데이터 부족 해결 시도
- [[VLA]] — Embodied AI의 핵심 모델 아키텍처
- [[LingBot]] — Embodied AI 로봇 태스크에 활용
- [[EmbodiedMidtrain]] — VLM-VLA 전환으로 Embodied AI 성능 향상
- [[Tesla]] [[EndToEndAutonomy]] — 차량 Embodied AI 구현
- [[Cosmos-Reason1]] — Physical common sense에서 embodied reasoning으로 확장

## Key Characteristics
- **Physical interaction**: 환경과의 직접적인 상호작용
- **Action grounding**: 언어/시각 입력에서 행동으로의 매핑
- **Data scarcity**: Robot teleoperation data는 expensive하고 fragmented
- **Long-tail coverage**: 일반적인 동작보다 특수한 상황의 데이터 부족
- **Embodiment gap**: Human demonstration에서 robot deployment로의 전환 문제

## Related Concepts
- [[VLA]]: Embodied AI의 핵심 모델
- [[DataSelection]]: 데이터 효율적 학습 기법
- [[Simulation]]: 시뮬레이션 기반 학습 ([[Tesla]] [[WorldSimulator]] 참조)
