---
title: "DeepSeek V4"
type: entity
tags: [DeepSeek, OpenSource, LongContext, GPU, NPU]
last_updated: 2026-05-10
source: [the-coding-assistant-breakdown-more-tokens-please]
---

## Profile

[[DeepSeek V4]]는 [[DeepSeek]]의 장문맥 및 오픈소스 공개를 강조한 코딩/추론 모델군이다.

## Key Points

- [[DeepSeek V4]]는 컨텍스트 윈도우를 128k에서 1M으로 확장한 것으로 요약됨.
- [[DeepEP]], [[DeepGEMM]], [[FlashMLA]] 관련 오픈소스 공개가 기술적 기여점으로 언급.
- V4-Pro와 V4-Flash 변종(1.6T/49B, 284B/13B 구성)이 소개됨.
- 공개 벤치마크에서는 일부 영역에서 상위 모델군과 경쟁 가능성이 보이지만, 어려운 중국어 창작 등 일부 언어·작문 작업에서는 [[Claude Opus 4.7]]이 우세하다는 평가가 있음.

## Connections

- [[DeepSeek]]
- [[OpenSource]]
- [[LongContext]]
- [[NVIDIA]] / [[Huawei Ascend]]
- [[NPU]]
- [[SWA], [KVCache], [Benchmarking]

## Notes

코드 생성/엔지니어링 업무에서는 성능 수치보다 툴링, 컨텍스트 정책, 에이전트 하네스 적합성이 우선 선택 기준이 될 수 있다.