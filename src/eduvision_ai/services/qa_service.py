"""
Question Answering Service.
"""
from eduvision_ai.models.llm_response import LLMResponse
from eduvision_ai.services.base_llm_service import BaseLLMService


class QAService(BaseLLMService):

    def ask(self, question: str) -> LLMResponse:
        return self.generate(question)