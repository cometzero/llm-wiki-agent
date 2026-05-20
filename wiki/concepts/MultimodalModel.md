---
title: "Multimodal Model"
type: concept
tags: [multimodal, vision-language, cross-modal, modality]
sources: [2026-05-20-day28-ai-ml-learning-review.md]
last_updated: 2026-05-20
---

## Definition
A multimodal model processes and understands multiple data modalities — such as text, images, audio, video, and sensor data — together. This mirrors human perception which combines visual, auditory, and textual information.

## Modality Types
- **Text**: Written language, code, structured data
- **Image**: Photos, charts, diagrams, documents
- **Audio**: Speech, music, environmental sounds
- **Video**: Spatiotemporal sequences of images and audio
- **Sensor data**: LiDAR, depth, motion, tactile

## Why Multimodal Models Matter
Many real-world tasks require understanding multiple modalities:
- Reading receipts and invoices (image + text)
- Medical image analysis (image + clinical notes)
- Autonomous driving (camera + LiDAR + sensor data)
- Robot manipulation (visual + tactile + proprioceptive)
- Math problem solving from photos

## Architecture Components

### 1. Modality-Specific Encoders
- **Image**: Vision Transformer (ViT), CNN-based encoders
- **Text**: Transformer text encoder
- **Audio**: Spectrogram-based encoders
- Each encoder processes its modality into a vector representation

### 2. Projection Layer
- Converts different encoder outputs to matching dimensions
- Example: 1024-dim image features → 4096-dim LLM hidden size

### 3. Fusion Mechanism
- **Concatenation**: Simply joining vectors
- **Cross-attention**: Let modalities attend to each other
- **Late fusion**: Process separately, combine at decision stage

### 4. LLM or Decoder
- Generates responses, captions, or action commands
- Receives combined multimodal information

### 5. Alignment Objective
- Loss function ensuring matched image-text pairs are close in embedding space
- Cosine similarity for measuring alignment

## Examples
- **GPT-4o**: Vision capabilities integrated with language
- **Gemini**: Native multimodal training
- **Claude vision**: Image understanding and analysis
- **CLIP**: Image-text alignment for retrieval and generation
- **BLIP, LLaVA**: Vision-language understanding models

## Connections
- [[VisionLanguageModel]] — text + image focus
- [[CrossModalAlignment]] — aligning different modalities
- [[FoundationModel]] — often the language backbone
- [[Embedding]] — representation space for alignment
