---
title: "WorldDiT — 참고 레퍼런스"
type: source
tags: [huggingface-weekly, robotics, vla, embodied-ai]
date: 2026-07-29
last_updated: 2026-07-29
source_url: "https://arxiv.org/html/2607.23909"
hf_url: "https://huggingface.co/papers/2607.23909"
arxiv_id: "2607.23909"
arxiv_url: "https://arxiv.org/abs/2607.23909"
pdf_url: "https://arxiv.org/pdf/2607.23909"
week: "2026-W31"
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W31/worlddit-unified-diffusion-world-action-2607-23909/references.md
source_hash: b3d30154b8472337
---

## Summary
Paris 2.0, MMaDA-VLA, VLANeXt, ACoT-VLA, Diffusion Policy, LIBERO 등 WorldDiT 선행군을 요약한다.

## Key Claims
- 이 raw deliverable은 2026-W31 Hugging Face Weekly Best Papers 자동화에서 새로 선별된 문서이며, full raw path를 `source_file`에 보존한다.
- WorldDiT는 큰 VLM action backbone 없이 shared DiT로 action chunk와 future visual supervision을 결합한다.
- 자율주행 VLA로 확장할 때 future BEV/occupancy prediction을 auxiliary로 학습하고 inference에서는 trajectory/action만 내보내는 compact closed-loop 설계와 연결된다.

## Key Quotes
> 원문/번역 raw 문서의 핵심 내용은 `raw/Robotics/HuggingFaceWeeklyPapers/2026-W31/worlddit-unified-diffusion-world-action-2607-23909/references.md`에 보존되어 있다.

## Connections
- [[Paris20]]
- [[MMaDAVLA]]
- [[VLANeXt]]
- [[ACoTVLA]]
- [[DiffusionPolicy]]

## Contradictions
- 기존 wiki 주장과 직접 충돌 없음. 다만 성능 수치와 data recipe는 paper-specific context로 해석해야 한다.
