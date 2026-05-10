---
source_url: https://arxiv.org/abs/2604.20012
html_url: https://arxiv.org/html/2604.20012
pdf_url: https://arxiv.org/pdf/2604.20012
hf_url: https://huggingface.co/papers/2604.20012
paper_id: "2604.20012"
title: "EmbodiedMidtrain: Bridging the Gap between Vision-Language Models and Vision-Language-Action Models via Mid-training"
authors: ["Yiyang Du", "Zhanqiu Guo", "Xin Ye", "Liu Ren", "Chenyan Xiong"]
created: 2026-05-10
topic: ["VLA", "VLM", "robotics", "embodied AI", "mid-training", "data selection"]
---

# EmbodiedMidtrain: VLM과 VLA 사이의 간극을 Mid-training으로 잇기

## 0. 왜 이 논문을 골랐나

이번 Hugging Face Weekly 후보 중 `2604.20012`는 VLA(Vision-Language-Action)와 VLM(Vision-Language Model)을 직접 연결하는 논문입니다. 기존 VLA 연구는 큰 VLM을 backbone으로 가져와 robot action head를 붙이고 fine-tuning하는 방식이 많았지만, 이 논문은 "VLM pretraining 데이터 분포 자체가 VLA/robot manipulation 분포와 다르다"는 문제를 먼저 측정한 뒤, VLA와 가까운 VLM 샘플만 골라 mid-training하는 data engine을 제안합니다.

핵심 메시지는 간단합니다.

- VLA 성능은 단순히 VLM 크기나 pretraining 양만으로 결정되지 않습니다.
- robot manipulation에 가까운 spatial/embodied VLM 샘플을 선별해 mid-training하면, 더 작은 backbone도 큰 VLM/VLA baseline과 경쟁할 수 있습니다.
- 학습 loss가 비슷해도 downstream VLA 성능은 크게 달라질 수 있으므로, representation alignment가 중요합니다.

## 1. 메타데이터

- 논문: EmbodiedMidtrain: Bridging the Gap between Vision-Language Models and Vision-Language-Action Models via Mid-training
- arXiv: 2604.20012
- 제출일: 2026-04-21
- 저자: Yiyang Du, Zhanqiu Guo, Xin Ye, Liu Ren, Chenyan Xiong
- 프로젝트 페이지: https://adu2021.github.io/blog/EmbodiedMidtrain/
- 주제 분류: VLA, embodied AI, robotics foundation model, data selection, mid-training

## 2. 초록 번역

VLA(Vision-Language-Action Model)는 VLM(Vision-Language Model)으로부터 시각 및 언어 능력을 물려받습니다. 하지만 대부분의 VLA는 embodied domain에 맞게 조정되지 않은 off-the-shelf VLM에서 출발하기 때문에 downstream 성능이 제한됩니다. 이 논문은 VLM과 VLA 사이의 간극을 줄이기 위해 EmbodiedMidtrain을 제안합니다.

저자들은 먼저 VLM 데이터와 VLA 데이터 사이의 분포 차이를 분석합니다. VLA 데이터는 더 작고 조밀한 영역에 모여 있으며, 넓게 퍼진 VLM 데이터 분포와 상당히 분리되어 있습니다. 동시에 VLM 데이터 내부에서도 VLA와 가까운 샘플과 먼 샘플이 섞여 있어, 정렬(alignment) 정도는 데이터셋 사이뿐 아니라 같은 데이터셋 내부에서도 크게 다릅니다.

이를 바탕으로 저자들은 lightweight learnable proximity estimator를 사용하는 mid-training data engine을 만듭니다. 이 estimator는 큰 VLM 후보 풀에서 VLA에 더 가까운 샘플을 골라내고, 이 curated mixture로 VLM을 mid-training한 뒤 VLA fine-tuning을 수행합니다.

세 가지 robot manipulation benchmark 실험에서 이 방식은 여러 VLM backbone에 걸쳐 일관되게 성능을 높였습니다. 더 큰 모델과 더 많은 학습 예산을 사용한 expert VLA 또는 off-the-shelf VLM baseline과도 경쟁 가능한 결과를 냈습니다. 추가 분석에서는 mid-training이 VLA fine-tuning의 더 좋은 초기값(initialization)을 제공하며, 이 이득이 fine-tuning 초반부터 나타나고 학습이 진행될수록 커진다는 점을 보였습니다.

## 3. 절별 원문 번역/해설

### 3.1 Introduction

최근 robotics foundation model 연구는 vision perception, language understanding, action generation을 하나의 모델 안에서 통합하는 VLA를 발전시켰습니다. 대부분의 VLA는 VLM을 backbone으로 사용하므로, VLM이 가진 풍부한 시각/언어 표현을 embodied setting으로 빠르게 이전할 수 있습니다.

