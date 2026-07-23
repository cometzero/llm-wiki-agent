---
title: "StateTransitionCaptioning"
type: concept
tags: [state-transition, grounding, action-generation, vla, vision-language]
last_updated: 2026-07-22
sources:
  - "xiaomi-robotics-1-2607-15330-learning"
  - "xiaomi-robotics-1-2607-15330"
---

## 정의
[[StateTransitionCaptioning]]은 조작 궤적 segment를 
"현재 상태에서 목표 상태로의 전환" 형태로 언어화해, 이를 정책 학습의 지도 신호로 사용하는 방법이다.
단순 task label("컵 조작하기”)과 달리, action가 실제로 만들려는 world state 변화(예: 대상 물체 위치/접근/고정 상태) 자체를 직접적으로 조건으로 둔다.

## 작동 방식
- 입력 trajectory를 segment 단위로 분할
- 각 segment를 모델이 이해할 수 있는 짧은 전이 문장으로 자동 캡션(예: "손이 컵 손잡이를 잡고 오른쪽 접시로 이동")
- 시각-언어 인코더가 이 문장을 state transition prior로 받아 행동 생성기로 전달
- 결과적으로 [[ActionGrounding]] 정합성이 증가하고 instruction grounding이 과도한 중간 단계 없이 강화됨

## Xiaomi-Robotics-1에서의 역할
[[Xiaomi-Robotics-1]]는 사전학습 단계에서 task label보다 [[StateTransitionCaptioning]]을 더 강한 감독 신호로 사용해,
실제 조작 성능 및 downstream 적응력 향상에 기여한다.

## AD 전환 관점
자율주행 맥락에서는 state-transition caption을 "씬 상태 변화/루트 전환/규칙 위반 회피"로 치환해
[[AutonomousDrivingVLA]]의 route/action coupling을 정합할 수 있다.

## 연관 개념
- [[ActionGrounding]]
- [[ActionChunking]]
- [[FlowMatching]]
- [[Qwen3-VL]]
- [[DiT]]
- [[ClosedLoopEvaluation]]
- [[CrossEmbodimentLearning]]