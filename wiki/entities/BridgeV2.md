---
title: "Bridge V2"
type: entity
tags: [dataset, robotics, benchmark, manipulation]
sources:
  - xiaomi-robotics-1-2607-15330-references
last_updated: 2026-07-22
---

## 개요

[[Bridge V2]]는 로봇 manipulation 정책 학습에서 쓰이는 공개 로봇 데이터셋 계열 중 하나로, [[Xiaomi-Robotics-1]] post-training 데이터 구성에서 활용된 소스로 정리된다.

## 핵심 역할

- [[UMI]] 기반 사전학습 이후의 실제 embodiment 정렬에서 분포 보강.
- 고비용 teleoperation-only 데이터의 한계를 완화하기 위한 공개 데이터 공급원.
- [[DROID]] 등 다른 공개 로그와 함께 cross-embodiment 성능 이전에서 보조 데이터 축을 구성.

## 연결

- [[Xiaomi-Robotics-1]]: post-training 및 실험 재현에서 보조 데이터로 언급.
- [[DROID]]: 로봇 manipulation 공개 데이터 생태계의 동반 집합.
- [[RoboCasa365]], [[RoboDojo]]: 시뮬레이션/실환경으로의 전이 검증과 병행되는 벤치마크 맥락.

## 상태

- 존재하는 위키 링크는 보강 필요. 현재는 레퍼런스 기반 핵심 엔트리로 등록.
