---
title: "Closed-Loop Robot Deployment"
type: concept
tags: [robot-deployment, real-time-control, feedback-loop]
sources: [embodied-cpp-2607-02501]
last_updated: 2026-07-08
---

## Overview
Closed-Loop Robot Deployment는 sensor feedback과 action output이 반복적으로 교환되는 실시간 로봇 제어 시나리오를 말한다. 일반 LLM serving의 request-response(open interaction)와 달리, closed-loop는 환경과의 지속적인 상호작용이 필요하다.

## Key Characteristics
- **Feedback loop**: Sensor → Perception → Decision → Action → Sensor
- **Real-time constraints**: Latency + jitter + worst-case latency
- **Safety-critical**: Watchdog, recovery behavior 필요
- **Heterogeneous hardware**: NPU/accelerator별 역할 분배

## Deployment Challenges
1. Python research stack과 실제 런타임 간 불일치
2. 기존 LLM serving runtime 미지원
3. Batch-1, low jitter 요구사항
4. Simulator/robot adapter 필요성

## Connections
- [[VLA]] — deployment target model
- [[WAM]] — deployment target model with future prediction
- [[LatencyFirstBatch1]] — optimization strategy
- [[MultiRateExecution]] — scheduling strategy
- [[EmbodiedCpp]] — proposed solution
