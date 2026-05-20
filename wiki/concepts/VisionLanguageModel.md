---
title: "Vision-Language Model (VLM)"
type: concept
tags: [vision-language-model, multimodal, image-understanding]
sources: [2026-05-20-day28-ai-ml-learning-review.md]
last_updated: 2026-05-20
---

## Definition
A vision-language model (VLM) is a multimodal model specifically designed to understand and reason about both images and text. VLMs can describe images, answer questions about visual content, retrieve images by text, and generate text conditioned on images.

## Capabilities
- **Image captioning**: "Describe what's in this image"
- **Visual question answering**: "Where is the red object in this photo?"
- **Image retrieval**: "Find images matching 'cat playing piano'"
- **Visual reasoning**: Understanding relationships, spatial positions, text in images
- **Document understanding**: Reading charts, diagrams, receipts

## Example: Apple Photo and "apple" Text
Multimodal models learn to align:
- Text "apple" embedding: [0.9, 0.1]
- Apple photo embedding: [0.8, 0.2] (similar direction)
- Car photo embedding: [0.1, 0.9] (different direction)

Cosine similarity between matching pairs is high; non-matching pairs are low.

## Applications
- **OCR and document processing**: Reading text from images
- **Medical imaging**: Assisting diagnosis with visual analysis
- **Autonomous driving**: Scene understanding from camera
- **E-commerce**: Visual search ("find similar products")
- **Education**: Solving math problems from photos
- **Content moderation**: Understanding image content

## Production Examples
- GPT-4o with vision
- Claude with vision capabilities
- Gemini
- CLIP (retrieval-focused)
- BLIP (bootstrapped language-image pre-training)
- LLaVA (large language and vision assistant)

## Relationship to Image Generation Models
VLMs focus on **understanding** and **reasoning**, while image generation models (like Stable Diffusion, DALL-E) focus on **creation**. Many systems combine both capabilities.

## Connections
- [[MultimodalModel]] — parent concept
- [[CrossModalAlignment]] — enabling mechanism
- [[CLIP]] — foundational vision-language model
- [[GPT-4o]], [[Claude]], [[Gemini]] — production VLMs
