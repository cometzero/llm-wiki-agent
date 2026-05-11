import os
import sys
import types
import unittest

from tools import llm_backend


MINIMAX_MODEL = "minimaxai/minimax-m2.7"


class NvidiaBackendTests(unittest.TestCase):
    def setUp(self):
        self.env_backup = os.environ.copy()
        self.openai_backup = sys.modules.get("openai")
        self.openai_was_present = "openai" in sys.modules
        self.clear_model_env()

    def tearDown(self):
        os.environ.clear()
        os.environ.update(self.env_backup)
        if self.openai_was_present:
            sys.modules["openai"] = self.openai_backup
        else:
            sys.modules.pop("openai", None)

    def clear_model_env(self):
        for name in (
            "LLM_MODEL",
            "LLM_MODEL_FAST",
            "NVIDIA_MODEL",
            "NVIDIA_MODEL_FAST",
            "NVIDIA_TEMPERATURE",
            "NVIDIA_TOP_P",
            "NVIDIA_THINKING",
            "NVIDIA_STREAM",
            "NVIDIA_REQUEST_TIMEOUT",
            "NVIDIA_REASONING_EFFORT",
        ):
            os.environ.pop(name, None)

    def test_nvidia_defaults_to_minimax_m2_7(self):
        os.environ["WIKI_LLM_BACKEND"] = "nvidia"

        self.assertEqual(llm_backend.NVIDIA_DEFAULT_MODEL, MINIMAX_MODEL)
        self.assertEqual(llm_backend.NVIDIA_DEFAULT_FAST_MODEL, MINIMAX_MODEL)
        self.assertEqual(llm_backend.selected_backend(), ("nvidia", MINIMAX_MODEL))
        self.assertEqual(llm_backend.selected_backend(model_env="LLM_MODEL_FAST"), ("nvidia", MINIMAX_MODEL))

    def test_minimax_profile_matches_nvidia_reference_request(self):
        profile = llm_backend._nvidia_model_profile(MINIMAX_MODEL)

        self.assertEqual(profile["temperature"], 1.0)
        self.assertEqual(profile["top_p"], 0.95)
        self.assertIs(profile["thinking"], False)
        self.assertIs(profile["stream"], True)

    def test_minimax_request_omits_thinking_extra_body(self):
        profile = llm_backend._nvidia_model_profile(MINIMAX_MODEL)

        request = llm_backend._nvidia_request_kwargs("hello", MINIMAX_MODEL, 8192, profile)

        self.assertEqual(request["model"], MINIMAX_MODEL)
        self.assertEqual(request["temperature"], 1.0)
        self.assertEqual(request["top_p"], 0.95)
        self.assertEqual(request["max_tokens"], 8192)
        self.assertEqual(request["messages"], [{"role": "user", "content": "hello"}])
        self.assertNotIn("extra_body", request)

    def test_call_nvidia_streams_minimax_chunks(self):
        os.environ["NVIDIA_API_KEY"] = "test-key"
        os.environ["WIKI_LLM_BACKEND"] = "nvidia"
        calls = []

        class FakeDelta:
            def __init__(self, content):
                self.content = content

        class FakeChoice:
            def __init__(self, content):
                self.delta = FakeDelta(content)

        class FakeChunk:
            def __init__(self, content=None, choices=None):
                self.choices = choices if choices is not None else [FakeChoice(content)]

        class FakeCompletions:
            def create(self, **kwargs):
                calls.append(kwargs)
                return [
                    FakeChunk(choices=[]),
                    FakeChunk('{"ok":'),
                    FakeChunk("true}"),
                ]

        class FakeChat:
            def __init__(self):
                self.completions = FakeCompletions()

        class FakeOpenAI:
            def __init__(self, *, base_url, api_key, timeout):
                self.base_url = base_url
                self.api_key = api_key
                self.timeout = timeout
                self.chat = FakeChat()

        sys.modules["openai"] = types.SimpleNamespace(OpenAI=FakeOpenAI)

        response = llm_backend.call_nvidia("Return JSON", max_tokens=8192)

        self.assertEqual(response, '{"ok":true}')
        self.assertEqual(len(calls), 1)
        self.assertIs(calls[0]["stream"], True)
        self.assertEqual(calls[0]["model"], MINIMAX_MODEL)
        self.assertEqual(calls[0]["temperature"], 1.0)
        self.assertEqual(calls[0]["top_p"], 0.95)
        self.assertEqual(calls[0]["max_tokens"], 8192)
        self.assertNotIn("extra_body", calls[0])


if __name__ == "__main__":
    unittest.main()
