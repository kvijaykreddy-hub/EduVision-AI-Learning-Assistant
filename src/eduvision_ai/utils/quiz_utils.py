"""
Utility functions for Quiz Generator.
"""

from eduvision_ai.models.quiz_question import QuizQuestion


def calculate_score(
    questions: list[QuizQuestion],
    user_answers: list[int],
) -> int:
    """
    Calculate the user's quiz score.
    """

    score = 0

    for question, answer in zip(questions, user_answers):
        if answer == question.answer:
            score += 1

    return score