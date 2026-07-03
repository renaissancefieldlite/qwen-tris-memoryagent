from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from qwen_agent_buildout.trini_recall.alibaba_qwen_cloud_client import (
    ALIBABA_QWEN_COMPATIBLE_BASE,
    DEFAULT_QWEN_MODEL,
    build_qwen_cloud_payload,
    qwen_cloud_chat_completions_endpoint,
)
from qwen_agent_buildout.trini_recall.providers import QwenCloudProvider


class AlibabaQwenCloudClientTest(unittest.TestCase):
    def test_endpoint_targets_alibaba_qwen_cloud_compatible_api(self):
        endpoint = qwen_cloud_chat_completions_endpoint()

        self.assertEqual(
            endpoint,
            "https://dashscope-intl.aliyuncs.com/compatible-mode/v1/chat/completions",
        )

    def test_endpoint_does_not_double_append_chat_completions(self):
        endpoint = qwen_cloud_chat_completions_endpoint(
            "https://dashscope-intl.aliyuncs.com/compatible-mode/v1/chat/completions"
        )

        self.assertEqual(
            endpoint,
            "https://dashscope-intl.aliyuncs.com/compatible-mode/v1/chat/completions",
        )

    def test_payload_uses_qwen_model_and_public_safe_messages(self):
        payload = build_qwen_cloud_payload("What is the current gate?")

        self.assertEqual(payload["model"], DEFAULT_QWEN_MODEL)
        self.assertEqual(payload["temperature"], 0.0)
        self.assertEqual(payload["messages"][0]["role"], "system")
        self.assertEqual(payload["messages"][1]["content"], "What is the current gate?")

    def test_provider_uses_same_alibaba_endpoint_constant(self):
        provider = QwenCloudProvider(api_key="test")

        self.assertEqual(provider.api_base, ALIBABA_QWEN_COMPATIBLE_BASE)


if __name__ == "__main__":
    unittest.main()
