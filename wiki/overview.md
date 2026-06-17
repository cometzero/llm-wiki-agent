## 2026-W25 HF Weekly VLA update: retrieval adaptation and action-expert pretraining

이번 업데이트는 VLA scaling의 두 병목을 추가한다. [[ReCAP]]/[[retrieve-dont-retrain-2606-15631]]은 새 task를 parameter update가 아니라 retrieval pool 확장으로 흡수하는 [[RetrievalAugmentedPolicy]] 방향을 제시한다. [[APT]]/[[apt-action-expert-pretraining-2606-12366]]는 continuous action expert가 language imbalance 때문에 visual shortcut을 학습하는 문제를 [[ActionExpertPretraining]]과 gated fusion으로 완화한다. 두 논문 모두 manipulation 중심이지만, 자율주행 VLA에서는 waypoint/trajectory planner, closed-loop latency, safety verifier와 결합해야 한다.

## Visual Intermediate Reasoning in VLA Systems

VisualThink-VLA는 VLA(Vision-Language-Action) 정책에서 textual chain-of-thought의 한계를 극복하기 위한 핵심 approach로, compact visual evidence interface를 통해 action prediction을 bootstrap한다. 이 접근법은 text 기반 reasoning의 느린 디코딩(latency 8.377s)과 약한 visual grounding 문제를 동시에 해결한다.

### Key Papers
- [[RoboSemanticBench]]: VLA의 semantic grounding 격차를 진단하는 benchmark
- [[VisualThink-VLA]]: Visual intermediate reasoning으로 저지연 VLA 정책实现
- [[PhysBrain]]: VLA adaptation을 위한 physical commonsense 추출 approach
- [[HumanNet]]: VLA pretraining을 위한 human-centric video corpus

### Related Concepts
- [[VLA]]: Vision-Language-Action policy framework
- [[SemanticGrounding]]: VLA에서 textual vs visual reasoning의 grounding 차이
- [[ECoT]]: Textual chain-of-thought baseline

## Linux Kernel, BPF, and Open-Source AI Governance

The LWN Weekly corpus now tracks a sequence of 2026 Linux kernel and open-source infrastructure discussions. The May 28 edition connects [[LinusTorvalds]]'s AI/security-report workflow concerns with LSFMM+BPF coverage of [[BPF]], [[GCC]], [[PageCache]], [[MemoryController]], [[MemoryTiering]], and [[TransparentHugePage]], plus [[OpenSource]] AI governance concerns around openwashing. The June 4 edition extends that thread with [[MeshCore]] trademark governance, [[X32ABI]] maintenance economics, collaborative open-source security, [[PackageMetadata]] semantics, [[FilesystemMergePolicy]], [[KernelFunctionSignatures]], [[XattrCaching]], agentic-era [[BPF]], and [[FIPSCertification]] boundaries for kernel crypto.

