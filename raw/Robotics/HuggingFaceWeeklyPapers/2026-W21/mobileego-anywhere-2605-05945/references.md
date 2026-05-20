---
title: "MobileEgo Anywhere: 범용 하드웨어 기반 장기 egocentric 데이터 수집 오픈 인프라 — references"
source_url: "https://arxiv.org/abs/2605.05945"
hf_url: "https://huggingface.co/papers/2605.05945"
arxiv_id: "2605.05945"
arxiv_url: "https://arxiv.org/abs/2605.05945"
pdf_url: "https://arxiv.org/pdf/2605.05945"
week: "2026-W21"
ingested_at_kst: "2026-05-20 09:40:06 KST"
selected_reason: "현재 주(2026-W21) 후보 중 VLA 모델 스케일링의 핵심 병목인 long-horizon egocentric data 수집 인프라를 직접 다루며, 스마트폰 기반 6-DoF pose/RGB-D/hand trajectory 파이프라인이 자율주행·로보틱스 VLA 데이터 전략과 연결됨."
---

# 참고 레퍼런스 논문 요약

## 1. EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data

- 링크/식별자: arXiv:2602.16710
- 관계: MobileEgo가 직접 인용하는 scaling-law/egocentric manipulation 선행 연구. MobileEgo는 EgoScale보다 훨씬 긴 episode와 commodity smartphone 수집성을 강조한다.

## 2. Universal Manipulation Interface (UMI)

- 링크/식별자: RSS 2024
- 관계: in-the-wild robot teaching을 낮은 장벽으로 만든 대표 연구. MobileEgo는 UMI의 특수 gripper/마운트 부담보다 더 범용적인 smartphone sensor suite를 선택한다.

## 3. Ego4D: Around the World in 3,000 Hours of Egocentric Video

- 링크/식별자: CVPR 2022
- 관계: 대규모 egocentric video의 대표 데이터셋. 하지만 MobileEgo가 원하는 연속 6-DoF pose, RGB-D, long-horizon state tracking은 부족하다.

## 4. EPIC-KITCHENS / EPIC-KITCHENS-100

- 링크/식별자: ECCV 2018 / IJCV 2022
- 관계: 주방 egocentric action recognition의 핵심 데이터셋. MobileEgo는 action recognition을 넘어 VLA pretraining용 trajectory/hand/action hierarchy를 제공하려 한다.

## 5. Ego-Exo4D

- 링크/식별자: CVPR 2024
- 관계: first-person/third-person paired skilled activity dataset. MobileEgo와 달리 Project Aria 등 비범용 장비 의존성이 크다.

## 6. HOI4D

- 링크/식별자: CVPR 2022
- 관계: 4D human-object interaction dataset. MobileEgo의 hand-object interaction annotation 필요성과 연결된다.

## 7. HOT3D

- 링크/식별자: CVPR 2025
- 관계: 고정밀 hand/object tracking benchmark. MobileEgo는 대규모 unconstrained recordings에서 ground-truth-free consistency metric으로 hand pose 품질을 점검한다.

## 8. ARCTIC

- 링크/식별자: CVPR 2023
- 관계: dexterous bimanual hand-object manipulation dataset. MobileEgo의 MANO hand-pose 평가와 비교되는 controlled high-precision dataset이다.

## 9. WiLoR: End-to-end 3D Hand Localization and Reconstruction in-the-wild

- 링크/식별자: arXiv:2409.12259
- 관계: MobileEgo의 3D hand trajectory pipeline에서 hand pose estimation에 사용되는 핵심 방법.

## 10. MCAP

- 링크/식별자: mcap.dev
- 관계: RGB-D/IMU/pose raw stream을 표준 로그 포맷으로 저장하기 위한 container. downstream VLA dataset conversion의 기반이다.
