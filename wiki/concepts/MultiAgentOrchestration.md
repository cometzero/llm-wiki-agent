---
title: "Multi-Agent Orchestration"
type: concept
tags: [agentic, orchestration]
sources: [code-with-claude-2026-opening-keynote]
last_updated: 2026-05-10
---

## Definition

[[MultiAgentOrchestration]] is a control pattern in which multiple AI agents with specialized roles collaborate on a shared objective under coordination logic.

## Core Mechanism

- Task decomposition into role-specific subtasks.
- Controlled session boundaries for each role/agent.
- Communication or shared state between agents.
- Centralized review path with policy checks.

## Example From Source

The keynote describes a pattern with a commander, detector, and navigator agent combination in a simulated landing scenario.

## Relation to Existing Concepts

- Related to [[AgenticSystems]] and [[LLMAgents]].
- A control form of [[ClosedLoopEvaluation]] and [[ToolUse]] orchestration.

## Potential Risks

- Coordination drift if objectives are underspecified.
- Higher failure surface if role boundaries and memory handoff are not explicitly governed.

## Signals from Source

In the keynote, [[Anthropic]] ties this concept to improved quality and speed on hard, long-horizon tasks through explicit role partitioning and repeated evaluation.
