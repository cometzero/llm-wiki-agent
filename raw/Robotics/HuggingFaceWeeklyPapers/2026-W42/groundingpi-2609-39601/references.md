---
title: "GroundingPI 참고문헌: Generative Grounding·VLA Flow·Controlled Transfer"
source_url: https://arxiv.org/html/2609.39601v1
hf_url: https://huggingface.co/papers/2609.39601
arxiv_id: "2609.39601"
arxiv_url: https://arxiv.org/abs/2609.39601
pdf_url: https://arxiv.org/pdf/2609.39601
week: 2026-W42
ingested_at_kst: "2026-10-14"
selected_reason: "GroundingPI의 perception→action 전이를 이해하는 핵심 9개 문헌을 원문 bibliography에서 선정"
---

# GroundingPI 참고문헌 지도

Semantic Scholar `paper/arXiv:2609.39601/references` 요청은 성공했지만 `data: []`였다. 이를 '참고문헌 없음'으로 해석하지 않고 arXiv HTML의 실제 References를 사용했다. 아래는 원문에서의 인용 맥락을 바탕으로 한 문헌 요약이며, 각 reference의 전체 PDF를 이번에 별도로 deep-read한 것은 아니다. 확인되지 않은 DOI·arXiv ID는 만들어 넣지 않았다.

## 1. Pix2Seq — Coordinate를 Language Token으로

