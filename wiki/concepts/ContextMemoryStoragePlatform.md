---
title: "Context Memory Storage Platform"
type: concept
tags: [kv-cache, storage, inference, long-context]
last_updated: 2026-04-20
sources: [gtc-2026-the-inference-kingdom-expands]
---

## Definition
[[CMX]] 및 연계되는 [[STX]] 계열은 긴 컨텍스트 추론에서 발생하는 KV 캐시 확장 압력을 완화하기 위한 스토리지 오프로드 플랫폼 개념이다.

## Core Idea
- HBM 단독으로는 사용자 수/시퀀스 길이가 길어지는 환경에서 KV 캐시를 충분히 감당하기 어렵다.
- NVMe/스토리지 레이어를 계층적으로 추가해 추론 비용 곡선을 유연하게 만든다.

## Source Mapping
- [[CMX]]는 NVMe 기반 오프로드와 BlueField-4 중심 접속 구조를 통해 컨텍스트 저장을 확장한다.
- [[STX]]는 CMX의 범위를 실제 컴퓨팅 클러스터에 맞게 레퍼런스화한 저장 랙 구조다.

## Related Concepts
- [[LongContext]], [[KVCache]], [[NVMe]], [[BlueField-4]], [[NVIDIA]]
