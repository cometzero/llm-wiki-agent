---
title: "Xiaomi-Robotics-1 학습 노트: VLA scaling과 action grounding"
type: source
tags: [robotics, vla, vision-language-action, scaling, state-transition, action-grounding]
date: 2026-07-22
last_updated: 2026-07-22
source_url: "https://arxiv.org/html/2607.15330"
hf_url: "https://huggingface.co/papers/2607.15330"
arxiv_id: "2607-15330"
arxiv_url: "https://arxiv.org/abs/2607-15330"
pdf_url: "https://arxiv.org/pdf/2607-15330"
week: "2026-W30"
selected_reason: "Xiaomi-Robotics-1의 데이터-모델-사후 정렬 설계를 action grounding/자율주행 전환 관점에서 학습 정리하기 위해 선정"
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W30/xiaomi-robotics-1-scaling-vla-2607-15330/learning.md
source_hash: 5970d80d8a5ed260
---

## Summary
[[Xiaomi-Robotics-1]]는 UMI 기반의 100K+ 시간 robot 조작 궤적을 축적하고, 이를 
[[StateTransitionCaptioning]]으로 변환해 [[Qwen3-VL]] + [[DiT]] 기반 
[[DiffusionTransformer]] 파이프라인에 넣어 [[ActionChunking]]을 학습하는 방식의 VLA 스케일링 연구를 정리한다.
이 노트는 핵심 수식, 단계별 구성, 실험 관점, AD 전이 제안까지 학습자 관점에서 압축해 action grounding과 scaling transfer의 실무 요점을 정리한다.

## Key Claims
- [[UMI]]는 실제 로봇 하드웨어 없이도 대규모 조작 데이터(100K+시간)를 확보해 VLA 사전학습 비용을 낮추는 실용적 경로를 제시한다.
- State 설명 기반 캡션(
"state-transition description")은 단순 task label보다 액션 생성의 grounding 신호로 더 직접적이다.
- [[Qwen3-VL]]은 관측/언어 인코딩 백본으로 작동하고, [[DiT]]는 
[[FlowMatching]]/flow-matching 기반의 연속 [[ActionChunk]]를 생성한다.
- Pre-train과 post-train을 분리한 이중 단계에서, pre-training은 trajectory prior를, post-training은 embodiment/언어 조건 정합을 담당한다.
- 실험 축은 open-loop 지표뿐 아니라 closed-loop 실환경/시뮬레이션 성공률로 scaling 효과의 과도기 전이를 강조한다.
- 자율주행 전이 관점에서는 task label을 "상태-장면 변화/경로 의도/안전 제약" 조건으로 바꿔 적용할 수 있다.

## Key Quotes
> "task label is about what to do, state-transition caption is about what state must change" — 학습 노트 핵심 요약 해석

> "flow matching을 이용한 action chunk는 긴 시퀀스 제어의 안정성-효율성 절충을 개선" — action chunk 설계 근거 요약

## Step-by-step 요약

### Step 1. 데이터 확장
- 조작 데이터의 비용 장벽을 낮추기 위해 [[UMI]]로 실제 human-taught trajectory를 대량 수집.

### Step 2. Supervision 정렬
- trajectory segment를 잘라 고정 길이 문장으로 분할 후 
  [[Qwen3-VL|Qwen3.5-27B]] 기반 caption을 통해 state transition 기술.
- "gripper가 컵 손잡이를 잡고 컵을 오른쪽 접시로 이동"처럼 동작 이전/이후 상태 변화를 서술.

### Step 3. 모델 본체
- 비전+언어는 [[Qwen3-VL]], 행동 분기는 [[DiT]] + [[KVCache]] 조건을 통해 연속 액션 블록을 생성.
- action chunk는 한 번에 여러 스텝을 출력해 폐쇄루프 재호출 비용을 줄이는 구조.

### Step 4. Cross-embodiment 정합
- UMI 사전학습 분포를 mobile arm, dual-arm, static arm, instruction-conditioned 환경으로 정렬.
- [[CrossEmbodimentLearning]]은 데이터-모델 갭뿐 아니라 인터페이스/상태 표현 차이를 맞추는 목적이 핵심.

### Step 5. AD로의 전환
- 자율주행 대응에서는 state-transition caption을 
  scene evolution, route intent, safety constraint로 바꿔 사용해야 한다.
- waypoint/trajectory generator 자체보다 closed-loop safety verifier(충돌/안전 제약·latency)가 선행되어야 한다.

## 핵심 수식
- 논문 문맥의 핵심식은 기본적으로 flow matching의 방향장(velocity field) 회귀 형식을 따른다:

\[
L_{Flow}(\theta)=\lVert v_\theta(o_t,l,s_t,\tilde{a}^{\tau}_{t:t+H},\tau)-u(\tilde{a}^{\tau}_{t:t+H},a_{t:t+H},\tau)\rVert_2^2
\]

여기서 언어 상태 설명은 조건 벡터로 들어가며, action chunk가 robot state와 함께 정렬되도록 만든다.

## 실무 체크리스트(학습 관점)
- trajectory 분포 편향이 큰지(상대적으로 open-world coverage) 점검
- auto-label 문장 질(잡음) 측정 및 필터링 규칙 도입
- closed-loop success를 open-loop MSE보다 우선 확인
- post-training 데이터에서 embodiment 불일치 케이스 구분
- safety/latency/불확실성 지표를 별도 집계

## Connections
- [[Xiaomi-Robotics-1]] — 이 노트의 핵심 대상.
- [[UMI]] — 대규모 trajectory 수집 인터페이스.
- [[Qwen3-VL]] — multimodal backbone.
- [[FlowMatching]] — action flow-matching 학습 토대.
- [[DiffusionTransformer]] — action chunk 생성 구조 정합.
- [[StateTransitionCaptioning]] — 본 노트의 핵심 감독 설계.
- [[ActionGrounding]] — 실무 목표: instruction과 제어의 직접 접속.
- [[CrossEmbodimentLearning]] — UMI 중심 사전학습과 실제 robot 정합의 핵심.
- [[ClosedLoopEvaluation]], [[RoboCasa365]], [[RoboDojo]] — 성능 이전 검증 축.
- [[AutonomousDrivingVLA]] — state-transition grounding을 scene/route planning으로 치환 가능.

## Contradictions
- 기존 출처의 요약과 직접 충돌되는 내용은 확인되지 않았다. 다만 실험에서 제시된 safety/uncertainty 지표 부족은 해당 소스군의 공통한 한계 설명으로 기존 [[OpenLoopMSE]]/폐쇄루프 논점과 일치한다.
