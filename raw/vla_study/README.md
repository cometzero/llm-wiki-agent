# VLA for Autonomous Driving Weekly Study

이 폴더는 VLA(Vision-Language-Action) for Autonomous Driving 주간 학습 자료를 모으는 raw corpus입니다.

운영 방식:
- 매주 화요일 Asia/Seoul 기준으로 1회 학습 노트를 생성합니다.
- 각 주차 자료는 `weeks/week-XX-*.md`에 저장합니다.
- 논문 내용은 한국어 학습 노트 형태로 번역·요약·분석합니다.
- 시각 자료는 Markdown 표, Mermaid diagram, architecture map, evaluation matrix 위주로 넣습니다.
- 모든 노트는 action grounding, language role, closed-loop evaluation, safety/long-tail 관점으로 분석합니다.

핵심 질문:
> 이 모델에서 language는 실제 driving action을 더 안전하고 일반화 가능하게 만드는가, 아니면 설명 가능성을 덧붙이는 역할에 머무는가?

파일:
- `curriculum.json`: 12주 커리큘럼 원본
- `state.json`: 주간 진행 상태
- `template.md`: 매주 생성되는 학습 노트 템플릿
- `weeks/`: 실제 주간 학습 markdown
