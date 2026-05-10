---
title: "NVIDIA GR00T"
type: entity
tags: [NVIDIA, Robotics, VLA, HumanoidRobotics]
last_updated: 2026-05-10
sources:
  - nvidia-gr00t-vs-gemini-robotics-vs-pi-로봇의-뇌는-어떻게-다르게-설계됐을까-vla-모델-3대장-비교-분석
---

## Summary
[[NVIDIA|NVIDIA]]의 로봇 AI 제품군으로, 휴머노이드 및 다중 인바디먼트를 대상으로 한 [[VisionLanguageAction]](VLA) 파운데이션 전략이다.

### 핵심 특징
- [[NVIDIAGR00T]]은 상위 인지 경로와 하위 제어 경로를 분리하는 이원 구조를 채택한다.
- 데이터는 웹 비전-언어 데이터, 시뮬레이션 생성 데이터, 실기체 텔레오퍼레이션 데이터 등 다층 피라미드로 구성한다.
- 최신 버전에서는 액션 토큰 표현, VLM 적응, 그라운딩 강화, 긴 작업 대응으로 진화한다.
- 인바디먼트 전이와 다작업 확장을 핵심 목표로 둔다.

### 연결
- [[NVIDIA]]의 자율주행/로보틱스 연구와의 연계가 중요하다.
- [[FlowMatching]], [[ActionChunking]], [[CrossEmbodimentTransfer]]와의 결합이 실제 성능의 핵심이다.
