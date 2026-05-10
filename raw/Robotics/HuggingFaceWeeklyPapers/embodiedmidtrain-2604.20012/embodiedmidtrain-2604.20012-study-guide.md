---
source_url: https://arxiv.org/abs/2604.20012
paper_id: "2604.20012"
title: "EmbodiedMidtrain study guide"
created: 2026-05-10
topic: ["VLA", "VLM", "robotics", "study guide", "mid-training"]
---

# EmbodiedMidtrain 학습 자료

## 1. 한 문장 요약

EmbodiedMidtrain은 일반 VLM 데이터 중 VLA/robot manipulation 분포에 가까운 샘플을 proximity estimator로 골라 mid-training함으로써, downstream VLA fine-tuning의 초기값을 더 좋게 만드는 방법입니다.

## 2. 먼저 알아야 할 배경

### VLM
VLM은 image/video와 text를 함께 이해하는 모델입니다. captioning, VQA, OCR, document understanding 같은 task에 강합니다. 하지만 이런 능력이 곧바로 robot action으로 이어지지는 않습니다.

### VLA
VLA는 vision, language, action을 연결합니다. 입력은 camera observation과 language instruction이고, 출력은 robot action입니다. 일반 VLM보다 physical state, spatial relation, affordance, temporal action sequence가 중요합니다.

### Mid-training
Pretraining과 downstream fine-tuning 사이에 한 번 더 domain-adaptive training을 넣는 단계입니다. 이 논문에서는 VLM을 VLA에 더 잘 맞는 초기값으로 만들기 위해 mid-training을 사용합니다.

### Data distribution gap
두 데이터 분포가 다르면 같은 모델이라도 한쪽에서 배운 representation이 다른 쪽 task에 잘 맞지 않을 수 있습니다. 이 논문은 VLM data와 VLA data가 representation space에서 실제로 떨어져 있음을 MMD와 t-SNE로 보입니다.

## 3. 핵심 알고리즘

1. VLM data pool과 VLA target data를 준비합니다.
2. frozen VLM으로 각 샘플의 hidden feature를 뽑습니다.
3. VLA 샘플은 positive, VLM 샘플은 negative로 두고 binary classifier를 학습합니다.
4. classifier의 sigmoid output을 proximity score로 사용합니다.
5. VLM pool의 모든 샘플을 score로 정렬하고 top-K를 고릅니다.
6. 이 selected VLM data로 VLM을 mid-training합니다.
7. mid-trained VLM을 VLA backbone으로 초기화하고 action decoder와 함께 fine-tuning합니다.
8. Calvin, SimplerEnv, LIBERO에서 downstream action 성능을 봅니다.

## 4. 수식 직관

### MMD
MMD는 두 distribution P, Q가 feature space에서 얼마나 다른지 측정합니다. kernel을 써서 P 내부 유사도, Q 내부 유사도, P-Q cross 유사도를 비교합니다. VLM-VLA cross MMD가 크면 두 데이터 분포가 많이 다르다는 뜻입니다.

### Proximity score
이상적으로는 `p_VLA(x) / p_VLM(x)`가 높은 샘플을 고르고 싶습니다. 즉 VLM pool 안의 샘플 중에서도 VLA distribution에서 나왔을 법한 샘플을 고르는 것입니다. 직접 density ratio를 추정하기 어렵기 때문에, 논문은 domain classifier의 출력 `s(x)`를 proximity score로 사용합니다.

## 5. 실험 결과를 읽는 법

중요한 비교는 baseline VLM과 `+ EmbodiedMidtrain`입니다.

- InternVL3.5-1B: Calvin 3.173 → 3.714, Simpler 36.5 → 56.3, LIBERO 39.0 → 54.2
- Qwen3VL-2B: Calvin 3.205 → 3.584, Simpler 38.5 → 45.8, LIBERO 33.8 → 40.2

이 수치는 mid-training data selection이 실제 action success로 이어졌음을 보여줍니다.

## 6. 자주 헷갈리는 포인트

### Q1. 왜 그냥 embodied data만 쓰지 않나?
Embodied data만 쓰면 domain alignment는 좋아질 수 있지만 diversity가 줄어들 수 있습니다. 논문은 general VLM data와 embodied-oriented data를 모두 후보로 두고 sample-level로 고릅니다.

### Q2. proximity estimator가 학습한 것은 정확히 무엇인가?
정확히는 "이 sample의 frozen VLM representation이 VLA target data와 비슷한가"입니다. 이는 action label을 직접 예측하는 것이 아니라, VLA-like data membership을 예측하는 것입니다.

