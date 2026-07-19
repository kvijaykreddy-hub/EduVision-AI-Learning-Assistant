"""
Quiz Generation Service.
"""

import json

from eduvision_ai.models.llm_response import LLMResponse
from eduvision_ai.models.quiz_question import QuizQuestion
from eduvision_ai.prompts.quiz import build_quiz_prompt
from eduvision_ai.services.base_llm_service import BaseLLMService


class QuizService(BaseLLMService):
    """
    Service responsible for quiz generation.
    """

    def generate_quiz(
        self,
        text: str,
        difficulty: str,
        num_questions: int,
    ) -> tuple[LLMResponse, list[QuizQuestion]]:

        prompt = build_quiz_prompt(
            text=text,
            difficulty=difficulty,
            num_questions=num_questions,
        )

        response = self.generate(prompt)

        quiz_json = json.loads(response.content)

        questions = [
            QuizQuestion(
                question=item["question"],
                options=item["options"],
                answer=item["answer"],
                explanation=item["explanation"],
            )
            for item in quiz_json
        ]

        return response, questions