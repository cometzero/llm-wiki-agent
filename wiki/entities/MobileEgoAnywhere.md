---
title: "MobileEgo Anywhere"
type: entity
tags: [VLA, data-collection, open-source, robotics]
sources: [mobileego-anywhere-2605-05945-analysis]
last_updated: 2026-05-20
---

## Overview
iPhone 기반 범용 하드웨어로 장기 egocentric 데이터를 수집하는 오픈 인프라 프로젝트. VLA 정책 학습에 필요한 long-horizon trajectory 데이터를 commodity hardware로 확장 수집하는 것을 목표로 한다.

## Key Components
- **STERA Pipeline**: 3D hand trajectory, atomic action labels, hierarchical instruction tree 생성
- **MCAP Logging**: RGB-D, IMU, intrinsics, ARKit pose 동기화 기록
- **Data Scale**: 200시간, 354세션, 16 기여자

## Connection to VLA Ecosystem
- [[HumanNet]]과 함께 VLA pretraining용 egocentric 데이터 소스로 활용
- [[GR00T]] 계열 VLA 모델의 human-to-robot trajectory mapping 지원
- [[Ego4D]], [[EPIC-KITCHENS]] 등 기존 데이터셋과 상호 보완

## Related
- [[VLA]] — 주요 downstream 활용
- [[STERA]] — 핵심 처리 파이프라인
- [[HumanNet]] — 경쟁/보완 데이터셋
