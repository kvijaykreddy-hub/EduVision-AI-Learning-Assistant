from eduvision_ai.llm.gemini_provider import GeminiProvider


class LLMService:
    """Application LLM Service"""

    def __init__(self):
        self.provider = GeminiProvider()

    def ask(self, question: str) -> str:
        return self.provider.invoke(question)