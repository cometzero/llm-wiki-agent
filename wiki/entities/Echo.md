---
title: "Echo"
type: entity
tags: [VLA, robotics, task-status, flow-matching]
sources: [echo-2610-31569-paper-ko, echo-2610-31569-analysis, echo-2610-31569-references, echo-2610-31569-learning]
last_updated: 2026-10-28
---

# Echo

Echo（arXiv `2610.31569`）는 π0.5 기반 [[VLA]]에서 action chunk와 stop/failure signal을 함께 denoise하는 framework다. [[StatusGuidedActionDenoising]]으로 두 signal을 action보다 먼저 clean하게 만들고 controlled attention으로 corrective action generation에 사용한다.

## 핵심 설계

- Success·terminal failure·pre-intervention failure·recovery data를 구분한다. Failure action은 imitation하지 않는다.
- SS는 termination, FS는 failure를 표현한다. Low SS/high FS는 recoverable failure이며 즉시 종료와 같지 않다.
- Action↔SS, action↔FS attention은 허용하고 direct SS↔FS는 차단한다. Group별 MLP와 token-wise flow time을 쓴다.
- [[FlowMatching]]에서 real-world τclean=0.5/H=60, simulation τclean=0.7/H=50이다. Recipe를 혼합하지 않는다.

## 근거와 한계

실물 다섯 task에서 0–10 completion score가 개선되며 simulation SR은 32.67→34.76%(+2.09 pp)다. RTX 4090 inference는 115→120 ms이고 실제 실물 policy query는 5 Hz다. 결과는 저자 보고이며 독립 재현하지 않았다. Frame-level progress label을 요구하지 않지만 segment/boundary annotation은 필요하다. Simulation 89.97% status accuracy는 terminal-failure detection 성능이 아니다. AD closed-loop·NPU performance·formal safety를 입증하지 않는다.

## 연결

- [[echo-2610-31569-paper-ko]] — CC BY 4.0 본문 번역·선별 부록
- [[echo-2610-31569-analysis]] — metric·causality·deployment boundary
- [[echo-2610-31569-references]] — 핵심 8편
- [[echo-2610-31569-learning]] — 실행한 교육 예제
- [[FailureRecovery]] — state recognition과 corrective action
- [[MotorMind]] — external harness와 policy-internal feedback의 비교
- [[MorphAct]] — context-dependent parameter generation과 status conditioning의 차이
