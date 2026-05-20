---
title: "Physical QA"
type: concept
tags: [physical-reasoning, vlm-training, supervision]
sources: [physbrain-1-0-2605-15298, physbrain-1-0-2605-15298-learning, physbrain-1-0-2605-15298-analysis]
last_updated: 2026-05-20
---

## Definition
Human egocentric video에서 추출한 structured physical record(scene elements, spatial dynamics, action execution, depth-aware relations)를 자연어 question-answer 쌍으로 rendering한 학습용 supervision 형식.

## Purpose
Raw video나 generic caption보다 [[PhysicalCommonsense]]와 action order를 더 강력하게 학습시킬 수 있는 supervision signal을 제공한다.

## Generation Pipeline
1. Human egocentric video → structured meta-record (JSON-like schema)
2. Schema validation (hallucination 방지를 위해 필수)
3. Meta-record → Q&A pairs 변환
4. Q&A pairs → [[VLM]] 학습 데이터

## Key Risk
Annotation model이 만든 [[PhysicalQA]]의 오류가 [[VLM]]/[[VLA]]에 체계적으로 주입될 수 있다. 따라서 schema validation이 중요하다.

## Related Concepts
- [[PhysicalCommonsense]] — 학습 대상
- [[VLM]] — 학습 대상 모델
- [[VLA]] — 최종 적용 모델
- [[StructuredMetaRecord]] — Q&A 생성의 입력
