---
title: "Retrieve, Don't Retrain: 테스트 시점 검색으로 VLA를 새 태스크에 확장하기 — references"
source_url: "https://arxiv.org/abs/2606.15631"
hf_url: "https://huggingface.co/papers/2606.15631"
arxiv_id: "2606.15631"
arxiv_url: "https://arxiv.org/abs/2606.15631"
pdf_url: "https://arxiv.org/pdf/2606.15631"
week: "2026-W25"
ingested_at_kst: "2026-06-17 09:40:19 KST"
selected_reason: "현재 주(2026-W25) 후보 중 VLA/action policy 관련 점수가 가장 높고, per-task retraining 대신 retrieval pool 확장으로 새 작업을 흡수하는 test-time adaptation 패러다임을 제안해 VLA 스케일링 병목과 직접 연결된다."
---

# Retrieve, Don't Retrain: 테스트 시점 검색으로 VLA를 새 태스크에 확장하기 참고 레퍼런스 정리

Semantic Scholar references endpoint와 arXiv HTML bibliography를 먼저 시도했다. 신생 arXiv 항목이라 Semantic Scholar가 비어 있거나 404인 경우, 원문 reference/context와 논문 내 언급을 기준으로 핵심 레퍼런스를 선별했다.

## 핵심 레퍼런스 5–10개

### Cosmos Policy

- 관계: World-Action Model 기반 정책. ReCAP의 backbone으로 사용되어 retrieval trajectory와 future-image objective를 결합한다.
- 이 논문을 읽을 때의 역할: Cosmos Policy은/는 본 논문의 baseline, backbone, benchmark 또는 문제 정의를 이해하기 위한 anchor다.

### OpenVLA

- 관계: VLM backbone에 action generation을 붙이는 대표 VLA baseline. ReCAP은 이런 standard VLA에도 retrieval 효과가 있으나 WAM에서 더 크다고 설명한다.
- 이 논문을 읽을 때의 역할: OpenVLA은/는 본 논문의 baseline, backbone, benchmark 또는 문제 정의를 이해하기 위한 anchor다.

### π0.5

- 관계: Physical Intelligence 계열 generalist robot policy. action expert/continuous control 계열 비교 축이다.
- 이 논문을 읽을 때의 역할: π0.5은/는 본 논문의 baseline, backbone, benchmark 또는 문제 정의를 이해하기 위한 anchor다.

### GR00T N1.6

- 관계: NVIDIA 로보틱스 foundation model 계열로, VLA scaling 및 cross-embodiment generalization 맥락의 비교군이다.
- 이 논문을 읽을 때의 역할: GR00T N1.6은/는 본 논문의 baseline, backbone, benchmark 또는 문제 정의를 이해하기 위한 anchor다.

### DreamZero / Fast-WAM

- 관계: Video/world-action model 계열. ReCAP이 retrieval을 결합하는 WAM family의 선행 흐름이다.
- 이 논문을 읽을 때의 역할: DreamZero / Fast-WAM은/는 본 논문의 baseline, backbone, benchmark 또는 문제 정의를 이해하기 위한 anchor다.

### RoboTwin 2.0

- 관계: unseen task/cross-embodiment simulation benchmark로 사용된다.
- 이 논문을 읽을 때의 역할: RoboTwin 2.0은/는 본 논문의 baseline, backbone, benchmark 또는 문제 정의를 이해하기 위한 anchor다.

### PushT

- 관계: 2D pushing benchmark. retrieval이 goal-angle generalization과 motion prior를 제공하는지 분석하는 실험장이다.
- 이 논문을 읽을 때의 역할: PushT은/는 본 논문의 baseline, backbone, benchmark 또는 문제 정의를 이해하기 위한 anchor다.

### Open X-Embodiment / RT-X

- 관계: 여러 embodiment 데이터를 통합해 robot foundation model을 학습하는 대표 흐름. ReCAP은 이보다 test-time memory 확장을 더 강조한다.
- 이 논문을 읽을 때의 역할: Open X-Embodiment / RT-X은/는 본 논문의 baseline, backbone, benchmark 또는 문제 정의를 이해하기 위한 anchor다.


