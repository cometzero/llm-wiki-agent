---
title: "VisualThink-VLA: Visual Intermediate Reasoning References"
type: source
tags: [vla, visual-reasoning, references, huggingface-weekly]
date: 2026-06-03
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W23/visualthink-vla-2605-30011/references.md
source_hash: fb397709ee23cc56
---

## Summary
VisualThink-VLA 논문(arXiv:2605.30011)의 참고 문헌 중 Semantic Scholar와 arXiv HTML에서 확인한 10개 핵심 관련 연구를 정리한 페이지. [[VLA]] 정책의 [[VisualReasoning]]과 [[LanguageGrounding]] 개선, 효율적인 [[ChainOfThought]] 추론 방식, [[EmbodiedAI]] 평가를 위한 benchmark 연구를 포함한다.

## Key References

### 1. DeepThinkVLA (2025)
- arXiv:2511.15669 | citations:10
- 저자: C. Yin, Yankai Lin, Wang Xu
- 관계: [[LanguageGrounding]]이 [[Action]]으로 전달되는지라는 핵심 질문과 직접 연결

### 2. InternVLA-M1 (2025)
- arXiv:2510.13778 | citations:45
- 저자: Xinyi Chen, Yilun Chen, Yanwei Fu
- 관계: [[LanguageGrounding]]이 [[Action]]으로 전달되는지라는 핵심 질문과 직접 연결

### 3. Fast ECoT (2025)
- arXiv:2506.07639 | citations:18
- 저자: Zhekai Duan, Yuan Zhang, Shikai Geng
- 관계: [[ReasoningAugmentedVLA]] 계열 선행 연구로, textual/visual reasoning interface의 장단점을 비교하는 기준

### 4. SmolVLA (2025)
- arXiv:2506.01844 | citations:297
- 저자: Mustafa Shukor, Dana Aubakirova, Francesco Capuano
- 관계: 대표 [[VLAPolicy]]/backbone baseline으로 본 논문의 비교·문제의식 배경

### 5. Visual Planning (2025)
- arXiv:2505.11409 | citations:68
- 저자: Yi Xu, Chengzu Li, Han Zhou
- 관계: [[ReasoningAugmentedVLA]] 계열 선행 연구로, textual/visual reasoning interface의 장단점을 비교하는 기준

### 6. π0.5 (2025)
- arXiv:2504.16054 | citations:966
- 저자: [[PhysicalIntelligence]] (Kevin Black, Noah Brown)
- 관계: 대표 [[VLAPolicy]]/backbone baseline으로 본 논문의 비교·문제의식 배경

## Background References

### LMMs Meet Object-Centric Vision
- arXiv:2604.11789 | citations:5
- 저자: Yuqian Yuan, Wenqiao Zhang, Juekai Lin

### Unified Personalized Understanding, Generating and Editing
- arXiv:2601.06965 | citations:6
- 저자: Yu Zhong, Tianwei Lin, Rui Zhu

### PixelRefer
- arXiv:2510.23603 | citations:15
- 저자: Yuqian Yuan, Wenqiao Zhang, Xin Li

### EOC-Bench
- arXiv:2506.05287 | citations:16
- 저자: Yuqian Yuan, Ronghao Dang, Long Li

## Connections
- [[VisualThinkVLA]] — parent paper
- [[VLAPolicy]] — 공통 연구 주제
- [[LanguageGrounding]] — 핵심 과제 (DeepThinkVLA, InternVLA-M1)
- [[ReasoningAugmentedVLA]] — 계열 연구 (Fast ECoT, Visual Planning)
- [[SemanticGrounding]] — 관련 개념
- [[PhysicalIntelligence]] — π0.5 연구 기관
- [[SmolVLA]] — 비교 baseline

## Contradictions
- 없음
