---
title: "Visual State Composer"
type: entity
tags: [vla, visual-reasoning, architecture]
sources: [visualthink-vla-2605-30011-ko-analysis]
last_updated: 2026-06-03
---

## Overview
Visual State Composer는 VisualThink-VLA 아키텍처에서 selective router가 선택한 visual evidence states를 통합하여 frozen/base VLA action decoder에 입력으로 제공하는 구성 요소이다.

## Role in Pipeline
current/previous RGB + instruction → evidence bank → selective router → **visual state composer** → frozen/base VLA action decoder → action token/robot action

## Related Concepts
- [[VisualThinkVLA]] — 상위 architecture
- [[EvidenceBank]] — 입력 source
- [[SelectiveRouting]] — 선행 단계
