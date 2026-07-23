---
title: "RT-1"
type: entity
tags: [robotics, vision-language-action, transformer, baseline]
sources:
  - xiaomi-robotics-1-2607-15330-references
last_updated: 2026-07-22
---

## 개요

[[RT-1]]은 Anthony Brohan et al. (2022, <https://arxiv.org/abs/2212.06817>)의 실제 로봇 데이터 기반 transformer 정책 베이스라인으로, VLA 연구에서 대규모 real-world trajectory 기반 정책 학습의 핵심 좌표로 쓰였다.

## 핵심 포인트

- real-world robot trajectory를 직접 transformer 정책으로 학습.
- [[Xiaomi-Robotics-1]]이 다루는 [[UMI]] 기반 확장 전략의 역사적 비교군.
- scaling 논의에서 "사전학습 구조"보다 "데이터-모델 조합"의 실효성 비교에 자주 활용.

## 연결

- [[Xiaomi-Robotics-1]]: 사전학습/후학습 전략 비교군.
- [[pi0]], [[pi0.5]]: VLA 후속 선행군 간 구조적 비교 축.
- [[Diffusion Policy]]: action 생성 접근법의 대체군으로서의 대조군.
