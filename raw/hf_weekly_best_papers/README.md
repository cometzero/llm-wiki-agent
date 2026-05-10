# Hugging Face Weekly Best Papers → llm-wiki-agent

매주 수요일 Hugging Face Papers의 Weekly 랭킹에서 아래 주제와 관련된 논문을 1~2편 선별해 `raw/` 아래 적절한 디렉터리에 저장하고 `tools/ingest.py`로 llm-wiki-agent에 반영하는 자동화입니다.

대상 주제:
- 자율주행 / E2E Autonomous Driving
- VLA (Vision-Language-Action)
- VLM (Vision-Language Model)
- NPU / edge AI / AI accelerator

운영 방식:
1. `scripts/prepare_hf_weekly_best_papers.py`가 현재 ISO week와 직전 ISO week의 Hugging Face Weekly Papers 후보를 수집합니다.
2. Hermes cron agent가 후보 중 관련도가 높은 1~2편을 선택합니다.
3. 선택 논문마다 원문 한국어 번역 markdown, 분석 요약, 참고 레퍼런스 요약, 학습 자료를 생성합니다.
4. 논문 성격에 따라 아래 raw 디렉터리 중 하나에 저장합니다.
   - `raw/Robotics/HuggingFaceWeeklyPapers/` — 자율주행, VLA, robotics, embodied AI
   - `raw/AI/HuggingFaceWeeklyPapers/` — 일반 VLM / multimodal AI
   - `raw/Technology/HuggingFaceWeeklyPapers/` — NPU, accelerator, compiler, edge inference
5. 새 raw markdown을 ingest하고 graph/validation을 수행한 뒤 `personal` 브랜치에 commit/push합니다.

주의:
- `state.json`은 이미 처리한 Hugging Face/arXiv paper id를 추적해 중복 처리를 줄입니다.
- 준비 스크립트는 `state.json`뿐 아니라 기존 `raw/` 및 `wiki/sources/`의 파일명·frontmatter·source metadata에서 arXiv/HF paper id를 찾아 이미 분석된 논문을 후보에서 제외합니다.
- cron agent는 최종 선정 전에도 candidate id와 제목을 repo에서 다시 검색해, 이미 번역/분석된 흔적이 있으면 건너뜁니다.
- 논문 그림은 가능하면 arXiv HTML/PDF에서 내려받아 각 논문 폴더의 `figures/`에 저장하고 markdown에서 상대 경로로 참조합니다.
