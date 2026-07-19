"""
Model representing a quiz question.
"""

from dataclasses import dataclass


@dataclass
class QuizQuestion:
    question: str
    options: list[str]
    answer: int
    explanation: str