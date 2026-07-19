"""
Image Classification Service.
"""

import time

from PIL import Image
from google import genai

from eduvision_ai.config.settings import Settings
from eduvision_ai.models.llm_response import LLMResponse
from eduvision_ai.prompts.image_classification import (
    IMAGE_CLASSIFICATION_PROMPT,
)


class ImageClassificationService:
    """
    Image Classification Service.
    """

    def __init__(self):

        self.client = genai.Client(
            api_key=Settings.GOOGLE_API_KEY,
        )

        self.model_name = Settings.GEMINI_MODEL

    def classify(
        self,
        image: Image.Image,
    ) -> LLMResponse:

        start = time.perf_counter()

        response = self.client.models.generate_content(
            model=self.model_name,
            contents=[
                IMAGE_CLASSIFICATION_PROMPT,
                image,
            ],
        )

        elapsed = time.perf_counter() - start

        return LLMResponse(
            content=response.text,
            response_time=elapsed,
            model=self.model_name,
        )