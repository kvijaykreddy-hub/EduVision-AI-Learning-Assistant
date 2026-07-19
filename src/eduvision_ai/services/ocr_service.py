"""
OCR Service using Google's official Gen AI SDK.
"""

import time

from PIL import Image
from google import genai

from eduvision_ai.config.settings import Settings
from eduvision_ai.models.llm_response import LLMResponse
from eduvision_ai.prompts.ocr import OCR_PROMPT


class OCRService:
    """
    OCR Service.
    """

    def __init__(self):

        self.client = genai.Client(
            api_key=Settings.GOOGLE_API_KEY
        )

        self.model_name = Settings.GEMINI_MODEL

    def extract_text(
        self,
        image: Image.Image,
    ) -> LLMResponse:

        start = time.perf_counter()

        response = self.client.models.generate_content(
            model=self.model_name,
            contents=[
                OCR_PROMPT,
                image,
            ],
        )

        elapsed = time.perf_counter() - start

        return LLMResponse(
            content=response.text,
            response_time=elapsed,
            model=self.model_name,
        )