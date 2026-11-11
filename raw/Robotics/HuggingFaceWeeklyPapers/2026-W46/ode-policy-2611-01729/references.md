---
title: "ODE Policy 참고문헌 지도: ODE·Generative Policy·VLA/WAM·Benchmark"
source_url: "https://arxiv.org/html/2611.01729v1"
hf_url: "https://huggingface.co/papers/2611.01729"
arxiv_id: "2611.01729"
arxiv_url: "https://arxiv.org/abs/2611.01729"
pdf_url: "https://arxiv.org/pdf/2611.01729"
week: "2026-W46"
ingested_at_kst: "2026-11-11T09:46:49+09:00"
selected_reason: "현재 주 후보 중 action dynamics·VLA/WAM action head·실물 제어를 직접 다루는 고관련 신규 논문; ID와 distinctive title의 raw/wiki 중복 없음"
original_title: "ODE Policy: Robot Learning via Action Dynamics, Not Actions"
authors: ["Jindou Jia", "Jingliang Li", "Kuangji Zuo", "Tuo An", "Yuxuan Hu", "Mengfei Zhao", "Bofan Lyu", "Jiaqi Bai", "Daoyuan Zhu", "Hengyu Dai", "Junpeng Zhang", "Jianfei Yang"]
source_version: "2611.01729v1"
source_license: "arXiv perpetual non-exclusive distribution license"
document_policy: "독자적인 한국어 기술 해설 및 분석; 원문 전체 번역이나 대체본 아님"
---

# ODE Policy 핵심 참고문헌 9편

Semantic Scholar의 `arXiv:2611.01729/references` endpoint를 조회해 82개 항목(추가 pagination 없음)을 받았습니다. 원문 bibliography와 본문에서 방법/평가에 연결되는 아래 9편을 선별했습니다. 외부 metadata는 논문 ID 확인에 사용하고, 관계 설명은 ODE Policy 본문을 기준으로 독자 작성했습니다. 각 참고문헌의 전문을 모두 새로 읽거나 재현한 자료가 아닙니다. 저자 initial을 추측으로 확장하지 않습니다.

## 1. Neural Ordinary Differential Equations (2018)

- [arXiv:1806.07366](https://arxiv.org/abs/1806.07366)
- 관계와 읽을 포인트: Neural ODE의 출발점. Network가 상태 변화율을 정의하고 solver가 path를 만든다는 관점을 제공합니다. ODE Policy는 이를 hidden/environment state가 아니라 commanded action에 적용합니다.

## 2. Neural Dynamic Policies for End-to-End Sensorimotor Learning (2020)

- [arXiv:2012.02788](https://arxiv.org/abs/2012.02788)
- 관계와 읽을 포인트: Neural Dynamic Policies는 sensor input으로 dynamical movement를 구성하는 선행 연구입니다. 고정된 dynamic 구조와 자유로운 learned vector field의 차이를 비교할 읽을거리입니다.

## 3. Diffusion policy: Visuomotor policy learning via action diffusion (2023)

- [arXiv:2303.04137](https://arxiv.org/abs/2303.04137)
- 관계와 읽을 포인트: Diffusion Policy는 conditional action chunk distribution을 iterative denoising으로 학습하는 대표 baseline입니다. Generation-time denoising과 physical-time command integration을 구분하는 대조점입니다.

## 4. Flow Matching for Generative Modeling (2022)

- [arXiv:2210.02747](https://arxiv.org/abs/2210.02747)
- 관계와 읽을 포인트: Flow Matching의 vector-field training은 noise-to-data transport를 다룹니다. ODE라는 공통 형식만으로 같은 policy라고 볼 수 없다는 점을 배우기 좋습니다.

## 5. π0.5: a Vision-Language-Action Model with Open-World Generalization (2025)

- [arXiv:2504.16054](https://arxiv.org/abs/2504.16054)
- 관계와 읽을 포인트: π0.5는 language-conditioned pretrained VLA backbone입니다. ODE Policy에서는 action expert를 교체하며 pretrained expert와 random-init expert를 따로 비교합니다.

## 6. ImageWAM: Do World Action Models Really Need Video Generation, or Just Image Editing? (2026)

- [arXiv:2606.19531](https://arxiv.org/abs/2606.19531)
- 관계와 읽을 포인트: ImageWAM은 future visual modeling과 action prediction을 결합하는 WAM 비교 기반입니다. ODE head가 큰 backbone의 adaptation과 inference cost에 미치는 영향을 확인합니다.

## 7. SuperMimic: Scaling Humanoid Whole-Body Control with One Differentiable World Model (2026)

- [arXiv:2610.28480](https://arxiv.org/abs/2610.28480)
- 관계와 읽을 포인트: SuperMimic은 differentiable world model을 통한 model-based humanoid control입니다. ODE actor 비교는 이 학습 알고리즘을 유지한 채 actor parameterization만 바꾸는 실험입니다.

## 8. LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning (2023)

- [arXiv:2306.03310](https://arxiv.org/abs/2306.03310)
- 관계와 읽을 포인트: LIBERO는 language-conditioned manipulation의 네 suite 평가 기반입니다. ODE Policy의 suite-average SR과 seed별 결과를 읽을 때 task 구성과 평가 초기조건을 확인해야 합니다.

## 9. LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (2025)

- [arXiv:2510.13626](https://arxiv.org/abs/2510.13626)
- 관계와 읽을 포인트: LIBERO-Plus는 distribution shift robustness를 다루는 benchmark입니다. In-distribution success와 camera/pose/noise shift 대응을 분리해 보는 데 필요합니다.

## 추천 순서
Neural ODE → Diffusion Policy/Flow Matching → π0.5/ImageWAM → SuperMimic → LIBERO/LIBERO-Plus 순으로 읽으면 representation·training·evaluation을 분리하기 쉽습니다. 기존 corpus에서 이미 분석된 문헌도 참고문헌으로만 연결하며 이번 주 신규 선정으로 세지 않습니다.
