from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

from eduvision_ai.config.settings import Settings
from eduvision_ai.llm.provider import LLMProvider


class GeminiProvider(LLMProvider):
    """Gemini LLM Provider"""

    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model=Settings.GEMINI_MODEL,
            google_api_key=Settings.GOOGLE_API_KEY,
            temperature=0.3,
        )

    def invoke(self, prompt: str) -> str:
        response = self.llm.invoke(
            [HumanMessage(content=prompt)]
        )

        content = response.content

        # Handle LangChain's structured response format
        if isinstance(content, list):
            text_parts = [
                block["text"]
                for block in content
                if isinstance(block, dict) and block.get("type") == "text"
            ]
            return "\n".join(text_parts)

        return str(content)