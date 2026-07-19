"""
Test script for QuizService.
Run this file directly to verify quiz generation and JSON parsing.
"""

from eduvision_ai.services.quiz_service import QuizService


def main():
    sample_text = """
Machine Learning is a subset of Artificial Intelligence that enables computers
to learn from data without being explicitly programmed.

There are three main types of machine learning:

1. Supervised Learning
2. Unsupervised Learning
3. Reinforcement Learning

Supervised learning uses labeled data.

Unsupervised learning discovers hidden patterns in unlabeled data.

Reinforcement learning trains an agent using rewards and penalties.
"""

    service = QuizService()

    response, questions = service.generate_quiz(
        text=sample_text,
        difficulty="Medium",
        num_questions=5,
    )

    print("=" * 80)
    print("LLM Response")
    print("=" * 80)
    print(f"Model         : {response.model}")
    print(f"Response Time : {response.response_time:.2f} sec")
    print()

    print("=" * 80)
    print(f"Generated {len(questions)} Questions")
    print("=" * 80)

    for i, q in enumerate(questions, start=1):

        print(f"\nQuestion {i}")
        print("-" * 60)

        print(q.question)
        print()

        for index, option in enumerate(q.options):
            print(f"{chr(65 + index)}. {option}")

        print()
        print(f"Correct Answer : {chr(65 + q.answer)}")
        print(f"Explanation    : {q.explanation}")


if __name__ == "__main__":
    main()