---
title: "AI/ML Learning Review — Day 28 (2026-05-20): Foundation Model, Transfer Learning, Multimodal"
type: source
tags: [ai-ml-learning, foundation-model, transfer-learning, multimodal]
date: 2026-05-20
source_file: raw/ai_ml_learning/2026-05-20-day28-ai-ml-learning-review.md
source_hash: 2d55039eaa76b355
---

## Summary
Day 28 of the AI/ML learning journey covers three foundational concepts: the Foundation Model paradigm enabling transfer learning across tasks, parameter-efficient fine-tuning methods like PEFT and LoRA for cost-effective model adaptation, and multimodal model structures that bridge text, images, audio, and video through cross-modal alignment.

## Key Claims
- Foundation models are pre-trained on massive data and then adapted to downstream tasks rather than trained from scratch each time
- The modern AI system stack is "foundation model + adaptation methods + data/tools" rather than a single monolithic model
- LoRA achieves parameter efficiency by learning low-rank decomposition matrices A and B instead of updating entire weight matrices
- Multimodal models require cross-modal alignment to connect different data modalities in a shared embedding space
- Vision-language models use modality-specific encoders, projection layers, and fusion mechanisms to combine information

## Key Quotes
> "Foundation model의 핵심은 '모든 문제를 처음부터 다시 학습하지 않는다'입니다. 이미 배운 공통 능력을 재사용하고, 필요한 부분만 바꿉니다."

> "LoRA는 원래 W는 고정하고, 작은 A, B만 학습합니다. 실제 계산에서는 W + ΔW처럼 사용합니다. 이렇게 하면 모델의 큰 지식은 유지하면서, 필요한 방향으로만 살짝 조정할 수 있습니다."

> "Cross-modal alignment가 필요한 이유는 서로 다른 데이터 형식인 이미지와 텍스트가 같은 의미를 가리킬 때, 모델 내부에서도 그 둘을 가깝게 연결해야 하기 때문입니다."

## Connections
- [[FoundationModel]] — core paradigm discussed in detail
- [[TransferLearning]] — the learning approach enabled by foundation models
- [[LoRA]] — parameter-efficient adaptation technique
- [[PEFT]] — broader category of efficient fine-tuning methods
- [[MultimodalModel]] — models that process multiple data types
- [[VisionLanguageModel]] — specific multimodal models combining image and text
- [[CrossModalAlignment]] — the alignment process connecting different modalities
- [[FineTuning]] — contrast with parameter-efficient approaches
- [[Pretraining]] — the initial large-scale training phase of foundation models

## Contradictions
- No contradictions with existing wiki content found
