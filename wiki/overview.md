## Linux / Open Source Weekly 기술 동향

LWN.net Weekly Edition for May 14, 2026 번역 소스는 Fedora AI Developer Desktop 논쟁, Forgejo carrot disclosure, LSFMM+BPF 2026의 메모리 관리·BPF 논의, [[DMAbuf]], [[TransparentHugePage]], [[Mshare]], [[DAMON]], [[ReproducibleBuilds]], [[KernelKillswitch]] 등을 통해 Linux/open-source 운영·보안·커널 개발 흐름을 확장한다. May 7, 2026 번역 소스는 Linux 커널 ABI 호환성, LLM 기반 취약점 보고가 coordinated disclosure에 미치는 영향, Fedora/GNOME 패키지 유지보수 정책, Prolly tree 기반 database versioning, s390/Arm virtualization testing, 주간 보안 업데이트와 커널 패치 흐름을 한 번에 정리한다. 이 두 LWN 소스는 AI/ML 중심 corpus와 별도로 Linux/open-source 운영·보안·시스템 소프트웨어 동향을 추적하는 기준점 역할을 한다.

## Embodied AI & VLA 연구 동향

### Physical Commonsense 기반 VLA 학습

[[physbrain-1-0-2605-15298]]은 VLA 학습의 핵심을 trajectory imitation에서 [[PhysicalCommonsenseSupervision]] pretraining + controlled VLA adaptation으로 재구성한다. [[HumanNet]]의 100만 시간 규모 human-centric video corpus와 결합하여, robot trajectory 없이도 physical understanding이 강한 multimodal base model을 구축하는 방향이 가속화되고 있다.

[[HumanNet]] — VLA pretraining용 100만 시간 video corpus
[[physbrain-1-0-2605-15298]] — egocentric video → structured physical QA → VLA transfer
[[EmbodiedMidtrain]] — VLM 샘플 분포 정렬 기반 VLA 성능 향상
[[MobileEgoAnywhere]] — commodity smartphone 기반 200시간 egocentric 데이터 수집

## AI/ML Learning — 실전 LLM 시스템

2026-05-21 Day 29 학습은 현대 LLM 서비스가 단일 모델만으로 구성되지 않고 [[RAG]], [[EmbeddingModel]], [[VectorSearch]], [[PromptEngineering]]을 결합해 외부 지식 검색, context 보강, 답변 형식 제어를 수행한다는 점을 정리한다. [[Hallucination]]을 줄이기 위해서는 검색 품질, [[Chunking]], [[CosineSimilarity]], [[ContextWindow]] 관리, 그리고 필요 시 [[ToolUse]]나 [[FineTuning]]과의 역할 분리가 함께 중요하다.

2026-05-24 Day 30 학습은 [[Evaluation]]·[[Benchmark]]로 품질을 검증하고, [[Serving]]·[[InferenceOptimization]]으로 실제 요청을 빠르고 저렴하게 처리하며, [[DataPipeline]]·[[TrainingStack]]·[[InferenceStack]]·[[FeedbackLoop]]가 연결된 전체 AI 시스템 관점으로 학습 과정을 마무리한다.