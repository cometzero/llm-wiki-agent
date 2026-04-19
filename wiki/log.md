## [2026-04-19] ingest | Vibe coding in prod

Added source. Key claims: 정의적으로는 AI가 코드를 생성하는 것이 아니라 제품 중심·검증 중심으로 운영하는 방법을 제시하며, AI의 PM 역할 강화와 [[LeafNode]] 중심의 변경 전략을 중심 축으로 삼는다; Anthropic/[[ClaudeCode]] 사례를 통해 프로덕션 적용 시 기술 부채 통제와 보안 구간 분리가 중요함을 강조한다; [[TestDrivenDevelopment]]와 스트레스 테스트 기반의 체크포인트를 통해 구현 상세를 모두 읽지 않아도 신뢰를 축적하는 운영 모델이 제시된다.

## [2026-04-16] ingest | Bulk corpus sync

- Rebuilt `wiki/index.md` and `wiki/overview.md` after confirming all raw markdown sources are represented in `wiki/sources/`.
- Corpus status: 64 sources, 91 entities, 65 concepts.

# Wiki Log

Append-only chronological record of all operations.

Format: `## [YYYY-MM-DD] <operation> | <title>`

Parse recent entries: `grep "^## \[" wiki/log.md | tail -10`

---

## [2026-04-18] graph | Knowledge graph rebuilt

221 nodes, 1880 edges (1117 extracted, 763 inferred).

## [2026-04-19] graph | Knowledge graph rebuilt

227 nodes, 1920 edges (1140 extracted, 780 inferred).
