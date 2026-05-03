#!/usr/bin/env python3
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent


NVIDIA_BASE_URL = os.getenv("NVIDIA_BASE_URL", "https://integrate.api.nvidia.com/v1")
NVIDIA_DEFAULT_MODEL = "deepseek-ai/deepseek-v4-flash"
NVIDIA_DEFAULT_FAST_MODEL = NVIDIA_DEFAULT_MODEL


def normalized_nvidia_base_url() -> str:
    base_url = os.getenv("NVIDIA_BASE_URL", NVIDIA_BASE_URL).strip()
    if not base_url:
        return "https://integrate.api.nvidia.com/v1"
    if not base_url.startswith(("http://", "https://")):
        base_url = f"https://{base_url}"
    return base_url.rstrip("/")


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


def _env_bool(name: str, default: bool) -> bool:
    raw = os.getenv(name)
    if raw is None:
        return default
    return raw.strip().lower() not in {"0", "false", "no", "off"}



def _nvidia_model_profile(model: str) -> dict:
    model_lower = model.lower()
    profile = {
        "temperature": float(os.getenv("NVIDIA_TEMPERATURE", "0.2")),
        "top_p": float(os.getenv("NVIDIA_TOP_P", "0.95")),
        "reasoning_effort": os.getenv("NVIDIA_REASONING_EFFORT", "high"),
        "thinking": _env_bool("NVIDIA_THINKING", True),
        "stream": _env_bool("NVIDIA_STREAM", True),
        "request_timeout": float(os.getenv("NVIDIA_REQUEST_TIMEOUT", "300")),
    }

    # deepseek-v4-pro is stricter about chat_template_kwargs support in this repo's usage.
    # Keep the global env override, but make the default safer for structured ingest.
    if "deepseek-ai/deepseek-v4-pro" in model_lower:
        if os.getenv("NVIDIA_THINKING") is None:
            profile["thinking"] = False
        if os.getenv("NVIDIA_TEMPERATURE") is None:
            profile["temperature"] = 0.2

    return profile



def _is_degraded_thinking_error(exc: Exception) -> bool:
    text = str(exc).lower()
    return "degraded function cannot be invoked" in text or "chat_template_kwargs" in text



def _nvidia_request_kwargs(prompt: str, model: str, max_tokens: int, profile: dict, *, thinking_override: bool | None = None) -> dict:
    thinking = profile["thinking"] if thinking_override is None else thinking_override
    request_kwargs = dict(
        model=model,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a backend text generator running inside an automated Python script. "
                    "You have no tool access. Never emit tool-call markup, XML tags, DSML tags, or planning preambles. "
                    "Return only the final answer requested by the user prompt."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        temperature=profile["temperature"],
        top_p=profile["top_p"],
        max_tokens=max_tokens,
    )

    if thinking:
        request_kwargs["extra_body"] = {
            "chat_template_kwargs": {
                "thinking": True,
                "reasoning_effort": profile["reasoning_effort"],
            }
        }

    return request_kwargs



def _consume_nvidia_response(client, request_kwargs: dict, *, use_stream: bool) -> str:
    if use_stream:
        stream = client.chat.completions.create(stream=True, **request_kwargs)
        content_parts: list[str] = []
        for chunk in stream:
            if not getattr(chunk, "choices", None):
                continue
            delta = chunk.choices[0].delta
            if getattr(delta, "content", None) is not None:
                content_parts.append(delta.content)
        return "".join(content_parts).strip()

    response = client.chat.completions.create(stream=False, **request_kwargs)
    return (response.choices[0].message.content or "").strip()



def call_nvidia(prompt: str, model_env: str = "LLM_MODEL", default_model: str = NVIDIA_DEFAULT_MODEL, max_tokens: int = 4096) -> str:
    try:
        from openai import OpenAI
    except ImportError:
        print("Error: openai not installed. Run: pip install openai")
        sys.exit(1)

    api_key = os.getenv("NVIDIA_API_KEY")
    if not api_key:
        print("Error: NVIDIA_API_KEY is not set.")
        sys.exit(1)

    model = os.getenv(model_env, default_model)
    profile = _nvidia_model_profile(model)
    client = OpenAI(
        base_url=normalized_nvidia_base_url(),
        api_key=api_key,
        timeout=profile["request_timeout"],
    )

    try:
        request_kwargs = _nvidia_request_kwargs(prompt, model, max_tokens, profile)
        text = _consume_nvidia_response(client, request_kwargs, use_stream=profile["stream"])
    except Exception as exc:
        if profile["thinking"] and _is_degraded_thinking_error(exc):
            print(f"  NVIDIA request rejected thinking mode for {model}; retrying with thinking disabled")
            request_kwargs = _nvidia_request_kwargs(prompt, model, max_tokens, profile, thinking_override=False)
            text = _consume_nvidia_response(client, request_kwargs, use_stream=profile["stream"])
        else:
            raise

    if not text:
        print(f"Error: NVIDIA completion produced no content (model: {model})")
        sys.exit(1)
    return text


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


def selected_backend(model_env: str = "LLM_MODEL", litellm_default: str = "anthropic/claude-3-5-sonnet-latest", codex_default: str = "gpt-5.3-codex-spark", nvidia_default: str = NVIDIA_DEFAULT_MODEL) -> tuple[str, str]:
    backend = os.getenv("WIKI_LLM_BACKEND", "auto").lower()
    if backend == "nvidia":
        return "nvidia", os.getenv(model_env, os.getenv("NVIDIA_MODEL", os.getenv("LLM_MODEL", nvidia_default)))
    if backend == "codex":
        return "codex", os.getenv(model_env, os.getenv("CODEX_MODEL", os.getenv("LLM_MODEL", codex_default)))
    if backend == "litellm":
        return "litellm", os.getenv(model_env, litellm_default)
    if backend == "auto":
        if os.getenv("NVIDIA_API_KEY"):
            return "nvidia", os.getenv(model_env, os.getenv("NVIDIA_MODEL", os.getenv("LLM_MODEL", nvidia_default)))
        if shutil.which("codex") and not any(os.getenv(k) for k in ("ANTHROPIC_API_KEY", "OPENAI_API_KEY", "OPENROUTER_API_KEY")):
            return "codex", os.getenv(model_env, os.getenv("CODEX_MODEL", os.getenv("LLM_MODEL", codex_default)))
        return "litellm", os.getenv(model_env, litellm_default)
    print(f"Error: unsupported WIKI_LLM_BACKEND={backend}")
    sys.exit(1)


def _nvidia_default_for_env(model_env: str, default_model: str) -> str:
    if model_env == "LLM_MODEL_FAST":
        return os.getenv("NVIDIA_MODEL_FAST", NVIDIA_DEFAULT_FAST_MODEL)
    return os.getenv("NVIDIA_MODEL", default_model)


def call_llm(prompt: str, model_env: str = "LLM_MODEL", default_model: str = "anthropic/claude-3-5-sonnet-latest", max_tokens: int = 4096) -> str:
    nvidia_default = _nvidia_default_for_env(model_env, NVIDIA_DEFAULT_MODEL)
    backend, _ = selected_backend(model_env=model_env, litellm_default=default_model, nvidia_default=nvidia_default)
    if backend == "nvidia":
        return call_nvidia(prompt, model_env=model_env, default_model=nvidia_default, max_tokens=max_tokens)
    if backend == "codex":
        return call_codex(prompt, model_env=model_env, default_model="gpt-5.3-codex-spark", max_tokens=max_tokens)
    return call_litellm(prompt, model_env=model_env, default_model=default_model, max_tokens=max_tokens)
