"""
Text Summarization Service.
"""

from eduvision_ai.models.llm_response import LLMResponse
from eduvision_ai.prompts.summarization import build_summary_prompt
from eduvision_ai.services.base_llm_service import BaseLLMService


class SummarizationService(BaseLLMService):
    """
    Service responsible for text summarization.
    """

    def summarize(self, text: str) -> LLMResponse:
        prompt = build_summary_prompt(text)
        return self.generate(prompt)