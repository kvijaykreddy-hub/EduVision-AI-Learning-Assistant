"""
Prompt templates for text summarization.
"""


def build_summary_prompt(text: str) -> str:
    """
    Build prompt for summarization.
    """

    return f"""
You are an expert educational assistant.

Summarize the following text.

Requirements:
- Preserve the important ideas.
- Remove unnecessary details.
- Use clear and simple English.
- Organize into bullet points.
- Maximum 200 words.

TEXT:

{text}
"""