- Chen et al., *Pix2Seq: A Language Modeling Framework for Object Detection* (2022).
- [arXiv:2109.10852](https://arxiv.org/abs/2109.10852); 원문 reference [11].
- Object detection을 label·coordinate의 sequence prediction으로 표현하는 계보를 제공한다. Detection regression과 language generation을 분리하지 않고 autoregressive interface로 통합한다.
- GroundingPI와의 연결: point/box와 semantic label을 shared vocabulary로 출력하는 formulation을 이해하는 출발점이다. GroundingPI는 referring/OCR/GUI/spatial perception과 downstream action transfer까지 넓힌다.
- 읽을 질문: numerical string이 아니라 atomic coordinate token을 쓰면 sequence length와 precision tradeoff는 어떻게 바뀌는가?

## 2. π0 — VLM과 Flow-Matching Action Expert

- Black et al., *π0: A Vision-Language-Action Flow Model for General Robot Control* (2024).
- [arXiv:2410.24164](https://arxiv.org/abs/2410.24164); 원문 [5].
- Vision-language foundation의 semantic representation을 continuous robot action generation과 연결하는 flow-model 계열의 핵심 문헌이다.
- GroundingPI와의 연결: robot experiment의 π-style Action DiT와 flow-matching objective의 배경이다. 다만 GroundingPI 비교는 각 native policy를 그대로 실행하지 않고 fixed shared expert/interface로 backbone을 비교한다.
- 읽을 질문: perception feature가 action expert에 condition된다는 것과 decoded box가 actuator command라는 것은 왜 다른가?

## 3. π0.5 — Open-World Generalization과 Perceptual Supervision

- Physical Intelligence et al., *π0.5: A Vision-Language-Action Model with Open-World Generalization* (2025).
- [arXiv:2504.16054](https://arxiv.org/abs/2504.16054); 원문 [29].
- Broad knowledge·diverse supervision과 action learning을 연결하는 계보로 인용된다. GroundingPI는 π0→π0.5 progression에서 box prediction이 perception을 보완하는 사례에 주목한다.
- 연결: auxiliary perceptual task를 action training에 넣는 방식과, perception 자체를 foundation-native capability로 크게 학습하는 방식의 비교 축이다.
- 주의: GroundingPI의 matched expert 결과가 모든 π-family adaptation보다 우월하다는 주장은 아니다.

## 4. Knowledge Insulating VLA Models — 빠른 Action Adaptation의 분리

- Driess et al., *Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better* (2025).
- [arXiv:2505.23705](https://arxiv.org/abs/2505.23705); 원문 [24].
- Foundation knowledge와 action adaptation 사이의 보호·분리 recipe를 다루는 배경 문헌이다. 학습 속도뿐 아니라 runtime과 generalization을 함께 보는 문제 설정이 중요하다.
- 연결: perceptual foundation을 action objective가 어떻게 읽고 유지하는지, backbone와 expert의 역할을 나누는 논의를 이해하는 데 도움이 된다.
- 읽을 질문: pretraining knowledge를 유지하면서 control-specific gradient를 전달하려면 어떤 interface가 필요한가?

## 5. Flow Matching for Generative Modeling — Continuous Action의 수학

- Lipman et al., *Flow Matching for Generative Modeling* (2023).
- [arXiv:2210.02747](https://arxiv.org/abs/2210.02747); 원문 [43].
- Noise와 target 사이의 probability path를 따라 vector field를 학습하는 생성 모델 framework다.
- 연결: GroundingPI action expert의 $a_t=(1-t)\epsilon+ta$, $v^*=a-\epsilon$ 및 velocity MSE를 이해하는 직접 기반이다. Grounding coordinate CE와 robot continuous-control loss가 왜 다른지 설명한다.
- 읽을 질문: backbone cache와 4 Euler step은 서로 다른 계산 단계에서 비용을 줄인다. Step 수를 줄일 때 control quality는 어떻게 확인할 것인가?

## 6. StarVLA — Foundation-to-Action Interface

- StarVLA Community, *StarVLA: A Lego-like Codebase for Vision-Language-Action Model Developing* (2026).
- [arXiv:2604.05014](https://arxiv.org/abs/2604.05014); 원문 [17].
- VLA component를 조합하는 codebase로 본 연구의 layer-wise condition 및 VLM/video foundation adaptation pathways의 근거다.
- 연결: GroundingPI는 StarVLA π-style와 Wan-π 경로를 토대로 native action head confound를 줄이고 fixed-capacity Action DiT로 comparison한다.
- 읽을 질문: backbone마다 hidden width가 달라도 normalized depth와 common resampler로 condition budget을 어떻게 맞추는가?

## 7. RoboTwin 2.0 — Scene Randomization과 OOD

- Chen et al., *RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation* (2025).
- [arXiv:2506.18088](https://arxiv.org/abs/2506.18088); 원문 [12].
- Bimanual tabletop manipulation의 data generation와 strong domain randomization benchmark다.
- 연결: Full은 Clean/Randomized를 모두 사용하고 Clean2Random은 Clean-only training 뒤 Randomized test로 scene robustness를 평가한다. GroundingPI의 66.20% Full과 17.60% Clean2Random은 다른 protocol의 수치다.
- 읽을 질문: 왜 ID task success와 unseen lighting/clutter/texture의 OOD success를 합쳐 하나의 robustness score처럼 읽으면 안 되는가?

## 8. nuScenes — Driving Data와 Open-Loop의 범위

- Caesar et al., *nuScenes: A Multimodal Dataset for Autonomous Driving*, CVPR 2020; 원문 [7].
- [공식 프로젝트](https://www.nuscenes.org/).
- 다양한 driving sensor modality와 annotation을 제공하는 dataset이다. Dataset의 multimodality와 특정 논문이 사용하는 input modality는 구분해야 한다.
- 연결: GroundingPI는 front-camera image와 ego-state history로 six cumulative waypoint를 예측한다. 0.296 m는 recorded target와의 open-loop error이지 real-vehicle closed-loop SR가 아니다.
- 읽을 질문: imitation trajectory accuracy가 좋아도 policy-induced state shift, collision avoidance, rule compliance는 왜 별도 검증해야 하는가?

## 9. DeepSeekMath / GRPO — Group-Relative Reward

- Shao et al., *DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models* (2024).
- [arXiv:2402.03300](https://arxiv.org/abs/2402.03300); 원문 [68].
- Group-relative policy optimization의 배경으로 인용된다. 같은 prompt에서 생성한 candidate response의 상대 reward를 advantage로 사용한다.
- 연결: GroundingPI는 linguistic math correctness 대신 coverage·IoU·format·OCR text–geometry consistency를 reward로 쓴다. GRPO가 같아도 task reward와 normalization이 성능·reward hacking 위험을 결정한다.
- 읽을 질문: 왜 coverage reward만 높이면 oversized box나 duplicate가 유리해질 수 있으며 complementary strict reward가 필요한가?

## 읽기 순서

1. Pix2Seq: generative coordinate interface.
2. Flow Matching→π0: continuous action generation.
3. π0.5→Knowledge Insulation: foundation/action 역할과 knowledge preservation.
4. StarVLA: matched feature-to-action interface.
5. RoboTwin/nuScenes: benchmark protocol·metric boundary.
6. GRPO: reward와 optimization의 연결.

RoboCasa(원문 [52]), GR00T N1([54]), RynnBrain([21]), Qwen3-VL([2]), Kimi K3([72])도 backbone·embodiment 비교의 중요 문헌이다. 본 문서에서는 핵심 9개를 우선 설명했고 나머지 서지 정보는 원문 References를 참조한다.
