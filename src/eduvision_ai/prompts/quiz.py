"""
Prompt builder for Quiz Generation.
"""


def build_quiz_prompt(
    text: str,
    difficulty: str,
    num_questions: int,
) -> str:

    return f"""
You are an expert educational assessment assistant.

Generate exactly {num_questions} multiple-choice questions.

Difficulty:
{difficulty}

Return ONLY valid JSON.

Do NOT use markdown.

Do NOT use ```json.

Use exactly this schema:

[
  {{
    "question":"Question text",
    "options":[
      "Option A",
      "Option B",
      "Option C",
      "Option D"
    ],
    "answer":0,
    "explanation":"Short explanation"
  }}
]

Rules:

- Exactly {num_questions} questions.
- Exactly four options.
- answer is the zero-based index of the correct option.
- Generate valid JSON only.
- Do not include additional text.
- Use only the provided study material.

Study Material:

{text}
"""