---
title: "Robot-ready Subset"
type: concept
tags: [robotics, data-quality, subset-selection]
sources: [humannet-2605-06747]
last_updated: 2026-05-13
---

HumanNet에서 robot learning에 바로 사용 가능한高品质 비디오 subset을 선별하는 기준.

**선별 기준:**
- **Retargeting error < 15mm**: 3D hand/body pose를 robot-compatible format으로 변환할 때의 오차
- **Valid-frame coverage ≥ 60%**: 전체帧中对олон motion retargeting이 유효한 비율

**의미:**
- Human motion을 robot action space로 매핑하기에 충분한 품질
- Noise filtering을 통해 learning efficiency 향상
- Downstream task에 맞는 subset 선택 가능

**사용 시나리오:**
- VLA pretraining
- Motion-aware representation learning
- World-action model training

**연관:**
- [[HumanNet]] — 정의한 데이터셋
- [[DataSelection]] — [[EmbodiedMidtrain]]의 관련 개념
