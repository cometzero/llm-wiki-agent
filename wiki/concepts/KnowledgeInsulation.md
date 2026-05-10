---
title: "Knowledge Insulation"
type: concept
tags: [Robotics, ContinualLearning, CatastrophicForgetting, VLA]
last_updated: 2026-05-10
sources:
  - nvidia-gr00t-vs-gemini-robotics-vs-pi-로봇의-뇌는-어떻게-다르게-설계됐을까-vla-모델-3대장-비교-분석
---

## Definition
사전학습된 시각-언어 이해를 유지한 채 로봇 제어 학습을 수행하기 위해, 백본 표현이 퇴화하지 않도록 그라디언트 경로와 학습 전략을 분리·완화하는 설계 개념.

## Purpose
로봇 학습 과정에서 언어/지각 능력이 손실되지 않도록 하여 명령 수행 정확도와 학습 속도를 동시에 확보한다.

## In this source
[[PhysicalIntelligencePi]]의 Fast/0.5/0.6 계열에서 성능 하락 없이 파인튜닝 효율과 지시 이해를 개선하기 위한 핵심 장치로 다뤄진다.
