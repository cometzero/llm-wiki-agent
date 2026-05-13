---
title: "LingBot-VLA"
type: entity
tags: [VLA-architecture, robotics, Alibaba]
sources: [humannet-2605-06747]
last_updated: 2026-05-13
---

HumanNet validation 실험에 사용된 VLA 아키텍처. Qwen 백본에 action expert를 결합한 구조로, 20,000시간 real-robot training을 받은 상태.

**실험 설정:**
- HumanNet의 pretraining 효과를 검증하기 위해 LingBot-VLA architecture를 고정
- pretraining source만 변화시켜 controlled comparison 수행

**결과:**
- 1,000시간 HumanNet egocentric pretraining은 100시간 real-robot data와 유사/이하 validation loss
- 20,000시간 full robot baseline과의 gap을 크게 줄임

**연관:**
- [[HumanNet]] — validation 대상 데이터셋
- [[Qwen]] — 백본 VLM
- [[VLA]] — 해당 분야