## Semantic Scholar 상태

- 자동 reference endpoint 결과: <HTTPError 404: 'Not Found'>

## arXiv HTML bibliography 추출 샘플

- [1] A. Bahety, P. Mandikal, B. Abbatematteo, and R. Martín-Martín (2024) ScrewMimic: bimanual imitation from human videos with screw space projection . In Proc. of the Robotics: Science and Systems (RSS), 2024 , Cited by: §2 .
- [2] J. Bjorck et al. (2025) GR00T n: an open foundation model for generalist humanoid robots . arXiv preprint arXiv:2503.14734 . Cited by: §1 , §2 .
- [3] R. Cadene, S. Alibert, A. Soare, Q. Gallouedec, A. Zouitine, S. Palma, P. Kooijmans, M. Aractingi, M. Shukor, D. Aubakirova, M. Russi, F. Capuano, C. Pascal, J. Choghari, J. Moss, and T. Wolf (2024) LeRobot: state-of-the-art machine learning for real-world robotics in pytorch . Note: https://github.com/huggingface/lerobot Cited by: §5.1 .
- [4] N. Carion, L. Gustafson, Y. Hu, S. Debnath, R. Hu, D. Suris, C. Ryali, K. V. Alwala, H. Khedr, A. Huang, J. Lei, T. Ma, B. Guo, A. Kalla, M. Marks, J. Greer, M. Wang, P. Sun, R. Rädle, T. Afouras, E. Mavroudi, K. Xu, T. Wu, Y. Zhou, L. Momeni, R. Hazra, S. Ding, S. Vaze, F. Porcher, F. Li, S. Li, A. Kamath, H. K. Cheng, P. Dollár, N. Ravi, K. Saenko, P. Zhang, and C. Feichtenhofer (2025) SAM 3: segment anything with concepts . External Links: 2511.16719 , Link Cited by: Appendix E , §4.2 .
- [5] T. Chen, Z. Chen, B. Chen, Z. Cai, Y. Liu, Z. Li, Q. Liang, X. Lin, Y. Ge, Z. Gu, et al. (2025) Robotwin 2.0: a scalable data generator and benchmark with strong domain randomization for robust bimanual robotic manipulation . arXiv preprint arXiv:2506.18088 . Cited by: §1 , §5.1 , §5.3 , §5 , §6 .
- [6] C. Chi, Z. Xu, S. Feng, E. Cousineau, Y. Du, B. Burchfiel, R. Tedrake, and S. Song (2025) Diffusion policy: visuomotor policy learning via action diffusion . The International Journal of Robotics Research 44 ( 10-11 ), pp. 1684–1704 . Cited by: §1 , §5.1 , §5.2 , §5 .
- [7] M. Du, S. Nair, D. Sadigh, and C. Finn (2024) Behavior retrieval: few-shot imitation learning by querying unlabeled datasets . In Proc. of the Robotics: Science and Systems (RSS), 2024 , Cited by: §2 .
- [8] M. Hong, A. Liang, K. Kim, H. Rajaprakash, J. Thomason, E. Bıyık, and J. Zhang (2025) Hand me the data: fast robot adaptation via hand path retrieval . arXiv preprint arXiv:2505.20455 . Cited by: §2 .
- [9] V. Jain, M. Attarian, N. J. Joshi, A. Wahid, D. Driess, Q. Vuong, P. R. Sanketi, P. Sermanet, S. Welker, C. Chan, I. Gilitschenski, Y. Bisk, and D. Dwibedi (2024) Vid2Robot: end-to-end video-conditioned policy learning with cross-attention transformers . In Proc. of the Robotics: Science and Systems (RSS), 2024 , Cited by: §2 .
- [10] M. J. Kim, Y. Gao, T. Lin, Y. Lin, Y. Ge, G. Lam, P. Liang, S. Song, M. Liu, C. Finn, and J. Gu (2026) Cosmos policy: fine-tuning video models for visuomotor control and planning . In Proc. of the Fourteenth International Conference on Learning Representations (ICLR) , External Links: Link Cited by: Figure 1 , §1 , §1 , §1 , §1 , §2 , §4.1 , §5.3 , Table 1 .
