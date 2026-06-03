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