하지만 근본적인 간극이 있습니다. 일반 VLM pretraining은 captioning, VQA, document understanding 같은 broad vision-language task에 맞춰져 있는 반면, VLA training은 물리적 상호작용에 grounding된 robot manipulation trajectory를 다룹니다. 따라서 VLM backbone이 언어와 시각 이해에는 강하더라도, action generation에 필요한 embodied reasoning에는 잘 맞지 않을 수 있습니다.

EmbodiedMidtrain은 이 문제를 data distribution 관점에서 접근합니다. VLA 데이터는 VLM 데이터 전체와 비교하면 더 compact하고 분리된 cluster를 이루며, VLM 데이터 중 일부만 VLA에 가까운 곳에 있습니다. 따라서 모든 VLM 데이터를 무차별적으로 mid-training에 쓰는 대신, VLA domain에 가까운 VLM 샘플을 선별해 VLM을 한 번 더 적응시키는 것이 핵심입니다.

![Figure 1: EmbodiedMidtrain overview](figures/S1.F1-1.png)
![Figure 1 component](figures/S1.F1-2.png)
![Figure 1 component](figures/S1.F1-3.png)
![Figure 1 component](figures/S1.F1-4.png)

### 3.2 Related Work

논문은 세 흐름 위에 서 있습니다.

1. VLA: VLM이나 LLM을 확장해 robot action을 생성하는 모델 계열입니다. OpenVLA, π0, GR00T 같은 모델이 대표적입니다.
2. VLM mid-training: 일반 VLM은 pretraining 후 instruction tuning이나 task-specific adaptation을 거칩니다. 이 논문은 그 중간 단계를 embodied domain에 맞춰 설계합니다.
3. Embodied-oriented VLM: spatial understanding, affordance, robot-centric VQA 등을 강화하려는 데이터셋과 benchmark가 늘고 있습니다. EmbodiedMidtrain은 이런 데이터와 일반 VLM 데이터를 섞되, VLA와 가까운 샘플을 sample-level로 고르는 방식을 제안합니다.

### 3.3 VLM-VLA 데이터 분포 간극

저자들은 VLM/VLA 데이터를 같은 representation space에 올려놓고 비교합니다. 각 샘플은 VLM의 마지막 hidden state로 표현되고, 데이터셋 간 거리는 MMD(Maximum Mean Discrepancy)로 측정합니다. MMD는 두 분포가 얼마나 다른지를 kernel mean embedding 관점에서 재는 비모수 거리입니다.

분석 결과는 두 가지입니다.

- VLM 데이터 내부끼리, VLA 데이터 내부끼리는 상대적으로 가깝지만, VLM-VLA 사이의 cross-group distance는 더 큽니다.
- t-SNE 시각화에서도 VLA 데이터는 조밀한 cluster를 이루며, 넓고 다양한 VLM 데이터 분포에서 분리되어 있습니다.

다만 간극은 binary가 아닙니다. 일부 VLM 데이터셋/샘플은 VLA 데이터에 꽤 가깝습니다. 그래서 논문은 "VLM 전체가 VLA와 멀다"가 아니라, "VLM 내부에 VLA와 가까운 sample이 섞여 있으니 그것을 골라야 한다"는 방향으로 갑니다.

![Figure 2a: MMD matrix](figures/S3.F2-1.png)
![Figure 2b: t-SNE distribution](figures/S3.F2-2.png)

### 3.4 EmbodiedMidtrain data engine

EmbodiedMidtrain의 data engine은 두 조건을 만족하려고 합니다.

1. diversity 보존: general VLM data와 embodied-oriented VLM data를 모두 후보로 두어 일반 시각/언어 능력을 잃지 않게 합니다.
2. sample-level selection: 같은 dataset 안에서도 VLA에 가까운 샘플과 먼 샘플이 섞여 있으므로 dataset 단위가 아니라 sample 단위로 고릅니다.

방법은 domain-membership classifier에 가깝습니다. Frozen VLM feature 위에 lightweight classifier를 얹고, VLA 샘플을 positive, VLM 샘플을 negative로 두어 binary classification을 학습합니다. 학습된 classifier의 sigmoid score를 proximity score로 사용합니다. score가 높은 VLM 샘플은 VLA 분포에 더 가까운 샘플로 간주하고, top-K를 골라 mid-training corpus를 구성합니다.

수식으로 보면 이상적인 목표는 VLM 후보 pool에서 크기 K인 subset을 골라 그 subset의 분포가 VLA 분포와 가장 가깝게 만드는 것입니다. 직접 최적화하기 어렵기 때문에, density ratio 또는 domain membership score를 근사하는 per-sample scoring 문제로 바꿉니다.

