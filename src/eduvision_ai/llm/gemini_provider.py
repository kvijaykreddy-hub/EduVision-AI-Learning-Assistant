from PIL import Image

from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

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

        self.model_name = Settings.GEMINI_MODEL

    def invoke(self, prompt: str) -> str:
        """
        Text-only invocation.
        Used by QA, Summarization and Quiz Generator.
        """

        response = self.llm.invoke(
            [HumanMessage(content=prompt)]
        )

        return self._extract_text(response.content)

    def invoke_with_image(
        self,
        prompt: str,
        image: Image.Image,
    ) -> str:
        """
        Multimodal invocation.
        Used by OCR.
        """

        response = self.llm.invoke(
            [
                HumanMessage(
                    content=[
                        {
                            "type": "text",
                            "text": prompt,
                        },
                        {
                            "type": "image",
                            "image": image,
                        },
                    ]
                )
            ]
        )

        return self._extract_text(response.content)

    @staticmethod
    def _extract_text(content) -> str:
        """
        Extract plain text from LangChain response.
        """

        if isinstance(content, list):

            text_parts = [
                block["text"]
                for block in content
                if isinstance(block, dict)
                and block.get("type") == "text"
            ]

            return "\n".join(text_parts)

        return str(content)