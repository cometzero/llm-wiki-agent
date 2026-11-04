---
title: "OSWAM 핵심 참고문헌 9편: direct policy, structured flow, benchmark의 연결"
source_url: https://arxiv.org/html/2610.35850v1#bib
hf_url: https://huggingface.co/papers/2610.35850
arxiv_id: "2610.35850"
arxiv_url: https://arxiv.org/abs/2610.35850
pdf_url: https://arxiv.org/pdf/2610.35850
week: "2026-W45"
ingested_at_kst: "2026-11-04"
selected_reason: "OSWAM의 one-step action prior를 이해하는 직접 선행연구와 평가 근거를 분리해 학습"
---

# OSWAM 참고문헌 지도

## 수집 근거와 해석 범위

2026-11-04에 Semantic Scholar `paper/arXiv:2610.35850/references?fields=title,authors,year,url,externalIds&limit=100`에서 **59편**을 받았다. arXiv HTML bibliography의 **59개 항목**과 대조하여 아래 9편을 선택했다. 아래 설명은 OSWAM 본문에서 해당 연구를 어떻게 사용·비교하는지에 근거한 학습 메모이며, 9편의 전문을 모두 새로 정독·재현했다는 뜻은 아니다. 원문 author 표기를 우선하고 Semantic Scholar의 이름 normalization을 저자 신원의 추가 증거로 사용하지 않는다.

## 1. Fast-WAM — 직접적인 architecture 출발점

