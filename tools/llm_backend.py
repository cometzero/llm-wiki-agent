#!/usr/bin/env python3
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent


def call_litellm(prompt: str, model_env: str = "LLM_MODEL", default_model: str = "anthropic/claude-3-5-sonnet-latest", max_tokens: int = 4096) -> str:
    try:
        from litellm import completion
    except ImportError:
        print("Error: litellm not installed. Run: pip install litellm")
        sys.exit(1)

    model = os.getenv(model_env, default_model)
    response = completion(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content


def _codex_error_text(proc: subprocess.CompletedProcess[str]) -> str:
    return "\n".join(part for part in (proc.stderr, proc.stdout) if part).lower()


def is_token_exhaustion_error(proc: subprocess.CompletedProcess[str]) -> bool:
    error_text = _codex_error_text(proc)
    markers = [
        "rate_limit_exceeded",
        "token",
        "usage limit",
        "quota",
        "exceeded",
        "insufficient_quota",
        "context_length_exceeded",
    ]
    return any(marker in error_text for marker in markers)


def run_codex(prompt: str, model: str, reasoning_effort: str = "low") -> subprocess.CompletedProcess[str]:
    codex_bin = shutil.which("codex")
    if not codex_bin:
        print("Error: codex CLI not found in PATH.")
        sys.exit(1)

    command = [
        codex_bin,
        "exec",
        "--json",
        "-m",
        model,
        "-s",
        "read-only",
        "-C",
        str(REPO_ROOT),
        "-c",
        f'model_reasoning_effort="{reasoning_effort}"',
        "-",
    ]
    return subprocess.run(
        command,
        input=prompt,
        text=True,
        capture_output=True,
        cwd=REPO_ROOT,
        check=False,
    )


def call_codex(prompt: str, model_env: str = "LLM_MODEL", default_model: str = "gpt-5.3-codex-spark", max_tokens: int = 4096) -> str:
    primary_model = os.getenv(model_env, os.getenv("CODEX_MODEL", os.getenv("LLM_MODEL", default_model)))
    fallback_model = os.getenv("CODEX_FALLBACK_MODEL", "gpt-5.4-mini")
    reasoning_effort = os.getenv("CODEX_REASONING_EFFORT", "low")

    proc = run_codex(prompt, primary_model, reasoning_effort)
    active_model = primary_model
    if proc.returncode != 0 and is_token_exhaustion_error(proc) and fallback_model and fallback_model != primary_model:
        print(f"  codex primary model exhausted tokens; retrying with fallback model: {fallback_model}")
        proc = run_codex(prompt, fallback_model, reasoning_effort)
        active_model = fallback_model

    if proc.returncode != 0:
        print(f"Error: codex exec failed (model: {active_model})")
        if proc.stderr:
            print(proc.stderr)
        if proc.stdout:
            print(proc.stdout)
        sys.exit(proc.returncode)

    final_messages = []
    for line in proc.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get("type") == "item.completed":
            item = event.get("item", {})
            if item.get("type") == "agent_message" and item.get("text"):
                final_messages.append(item["text"])

    if not final_messages:
        print(f"Error: codex exec produced no final agent message (model: {active_model})")
        if proc.stdout:
            print(proc.stdout)
        sys.exit(1)

    return "\n".join(final_messages)


def selected_backend(model_env: str = "LLM_MODEL", litellm_default: str = "anthropic/claude-3-5-sonnet-latest", codex_default: str = "gpt-5.3-codex-spark") -> tuple[str, str]:
    backend = os.getenv("WIKI_LLM_BACKEND", "auto").lower()
    if backend == "codex":
        return "codex", os.getenv(model_env, os.getenv("CODEX_MODEL", os.getenv("LLM_MODEL", codex_default)))
    if backend == "litellm":
        return "litellm", os.getenv(model_env, litellm_default)
    if shutil.which("codex") and not any(os.getenv(k) for k in ("ANTHROPIC_API_KEY", "OPENAI_API_KEY", "OPENROUTER_API_KEY")):
        return "codex", os.getenv(model_env, os.getenv("CODEX_MODEL", os.getenv("LLM_MODEL", codex_default)))
    return "litellm", os.getenv(model_env, litellm_default)


def call_llm(prompt: str, model_env: str = "LLM_MODEL", default_model: str = "anthropic/claude-3-5-sonnet-latest", max_tokens: int = 4096) -> str:
    backend, _ = selected_backend(model_env=model_env, litellm_default=default_model)
    if backend == "codex":
        return call_codex(prompt, model_env=model_env, default_model="gpt-5.3-codex-spark", max_tokens=max_tokens)
    return call_litellm(prompt, model_env=model_env, default_model=default_model, max_tokens=max_tokens)
