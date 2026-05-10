---
title: "Code with Claude 2026: Opening Keynote"
type: source
tags: [claude, agentic-ai, software-development, platform]
date: 2026-05-10
source_file: raw/AI/LilysAI/code-with-claude-2026-opening-keynote.md
source_hash: 5220400fea84797e
---

## Summary

This keynote presents [[Anthropic]]’s 2026 direction for [[Claude]] and [[ClaudeCode]], emphasizing that real impact now comes from operationalizing AI in complex workflows rather than only model benchmarking. The center of the announcement is the expansion of agentic capabilities through [[ClaudeManagedAgents]], including [[MultiAgentOrchestration]], [[Outcomes]], and [[Dreaming]]—designed to make teams more productive on long-horizon, multi-step work.

The talk frames current AI progress as increasingly exponential while organizations still adopt capability linearly, creating an application gap. To close that gap, Anthropic positions product changes as more important than pure model races: scalable productionization primitives, controlled orchestration, and stronger developer workflows.

## Key Claims

- [[Anthropic]] introduced three new managed-agent primitives in [[Claude Platform]]: [[MultiAgentOrchestration]], [[Outcomes]], and [[Dreaming]], enabling agents to collaborate on hard tasks, self-evaluate against success criteria, and improve over time using prior execution.
- [[MultiAgentOrchestration]] in this framing decomposes work into specialized roles (for example, commander, detector, navigator) and lets agents run concurrently with shared coordination.
- [[Outcomes]] is a goal-oriented execution loop: the user defines success conditions in files; a grader agent repeatedly evaluates agent trajectories and triggers retries until criteria are satisfied.
- [[Dreaming]] lets agents review prior sessions, summarize misses, and persist lessons into memory so future sessions can execute with improved strategy without manual rework.
- [[Anthropic]] is pushing developer adoption via better [[API]] primitives and production infrastructure: managed agents, memory defaults, advisor model routing, and higher [[Rate Limits]] to support scaling from prototype to production.
- [[ClaudeCode]] has evolved from tightly supervised editing toward asynchronous, agent-supervised workflows: terminals, IDE, and desktop interfaces plus [[Routines]], [[Autofix]], and remote control support for non-blocking review loops.
- Case studies in the keynote cite productivity gains, including large codebase conversions, faster child placement documentation workflows, higher production engineering throughput, and improved iterative quality at companies like [[Stripe]], [[Intuit]], [[Binti]], and others.

## Key Quotes

> "클로드(Claude)가 목표를 성공 기준에 따라 반복 평가하면서 완성도를 높인다" — multi-step completion described in the [[Outcomes]] section.

> "드리밍(Dreaming)은 과거 세션을 리뷰해 배운 내용을 메모리에 반영하고 다음 세션에서 스스로 개선하게 한다" — mechanism summary.

> "개발자는 이제 자동 모드로 권한을 위임하고, 에이전트가 PR을 완성한 뒤 검토한다" — developer workflow shift for [[ClaudeCode]].

## Connections

- [[Claude]], [[Anthropic]], [[ClaudeCode]], [[Claude Managed Agents]] — source actors and platform primitives.
- [[MultiAgentOrchestration]] — core collaboration design pattern for complex tasks.
- [[Outcomes]] — explicit objective-driven evaluation and iteration.
- [[Dreaming]] — long-horizon memory and post-run improvement mechanism.
- [[AdvisorStrategy]] — cost-aware split between heavy and light models in agent stacks.
- [[Routines]] — scheduled, event-driven autonomous execution.
- [[ClosedLoopEvaluation]] — implicit relation through repeated grading and retry behavior.
- [[Autofix]] and [[CodeReview]] — execution-time quality guardrails for [[ClaudeCode]].
- [[AsynchronousExecution]] and [[DeveloperExperience]] — broader workflow consequence.

## Contradictions

- None identified against existing wiki summaries. This source largely deepens the direction already tracked in existing [[ClaudeCode]]-related pages such as [[VibeCoding]] and agentic tooling discussions.
