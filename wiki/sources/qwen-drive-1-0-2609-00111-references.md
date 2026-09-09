---
title: "Qwen-Drive-1.0 참고문헌 학습 메모"
type: source
tags: [autonomous-driving, references, foundation-model, planning]
date: 2026-09-09
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W36/qwen-drive-1-0-2609-00111/references.md
source_hash: e15764a43e77e084
---

## Summary
이 reference map은 Qwen-Drive를 UniAD/VAD의 end-to-end driving, DriveLM/DriveGPT4의 language interface, NAVSIM의 interaction-aware evaluation, SimWAM의 world-action framing, flow matching의 numerical generation과 연결한다.

## Key Claims
- Planning-oriented AD와 driving VQA의 문헌은 동일한 shared representation을 요구하지만 action interface가 다르다.
- NAVSIM류 metric은 logged trajectory error만으로 드러나지 않는 collision/progress/comfort 문제를 보완한다.

## Connections
- End-to-end driving, driving VLM, world-action model, generative trajectory planner의 읽기 순서를 제공한다.

## Contradictions
- Driving VQA의 explainability는 executable action grounding과 동의어가 아니다.
