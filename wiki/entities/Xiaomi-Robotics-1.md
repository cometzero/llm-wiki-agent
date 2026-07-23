---
title: "Xiaomi-Robotics-1"
type: entity
tags: [robotics, vla, vision-language-action, trajectory-scaling]
last_updated: 2026-07-22
---

## 개요
[[Xiaomi-Robotics-1]]는 [[UMI]] 기반의 대규모 조작 trajectory 수집, [[StateTransitionCaptioning]], 그리고 [[Qwen3-VL]] + [[DiffusionTransformer]] 기반 [[ActionChunking]] 파이프라인으로 action grounding과 cross-embodiment 성능 이전을 노린 로보틱스 VLA 프로젝트 계열이다.

## 핵심 축
- 대규모 데이터: [[UMI]] handheld 로그를 통해 조작 궤적 수집을 확장.
- 지도 신호: task label 대신 상태 변화 기술을 supervision으로 사용.
- 모델 구조: [[Qwen3-VL]] + [[KVCache]]로 context를 구성하고 [[DiT]]로 [[ActionChunk]] 생성.
- 일반화/전이: UMI 사전학습 뒤, 실제 로봇 embodiment(모바일/듀얼/정적 arm)로 post-training 정합.
- 평가 관점: open-loop MSE + [[ClosedLoopEvaluation]](real robot/simulation) 동시 검증.

## 관련 연결
- [[StateTransitionCaptioning]]
- [[Xiaomi-Robotics-1]]
- [[UMI]]
- [[Qwen3-VL]]
- [[DiffusionTransformer]]
- [[ActionChunking]]
- [[CrossEmbodimentLearning]]
- [[RoboCasa365]], [[RoboDojo]], [[RoboCasa]]

## 비고
해당 라인은 자율주행 전이에서는 state-transition 언어 신호를 scene/route transition+안전 제약 조건으로 치환할 수 있다는 점에서 [[AutonomousDrivingVLA]] 맥락과 직접 연결된다.