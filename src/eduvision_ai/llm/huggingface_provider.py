from langchain_huggingface import HuggingFaceEndpoint

from eduvision_ai.config.settings import Settings
from eduvision_ai.llm.provider import LLMProvider


class HuggingFaceProvider(LLMProvider):

    def __init__(self):

        self.llm = HuggingFaceEndpoint(
            repo_id="google/gemma-2-2b-it",
            huggingfacehub_api_token=Settings.HUGGINGFACEHUB_API_TOKEN,
            temperature=0.3,
            max_new_tokens=512,
        )

    def invoke(self, prompt: str) -> str:
        return self.llm.invoke(prompt)