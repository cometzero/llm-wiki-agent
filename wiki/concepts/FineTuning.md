---
title: "Fine-tuning"
type: concept
tags: [llm, training, adaptation]
sources: ["2026-05-21-day29-ai-ml-learning-review", "2026-05-20-day28-ai-ml-learning-review"]
last_updated: 2026-05-21
---

# Fine-tuning

## 정의

Fine-tuning은 사전 학습된 [[LLM]]의 [[Weight]]를 추가 학습하여 특정 작업이나 도메인에 적응시키는 과정이다.

## [[RAG]]과의 차이

| 구분 | [[RAG]] | [[FineTuning]] |
|------|---------|-----------------|
| 변경 대상 | 입력 [[Context]] | 모델 [[Weight]] |
| 비용 | 낮음 | 높음 |
| 업데이트 주기 | 문서만 | 재학습 필요 |
| 최신 정보 | ✅ 즉시 | ❌ |
| 패턴 학습 | ❌ | ✅ |

## 종류

- **Full fine-tuning**: 전체 weight 학습
- **[[PEFT]]**: [[LoRA]] 등 일부 파라미터만 학습
- **[[SupervisedFineTuning]]**: Supervised Fine-Tuning
- **[[RLHF]]**: Reinforcement Learning from Human Feedback

## 언제 사용하나

- 특정 스타일이나 톤 학습 필요
- 반복되는 특정 형식 작업
- [[RAG]]로 해결하기 어려운 패턴 학습

## 연관 개념

- [[RAG]] — 비교 대상
- [[Weight]] — 학습 대상
- [[PEFT]], [[LoRA]] — 효율적 fine-tuning
- [[SupervisedFineTuning]], [[RLHF]] — fine-tuning 기법

## 출처

- [[2026-05-21-day29-ai-ml-learning-review]]
- [[2026-05-20-day28-ai-ml-learning-review]]
