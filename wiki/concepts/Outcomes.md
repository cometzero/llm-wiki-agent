---
title: "Outcomes"
type: concept
tags: [agent-evaluation, objective-driven, automation]
sources: [code-with-claude-2026-opening-keynote]
last_updated: 2026-05-10
---

## Definition

[[Outcomes]] in this context is an agent execution mode where work continues until predefined success conditions are met.

## Core Mechanism

- User defines success criteria in machine-readable or human-readable form (for example markdown).
- A grader/checker agent evaluates each run against these criteria.
- If criteria are not met, the loop retries with adjusted actions.

## Benefits

- Better control over task completion quality.
- Reduced ambiguity in handoff from autonomous execution to human review.

## Relation

- Strongly coupled with [[ClosedLoopEvaluation]].
- Compatible with [[Routines]] and [[AsynchronousExecution]].

## Source Evidence

The keynote highlights a drone landing simulation case in which explicit success rules (smooth landing, safe terrain, fuel for return) were central to iterative agent improvement.
