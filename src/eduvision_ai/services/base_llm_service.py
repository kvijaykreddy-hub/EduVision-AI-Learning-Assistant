"""
Base service for all LLM-powered features.
"""

import time

from eduvision_ai.config.settings import Settings
from eduvision_ai.llm.gemini_provider import GeminiProvider
from eduvision_ai.models.llm_response import LLMResponse


class BaseLLMService:
    """
    Base class for all LLM-powered services.
    """

    def __init__(self):
        self.provider = GeminiProvider()

    def generate(self, prompt: str) -> LLMResponse:
        """
        Generate a response using the configured LLM.
        """

        start = time.perf_counter()

        content = self.provider.invoke(prompt)

        end = time.perf_counter()

        return LLMResponse(
            content=content,
            response_time=end - start,
            model=Settings.GEMINI_MODEL,
        )