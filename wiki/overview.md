## Embodied AI & VLA 연구 동향

### Physical Commonsense 기반 VLA 학습

[[physbrain-1-0-2605-15298]]은 VLA 학습의 핵심을 trajectory imitation에서 [[PhysicalCommonsenseSupervision]] pretraining + controlled VLA adaptation으로 재구성한다. [[HumanNet]]의 100만 시간 규모 human-centric video corpus와 결합하여, robot trajectory 없이도 physical understanding이 강한 multimodal base model을 구축하는 방향이 가속화되고 있다.

[[HumanNet]] — VLA pretraining용 100만 시간 video corpus
[[physbrain-1-0-2605-15298]] — egocentric video → structured physical QA → VLA transfer
[[EmbodiedMidtrain]] — VLM 샘플 분포 정렬 기반 VLA 성능 향상
[[MobileEgoAnywhere]] — commodity smartphone 기반 200시간 egocentric 데이터 수집