중요한 점은 이 방식이 architecture를 바꾸지 않는다는 것입니다. VLM과 VLA 구조는 그대로 두고, 어떤 VLM data로 mid-training할지 선택하는 layer만 추가합니다.

### 3.5 실험 설정

후보 VLM 데이터는 두 범주로 구성됩니다.

- General VLM data: LAION-400M subset, CC-12M, LLaVA-Instruct-665k, VCR 등 일반 vision-language 학습 데이터
- Embodied-oriented VLM data: RefSpatial, EmbSpatial-Bench, Robo2VLM, RoboPoint 등 spatial grounding, affordance, robotic VQA에 가까운 데이터

Target VLA 데이터는 downstream VLA fine-tuning에 쓰이는 training data mixture에서 가져와 proximity estimator 학습에 사용합니다. estimator가 validation accuracy 90%에 도달하면 early stopping을 적용해 과적합을 막습니다.

Mid-training은 InternVL3.5-1B와 Qwen3VL-2B backbone에 적용합니다. 이후 VLM4VLA pipeline을 따라 VLA로 fine-tuning하며, VLM backbone 뒤에 continuous arm action과 binary gripper action을 예측하는 two-branch MLP action decoder를 붙입니다.

평가는 세 benchmark에서 진행됩니다.

- Calvin ABC-D: ABC split으로 학습하고 unseen D split에서 1,000개의 5-subtask sequence를 평가합니다.
- SimplerEnv-Bridge: real-to-sim tabletop manipulation benchmark입니다.
- LIBERO-10: long-horizon manipulation task 10개로 구성된 어려운 suite입니다.

### 3.6 주요 결과

proximity-based mid-training은 세 benchmark 모두에서 일관된 성능 향상을 보입니다.

대표 수치:

- InternVL3.5-1B baseline: Calvin average length 3.173, Simpler 36.5, LIBERO 39.0
- InternVL3.5-1B + EmbodiedMidtrain: Calvin average length 3.714, Simpler 56.3, LIBERO 54.2
- Qwen3VL-2B baseline: Calvin average length 3.205, Simpler 38.5, LIBERO 33.8
- Qwen3VL-2B + EmbodiedMidtrain: Calvin average length 3.584, Simpler 45.8, LIBERO 40.2

특히 1.1B급 InternVL3.5-1B + EmbodiedMidtrain은 더 큰 off-the-shelf VLM 일부와 경쟁하거나 앞섭니다. 논문의 해석은 "pretraining data를 얼마나 많이 봤는가"보다 "downstream embodied distribution과 얼마나 잘 맞는 data로 적응했는가"가 중요하다는 것입니다.

또 하나 중요한 결과는 cross-backbone transferability입니다. InternVL3.5-1B feature space에서 고른 mid-training data를 Qwen3VL-2B에도 적용했는데, Qwen3VL-2B에서도 성능이 개선되었습니다. 즉 proximity score가 특정 backbone의 artifact만은 아니며, VLA에 가까운 sample의 일반적 특성을 어느 정도 포착한다는 뜻입니다.

### 3.7 Ablation

논문은 random selection과 여러 proximity metric을 비교합니다.

- Random selection: Calvin 3.398, Simpler 43.8, LIBERO 48.4
- Feature-space average distance: Calvin 3.126, Simpler 53.1, LIBERO 51.2
- VLA-conditioned perplexity: Calvin 3.159, Simpler 55.2, LIBERO 48.0
- Delta perplexity: Calvin 1.527, Simpler 39.6, LIBERO 54.2
- Learned estimator: Calvin 3.714, Simpler 56.3, LIBERO 54.2

결론은 명확합니다. 단순히 mid-training을 더 하는 것만으로는 충분하지 않고, VLA-aligned sample을 잘 고르는 것이 중요합니다. 또한 hand-crafted metric보다 learned estimator가 더 안정적입니다.

### 3.8 Training dynamics

fine-tuning 중간 checkpoint를 비교하면, EmbodiedMidtrain을 거친 모델은 학습 초반부터 더 높은 downstream 성능을 보입니다. 이 차이는 시간이 지나도 사라지지 않고 오히려 벌어집니다.

흥미로운 점은 training loss가 두 initialization 사이에서 크게 다르지 않다는 것입니다. 즉 loss만 보면 비슷하게 학습되는 것처럼 보여도, 실제 robot task success는 크게 달라질 수 있습니다. 이 결과는 VLA에서 좋은 initialization의 품질을 판단할 때 training loss만으로는 부족하고, embodied benchmark 성능을 직접 봐야 함을 시사합니다.

### 3.9 선택된 VLM 데이터 분석

proximity estimator는 dataset-level preference와 sample-level preference를 동시에 보입니다. RefSpatial은 높은 평균 score를 받았고, VCR은 낮은 score를 받았습니다. 하지만 같은 dataset 안에서도 score 분포가 넓기 때문에, 단순히 dataset 전체를 선택하는 것이 아니라 sample-level top-K가 필요합니다.