- Tianyuan Yuan, Zibin Dong, Yicheng Liu, Hang Zhao. **Fast-WAM: Do World Action Models Need Test-time Future Imagination?** (2026).
- [arXiv:2603.16666](https://arxiv.org/abs/2603.16666), DOI `10.48550/arXiv.2603.16666`. OSWAM bibliography [4].
- **요점:** video prediction을 학습의 representation objective로 남기고 추론에서 future rollout을 제거하는 direct-policy WAM이다.
- **OSWAM과의 관계:** Wan backbone, action expert 구성, first-frame-only interface를 이어받는다. Fast-WAM에는 multi-step action denoising이 남고 OSWAM은 AIT prior를 도입해 그 부분을 one-step으로 바꾼다.
- **읽을 질문:** 미래를 출력하지 않으면서도 video-generative pretraining의 지식이 action expert에 전달되는 경로는 무엇인가?

## 2. SimWAM — 자율주행의 가장 가까운 latency baseline

- Zongchuang Zhao et al. **SimWAM: A Simple World Action Model for End-to-End Autonomous Driving** (2026).
- [arXiv:2608.07468](https://arxiv.org/abs/2608.07468), DOI `10.48550/arXiv.2608.07468`. [11].
- **요점:** Fast-WAM의 direct-policy 설계를 E2E driving에 적용하여 test-time video rollout을 제거한다.
- **관계:** OSWAM의 single-front-camera driving 설정과 PDMS/latency 비교의 직접 기준이다. 원문 Table 1은 RL 제외 SimWAM을 사용한다. 10-step 90.3 PDMS/410ms와 one-step OSWAM 90.3/136ms를 비교한다.
- **주의:** one-step 별도 비교표, component-ablation baseline, RL 포함 결과를 섞지 않는다. 기존 wiki에 SimWAM 분석이 있어도 이번 새 논문의 참고문헌으로 인용하는 것은 중복 ingest가 아니다.

## 3. Flash-WAM — distillation만으로 줄이는 경로와 비교

- Arman Akbari et al. **Flash-WAM: Modality-Aware Distillation for World Action Models** (2026).
- [arXiv:2606.05254](https://arxiv.org/abs/2606.05254), DOI `10.48550/arXiv.2606.05254`. [17].
- **요점:** modality-aware distillation로 video/action generation step을 줄이는 효율화 계열이다.
- **관계:** OSWAM은 future video 생성이 남는 few-step approach와 달리 current-frame interface를 유지하고 action 초기화를 바꾼다. 원문 RoboTwin one-video/one-action variant 평균 81.41%와 OSWAM 90.00%의 차이를 논의한다.
- **읽을 질문:** sampler step 감소와 online future generation 제거는 왜 독립된 optimization 축인가?

## 4. Light-WAM — single-pass가 곧 충분한 성능은 아니다

- Ziang Li et al. **Light-WAM: Efficient World Action Models with State-Fusion Action Decoding** (2026).
- [arXiv:2606.08242](https://arxiv.org/abs/2606.08242), DOI `10.48550/arXiv.2606.08242`. [34].
- **요점:** generative action expert 대신 lightweight fusion head로 single-pass action prediction을 수행하는 대안이다.
- **관계:** OSWAM은 이 방식보다 RoboTwin 평균 성공률이 높지만 latency도 더 크다. H20 비교는 76.40%/107ms 대 90.00%/142ms다. 따라서 속도·정확도 Pareto frontier 관점으로 읽어야 한다.
- **질문:** action expert를 제거하는 것과 structured initial state에서 한 번 refine하는 것의 representation capacity 차이는 무엇인가?

## 5. Wan — physical prior의 backbone

- Team Wan et al. **Wan: Open and Advanced Large-Scale Video Generative Models** (2025).
- [arXiv:2503.20314](https://arxiv.org/abs/2503.20314), DOI `10.48550/arXiv.2503.20314`. [14].
- **요점:** 대규모 video generation backbone의 계보를 제공한다.
- **관계:** OSWAM의 구체적인 checkpoint는 Wan2.2-5B이며 T5/video VAE를 사용한다. Bibliography의 Wan 논문 ID를 Wan2.2 checkpoint revision 그 자체와 혼동하지 않는다.
- **질문:** pretrained video transformer를 policy에 사용할 때 어떤 weight는 유지하고 어떤 token/attention path를 적응해야 하는가?

## 6. Rectified Flow — velocity와 one-step update의 수학 배경

- Xingchao Liu, Chengyue Gong, Qiang Liu. **Flow Straight and Fast: Learning to Generate and Transfer Data with Rectified Flow** (2022 preprint).
- [arXiv:2209.03003](https://arxiv.org/abs/2209.03003), DOI `10.48550/arXiv.2209.03003`. [18].
- **요점:** distribution 사이의 transport를 velocity field로 학습하고 적은 수의 적분 step으로 생성하는 관점을 제공한다.
- **관계:** OSWAM은 action initialization ablation에서 rectified-flow refinement와 re-noising을 비교한다. OSWAM의 장점 전체가 일반적인 straight-flow 원리에서 자동으로 따라오는 것은 아니며, 본문의 residual-target/stop-gradient/noise contract를 따로 이해해야 한다.
- **질문:** $a_t=(1-t)a+t\epsilon$ convention에서 inference가 noise→data라면 update 부호는 왜 음수인가?

## 7. LoRA — imagination token을 위한 저비용 backbone 적응

- Edward J. Hu et al. **LoRA: Low-Rank Adaptation of Large Language Models** (2021 preprint).
- [arXiv:2106.09685](https://arxiv.org/abs/2106.09685), DOI `10.48550/arXiv.2106.09685`. [35].
- **요점:** pretrained weight의 update를 low-rank factorization으로 표현하는 적응 기법이다.
- **관계:** OSWAM은 새 AIT/SIT token을 Video DiT가 처리하도록 rank 8, alpha 4의 LoRA를 사용한다. LoRA 자체는 action prior나 physical reasoning objective가 아니며 추가 loss/attention mask와 함께 역할을 한다.
- **질문:** trainable parameter 감소가 model forward FLOP이나 peak activation memory 감소와 항상 같은가?

## 8. NAVSIM — 평가가 말할 수 있는 범위를 정하는 논문

- Daniel Dauner et al. **NAVSIM: Data-Driven Non-Reactive Autonomous Vehicle Simulation and Benchmarking** (2024).
- [arXiv:2406.15349](https://arxiv.org/abs/2406.15349), DOI `10.48550/arXiv.2406.15349`. [43].
- **요점:** recorded driving data 기반 non-reactive simulation으로 planner의 safety/progress/comfort를 평가한다.
- **관계:** OSWAM의 핵심 driving metric PDMS의 근거다. 단순 ground-truth trajectory L2보다 행동 품질을 더 다루지만 reactive agents와 상호작용하는 실차 closed-loop와 동일하지 않다.
- **질문:** 같은 PDMS일 때 collision tail, comfort, progress가 달라도 배포 의사결정은 같은가?

## 9. RoboTwin 2.0 — visual/domain randomization에서의 action 품질

- Tianxing Chen et al. **RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation** (2025).
- [arXiv:2506.18088](https://arxiv.org/abs/2506.18088), DOI `10.48550/arXiv.2506.18088`. [44].
- **요점:** bimanual manipulation demonstration과 domain-randomized evaluation을 제공한다.
- **관계:** OSWAM은 clean/randomized 50-task closed-loop success를 사용한다. 평균 SR 90.00%는 task별 잔여 실패와 multi-step baseline의 더 높은 평균을 감추면 안 된다.
- **질문:** clean/randomized 평균이 가까우면 texture robustness는 좋아도 unseen dynamics나 contact force robustness까지 증명되는가?

## 추천 읽기 순서

1. NAVSIM/RoboTwin의 evaluation contract를 먼저 읽어 수치를 해석한다.
2. Fast-WAM → SimWAM으로 direct-policy interface를 이해한다.
3. Rectified Flow → OSWAM Eq. 5/6/11로 structured initialization과 residual target을 연결한다.
4. Wan/LoRA로 실제 backbone 적응 비용을 확인한다.
5. Flash-WAM/Light-WAM과 비교해 quality–latency trade-off가 달라지는 이유를 적는다.

## 문헌 추적의 주의점

본문에는 서로 다른 두 Faster-WAM이 인용된다. [19]는 *Efficient Inference-time Future Conditioning* (2608.04404), [46]은 *Do World Action Models Need Deep Action Modules?* (2608.02365)다. 이름이 같다고 하나의 paper id로 합치지 않는다. 본 주간 선정은 OSWAM 한 편이며 위 참고문헌들을 신규 선정 논문으로 state에 추가하지 않는다.
