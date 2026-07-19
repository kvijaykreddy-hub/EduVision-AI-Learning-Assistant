"""
Question Answering Service.
"""

from eduvision_ai.models.llm_response import LLMResponse
from eduvision_ai.services.base_llm_service import BaseLLMService


class QAService(BaseLLMService):
    """
    Question Answering Service.

    Supports:
    - General question answering
    - Context-aware question answering
    """

    def ask(
        self,
        question: str,
        context: str | None = None,
    ) -> LLMResponse:
        """
        Ask a question.

        Args:
            question: User question
            context: Optional document context (OCR text)

        Returns:
            LLMResponse
        """

        if context and context.strip():

            prompt = f"""
You are an expert educational AI assistant.

Answer the question ONLY using the document provided below.

If the answer is not available in the document,
reply with:

"The answer is not present in the provided document."

---------------- DOCUMENT ----------------

{context}

------------------------------------------

Question:

{question}

Answer:
"""

            return self.generate(prompt)

        return self.generate(question)