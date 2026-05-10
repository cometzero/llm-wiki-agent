---
title: "Physical Intelligence Pi"
type: entity
tags: [PhysicalIntelligence, Robotics, VLA, GeneralistPolicy]
last_updated: 2026-05-10
sources:
  - nvidia-gr00t-vs-gemini-robotics-vs-pi-로봇의-뇌는-어떻게-다르게-설계됐을까-vla-모델-3대장-비교-분석
---

## Summary
[[Physical Intelligence]]의 대표 모델 계열로, 범용 로봇 정책을 중심으로 [[VisionLanguageAction]]를 구현해 다양한 몸체·작업으로의 전이를 시도한다.

### 핵심 특징
- π(파이) 계열은 [[FlowMatching]] 기반 액션 생성과 계층적 제어 설계를 결합한다.
- [[KnowledgeInsulation]]은 VLM으로부터의 언어/시각 이해를 유지한 채 로봇 학습을 안정화하는 전략이다.
- [[ActionChunking]]/연속 제어 정합성 개선으로 실사용 동작 안정성에 초점을 둔다.
- 긴 작업을 위한 [[MembasedRoboticsMemory]](오래된 작업 기억, 장기 컨텍스트) 연구까지 확장 중이다.

### 연결
- [[Robotics]], [[Physical Intelligence]], [[VLA]], [[Generalization]], [[HumanoidRobotics]]와 직접 연결된다.
