---
title: "SimWAM 참고 레퍼런스"
document_type: references
source_url: https://api.semanticscholar.org/graph/v1/paper/ARXIV:2608.07468/references
hf_url: https://huggingface.co/papers/2608.07468
arxiv_id: "2608.07468"
arxiv_url: https://arxiv.org/abs/2608.07468
pdf_url: https://arxiv.org/pdf/2608.07468
week: "2026-W33"
ingested_at_kst: "2026-08-12 09:40:01 KST"
selected_reason: "WAM, video generative prior, E2E AD, RL의 직접 선행 연구를 한국어로 연결한다."
---

# SimWAM 참고 레퍼런스

Semantic Scholar `ARXIV:2608.07468/references` 응답과 원문 reference section에서 선별했다(조회 성공). 요약은 공개 제목/메타데이터 및 본 논문에서의 관계를 기준으로 한다.

1. **DriveWAM: Video Generative Priors Enable Scalable World-Action Modeling for Autonomous Driving** (2026), [arXiv:2605.28544](https://arxiv.org/abs/2605.28544)
   video generative prior를 AD action model에 쓰는 직접 선행 WAM이다. SimWAM은 이 계열의 미래 generation 비용을 training-only prior transfer로 줄이려 한다.
2. **DriveVA: Video Action Models are Zero-Shot Drivers** (2026), [arXiv:2604.04198](https://arxiv.org/abs/2604.04198)
   video/action model을 driving policy로 쓰는 흐름을 대표한다. SimWAM의 zero-shot nuScenes transfer와 “video dynamics→action” 연결을 해석하는 비교 기준이다.
3. **ExploreVLA: Dense World Modeling and Exploration for End-to-End Autonomous Driving** (2026), [arXiv:2604.02714](https://arxiv.org/abs/2604.02714)
   dense world modeling·exploration을 E2E AD에 결합한다. SimWAM은 language-centric VLA보다 numerical trajectory policy에 가깝지만, world modeling을 planning에 접속한다는 공통점이 있다.
4. **DriveDreamer-Policy: A Geometry-Grounded World-Action Model for Unified Generation and Planning** (2026), [arXiv:2604.01765](https://arxiv.org/abs/2604.01765)
   geometry-grounded generation과 planning을 통합하는 WAM이다. SimWAM이 generation output을 배포 시 제거하는 설계와 대비된다.
5. **Uni-World VLA: Interleaved World Modeling and Planning for Autonomous Driving** (2026), [arXiv:2603.27287](https://arxiv.org/abs/2603.27287)
   world modeling과 planning을 interleave하는 VLA 계열이다. SimWAM은 larger VLM/VLA inference 대신 action DiT를 남기는 latency 중심 대안이다.
6. **Fast-WAM: Do World Action Models Need Test-time Future Imagination?** (2026), [arXiv:2603.16666](https://arxiv.org/abs/2603.16666)
   test-time future imagination의 필요성을 직접 묻는다. SimWAM의 핵심 주장—미래 video는 training signal이면 충분할 수 있음—을 위치시키는 핵심 비교 문헌이다.
7. **World Action Models are Zero-shot Policies** (2026), [arXiv:2602.15922](https://arxiv.org/abs/2602.15922)
   world action model을 zero-shot policy로 해석하는 일반 관점이다. SimWAM의 nuScenes zero-shot 결과를 broader policy-transfer 관점에서 읽게 한다.
8. **DriveLaW: Unifying Planning and Video Generation in a Latent Driving World** (2025), [arXiv:2512.23421](https://arxiv.org/abs/2512.23421)
   latent driving world에서 planning과 video generation을 통합한다. SimWAM은 통합 training의 이점은 유지하되 action inference에서 video branch를 제거한다.

## 읽기 순서
DriveLaW/DriveWAM으로 classic WAM interface를 잡고 → Fast-WAM의 test-time imagination 논점을 읽은 뒤 → SimWAM의 isolated attention mask와 joint flow matching을 보면 설계 차이가 선명하다.
