---
title: "ReCAP"
type: entity
tags: [vla, robotics, retrieval]
sources: [retrieve-dont-retrain-2606-15631]
last_updated: 2026-06-17
---

## Overview
ReCAP(Re​trieval-Conditioned Action Policy)은 [[VisionLanguageAction]]/robot policy를 새 task에 확장할 때 per-task retraining 대신 retrieval pool update를 사용하는 VLA adaptation framework다.

## Key Facts
- Source/pool embodiment demonstration을 검색해 target robot action generation의 high-level motion prior로 사용한다.
- [[WorldActionModel]] 계열인 Cosmos Policy와 결합해 future-image consistency signal을 활용한다.
- 핵심 raw/source: [[retrieve-dont-retrain-2606-15631]].

## Connections
- [[RetrievalAugmentedPolicy]] — ReCAP의 정책 설계 패턴.
- [[ActionGrounding]] — retrieved trajectory를 executable target action으로 변환하는 문제.
- [[VisionLanguageAction]] — ReCAP이 확장하려는 VLA framework.