### Q3. training loss가 비슷한데 왜 성능이 다른가?
loss는 train distribution에서의 next-token/action prediction 품질을 제한적으로 반영합니다. VLA task success는 spatial grounding, temporal consistency, action robustness 같은 요소에 민감하므로, loss가 비슷해도 실제 성공률은 다를 수 있습니다.

### Q4. 이 방법은 real robot에도 바로 적용 가능한가?
논문은 simulation benchmark 중심입니다. real robot에서는 sensor noise, dynamics mismatch, safety constraints가 더 크므로 추가 검증이 필요합니다. 하지만 target robot data가 조금이라도 있다면, 그 distribution에 맞는 VLM sample selection에는 활용 가능성이 있습니다.

## 7. 실습 아이디어

### 실습 1: 간단한 proximity estimator 만들기
- CLIP 또는 SigLIP feature extractor를 frozen으로 둡니다.
- 일반 image-text 데이터와 robot/spatial 데이터 일부를 준비합니다.
- logistic regression으로 domain classifier를 학습합니다.
- top-score sample을 눈으로 확인해 spatial/embodied sample이 많이 나오는지 봅니다.

### 실습 2: selection 전후 데이터 분포 보기
- feature를 t-SNE/UMAP으로 2D에 투영합니다.
- 전체 VLM pool, selected VLM subset, VLA target data를 함께 그립니다.
- selected subset이 VLA 쪽으로 이동하는지 확인합니다.

### 실습 3: ablation 재현
- random selection
- nearest-neighbor distance selection
- learned classifier selection
세 방법으로 selected set을 만들고 downstream proxy task 성능을 비교합니다.

## 8. 복습 질문

1. EmbodiedMidtrain이 해결하려는 VLM-VLA gap은 무엇인가요?
2. 왜 dataset-level selection보다 sample-level selection이 중요한가요?
3. proximity estimator의 positive/negative sample은 각각 무엇인가요?
4. MMD와 t-SNE 분석이 논문 주장에 어떤 근거를 제공하나요?
5. InternVL3.5-1B 결과에서 EmbodiedMidtrain이 준 성능 향상은 어떤 의미가 있나요?
6. training loss가 비슷한데 downstream 성능이 다를 수 있는 이유는 무엇인가요?
7. 이 방법을 autonomous driving 또는 edge robotics에 적용한다면 어떤 data를 positive target으로 둘 수 있을까요?

## 9. 정답/설명

1. 일반 VLM은 captioning/VQA/document understanding 중심 데이터로 학습되지만, VLA는 physical interaction과 action trajectory가 필요한 robot manipulation 데이터로 학습됩니다. 이 둘의 representation distribution이 달라 downstream VLA fine-tuning의 출발점이 어긋나는 문제가 VLM-VLA gap입니다.
2. 같은 데이터셋 안에서도 embodied task에 가까운 샘플과 먼 샘플이 섞여 있습니다. dataset 전체를 고르면 불필요한 text-centric/VQA 샘플도 같이 들어가므로, sample 단위 score가 더 정밀합니다.
3. positive는 target VLA 데이터, negative는 candidate VLM pool의 샘플입니다. classifier는 frozen VLM feature가 VLA-like인지 예측합니다.
4. MMD는 VLM/VLA 데이터가 정량적으로 떨어져 있음을 보여주고, t-SNE는 VLA 데이터가 compact cluster로 분리되어 있음을 시각적으로 보여줍니다. 동시에 일부 VLM sample이 VLA 근처에 있음을 보여 selection 가능성을 제공합니다.
5. 작은 1.1B backbone도 VLA-aligned mid-training을 거치면 훨씬 큰 backbone과 경쟁할 수 있음을 뜻합니다. 이는 robotics에서 data alignment가 model scale만큼 중요하다는 근거입니다.
6. loss는 학습 데이터에 대한 평균적 예측 오류일 뿐, 실제 robot task success에 필요한 spatial grounding, action robustness, long-horizon consistency를 충분히 반영하지 못할 수 있습니다.
7. autonomous driving이라면 closed-loop driving log, planning trajectory, BEV/occupancy scene, driving QA 데이터를 positive target으로 둘 수 있습니다. edge robotics라면 실제 target robot의 teleoperation/demo data나 affordance-labeled data를 positive로 둘 수 있습니다.

## 10. 더 읽을 거리

- VLM4VLA: 여러 VLM backbone을 VLA setting에서 비교하는 기반 작업
- OpenVLA / π0 / GR00T: 범용 VLA/robot foundation model 흐름
- RefSpatial / RoboPoint / Robo2VLM: embodied/spatial VLM data
- Target-guided data selection for LLM pretraining: downstream domain에 맞춰 corpus를 고르는 방법론

