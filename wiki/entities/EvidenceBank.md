---
title: "Evidence Bank"
type: entity
tags: [vla, visual-reasoning, architecture]
sources: [visualthink-vla-2605-30011-ko-analysis]
last_updated: 2026-06-03
---

## Overview
Evidence Bank은 VisualThink-VLA 아키텍처의 핵심 구성 요소로, 후보 visual evidence states를 저장하고 selective router에 제공하는 저장소이다. Visual intermediate reasoning에서 evidence 선택의 기반이 된다.

## Role in Pipeline
current/previous RGB + instruction → **evidence bank** → selective router → visual state composer → VLA action decoder

## Related Concepts
- [[VisualThinkVLA]] — 상위 architecture
- [[SelectiveRouting]] — evidence bank 출력 활용
- [[VisualStateComposer]] — evidence bank 선택 결과 수신
