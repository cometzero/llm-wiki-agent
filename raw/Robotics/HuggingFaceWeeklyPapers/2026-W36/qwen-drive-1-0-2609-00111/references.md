---
title: "Qwen-Drive-1.0 참고문헌 학습 메모"
document_type: references
source_url: https://api.semanticscholar.org/graph/v1/paper/ARXIV:2609.00111/references
hf_url: https://huggingface.co/papers/2609.00111
arxiv_id: "2609.00111"
arxiv_url: https://arxiv.org/abs/2609.00111
pdf_url: https://arxiv.org/pdf/2609.00111
week: "2026-W36"
ingested_at_kst: "2026-09-09 09:40:43 KST"
selected_reason: "Qwen-Drive의 foundation-model/BEV/planning 계보를 연결한다."
---

# Qwen-Drive-1.0 참고 레퍼런스 논문 요약

> Semantic Scholar `ARXIV:2609.00111/references` endpoint와 원문 reference/related-work 맥락을 대조했다. endpoint는 100개 reference를 반환했으며 아래는 Qwen-Drive의 문제 설정에 직접적인 항목만 추렸다.

1. **SimWAM: A Simple World Action Model for End-to-End Autonomous Driving** (2026), [arXiv:2608.07468](https://arxiv.org/abs/2608.07468)
   World Action Model 관점에서 driving observation과 action/dynamics를 연결한다. Qwen-Drive가 VLM representation에서 explicit BEV 및 planner를 유지하는 설계와 비교할 때, action/world representation을 어디까지 shared generative model로 흡수할지의 대비점이다.

2. **UniAD: Planning-oriented End-to-end Autonomous Driving** (2023), [arXiv:2212.10156](https://arxiv.org/abs/2212.10156)
   tracking, mapping, motion forecasting, occupancy, planning을 planning-oriented unified framework에 넣은 E2E AD의 중요한 background다. Qwen-Drive는 UniAD류 task integration에 VLM language capability와 cross-dataset 3D interface를 더한다.

3. **VAD: End-to-End Vectorized Autonomous Driving** (2023), [arXiv:2303.12069](https://arxiv.org/abs/2303.12069)
   vectorized scene representation과 planning을 결합한다. Qwen-Drive의 trajectory generator를 볼 때 BEV/grid representation과 vector/agent-centric representation의 trade-off를 비교하는 기준이다.

4. **DriveLM: Driving with Graph Visual Question Answering** (2023), [arXiv:2312.14150](https://arxiv.org/abs/2312.14150)
   driving scene understanding을 graph VQA로 구조화한다. Qwen-Drive의 VQA component는 language reasoning의 broad interface를 제공하지만, VQA correctness가 planner behavior와 어떻게 causal하게 연결되는지는 별도 검증이 필요하다.

5. **DriveGPT4: Interpretable End-to-end Autonomous Driving via Large Language Model** (2023), [arXiv:2310.01412](https://arxiv.org/abs/2310.01412)
   language explanation을 E2E driving과 연결한 초기 계열이다. Qwen-Drive는 prose explanation에서 멈추지 않고 numerical Planning Expert와 3D head를 둔다는 점에서 action grounding을 더 명시한다.

6. **NAVSIM: Data-Driven Non-Reactive Autonomous Vehicle Simulation and Benchmarking** (2024), [arXiv:2406.15349](https://arxiv.org/abs/2406.15349)
   planning policy를 PDMS 및 안전/진행/comfort component로 평가하는 benchmark다. Qwen-Drive의 pseudo-closed-loop 결과를 해석할 때 ADE와 PDMS가 서로 다른 failure mode를 측정한다는 점이 핵심이다.

7. **nuScenes: A Multimodal Dataset for Autonomous Driving** (2020), [project](https://www.nuscenes.org/)
   multi-sensor 3D detection, tracking, map 등 AD benchmark 기반이다. Qwen-Drive의 perception data unification에서 canonical six-camera reference로 쓰이지만 OpenScene과 camera/label structure가 달라 cross-dataset generalization 문제를 드러낸다.

8. **OpenScene: 3D Scene Understanding with Open Vocabularies** (2023), [arXiv:2312.04794](https://arxiv.org/abs/2312.04794)
   open-world 3D semantic understanding 및 large-scale scene label context를 제공한다. Qwen-Drive는 nuScenes-only head의 fixed-rig limitation을 넘는 cross-dataset perception evidence로 OpenScene split을 사용한다.

9. **Flow Matching for Generative Modeling** (2023), [arXiv:2210.02747](https://arxiv.org/abs/2210.02747)
   noise-to-data probability path의 vector field를 학습하는 generative framework다. Qwen-Drive Planning Expert의 noisy trajectory recovery를 이해하는 기본 도구이며, action trajectory에 적용할 때 constraint/safety handling은 별도 문제다.

10. **Qwen3.5 technical report / pretrained Qwen vision-language backbone** (backbone reference; 원문 참조)
    Qwen-Drive는 Qwen3.5-4B 계열의 general visual-language prior를 출발점으로 한다. 논문의 staged data recipe는 driving specialization 후에도 이 prior의 recognition/reasoning/spatial grounding을 보존하려는 방법이다.

## 읽는 순서

먼저 UniAD·VAD로 end-to-end perception–planning 배경을 잡고, DriveLM/DriveGPT4로 language가 driving에 들어온 초기 형태를 비교한다. 이어 NAVSIM으로 metric의 의미를 익힌 뒤, Flow Matching과 SimWAM을 통해 Qwen-Drive Planning Expert의 generative-action 설계를 분석한다.