높은 score를 받은 예시는 좌표, 방향, 위치 관계를 이해해야 하는 spatial grounding task입니다. 낮은 score 예시는 책 표지의 텍스트를 읽는 VQA처럼 embodied manipulation과 거리가 먼 task입니다. 따라서 estimator는 "시각 정보를 언어로 답하는 능력" 전체가 아니라, robot action에 전이될 가능성이 큰 spatial/embodied reasoning 패턴을 선호합니다.

![Figure 4 positive sample](figures/S6.F4-1.jpg)
![Figure 4 negative sample](figures/S6.F4-2.jpg)
![Figure 5 proximity shift](figures/S6.F5-1.png)

### 3.10 Conclusion

EmbodiedMidtrain은 VLM과 VLA 사이의 데이터 분포 차이를 proximity-based data selection으로 줄이는 mid-training pipeline입니다. frozen VLM feature 위에서 학습한 lightweight estimator가 VLA domain과 가까운 VLM 샘플을 찾아내고, 그 샘플로 VLM을 mid-training한 뒤 VLA fine-tuning을 수행합니다.

세 manipulation benchmark에서 이 방식은 일관되게 성능을 개선했고, 더 큰 모델/더 많은 학습 예산을 사용한 baseline과 경쟁했습니다. 또한 selected data가 다른 VLM backbone에도 전이되어, embodied alignment signal이 특정 모델에만 묶여 있지 않음을 보여줍니다.

## 4. 내 해석: 왜 중요한가

### 4.1 VLA는 "큰 VLM + action head"만으로 충분하지 않다

VLA 연구에서는 종종 큰 VLM을 가져와 action decoder를 붙이면 일반화가 좋아질 것이라는 기대가 있습니다. 이 논문은 그 기대를 부분적으로 반박합니다. 큰 VLM은 강력한 출발점이지만, pretraining distribution이 document/VQA/captioning 중심이면 robot action에 필요한 spatial grounding과 physical affordance와는 거리가 있습니다.

### 4.2 데이터 선별이 모델 스케일을 대체할 수 있다

InternVL3.5-1B처럼 작은 model도 VLA-aligned mid-training을 거치면 더 큰 VLM들과 경쟁할 수 있습니다. 이는 robotics에서는 model scale만 키우는 것보다 data distribution alignment가 비용 대비 효과적인 전략일 수 있음을 의미합니다.

### 4.3 NPU/edge 관점에서도 의미가 있다

로봇이나 차량에 들어가는 모델은 inference cost, latency, memory 제약을 강하게 받습니다. 작은 backbone을 잘 맞는 data로 mid-training해 성능을 끌어올릴 수 있다면, edge deployment나 NPU target에서도 실용적입니다. 즉 이 논문은 VLA 성능 향상뿐 아니라 on-device robotics model 설계에도 연결됩니다.

### 4.4 한계와 주의점

- 평가가 simulated manipulation benchmark 중심입니다. 실제 robot deployment에서 같은 폭의 성능 향상이 유지되는지는 추가 검증이 필요합니다.
- proximity estimator는 target VLA training distribution을 필요로 합니다. 완전히 새로운 robot/domain으로 갈 때는 target data가 얼마나 있어야 충분한지 명확하지 않습니다.
- top-K selection은 다양성과 alignment 사이의 trade-off가 있습니다. 너무 강하게 VLA-like sample만 고르면 VLM의 일반 시각/언어 능력이 줄어들 수 있습니다.
- safety, failure recovery, long-horizon planning에 대한 분석은 제한적입니다.

## 5. llm-wiki 연결 포인트

- [[VLA]]: VLM representation을 action generation으로 연결하는 모델 계열
- [[VLM]]: VLA backbone으로 쓰이지만, 일반 VLM pretraining 분포와 embodied action 분포 사이에는 간극이 있음
- [[EmbodiedAI]]: physical interaction과 spatial grounding이 중요한 학습 영역
- [[DataSelection]]: pretraining/mid-training corpus를 downstream distribution에 맞추는 방법
- [[RobotManipulation]]: Calvin, SimplerEnv, LIBERO 같은 benchmark에서 성능 검증
- [[EdgeAI]]: 작은 backbone을 domain-aligned data로 강화하는 전략은 edge/NPU 배포와도 연결됨

## 6. 그림 목록

- Figure 1: EmbodiedMidtrain overview — `figures/S1.F1-*.png`
- Figure 2: VLM/VLA distribution analysis — `figures/S3.F2-*.png`
- Figure 4: selected VLM data examples — `figures/S6.F4-*.jpg`
- Figure 5: proximity score distribution shift — `figures/S6.F5-1.png`

