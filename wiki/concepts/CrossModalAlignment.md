---
title: "Cross-Modal Alignment"
type: concept
tags: [cross-modal, alignment, embedding, multimodal]
sources: [2026-05-20-day28-ai-ml-learning-review.md]
last_updated: 2026-05-20
---

## Definition
Cross-modal alignment is the process of connecting representations from different modalities (e.g., images and text) in a shared embedding space so that semantically similar content from different modalities is positioned close together.

## The Problem It Solves
Different modalities start as completely different data:
- Text "apple" = word tokens
- Apple photo = pixel value arrays

Humans connect these naturally, but models need explicit learning to align them.

## Alignment Process
1. Image encoder converts image I to vector v
2. Text encoder converts text T to vector t
3. Pairs with same meaning → v and t should be close
4. Pairs with different meaning → v and t should be far
5. Learned via contrastive loss / cosine similarity optimization

## Cosine Similarity
Used to measure alignment quality:
```
similarity(a, b) = cos(θ) = (a · b) / (||a|| × ||b||)
```
- High similarity = same direction = semantically similar
- Low similarity = different directions = semantically different

## Example
| Pair | Embedding A | Embedding B | Similarity |
|------|-------------|-------------|------------|
| apple photo + "apple" | [0.8, 0.2] | [0.9, 0.1] | High |
| apple photo + "car" | [0.8, 0.2] | [0.1, 0.9] | Low |

## Why It Matters
Cross-modal alignment enables:
- **Image search by text**: Find images matching text query
- **Image description**: Generate text explaining images
- **Visual question answering**: Answer questions about images
- **Visual grounding**: Connect text references to image regions

## Applications
- Shopping apps: "Find similar to this photo"
- Document OCR: Connecting printed text to meaning
- Medical imaging: Linking visual findings to clinical notes
- Robot vision: Connecting camera input to language instructions

## Key Models Using Alignment
- [[CLIP]]: Contrastive Language-Image Pre-training
- [[BLIP]]: Bootstrapped Language-Image Pre-training
- [[LLaVA]]: Large Language and Vision Assistant
- [[GPT-4o]], [[Gemini]]: Production VLMs with alignment

## Connections
- [[MultimodalModel]] — where alignment is used
- [[VisionLanguageModel]] — application of alignment
- [[Embedding]] — the representation space
- [[CLIP]] — foundational alignment model
