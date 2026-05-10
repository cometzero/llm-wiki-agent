---
title: "Dreaming"
type: concept
tags: [agent-memory, self-improvement, long-horizon]
sources: [code-with-claude-2026-opening-keynote]
last_updated: 2026-05-10
---

## Definition

[[Dreaming]] refers to post-session reflective learning: agents analyze prior execution traces, capture misses, and reuse those lessons in future sessions.

## Core Mechanism

- Replay past failures and outputs.
- Extract actionable lessons.
- Persist learning artifacts (playbooks/checklists) into agent memory.
- Reuse in later sessions to increase first-pass success probability.

## Relation

- Extends ideas in [[SessionCompaction]] and [[Context Memory Storage]].
- Increases continuity across sessions for [[LLMAgents]].

## Use Case in Source

A simulated landing scenario used a descent playbook generated from prior failures and reused in later missions.

## Risks and Governance

- Memory staleness.
- Overfitting to past context and missing edge cases.
- Need for provenance and quality bounds on learned playbooks.
